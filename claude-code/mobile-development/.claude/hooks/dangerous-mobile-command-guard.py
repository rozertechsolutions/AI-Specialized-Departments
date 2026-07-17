#!/usr/bin/env python3
"""Deny destructive or scope-escaping shell commands before execution."""

from __future__ import annotations

import ntpath
import os
import posixpath
import re
import shlex
from typing import Any, List, Mapping, Optional, Sequence, Tuple

from hook_common import (
    HookInputError,
    emit_pretool_decision,
    normalize_target,
    project_root,
    protected_path_reason,
    read_event,
    tool_input,
)


SEPARATORS = {"&&", "||", ";", "|", "|&"}
REDIRECTIONS = {">", ">>", "<", "<<", "<<<", ">&", "<&", "<>"}
GENERATED_ROOTS = {
    ".gradle",
    ".dart_tool",
    ".cxx",
    ".kotlin",
    ".build",
    "build",
    "coverage",
    "deriveddata",
    "android/.gradle",
    "android/.cxx",
    "android/build",
    "ios/build",
}


def tokenize(command: str, *, posix: bool) -> List[str]:
    lexer = shlex.shlex(command, posix=posix, punctuation_chars=";&|<>")
    lexer.whitespace_split = True
    lexer.commenters = ""
    return list(lexer)


def _redirection_operator(token: str) -> Optional[str]:
    match = re.fullmatch(r"\d*(>>?|<<?|<<<|>&|<&|<>)", token)
    if match:
        return match.group(1)
    return token if token in REDIRECTIONS else None


def validate_path(
    raw: str,
    root: str,
    cwd: str,
    *,
    allow_dev_null: bool = False,
) -> Optional[str]:
    candidate = raw.strip("\"'")
    if allow_dev_null and candidate.lower() in {"/dev/null", "nul"}:
        return None
    reason = protected_path_reason(candidate)
    if reason:
        return f"path references {reason}: {candidate}"
    try:
        normalized = normalize_target(candidate, root, cwd=cwd)
    except HookInputError as exc:
        return str(exc)
    if normalized.traversal:
        return f"path contains '..' traversal: {candidate}"
    if not normalized.within_root:
        return f"path escapes CLAUDE_PROJECT_DIR: {candidate}"
    reason = protected_path_reason(normalized.relative)
    if reason:
        return f"resolved path references {reason}: {candidate}"
    return None


def split_segments(
    tokens: Sequence[str], root: str, cwd: str
) -> Tuple[List[List[str]], Optional[str]]:
    segments: List[List[str]] = []
    current: List[str] = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token == "&":
            return [], "background execution with '&' is not allowed"
        if token in SEPARATORS:
            if not current:
                return [], f"shell operator {token!r} has no preceding command"
            segments.append(current)
            current = []
            index += 1
            continue

        operator = _redirection_operator(token)
        if operator:
            if operator in {"<<", "<<<"}:
                return [], "heredoc and here-string redirection are not allowed"
            if current and current[-1].isdigit() and token == operator:
                current.pop()
            index += 1
            if index >= len(tokens):
                return [], "redirection is missing its target"
            target = tokens[index]
            if operator in {">&", "<&"} and target.isdigit():
                index += 1
                continue
            reason = validate_path(target, root, cwd, allow_dev_null=True)
            if reason:
                return [], f"unsafe redirection: {reason}"
            index += 1
            continue

        current.append(token)
        index += 1

    if current:
        segments.append(current)
    if not segments:
        return [], "command contains no executable segment"
    return segments, None


def command_basename(command: str) -> str:
    return ntpath.basename(posixpath.basename(command)).lower()


