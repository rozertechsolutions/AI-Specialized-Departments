#!/usr/bin/env python3
"""Qwen Code PreToolUse guard requiring review for sensitive mobile changes."""

from __future__ import annotations

import json
import ntpath
import os
import re
import shlex
import sys
from typing import Any, Iterable


class PolicyInputError(ValueError):
    """Raised when the hook input cannot be evaluated safely."""


WRITE_TOOLS = {
    "write",
    "writefile",
    "write_file",
    "edit",
    "editfile",
    "notebookedit",
    "notebook_edit",
}
SHELL_TOOLS = {"bash", "shell", "run_shell_command"}
PATH_KEYS = {
    "path",
    "file",
    "file_path",
    "filepath",
    "notebook_path",
    "source_path",
    "target_path",
    "destination_path",
}
CONTROL_TOKENS = {";", "&&", "||", "|", "&", ">", ">>", "<", "<<", "<<<"}
SENSITIVE_NAMES = {
    ".gitlab-ci.yml",
    "androidmanifest.xml",
    "app.json",
    "appfile",
    "azure-pipelines.yml",
    "babel.config.js",
    "babel.config.cjs",
    "babel.config.mjs",
    "bitrise.yml",
    "bitrise.yaml",
    "build.gradle",
    "build.gradle.kts",
    "bun.lock",
    "bun.lockb",
    "codemagic.yml",
    "codemagic.yaml",
    "consumer-rules.pro",
    "data_extraction_rules.xml",
    "deliverfile",
    "exportoptions.plist",
    "fastfile",
    "firebase_options.dart",
    "firebase.json",
    "gemfile.lock",
    "gradle-wrapper.properties",
    "gradle.properties",
    "google-services.json",
    "googleservice-info.plist",
    "gymfile",
    "info.plist",
    "jenkinsfile",
    "libs.versions.toml",
    "matchfile",
    "metro.config.js",
    "metro.config.cjs",
    "metro.config.mjs",
    "network_security_config.xml",
    "package-lock.json",
    "package.json",
    "package.resolved",
    "package.swift",
    "pnpm-lock.yaml",
    "podfile",
    "podfile.lock",
    "privacyinfo.xcprivacy",
    "proguard-rules.pro",
    "pubspec.lock",
    "pubspec.yaml",
    "react-native.config.js",
    "settings.gradle",
    "settings.gradle.kts",
    "yarn.lock",
    "backup_rules.xml",
}
SENSITIVE_SUFFIXES = (".entitlements", ".xcconfig", ".pbxproj")
MUTATING_FILE_COMMANDS = {
    "add-content",
    "copy",
    "copy-item",
    "cp",
    "install",
    "move",
    "move-item",
    "mv",
    "patch",
    "perl",
    "python",
    "python3",
    "remove-item",
    "ruby",
    "sed",
    "set-content",
    "tee",
    "touch",
    "truncate",
}


def _decision(kind: str, reason: str, context: str | None = None) -> dict[str, Any]:
    output: dict[str, Any] = {
        "hookEventName": "PreToolUse",
        "permissionDecision": kind,
        "permissionDecisionReason": reason,
    }
    if context:
        output["additionalContext"] = context
    return {"hookSpecificOutput": output}


def _validate_payload(payload: Any) -> tuple[str, dict[str, Any], str]:
    if not isinstance(payload, dict):
        raise PolicyInputError("input must be a JSON object")
    if payload.get("hook_event_name") != "PreToolUse":
        raise PolicyInputError("unexpected hook event")
    tool_name = payload.get("tool_name")
    tool_input = payload.get("tool_input")
    cwd = payload.get("cwd")
    if not isinstance(tool_name, str) or not tool_name.strip():
        raise PolicyInputError("tool_name must be a non-empty string")
    if not isinstance(tool_input, dict):
        raise PolicyInputError("tool_input must be an object")
    if (
        not isinstance(cwd, str)
        or not cwd.strip()
        or "\x00" in cwd
        or cwd.startswith("~")
        or not (cwd.startswith("/") or _is_windows_path(cwd))
    ):
        raise PolicyInputError("cwd must be a non-empty absolute path string")
    return tool_name.strip().lower(), tool_input, cwd


def _paths(tool_input: dict[str, Any]) -> list[str]:
    result: list[str] = []
    for key, value in tool_input.items():
        normalized = key.lower().replace("-", "_")
        if normalized not in PATH_KEYS:
            continue
        if isinstance(value, str):
            result.append(value)
        elif isinstance(value, list):
            result.extend(item for item in value if isinstance(item, str))
    return result


