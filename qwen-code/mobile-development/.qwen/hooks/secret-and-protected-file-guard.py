#!/usr/bin/env python3
"""Qwen Code PreToolUse guard for secrets, protected files, and path escapes."""

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


FILE_TOOLS = {
    "read",
    "readfile",
    "read_file",
    "readmanyfiles",
    "read_many_files",
    "grep",
    "grep_search",
    "glob",
    "listfiles",
    "list_directory",
    "write",
    "writefile",
    "write_file",
    "edit",
    "editfile",
    "notebookedit",
    "notebook_edit",
}
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
SHELL_INTERPRETERS = {"bash", "dash", "fish", "ksh", "sh", "zsh"}
CODE_INTERPRETERS = {"node", "perl", "php", "python", "python3", "ruby"}
PATH_KEYS = {
    "path",
    "paths",
    "file",
    "files",
    "file_path",
    "filepath",
    "file_paths",
    "directory",
    "directory_path",
    "dir_path",
    "notebook_path",
    "source_path",
    "target_path",
    "destination_path",
}
PATH_REQUIRED_TOOLS = {
    "readfile",
    "read_file",
    "readmanyfiles",
    "read_many_files",
    "listfiles",
    "list_directory",
    "write",
    "writefile",
    "write_file",
    "edit",
    "editfile",
    "notebookedit",
    "notebook_edit",
}
CONTENT_KEYS = {
    "content",
    "diff",
    "new_content",
    "new_string",
    "new_text",
    "patch",
    "replacement",
    "text",
}
SHELL_FILE_COMMANDS = {
    "cat",
    "head",
    "tail",
    "less",
    "more",
    "sed",
    "awk",
    "grep",
    "rg",
    "find",
    "ls",
    "stat",
    "file",
    "cp",
    "mv",
    "rm",
    "rmdir",
    "touch",
    "truncate",
    "tee",
    "chmod",
    "chown",
    "install",
    "open",
    "xdg-open",
    "type",
    "get-content",
    "set-content",
    "add-content",
    "copy-item",
    "move-item",
    "remove-item",
}
PROTECTED_DIRECTORIES = {
    ".aws",
    ".azure",
    ".docker",
    ".gem",
    ".git",
    ".gnupg",
    ".kube",
    ".ssh",
}
PROTECTED_SUFFIXES = (
    ".p12",
    ".p8",
    ".pfx",
    ".jks",
    ".keystore",
    ".mobileprovision",
    ".provisionprofile",
    ".pem",
    ".key",
    ".der",
    ".cer",
    ".crt",
)
PROTECTED_NAMES = {
    ".envrc",
    ".netrc",
    ".npmrc",
    ".pypirc",
    "auth.json",
    "credentials",
    "credentials.json",
    "id_dsa",
    "id_ecdsa",
    "id_ed25519",
    "id_rsa",
    "key.properties",
    "keystore.properties",
    "local.properties",
    "mcp-oauth-tokens.json",
    "mcp-oauth-tokens-v2.json",
    "secrets.json",
    "service-account.json",
}
PUBLIC_MOBILE_CONFIGS = {
    "firebase_options.dart",
    "google-services.json",
    "googleservice-info.plist",
}
SAFE_ENV_SUFFIXES = (".defaults", ".example", ".sample", ".template")
CONTROL_TOKENS = {";", "&&", "||", "|", "&", ">", ">>", "<", "<<", "<<<"}

HIGH_CONFIDENCE_PATTERNS = (
    re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b"),
)
GOOGLE_API_KEY_PATTERN = re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")
ASSIGNMENT_PATTERN = re.compile(
    r"(?i)\b(?:access[_-]?token|api[_-]?key|client[_-]?secret|password|passwd|"
    r"private[_-]?key|refresh[_-]?token|secret|token)\b[\"']?\s*[:=]\s*"
    r"(?:\"(?P<double>[^\"\r\n]{8,})\"|'(?P<single>[^'\r\n]{8,})'|"
    r"(?P<bare>[^\s\"',;}{]{12,}))"
)
ENVIRONMENT_REFERENCE = re.compile(
    r"(?i)^(?:\$\{[A-Z_][A-Z0-9_]*\}|\$[A-Z_][A-Z0-9_]*|"
    r"%[A-Z_][A-Z0-9_]*%|process\.env\.[A-Z_][A-Z0-9_]*|"
    r"\{\{\s*[A-Z_][A-Z0-9_]*\s*\}\})$"
)