def unwrap_wrapper(tokens: Sequence[str]) -> Tuple[List[str], Optional[str]]:
    current = list(tokens)
    for _ in range(4):
        if not current:
            return [], "command wrapper has no inner command"
        base = command_basename(current[0])
        if base not in {"env", "command", "time", "timeout", "nice", "nohup", "stdbuf"}:
            return current, None

        index = 1
        if base == "env":
            while index < len(current):
                item = current[index]
                if re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", item):
                    index += 1
                elif item in {"-i", "--ignore-environment", "--null"}:
                    index += 1
                elif item in {"-u", "--unset"}:
                    if index + 1 >= len(current):
                        return [], "env --unset is missing its variable name"
                    index += 2
                elif item.startswith("--unset="):
                    index += 1
                elif item == "--":
                    index += 1
                    break
                elif item.startswith("-"):
                    return [], f"environment wrapper option is blocked: {item}"
                else:
                    break
        elif base == "command":
            while index < len(current) and current[index].startswith("-"):
                index += 1
        elif base in {"time", "nohup"}:
            while index < len(current) and current[index].startswith("-"):
                item = current[index]
                index += 1
                if base == "nohup" and item != "--":
                    return [], f"nohup wrapper option is blocked: {item}"
                if base == "time" and item in {"-f", "--format", "-o", "--output"}:
                    if index >= len(current):
                        return [], f"{item} is missing its value"
                    index += 1
        elif base == "timeout":
            while index < len(current) and current[index].startswith("-"):
                if current[index] in {"-k", "--kill-after", "-s", "--signal"}:
                    index += 1
                index += 1
            if index < len(current):
                index += 1
        elif base == "nice":
            while index < len(current) and current[index].startswith("-"):
                if current[index] in {"-n", "--adjustment"}:
                    index += 1
                index += 1
        elif base == "stdbuf":
            while index < len(current) and current[index].startswith("-"):
                item = current[index]
                index += 1
                if item in {"-i", "-o", "-e"}:
                    if index >= len(current):
                        return [], f"{item} is missing its buffering mode"
                    index += 1
        current = current[index:]
    return [], "too many nested command wrappers"


def validate_executable(raw: str, root: str, cwd: str) -> Optional[str]:
    if raw.startswith("./") or raw.startswith(".\\") or re.search(r"[\\/]", raw):
        normalized = normalize_target(raw, root, cwd=cwd)
        if normalized.traversal:
            return f"executable path contains '..' traversal: {raw}"
        if normalized.within_root:
            return None
        posix_trusted = (
            "/bin/",
            "/usr/bin/",
            "/usr/local/bin/",
            "/opt/homebrew/bin/",
            "/Applications/Xcode.app/Contents/Developer/usr/bin/",
        )
        windows_trusted = ("c:\\windows\\system32\\", "c:\\program files\\")
        lowered = normalized.absolute.lower()
        if normalized.windows_style and lowered.startswith(windows_trusted):
            return None
        if not normalized.windows_style and normalized.absolute.startswith(posix_trusted):
            return None
        return f"executable is outside CLAUDE_PROJECT_DIR: {raw}"
    return None


def validate_generic_paths(tokens: Sequence[str], root: str, cwd: str) -> Optional[str]:
    for token in tokens:
        candidate = token.strip("\"'")
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", candidate):
            continue
        if candidate.startswith("-") and "=" not in candidate:
            continue
        if "=" in candidate:
            key, value = candidate.split("=", 1)
            if key.startswith("-") or re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", key):
                candidate = value
        if not candidate or candidate.lower() in {"/dev/null", "nul"}:
            continue
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", candidate):
            continue
        if candidate.startswith("~") or re.search(r"(^|[\\/])\.\.([\\/]|$)", candidate):
            return f"argument uses a home or traversal path: {candidate}"
        is_path = (
            candidate.startswith(("/", "./", ".\\", "\\\\"))
            or bool(re.match(r"^[A-Za-z]:[\\/]", candidate))
            or "/" in candidate
            or "\\" in candidate
        )
        if not is_path and not re.match(r"^[A-Za-z]:[\\/]", cwd):
            is_path = os.path.lexists(os.path.join(cwd, candidate))
        if is_path:
            reason = validate_path(candidate, root, cwd, allow_dev_null=True)
            if reason:
                return reason
    return None