def _has_traversal(path: str) -> bool:
    return any(part == ".." for part in path.replace("\\", "/").split("/"))


def _is_windows_path(path: str) -> bool:
    return bool(re.match(r"^[A-Za-z]:[\\/]", path)) or path.startswith("\\\\")


def _within_cwd(path: str, cwd: str) -> bool:
    if path.startswith("~"):
        return False
    if _is_windows_path(path) or _is_windows_path(cwd):
        if not _is_windows_path(cwd):
            return False
        try:
            candidate_path = path if _is_windows_path(path) else ntpath.join(cwd, path)
            candidate = ntpath.normcase(ntpath.abspath(candidate_path))
            root = ntpath.normcase(ntpath.abspath(cwd))
            return ntpath.commonpath([candidate, root]) == root
        except ValueError:
            return False
    try:
        candidate_path = path if os.path.isabs(path) else os.path.join(cwd, path)
        candidate = os.path.realpath(candidate_path)
        root = os.path.realpath(cwd)
        return os.path.commonpath([candidate, root]) == root
    except ValueError:
        return False


def _sensitive_path(path: str) -> bool:
    normalized = path.strip().strip("\"'").replace("\\", "/").rstrip("/.,;:)").lower()
    parts = [part for part in normalized.split("/") if part not in {"", "."}]
    base_name = parts[-1] if parts else normalized
    if base_name in SENSITIVE_NAMES or base_name.endswith(SENSITIVE_SUFFIXES):
        return True
    if ".qwen" in parts and any(part in {"settings.json", "hooks"} for part in parts):
        return True
    if ".github" in parts and "workflows" in parts:
        return True
    if ".circleci" in parts and base_name == "config.yml":
        return True
    if "fastlane" in parts and base_name in {name.lower() for name in EXPLICIT_FASTLANE_FILES}:
        return True
    return False


EXPLICIT_FASTLANE_FILES = {"Appfile", "Deliverfile", "Fastfile", "Gymfile", "Matchfile", "Pluginfile"}


def _tokenize(command: str) -> list[str]:
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|<>")
        lexer.whitespace_split = True
        lexer.commenters = ""
        return list(lexer)
    except ValueError as exc:
        raise PolicyInputError("shell command cannot be parsed safely") from exc


def _segments(tokens: list[str]) -> Iterable[list[str]]:
    current: list[str] = []
    for token in tokens:
        if token in CONTROL_TOKENS or (token and all(char in ";&|<>" for char in token)):
            if current:
                yield current
                current = []
        else:
            current.append(token)
    if current:
        yield current


