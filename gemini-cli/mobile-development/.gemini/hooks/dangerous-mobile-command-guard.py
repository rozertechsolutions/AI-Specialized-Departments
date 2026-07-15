#!/usr/bin/env python3
"""Gemini CLI BeforeTool hook for destructive and evasive shell commands."""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
import unittest
from pathlib import Path, PurePosixPath
from typing import Any

MAX_INPUT_BYTES = 1_048_576
MAX_COMMAND_CHARS = 20_000

UNSAFE_SHELL_SYNTAX = re.compile(
    r"(?:&&|\|\||[;|`\n\r]|\$\(|\$\{|\$[A-Za-z_]|<\(|>\(|(?<![<>=])>(?![>=])|(?<![<>=])<(?![<=])|(?<!&)&(?!&))"
)

OBFUSCATION_PATTERNS = (
    re.compile(r"(?i)(?:^|\s)(?:ba|z|fi)?sh\s+-c\b"),
    re.compile(r"(?i)(?:^|\s)(?:cmd(?:\.exe)?\s+/c|powershell(?:\.exe)?\s+.*-(?:enc|encodedcommand)\b)"),
    re.compile(r"(?i)(?:^|\s)(?:python(?:3)?\s+-c|node\s+-e|ruby\s+-e|perl\s+-e)\b"),
    re.compile(r"(?i)(?:^|\s)(?:eval|exec)\s+"),
    re.compile(r"(?i)(?:^|\s)(?:base64\b|xxd\s+-r\b|openssl\s+enc\b)"),
    re.compile(r"(?i)(?:^|\s)(?:curl|wget)\b.*(?:\|\s*(?:sh|bash)|-o\s*-)"),
)

DESTRUCTIVE_PATTERNS = (
    re.compile(r"(?i)^\s*(?:sudo\s+)?(?:rm|rmdir|unlink|shred|truncate)\b"),
    re.compile(r"(?i)^\s*(?:sudo\s+)?(?:dd|mkfs(?:\.[a-z0-9]+)?|fdisk|parted)\b"),
    re.compile(r"(?i)^\s*diskutil\s+(?:erase|partition|apfs\s+delete)\b"),
    re.compile(r"(?i)^\s*find\b.*(?:-delete|-exec(?:dir)?\s+(?:rm|rmdir|shred)\b)"),
    re.compile(r"(?i)^\s*(?:chmod|chown)\b.*(?:\s-R\b|--recursive\b)"),
    re.compile(r"(?i)^\s*xattr\s+-(?:r|c|cr|rc)\b"),
    re.compile(r"(?i)^\s*(?:killall|pkill)\b"),
    re.compile(r"(?i)^\s*xcrun\s+simctl\s+(?:erase|delete|shutdown\s+all)\b"),
    re.compile(r"(?i)^\s*adb\b.*\b(?:uninstall|factory-reset|wipe-data|pm\s+clear)\b"),
)

GIT_WRITE = re.compile(
    r"(?i)^\s*git\s+(?:(?:-C|--git-dir|--work-tree)\s+\S+\s+)?"
    r"(?:add|am|apply|branch|checkout|cherry-pick|clean|commit|merge|mv|notes|"
    r"push|rebase|reset|restore|revert|rm|stash|submodule\s+update|switch|tag|worktree)\b"
)

GIT_COMMAND = re.compile(r"(?i)^\s*git\b")
GIT_READ_ONLY = re.compile(r"(?i)^\s*git\s+(?:status|diff|log|show|ls-files|grep)\b")