def validate_generated_delete(args: Sequence[str], root: str, cwd: str) -> Optional[str]:
    paths = [arg for arg in args if arg != "--" and not arg.startswith("-")]
    if not paths:
        return "delete command has no explicit generated-output target"
    for raw in paths:
        if any(char in raw for char in "{}[]"):
            return f"delete target uses ambiguous expansion: {raw}"
        normalized = normalize_target(raw, root, cwd=cwd)
        if normalized.traversal or not normalized.within_root:
            return f"delete target escapes project scope: {raw}"
        relative = normalized.relative.replace("\\", "/").lower().rstrip("/")
        relative = relative.split("/*", 1)[0]
        if not any(relative == item or relative.startswith(item + "/") for item in GENERATED_ROOTS):
            return f"delete target is not recognized generated output: {raw}"
    return None


def validate_git(args: Sequence[str]) -> Optional[str]:
    remaining = list(args)
    index = 0
    while index < len(remaining) and remaining[index].startswith("-"):
        option = remaining[index]
        if option == "-c" or option.startswith("-c") and len(option) > 2:
            return "Git configuration overrides are blocked"
        if option == "--config-env" or option.startswith("--config-env="):
            return "Git environment-backed configuration overrides are blocked"
        if option == "--exec-path" or option.startswith("--exec-path="):
            return "Git executable-path overrides are blocked"
        if option in {"-C", "--git-dir", "--work-tree", "--namespace"}:
            index += 2
            continue
        if option.startswith(("-C", "--git-dir=", "--work-tree=", "--namespace=")):
            index += 1
            continue
        if option in {
            "--no-pager",
            "--paginate",
            "-p",
            "--literal-pathspecs",
            "--glob-pathspecs",
            "--noglob-pathspecs",
            "--icase-pathspecs",
        }:
            index += 1
            continue
        return f"unrecognized Git global option is blocked: {option}"
    if index >= len(remaining):
        return None
    subcommand = remaining[index].lower()
    rest = [item.lower() for item in remaining[index + 1 :]]
    if subcommand in {
        "config",
        "filter-branch",
        "gc",
        "prune",
        "reflog",
        "replace",
        "reset",
        "restore",
        "update-ref",
        "clean",
        "rm",
    }:
        return f"destructive Git operation is blocked: git {subcommand}"
    if subcommand == "checkout":
        return "git checkout is blocked because it can replace working-tree content; use an approved git switch for branch changes"
    if subcommand == "switch" and any(
        item in {"-f", "--force", "--discard-changes"} for item in rest
    ):
        return "destructive git switch is blocked"
    if subcommand == "mv" and any(item in {"-f", "--force"} for item in rest):
        return "forced Git move is blocked"
    if subcommand == "branch" and any(item in {"-d", "-D", "--delete"} for item in remaining[index + 1 :]):
        return "Git branch deletion is blocked"
    if subcommand == "tag" and any(item in {"-d", "--delete"} for item in rest):
        return "Git tag deletion is blocked"
    if subcommand == "push" and any(
        "force" in item
        or item in {"--delete", "-d", "--mirror", "--prune"}
        or item.startswith(("+", ":"))
        for item in rest
    ):
        return "destructive remote Git push is blocked"
    if subcommand == "stash" and any(item in {"drop", "clear", "pop"} for item in rest):
        return "destructive git stash operation is blocked"
    if subcommand == "rebase":
        return "git rebase is blocked by the specialization safety policy"
    if subcommand in {"merge", "cherry-pick", "revert", "am"} and any(
        item in {"--abort", "--quit"} for item in rest
    ):
        return f"destructive git {subcommand} state change is blocked"
    if subcommand == "remote" and any(
        item in {"add", "remove", "rename", "set-head", "set-branches", "set-url", "prune"}
        for item in rest[:1]
    ):
        return "Git remote configuration mutation is blocked"
    if subcommand == "worktree" and any(
        item in {"remove", "prune", "move", "lock", "unlock"} for item in rest[:1]
    ):
        return "destructive Git worktree mutation is blocked"
    if subcommand == "submodule" and any(item in {"deinit", "absorbgitdirs"} for item in rest[:1]):
        return "destructive Git submodule mutation is blocked"
    return None