def _executable(token: str) -> str:
    name = ntpath.basename(token).lower()
    for suffix in (".exe", ".cmd", ".bat", ".ps1"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def _unwrap_segment(segment: list[str]) -> list[str]:
    result = list(segment)
    while result:
        while result and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", result[0]):
            result.pop(0)
        if not result:
            break
        executable = _executable(result[0])
        if executable in {"command", "builtin"}:
            result.pop(0)
            continue
        if executable == "env":
            result.pop(0)
            while result:
                if re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", result[0]):
                    result.pop(0)
                    continue
                if result[0] in {"-u", "--unset", "-C", "--chdir", "-S", "--split-string"}:
                    result = result[2:] if len(result) >= 2 else []
                    continue
                if result[0].startswith("-"):
                    result.pop(0)
                    continue
                break
            continue
        break
    return result


def _dependency_mutation(executable: str, args: list[str]) -> bool:
    lowered = [arg.lower() for arg in args]
    if executable in {"npm", "pnpm", "yarn", "bun"}:
        return bool(lowered and lowered[0] in {"add", "install", "remove", "uninstall", "update", "upgrade", "up"})
    if executable == "pod":
        return bool(lowered and lowered[0] in {"install", "update", "deintegrate"})
    if executable in {"flutter", "dart"}:
        return len(lowered) >= 2 and lowered[0] == "pub" and lowered[1] in {"add", "get", "remove", "upgrade", "downgrade"}
    if executable == "bundle":
        return bool(lowered and lowered[0] in {"add", "install", "remove", "update"})
    if executable in {"gradle", "gradlew"}:
        return any(arg.lower() == "wrapper" or arg.lower().endswith(":wrapper") for arg in args)
    return False


def _shell_finding(command: str) -> tuple[str, str] | None:
    if not command.strip() or "\x00" in command:
        raise PolicyInputError("shell command must be a non-empty valid string")
    tokens = _tokenize(command)
    if not tokens:
        raise PolicyInputError("shell command contains no executable tokens")

    for index, token in enumerate(tokens):
        if token in {">", ">>"} and index + 1 < len(tokens) and _sensitive_path(tokens[index + 1]):
            return "ask", "Writing sensitive mobile configuration requires human review."

    for segment in _segments(tokens):
        segment = _unwrap_segment(segment)
        if not segment:
            continue
        executable = _executable(segment[0])
        args = segment[1:]
        if _dependency_mutation(executable, args):
            return "ask", "Dependency or toolchain configuration changes require human review."
        if executable == "git" and args and args[0].lower() in {"apply", "am"}:
            return "ask", "Applying a patch may change sensitive configuration and requires human review."
        if executable not in MUTATING_FILE_COMMANDS:
            continue
        if executable == "sed" and not any(arg == "-i" or arg.startswith("-i") for arg in args):
            continue
        if executable == "perl" and not any("i" in arg and arg.startswith("-") for arg in args):
            continue
        if any(_sensitive_path(arg) for arg in args):
            return "ask", "Changing sensitive mobile configuration requires human review."
    return None


def evaluate(payload: Any) -> dict[str, Any]:
    tool, tool_input, cwd = _validate_payload(payload)
    finding: tuple[str, str] | None = None
    if tool in WRITE_TOOLS:
        paths = _paths(tool_input)
        if not paths:
            raise PolicyInputError("write tool input contains no recognized path")
        for path in paths:
            if not path.strip() or "\x00" in path:
                raise PolicyInputError("write path is invalid")
            if _has_traversal(path):
                return _decision("deny", "Sensitive-change policy rejects path traversal.")
            if not _within_cwd(path, cwd):
                return _decision("deny", "Sensitive-change policy rejects writes outside the project.")
            if _sensitive_path(path):
                finding = ("ask", "Changing sensitive mobile configuration requires human review.")
                break
    elif tool in SHELL_TOOLS:
        command = tool_input.get("command", tool_input.get("cmd"))
        if not isinstance(command, str):
            raise PolicyInputError("shell tool input must contain a command string")
        finding = _shell_finding(command)
    if not finding:
        return {}
    return _decision(
        finding[0],
        finding[1],
        "After an approved sensitive change, obtain the applicable security, test, accessibility, performance, release, and independent code reviews.",
    )


def _payload(tool: str, tool_input: dict[str, Any], cwd: str = "/workspace/app") -> dict[str, Any]:
    return {
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": tool_input,
        "cwd": cwd,
    }


def _result_decision(result: dict[str, Any]) -> str | None:
    return result.get("hookSpecificOutput", {}).get("permissionDecision")


def self_test() -> int:
    cases = [
        (_payload("write_file", {"file_path": "src/Main.kt"}), None),
        (_payload("write_file", {"file_path": "app/src/main/AndroidManifest.xml"}), "ask"),
        (_payload("write_file", {"file_path": "android/app/google-services.json"}), "ask"),
        (_payload("edit", {"file_path": "../AndroidManifest.xml"}), "deny"),
        (_payload("edit", {"file_path": ".qwen/settings.json"}), "ask"),
        (_payload("run_shell_command", {"command": "rg AndroidManifest.xml"}), None),
        (_payload("run_shell_command", {"command": "sed -i s/old/new/ AndroidManifest.xml"}), "ask"),
        (_payload("run_shell_command", {"command": "./gradlew test"}), None),
        (_payload("run_shell_command", {"command": "npm install"}), "ask"),
        (_payload("run_shell_command", {"command": "MODE=test npm install"}), "ask"),
        (_payload("run_shell_command", {"command": "printf value > pubspec.yaml"}), "ask"),
    ]
    for payload, expected in cases:
        actual = _result_decision(evaluate(payload))
        if actual != expected:
            raise AssertionError(f"expected {expected!r}, got {actual!r} for test case")
    print("sensitive-change-review self-test: ok")
    return 0


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    try:
        payload = json.load(sys.stdin)
        result = evaluate(payload)
    except (json.JSONDecodeError, PolicyInputError) as exc:
        print(f"sensitive-change-review: invalid input: {exc}", file=sys.stderr)
        return 2
    except Exception:
        print("sensitive-change-review: internal policy failure", file=sys.stderr)
        return 2
    if result:
        print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