INSTALL_OR_UPDATE = (
    re.compile(r"(?i)^\s*npm\s+(?:i|install|ci|update|uninstall)\b"),
    re.compile(r"(?i)^\s*pnpm\s+(?:add|install|update|remove|dlx)\b"),
    re.compile(r"(?i)^\s*yarn\s+(?:add|install|upgrade|remove|dlx)\b"),
    re.compile(r"(?i)^\s*(?:flutter|dart)\s+pub\s+(?:add|remove|get|upgrade|downgrade)\b"),
    re.compile(r"(?i)^\s*(?:bundle\s+install|gem\s+install|pod\s+(?:install|update|repo\s+update))\b"),
    re.compile(r"(?i)^\s*(?:sdk|brew|apt(?:-get)?|dnf|yum|pacman|choco|winget)\b.*\b(?:install|upgrade|update)\b"),
    re.compile(r"(?i)^\s*npx\b"),
    re.compile(r"(?i)^\s*(?:pip|pip3|pipx)\s+(?:install|uninstall|upgrade|inject)\b"),
    re.compile(r"(?i)^\s*(?:cargo|go)\s+install\b"),
)


class PayloadError(ValueError):
    """Raised when hook input is invalid."""


def deny(reason: str) -> dict[str, Any]:
    return {"decision": "deny", "reason": reason, "continue": True}