def uses_inline_interpreter(base: str, args: Sequence[str]) -> bool:
    inline_options = {
        "node": {"-e", "--eval", "-p", "--print"},
        "perl": {"-e"},
        "ruby": {"-e", "--eval"},
    }
    python = bool(re.fullmatch(r"python\d*(?:\.\d+)?(?:\.exe)?", base))
    targets = {"-c"} if python else inline_options.get(base, set())
    if not targets:
        return False

    options_with_value = {
        "node": {"-r", "--require", "--import"},
        "perl": {"-I", "-M", "-m"},
        "ruby": {"-I", "-r", "--require"},
    }.get(base, set())
    if python:
        options_with_value = {"-W", "-X", "--check-hash-based-pycs"}

    index = 0
    while index < len(args):
        item = args[index]
        if (
            item in targets
            or any(item.startswith(option + "=") for option in targets)
            or any(
                option.startswith("-")
                and not option.startswith("--")
                and item.startswith(option)
                and len(item) > len(option)
                for option in targets
            )
        ):
            return True
        if python and item == "-m":
            return False
        if item == "--" or not item.startswith("-"):
            return False
        if item in options_with_value:
            index += 2
        else:
            index += 1
    return False


def package_mutation_reason(base: str, args: Sequence[str]) -> Optional[str]:
    package_commands = {
        "npm": {"install", "i", "ci", "add", "update", "upgrade", "dedupe", "link", "uninstall", "remove", "rm"},
        "pnpm": {"install", "i", "add", "update", "upgrade", "link", "remove", "rm"},
        "yarn": {"install", "add", "up", "upgrade", "link", "remove"},
        "bun": {"install", "add", "update", "upgrade", "remove"},
        "pod": {"install", "update"},
        "bundle": {"install", "update", "add"},
        "gem": {"install", "update", "uninstall"},
        "pip": {"install", "uninstall"},
        "pip3": {"install", "uninstall"},
    }
    blocked = package_commands.get(base)
    if blocked:
        for arg in args:
            lowered = arg.lower()
            if lowered == "run":
                return None
            if lowered.startswith("-"):
                continue
            if lowered in blocked:
                return f"package dependency mutation is blocked: {base} {lowered}"

    python = bool(re.fullmatch(r"python\d*(?:\.\d+)?(?:\.exe)?", base))
    if python and len(args) >= 3 and args[0] == "-m" and command_basename(args[1]) in {"pip", "pip3"}:
        subcommand = args[2].lower()
        if subcommand in {"install", "uninstall"}:
            return f"package dependency mutation is blocked: python -m {command_basename(args[1])} {subcommand}"
    return None