def _decision(kind: str, reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": kind,
            "permissionDecisionReason": reason,
        }
    }


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
        or not _is_absolute(cwd)
        or cwd.startswith("~")
    ):
        raise PolicyInputError("cwd must be a non-empty absolute path string")
    return tool_name.strip().lower(), tool_input, cwd


def _collect_string_values(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from _collect_string_values(item)


def _collect_content_values(tool_input: dict[str, Any]) -> Iterable[str]:
    for key, value in tool_input.items():
        if key.lower().replace("-", "_") in CONTENT_KEYS:
            yield from _collect_string_values(value)


def _extract_paths(tool: str, tool_input: dict[str, Any]) -> list[str]:
    paths: list[str] = []
    for key, value in tool_input.items():
        normalized_key = key.lower().replace("-", "_")
        if normalized_key in PATH_KEYS:
            paths.extend(_collect_string_values(value))
        elif tool in {"glob"} and normalized_key in {"pattern", "patterns"}:
            paths.extend(_collect_string_values(value))
    if tool in PATH_REQUIRED_TOOLS and not paths:
        raise PolicyInputError("file tool input contains no recognized path")
    return paths


def _has_traversal(path: str) -> bool:
    normalized = path.replace("\\", "/")
    return any(part == ".." for part in normalized.split("/"))


def _is_windows_path(path: str) -> bool:
    return bool(re.match(r"^[A-Za-z]:[\\/]", path)) or path.startswith("\\\\")


def _is_absolute(path: str) -> bool:
    return path.startswith("/") or path.startswith("~") or _is_windows_path(path)


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


def _is_env_secret(base_name: str) -> bool:
    if base_name.startswith(".env") and base_name.endswith(SAFE_ENV_SUFFIXES):
        return False
    if base_name == ".env" or base_name.startswith(".env."):
        return True
    return base_name.startswith(".env") and len(base_name) > 4 and base_name[4] in "*?["


def _is_protected(path: str) -> bool:
    normalized = path.strip().strip("\"'").replace("\\", "/").rstrip("/.,;:)")
    lowered = normalized.lower()
    parts = [part for part in lowered.split("/") if part not in {"", "."}]
    base_name = parts[-1] if parts else lowered
    if base_name in PUBLIC_MOBILE_CONFIGS:
        return False
    return (
        any(part in PROTECTED_DIRECTORIES for part in parts)
        or _is_env_secret(base_name)
        or base_name in PROTECTED_NAMES
        or base_name.endswith(PROTECTED_SUFFIXES)
        or bool(
            re.search(
                r"(?i)(?:service[-_]?account|appstoreconnect).*(?:\.json|\.p8)$",
                base_name,
            )
        )
    )


def _is_public_mobile_config(path: str) -> bool:
    normalized = path.strip().strip("\"'").replace("\\", "/").rstrip("/.,;:)")
    return normalized.rsplit("/", 1)[-1].lower() in PUBLIC_MOBILE_CONFIGS


def _looks_like_placeholder(value: str) -> bool:
    stripped = value.strip()
    lowered = stripped.lower()
    if ENVIRONMENT_REFERENCE.fullmatch(stripped):
        return True
    if stripped.startswith("<") and stripped.endswith(">"):
        return True
    normalized = re.sub(r"[^a-z0-9]+", "_", lowered).strip("_")
    markers = {
        "changeme",
        "dummy",
        "example",
        "fake",
        "placeholder",
        "redacted",
        "replace_me",
        "test_only",
    }
    if any(normalized == marker or normalized.startswith(marker + "_") for marker in markers):
        return True
    if normalized.startswith("your_"):
        return True
    collapsed = re.sub(r"[^a-z0-9]", "", lowered)
    return bool(collapsed) and len(set(collapsed)) <= 2


def _looks_like_unquoted_identifier(value: str) -> bool:
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", value):
        return False
    character_classes = sum(
        (
            any(character.islower() for character in value),
            any(character.isupper() for character in value),
            any(character.isdigit() for character in value),
        )
    )
    return character_classes < 3


def _contains_secret(value: str, allow_public_firebase_key: bool = False) -> bool:
    if any(pattern.search(value) for pattern in HIGH_CONFIDENCE_PATTERNS):
        return True
    if not allow_public_firebase_key and GOOGLE_API_KEY_PATTERN.search(value):
        return True
    for line in value.splitlines():
        for match in ASSIGNMENT_PATTERN.finditer(line):
            candidate = match.group("double") or match.group("single") or match.group("bare")
            if _looks_like_placeholder(candidate):
                continue
            if match.group("bare") and _looks_like_unquoted_identifier(candidate):
                continue
            return True
    return False


def _inspect_path(path: str, cwd: str) -> str | None:
    stripped = path.strip().strip("\"'")
    if not stripped or "\x00" in stripped:
        return "empty or invalid path"
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", stripped):
        return "non-file path supplied to a file operation"
    if _has_traversal(stripped):
        return "path traversal is not permitted"
    if not _within_cwd(stripped, cwd):
        return "path is outside the project working directory"
    if _is_protected(stripped):
        return "path targets a secret, signing asset, or protected file"
    return None


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
        if token in CONTROL_TOKENS or all(char in ";&|<>" for char in token):
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
        if executable in {"nohup", "time"}:
            result.pop(0)
            while result:
                if executable == "time" and result[0] in {"-f", "--format", "-o", "--output"}:
                    result = result[2:] if len(result) >= 2 else []
                    continue
                if result[0].startswith("-"):
                    result.pop(0)
                    continue
                break
            continue
        if executable == "nice":
            result.pop(0)
            if result[:1] == ["-n"]:
                result = result[2:] if len(result) >= 2 else []
            elif result and re.match(r"^-\d+$", result[0]):
                result.pop(0)
            continue
        if executable == "timeout":
            result.pop(0)
            while result:
                if result[0] in {"-k", "--kill-after", "-s", "--signal"}:
                    result = result[2:] if len(result) >= 2 else []
                    continue
                if result[0].startswith("-"):
                    result.pop(0)
                    continue
                result.pop(0)
                break
            continue
        break
    return result


def _search_command_paths(executable: str, args: list[str]) -> Iterable[str]:
    pattern_supplied = False
    files_mode = executable == "rg" and any(arg in {"--files", "--files-with-matches"} for arg in args)
    positionals: list[str] = []
    index = 0
    pattern_options = {"-e", "--regexp", "-g", "--glob", "--iglob", "--include", "--exclude"}
    path_options = {"-f", "--file", "--exclude-from"}
    options_with_value = pattern_options | path_options | {
        "-A",
        "-B",
        "-C",
        "--after-context",
        "--before-context",
        "--context",
        "--encoding",
        "--max-count",
        "--type",
        "--type-add",
        "--type-not",
    }
    while index < len(args):
        argument = args[index]
        if argument == "--":
            positionals.extend(args[index + 1 :])
            break
        if argument in options_with_value:
            if index + 1 < len(args):
                if argument in path_options:
                    yield args[index + 1]
                    pattern_supplied = True
                elif argument in {"-e", "--regexp"}:
                    pattern_supplied = True
                index += 2
                continue
        if argument.startswith(("--regexp=", "--glob=", "--iglob=", "--include=", "--exclude=")):
            if argument.startswith("--regexp="):
                pattern_supplied = True
            index += 1
            continue
        if argument.startswith(("--file=", "--exclude-from=")):
            yield argument.split("=", 1)[1]
            pattern_supplied = True
            index += 1
            continue
        if argument.startswith("-"):
            index += 1
            continue
        positionals.append(argument)
        index += 1
    if files_mode or pattern_supplied:
        yield from positionals
    elif positionals:
        yield from positionals[1:]


def _script_command_paths(executable: str, args: list[str]) -> Iterable[str]:
    script_supplied = False
    positionals: list[str] = []
    index = 0
    while index < len(args):
        argument = args[index]
        if argument == "--":
            positionals.extend(args[index + 1 :])
            break
        if argument in {"-e", "--expression"} and index + 1 < len(args):
            script_supplied = True
            index += 2
            continue
        if argument in {"-f", "--file"} and index + 1 < len(args):
            yield args[index + 1]
            script_supplied = True
            index += 2
            continue
        if executable == "awk" and argument == "-v" and index + 1 < len(args):
            index += 2
            continue
        if argument.startswith("-"):
            index += 1
            continue
        positionals.append(argument)
        index += 1
    if script_supplied:
        yield from positionals
    elif positionals:
        yield from positionals[1:]


def _file_command_paths(executable: str, args: list[str]) -> Iterable[str]:
    if executable in {"grep", "rg"}:
        yield from _search_command_paths(executable, args)
        return
    if executable in {"awk", "sed"}:
        yield from _script_command_paths(executable, args)
        return
    skip_next_for = {"-name", "-iname", "-path", "-ipath", "-regex", "-iregex", "-lname"}
    index = 0
    while index < len(args):
        argument = args[index]
        if executable == "find" and argument in skip_next_for:
            index += 2
            continue
        if argument.startswith("-") and not argument.startswith("../"):
            index += 1
            continue
        yield argument
        index += 1


def _inline_code_path_problem(script: str, cwd: str) -> str | None:
    file_api_markers = (
        "file.read",
        "file.write",
        "fs.read",
        "fs.write",
        "open(",
        "path(",
        "read_text",
        "write_text",
    )
    if not any(marker in script.lower() for marker in file_api_markers):
        return None
    for match in re.finditer(r"[\"']([^\"']+)[\"']", script):
        candidate = match.group(1)
        if _is_protected(candidate):
            return "inline code accesses a secret, signing asset, or protected file"
        if _has_traversal(candidate) or not _within_cwd(candidate, cwd):
            return "inline code accesses a path outside the project"
    return None


def _shell_path_problem(command: str, cwd: str, depth: int = 0) -> str | None:
    if depth > 3:
        return "nested shell evaluation exceeded the safe inspection limit"
    if "\x00" in command:
        return "shell command contains an invalid byte"
    tokens = _tokenize(command)
    for index, token in enumerate(tokens):
        if token not in {">", ">>", "<"}:
            continue
        if index + 1 >= len(tokens):
            return "shell redirection is missing a target"
        target = tokens[index + 1]
        if target.lower() in {"/dev/null", "nul"}:
            continue
        if _is_protected(target):
            return "shell redirection accesses a secret, signing asset, or protected file"
        if _has_traversal(target):
            return "shell redirection contains path traversal"
        if not _within_cwd(target, cwd):
            return "shell redirection targets a path outside the project"
    for segment in _segments(tokens):
        segment = _unwrap_segment(segment)
        if not segment:
            continue
        executable = _executable(segment[0])
        if executable in SHELL_INTERPRETERS:
            for flag in ("-c", "--command"):
                if flag in segment[1:]:
                    index = segment.index(flag)
                    if index + 1 >= len(segment):
                        return "nested shell input is malformed"
                    problem = _shell_path_problem(segment[index + 1], cwd, depth + 1)
                    if problem:
                        return problem
        if executable in CODE_INTERPRETERS:
            for flag in ("-c", "-e", "--eval"):
                if flag in segment[1:]:
                    index = segment.index(flag)
                    if index + 1 >= len(segment):
                        return "inline interpreter input is malformed"
                    problem = _inline_code_path_problem(segment[index + 1], cwd)
                    if problem:
                        return problem
        if executable not in SHELL_FILE_COMMANDS:
            continue
        for token in _file_command_paths(executable, segment[1:]):
            if _is_protected(token):
                return "shell command accesses a secret, signing asset, or protected file"
            if _has_traversal(token):
                return "shell file operation contains path traversal"
            if not _within_cwd(token, cwd):
                return "shell file operation targets a path outside the project"
    return None


def evaluate(payload: Any) -> dict[str, Any]:
    tool, tool_input, cwd = _validate_payload(payload)
    if tool in FILE_TOOLS:
        paths = _extract_paths(tool, tool_input)
        for path in paths:
            problem = _inspect_path(path, cwd)
            if problem:
                return _decision("deny", f"Protected-file policy blocked the operation: {problem}.")
        if tool in WRITE_TOOLS:
            allow_public_firebase_key = bool(paths) and all(
                _is_public_mobile_config(path) for path in paths
            )
            if any(
                _contains_secret(content, allow_public_firebase_key)
                for content in _collect_content_values(tool_input)
            ):
                return _decision(
                    "deny",
                    "Protected-file policy blocked high-confidence credential or private-key content.",
                )
    elif tool in SHELL_TOOLS:
        command = tool_input.get("command", tool_input.get("cmd"))
        if not isinstance(command, str) or not command.strip():
            raise PolicyInputError("shell tool input must contain a non-empty command")
        problem = _shell_path_problem(command, cwd)
        if problem:
            return _decision("deny", f"Protected-file policy blocked the operation: {problem}.")
        allow_public_firebase_key = any(
            config_name in command.lower() for config_name in PUBLIC_MOBILE_CONFIGS
        )
        if _contains_secret(command, allow_public_firebase_key):
            return _decision(
                "deny",
                "Protected-file policy blocked high-confidence credential or private-key content.",
            )
    return {}


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
        (_payload("read_file", {"file_path": "README.md"}), None),
        (_payload("read_file", {"file_path": ".env.example"}), None),
        (_payload("read_file", {"file_path": ".env.production.template"}), None),
        (_payload("read_file", {"file_path": ".env"}), "deny"),
        (_payload("read_file", {"file_path": "android/app/google-services.json"}), None),
        (_payload("write_file", {"file_path": "../secret.txt"}), "deny"),
        (_payload("read_file", {"file_path": "/etc/passwd"}), "deny"),
        (_payload("read_file", {"file_path": "..\\secret.txt"}, "C:\\work\\app"), "deny"),
        (
            _payload(
                "write_file",
                {"file_path": "src/config.txt", "content": "password=ActualSecret123456"},
            ),
            "deny",
        ),
        (
            _payload(
                "write_file",
                {"file_path": "src/config.txt", "content": "CLIENT_SECRET=${CLIENT_SECRET}"},
            ),
            None,
        ),
        (
            _payload(
                "write_file",
                {
                    "file_path": "android/app/google-services.json",
                    "content": '{"current_key":"AIzaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"}',
                },
            ),
            None,
        ),
        (_payload("run_shell_command", {"command": "echo '.env'"}), None),
        (_payload("run_shell_command", {"command": "rg '\\.env' README.md"}), None),
        (_payload("run_shell_command", {"command": "grep -f .env README.md"}), "deny"),
        (_payload("run_shell_command", {"command": "env MODE=test cat .env"}), "deny"),
        (_payload("run_shell_command", {"command": "nohup cat .env"}), "deny"),
        (_payload("run_shell_command", {"command": "bash -c 'cat .env'"}), "deny"),
        (
            _payload("run_shell_command", {"command": 'python3 -c "open(\'.env\').read()"'}),
            "deny",
        ),
        (
            _payload("run_shell_command", {"command": "echo client_secret=ActualSecret123456"}),
            "deny",
        ),
        (_payload("run_shell_command", {"command": "cat .env"}), "deny"),
        (_payload("run_shell_command", {"command": "printf value > ../outside.txt"}), "deny"),
        (_payload("run_shell_command", {"command": "printf value > /dev/null"}), None),
    ]
    for payload, expected in cases:
        actual = _result_decision(evaluate(payload))
        if actual != expected:
            raise AssertionError(f"expected {expected!r}, got {actual!r}")
    print("secret-and-protected-file-guard self-test: ok")
    return 0


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    try:
        payload = json.load(sys.stdin)
        result = evaluate(payload)
    except (json.JSONDecodeError, PolicyInputError) as exc:
        print(f"secret-and-protected-file-guard: invalid input: {exc}", file=sys.stderr)
        return 2
    except Exception:
        print("secret-and-protected-file-guard: internal policy failure", file=sys.stderr)
        return 2
    if result:
        print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