def validate_payload(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise PayloadError("payload must be an object")
    for key in (
        "session_id",
        "transcript_path",
        "cwd",
        "hook_event_name",
        "timestamp",
        "tool_name",
    ):
        if not isinstance(payload.get(key), str) or not payload[key]:
            raise PayloadError(f"{key} must be a non-empty string")
    if payload["hook_event_name"] != "BeforeTool":
        raise PayloadError("unexpected hook event")
    if not isinstance(payload.get("tool_input"), dict):
        raise PayloadError("tool_input must be an object")
    if not Path(payload["cwd"]).is_absolute():
        raise PayloadError("cwd must be absolute")
    return payload


def resolve_in_workspace(raw_path: str, cwd: Path) -> Path:
    if not raw_path or "\x00" in raw_path:
        raise PayloadError("invalid path")
    candidate = Path(raw_path).expanduser()
    if not candidate.is_absolute():
        candidate = cwd / candidate
    resolved_cwd = cwd.resolve(strict=False)
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(resolved_cwd)
    except ValueError as exc:
        raise PayloadError("working directory or path escapes the workspace") from exc
    return resolved


def command_path_escapes(command: str, cwd: Path) -> bool:
    try:
        tokens = shlex.split(command, posix=os.name != "nt")
    except ValueError:
        return True
    resolved_cwd = cwd.resolve(strict=False)
    for token in tokens:
        value = token.split("=", 1)[1] if token.startswith("-") and "=" in token else token
        value = value.strip("\"'")
        if not value or value.startswith(("http://", "https://")):
            continue
        normalized = value.replace("\\", "/")
        if normalized.startswith("~") or re.match(r"^[A-Za-z]:/", normalized) or normalized.startswith("//"):
            return True
        if ".." in PurePosixPath(normalized).parts:
            return True
        candidate = Path(value)
        if candidate.is_absolute():
            try:
                candidate.resolve(strict=False).relative_to(resolved_cwd)
            except ValueError:
                return True
    return False


def evaluate(payload: Any) -> dict[str, Any]:
    try:
        data = validate_payload(payload)
        if data["tool_name"] != "run_shell_command":
            return {"decision": "allow"}

        tool_input = data["tool_input"]
        command = tool_input.get("command")
        if not isinstance(command, str) or not command.strip():
            raise PayloadError("command must be a non-empty string")
        if len(command) > MAX_COMMAND_CHARS or "\x00" in command:
            raise PayloadError("command exceeds safety limits")

        cwd = Path(data["cwd"])
        dir_path = tool_input.get("dir_path", data["cwd"])
        if not isinstance(dir_path, str):
            raise PayloadError("dir_path must be a string")
        resolve_in_workspace(dir_path, cwd)

        if UNSAFE_SHELL_SYNTAX.search(command):
            return deny("Shell chaining, redirection, substitution, backgrounding, or multiline execution is blocked.")
        if any(pattern.search(command) for pattern in OBFUSCATION_PATTERNS):
            return deny("Encoded, nested-shell, evaluated, or otherwise obfuscated command execution is blocked.")
        if command_path_escapes(command, cwd):
            return deny("Commands may not reference paths outside the workspace.")
        if GIT_WRITE.search(command) or (GIT_COMMAND.search(command) and not GIT_READ_ONLY.search(command)):
            return deny("Git write, history, branch, worktree, or remote operations require explicit human control.")
        if any(pattern.search(command) for pattern in DESTRUCTIVE_PATTERNS):
            return deny("Destructive filesystem, device, simulator, or process operations are blocked.")
        if any(pattern.search(command) for pattern in INSTALL_OR_UPDATE):
            return deny("Package, plugin, SDK, runtime, or dependency installation/update commands are blocked.")
        return {"decision": "allow"}
    except (PayloadError, OSError, RuntimeError) as exc:
        return deny(f"Dangerous-command guard rejected invalid input: {exc}")


def read_stdin_payload() -> Any:
    raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
    if len(raw) > MAX_INPUT_BYTES:
        raise PayloadError("payload exceeds size limit")
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PayloadError("payload is not valid UTF-8 JSON") from exc


def base_payload(command: str, dir_path: str | None = None) -> dict[str, Any]:
    tool_input: dict[str, Any] = {"command": command}
    if dir_path is not None:
        tool_input["dir_path"] = dir_path
    return {
        "session_id": "test-session",
        "transcript_path": "/tmp/transcript.json",
        "cwd": "/tmp/mobile-project",
        "hook_event_name": "BeforeTool",
        "timestamp": "2026-01-01T00:00:00Z",
        "tool_name": "run_shell_command",
        "tool_input": tool_input,
    }


class DangerousCommandGuardTests(unittest.TestCase):
    def test_allows_scoped_gradle_test(self) -> None:
        self.assertEqual(evaluate(base_payload("./gradlew testDebugUnitTest"))["decision"], "allow")

    def test_allows_scoped_clean_commands(self) -> None:
        self.assertEqual(evaluate(base_payload("flutter clean"))["decision"], "allow")
        self.assertEqual(evaluate(base_payload("xcodebuild clean -scheme Demo"))["decision"], "allow")

    def test_blocks_destructive_filesystem_command(self) -> None:
        self.assertEqual(evaluate(base_payload("rm -rf build"))["decision"], "deny")
        self.assertEqual(
            evaluate(base_payload("find build -type f -execdir rm -f '{}' +"))["decision"],
            "deny",
        )

    def test_blocks_chaining(self) -> None:
        self.assertEqual(evaluate(base_payload("./gradlew test && git status"))["decision"], "deny")

    def test_blocks_git_write(self) -> None:
        self.assertEqual(evaluate(base_payload("git reset --hard HEAD"))["decision"], "deny")
        self.assertEqual(evaluate(base_payload("git config user.email test@example.com"))["decision"], "deny")
        self.assertEqual(evaluate(base_payload("git fetch origin"))["decision"], "deny")

    def test_allows_read_only_git(self) -> None:
        self.assertEqual(evaluate(base_payload("git status --short"))["decision"], "allow")

    def test_blocks_obfuscation(self) -> None:
        self.assertEqual(evaluate(base_payload("base64 -d payload.txt"))["decision"], "deny")

    def test_blocks_scope_escape(self) -> None:
        self.assertEqual(evaluate(base_payload("rg NEEDS_REVIEW ../other"))["decision"], "deny")
        self.assertEqual(evaluate(base_payload("rg NEEDS_REVIEW", "/tmp/other"))["decision"], "deny")

    def test_invalid_payload_fails_closed(self) -> None:
        self.assertEqual(evaluate({})["decision"], "deny")


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(DangerousCommandGuardTests)
        result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1
    try:
        payload = read_stdin_payload()
        result = evaluate(payload)
    except PayloadError as exc:
        result = deny(f"Dangerous-command guard rejected invalid input: {exc}")
    sys.stdout.write(json.dumps(result, separators=(",", ":")))
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