def validate_segment(
    tokens: Sequence[str], root: str, cwd: str, *, shell_tool: str
) -> Optional[str]:
    current = list(tokens)
    assignments: List[str] = []
    while current and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", current[0]):
        assignment = current.pop(0)
        key = assignment.split("=", 1)[0].upper()
        if key in {
            "BASH_ENV",
            "ENV",
            "GIT_CONFIG_COUNT",
            "GIT_CONFIG_GLOBAL",
            "GIT_CONFIG_SYSTEM",
            "GIT_EXEC_PATH",
            "IFS",
            "LD_PRELOAD",
            "NODE_OPTIONS",
            "PATH",
            "PERL5OPT",
            "PROMPT_COMMAND",
            "PYTHONPATH",
            "RUBYOPT",
            "SHELLOPTS",
        } or key.startswith("DYLD_"):
            return f"execution-control environment assignment is blocked: {key}"
        assignments.append(assignment)
    if not current:
        return "environment assignment has no command"

    unwrapped, reason = unwrap_wrapper(current)
    if reason:
        return reason
    executable = unwrapped[0]
    args = list(unwrapped[1:])
    base = command_basename(executable)

    reason = validate_executable(executable, root, cwd)
    if reason:
        return reason
    reason = validate_generic_paths([*assignments, *args], root, cwd)
    if reason:
        return reason
    reason = package_mutation_reason(base, args)
    if reason:
        return reason

    always_blocked = {
        "sudo",
        "su",
        "doas",
        "dd",
        "mkfs",
        "fdisk",
        "shutdown",
        "reboot",
        "halt",
        "poweroff",
        "chown",
        "builtin",
        "declare",
        "exec",
        "export",
        "printenv",
        "launchctl",
        "nc",
        "netcat",
        "osascript",
        "reg",
        "reg.exe",
        "shred",
        "ssh",
        "systemctl",
        "telnet",
        "truncate",
        "unlink",
        "set",
        "typeset",
        "xargs",
        "eval",
        "source",
        "bash",
        "sh",
        "zsh",
        "ksh",
        "fish",
        "powershell",
        "powershell.exe",
        "pwsh",
    }
    if base in always_blocked:
        return f"high-risk command is blocked: {base}"
    if uses_inline_interpreter(base, args):
        return f"inline interpreter execution is blocked: {base}"
    if base == "cd":
        targets = [item for item in args if not item.startswith("-")]
        if not targets or args == ["-"]:
            return "implicit or previous-directory cd is blocked"
        return validate_path(targets[-1], root, cwd)
    if base in {"pushd", "popd"}:
        return f"directory-stack mutation is blocked: {base}"
    if shell_tool == "PowerShell":
        if base in {"remove-item", "ri", "del", "erase", "rd"}:
            return validate_generated_delete(args, root, cwd)
        powershell_bypass_or_system_commands = {
            ".",
            "clear-content",
            "clear-disk",
            "cmd",
            "cmd.exe",
            "enter-pssession",
            "format-volume",
            "iex",
            "initialize-disk",
            "invoke-command",
            "invoke-expression",
            "new-pssession",
            "remove-partition",
            "restart-computer",
            "start-process",
            "stop-computer",
        }
        if base in powershell_bypass_or_system_commands:
            return f"high-risk PowerShell command is blocked: {base}"
        if base in {"set-location", "sl", "chdir"}:
            targets = [item for item in args if not item.startswith("-")]
            if not targets or args == ["-"]:
                return "implicit or previous PowerShell location change is blocked"
            return validate_path(targets[-1], root, cwd)
        if base in {"push-location", "pop-location"}:
            return f"PowerShell location-stack mutation is blocked: {base}"
    if base in {"chmod", "chflags"}:
        return f"permission or file-flag changes are blocked: {base}"
    if base in {"kill", "killall", "pkill"}:
        return f"process termination is blocked: {base}"
    if base == "diskutil" and args and args[0].lower() in {"erasevolume", "erasedisk", "partitiondisk", "apfs"}:
        return "destructive diskutil operation is blocked"
    if base == "defaults" and args and args[0].lower() in {"write", "delete", "rename", "import"}:
        return "system preference mutation is blocked"
    if base == "plutil" and any(arg.lower() in {"-replace", "-insert", "-remove"} for arg in args):
        return "plist mutation through the shell is blocked; use a scoped edit so review hooks run"
    if base in {"rm", "rmdir"}:
        return validate_generated_delete(args, root, cwd)
    if base == "find" and any(arg in {"-delete", "-exec", "-execdir", "-ok", "-okdir"} for arg in args):
        return "find deletion or command execution is blocked"
    if base == "git":
        return validate_git(args)
    if base == "adb" and args and args[0].lower() == "shell" and any(
        item.lower() in {"rm", "rmdir", "reboot", "uninstall", "clear", "reset", "wipe-data"}
        for item in args[1:]
    ):
        return "destructive Android device command is blocked"
    if base == "xcrun" and len(args) > 1 and args[0].lower() == "simctl" and args[1].lower() in {
        "delete",
        "erase",
    }:
        return "destructive Apple simulator command is blocked"
    if base == "avdmanager" and args and args[0].lower() == "delete":
        return "Android virtual-device deletion is blocked"
    if base == "sdkmanager" and any(arg.lower() == "--uninstall" for arg in args):
        return "Android SDK removal is blocked"
    if base == "docker" and any(arg.lower() in {"rm", "rmi", "prune"} for arg in args):
        return "destructive Docker operation is blocked"
    if base == "kubectl" and args and args[0].lower() in {"delete", "drain", "replace"}:
        return "destructive Kubernetes operation is blocked"
    if base == "terraform" and args and args[0].lower() in {"destroy", "apply"}:
        return "infrastructure mutation is outside mobile specialization scope"
    return None


def command_reason(command: str, root: str, cwd: str, *, shell_tool: str) -> Optional[str]:
    if not command.strip():
        return "Bash command is empty"
    if "\x00" in command:
        return "command contains a NUL byte"
    if "\n" in command or "\r" in command:
        return "multiline shell commands are not allowed"
    if re.search(r"`|\$\(|<\(|>\(", command):
        return "command substitution or process substitution is not allowed"
    if "$" in command:
        return "shell variable expansion is not allowed in guarded commands"
    if shell_tool == "PowerShell" and re.search(
        r"(?<![A-Za-z0-9_])(?:Env|Cert|Variable|Function|Alias|Registry|HKLM|HKCU|WSMan):",
        command,
        flags=re.IGNORECASE,
    ):
        return "PowerShell environment, credential, registry, or executable providers are blocked"
    encoded_patterns = (
        r"\bbase64\b[^|;&]*(?:-d|--decode)\b",
        r"\bopenssl\b[^|;&]*\bbase64\b[^|;&]*(?:-d|--decode)\b",
        r"\bpowershell(?:\.exe)?\b[^|;&]*(?:-enc|-encodedcommand)\b",
        r"\b(?:ba|z|k)?sh\b\s+-c\b",
    )
    if any(re.search(pattern, command, flags=re.IGNORECASE) for pattern in encoded_patterns):
        return "encoded or inline interpreter execution is not allowed"

    try:
        tokens = tokenize(command, posix=shell_tool == "Bash")
    except ValueError:
        return "command quoting is malformed and cannot be inspected safely"
    segments, reason = split_segments(tokens, root, cwd)
    if reason:
        return reason
    for segment in segments:
        reason = validate_segment(segment, root, cwd, shell_tool=shell_tool)
        if reason:
            return reason
    return None


def shell_command_reason(
    shell_tool: str, payload: Mapping[str, Any], root: str, cwd: str
) -> Optional[str]:
    """Return the deterministic policy failure for one shell tool payload."""
    if shell_tool not in {"Bash", "PowerShell"}:
        raise HookInputError("expected a Bash or PowerShell tool")
    command = payload.get("command")
    if not isinstance(command, str):
        raise HookInputError("shell command is required")
    cwd_check = normalize_target(cwd, root, cwd=root)
    if cwd_check.traversal or not cwd_check.within_root:
        return "working directory is outside project scope"
    return command_reason(command, root, cwd, shell_tool=shell_tool)


def main() -> int:
    try:
        event = read_event()
        shell_tool = event.get("tool_name")
        if event.get("hook_event_name") != "PreToolUse" or shell_tool not in {
            "Bash",
            "PowerShell",
        }:
            raise HookInputError("expected a PreToolUse Bash or PowerShell event")
        payload = tool_input(event)
        root = project_root(event)
        cwd = event.get("cwd") if isinstance(event.get("cwd"), str) else root
        reason = shell_command_reason(shell_tool, payload, root, cwd)
        if reason:
            return emit_pretool_decision("deny", f"Dangerous-command guard blocked the operation: {reason}.")
        return 0
    except HookInputError as exc:
        return emit_pretool_decision("deny", f"Dangerous-command guard failed closed: {exc}.")
    except Exception:
        return emit_pretool_decision("deny", "Dangerous-command guard failed closed because validation could not complete.")


if __name__ == "__main__":
    raise SystemExit(main())
