#!/usr/bin/env python3
"""Deny destructive commands and require review for high-impact state changes."""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
import unicodedata
from typing import Any


COMMAND_KEYS = {"command", "cmd", "script", "shell_command", "shellcommand"}
SHELLS = {"bash", "cmd", "cmd.exe", "dash", "fish", "powershell", "powershell.exe", "pwsh", "sh", "zsh"}
INTERPRETERS = {"bun", "deno", "node", "perl", "php", "python", "python3", "ruby"}
PACKAGE_MANAGERS = {
    "apt",
    "apt-get",
    "brew",
    "bundle",
    "choco",
    "dnf",
    "flutter",
    "gem",
    "npm",
    "pip",
    "pip3",
    "pnpm",
    "pod",
    "pub",
    "winget",
    "yarn",
    "yum",
}
GIT_REVIEW_ACTIONS = {
    "add",
    "am",
    "apply",
    "branch",
    "checkout",
    "cherry-pick",
    "clean",
    "commit",
    "merge",
    "mv",
    "rebase",
    "reset",
    "revert",
    "rm",
    "stash",
    "switch",
    "tag",
    "worktree",
}


def _deny(reason: str) -> dict[str, str]:
    return {"permissionDecision": "deny", "permissionDecisionReason": reason}


def _ask(reason: str) -> dict[str, str]:
    return {"permissionDecision": "ask", "permissionDecisionReason": reason}


def _extract_command(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key, item in value.items():
            if str(key).casefold() in COMMAND_KEYS and isinstance(item, str):
                return item
        for item in value.values():
            command = _extract_command(item)
            if command is not None:
                return command
    if isinstance(value, list):
        for item in value:
            command = _extract_command(item)
            if command is not None:
                return command
    return None


def _split_top_level(command: str) -> tuple[list[str], list[str]]:
    segments: list[str] = []
    operators: list[str] = []
    buffer: list[str] = []
    quote = ""
    escaped = False
    index = 0
    while index < len(command):
        char = command[index]
        if escaped:
            buffer.append(char)
            escaped = False
            index += 1
            continue
        if char == "\\" and quote != "'":
            buffer.append(char)
            escaped = True
            index += 1
            continue
        if quote:
            buffer.append(char)
            if char == quote:
                quote = ""
            index += 1
            continue
        if char in {"'", '"'}:
            quote = char
            buffer.append(char)
            index += 1
            continue
        if char in {";", "|", "&", "\n"}:
            segment = "".join(buffer).strip()
            if segment:
                segments.append(segment)
            buffer = []
            operator = char
            if index + 1 < len(command) and command[index + 1] == char and char in {"|", "&"}:
                operator += char
                index += 1
            operators.append(operator)
            index += 1
            continue
        buffer.append(char)
        index += 1
    segment = "".join(buffer).strip()
    if segment:
        segments.append(segment)
    return segments, operators


def _tokens(segment: str) -> list[str]:
    stripped = segment.strip().strip("() ")
    windows_like = bool(re.search(r"[A-Za-z]:\\", stripped)) or bool(
        re.search(r"(?i)\b(?:Remove-Item|Clear-Disk|Format-Volume)\b", stripped)
    )
    try:
        values = shlex.split(stripped, posix=not windows_like)
    except ValueError:
        return []
    return [value.strip("\"'") for value in values]


def _executable(token: str) -> str:
    normalized = token.replace("\\", "/").rstrip("/")
    return normalized.rsplit("/", 1)[-1].casefold()


def _unwrap(tokens: list[str]) -> list[str]:
    remaining = list(tokens)
    while remaining:
        executable = _executable(remaining[0])
        if executable in {"command", "env", "nohup"}:
            remaining.pop(0)
            while remaining and "=" in remaining[0] and not remaining[0].startswith(("/", "-")):
                remaining.pop(0)
            continue
        if executable == "bundle" and len(remaining) > 1 and remaining[1].casefold() == "exec":
            remaining = remaining[2:]
            continue
        break
    return remaining


def _root_or_traversal(path: str) -> bool:
    normalized = path.strip("\"' ").replace("\\", "/").casefold().rstrip("/")
    if normalized in {"", ".", "..", "/", "/*", "~", "$home", "${home}", "%userprofile%", "*"}:
        return True
    if normalized.startswith("../") or "/../" in f"/{normalized}/":
        return True
    if re.fullmatch(r"[a-z]:", normalized):
        return True
    return normalized.startswith(("/etc", "/system", "/usr", "/var", "/dev", "c:/windows", "c:/program files"))


def _outside_repository(path: str, cwd: str) -> bool:
    normalized = path.strip("\"' ").replace("\\", "/")
    if re.match(r"^[A-Za-z]:/", normalized):
        cwd_normalized = cwd.replace("\\", "/").casefold().rstrip("/")
        path_normalized = normalized.casefold().rstrip("/")
        return not cwd_normalized or (
            path_normalized != cwd_normalized and not path_normalized.startswith(cwd_normalized + "/")
        )
    if os.path.isabs(normalized):
        if not cwd or not os.path.isabs(cwd):
            return True
        try:
            return os.path.commonpath((os.path.abspath(normalized), os.path.abspath(cwd))) != os.path.abspath(cwd)
        except ValueError:
            return True
    return False


def _deletion_decision(targets: list[str], cwd: str) -> dict[str, str]:
    if not targets:
        return _deny("A deletion command without a reviewable target is blocked.")
    if any(_root_or_traversal(target) or _outside_repository(target, cwd) for target in targets):
        return _deny("Deletion of a root, system, traversal, or out-of-repository path is blocked.")
    return _ask("Deleting repository files requires explicit human approval.")


def _git_action(args: list[str]) -> tuple[str, list[str]]:
    index = 0
    value_options = {"-c", "-C", "--config-env", "--git-dir", "--namespace", "--work-tree"}
    flag_options = {
        "--bare",
        "--literal-pathspecs",
        "--no-optional-locks",
        "--no-pager",
        "--no-replace-objects",
        "--noglob-pathspecs",
        "--optional-locks",
        "--paginate",
    }
    value_prefixes = ("--config-env=", "--git-dir=", "--namespace=", "--work-tree=")
    while index < len(args):
        option = args[index]
        lowered_option = option.casefold()
        if option in value_options:
            index += 2
            continue
        if lowered_option in flag_options or lowered_option.startswith(value_prefixes):
            index += 1
            continue
        break
    if index >= len(args):
        return "", []
    return args[index].casefold(), [arg.casefold() for arg in args[index + 1 :]]


def _find_search_roots(args: list[str]) -> list[str]:
    index = 0
    while index < len(args):
        option = args[index]
        if option in {"-H", "-L", "-P"} or option.startswith("-O"):
            index += 1
            continue
        if option == "-D":
            index += 2
            continue
        break
    roots: list[str] = []
    while index < len(args) and not args[index].startswith("-") and args[index] not in {"!", "("}:
        roots.append(args[index])
        index += 1
    return roots or ["."]


def _batch_command(args: list[str]) -> list[str]:
    index = 0
    value_options = {"-E", "-I", "-L", "-P", "-n", "-s", "--eof", "--max-args", "--max-chars", "--max-lines", "--max-procs", "--replace"}
    while index < len(args):
        option = args[index]
        if option in value_options:
            index += 2
            continue
        if option.startswith("-"):
            index += 1
            continue
        break
    return _unwrap(args[index:])


def _redirection_decision(segment: str, cwd: str) -> dict[str, str] | None:
    for match in re.finditer(r"(?:^|\s)(?:\d*>>?|<)\s*([^\s;&|]+)", segment):
        target = match.group(1).strip("\"'")
        if _root_or_traversal(target):
            return _deny("Shell redirection to a root, protected system, or traversal path is blocked.")
        if _outside_repository(target, cwd):
            return _ask("Shell redirection outside the repository requires explicit human approval.")
    return None


def _package_decision(executable: str, args: list[str]) -> dict[str, str] | None:
    lowered = [arg.casefold() for arg in args]
    if executable not in PACKAGE_MANAGERS:
        return None
    mutating_actions = {
        "add",
        "ci",
        "get",
        "install",
        "remove",
        "uninstall",
        "update",
        "upgrade",
    }
    if executable == "flutter" and lowered[:2] == ["pub", "get"]:
        return _ask("Dependency resolution or installation requires explicit human approval.")
    if any(action in lowered[:3] for action in mutating_actions):
        return _ask("Package, plugin, or tool installation/change requires explicit human approval.")
    return None


def _segment_decision(segment: str, cwd: str, depth: int) -> dict[str, str] | None:
    redirection = _redirection_decision(segment, cwd)
    if redirection:
        return redirection

    tokens = _unwrap(_tokens(segment))
    if not tokens:
        return _deny("The shell command could not be parsed safely.")
    executable = _executable(tokens[0])
    args = tokens[1:]
    lowered = [arg.casefold() for arg in args]

    if executable in {"eval", "iex", "invoke-expression"}:
        return _deny("Dynamic command evaluation is blocked because its effects cannot be reviewed deterministically.")
    if executable in {"sudo", "su", "doas"}:
        return _deny("Privilege escalation and system-level changes are blocked.")

    if executable in SHELLS:
        command_flags = {"-c", "--command", "/c", "-command"}
        for index, arg in enumerate(lowered):
            if arg in command_flags and index + 1 < len(args):
                return _command_decision(args[index + 1], cwd, depth + 1)

    if executable in {"parallel", "xargs"}:
        batch_tokens = _batch_command(args)
        invoked = _executable(batch_tokens[0]) if batch_tokens else "echo"
        if invoked in {"rm", "rmdir", "shred", "truncate", "unlink"}:
            return _ask("Batch deletion through xargs or parallel requires explicit human approval.")
        if invoked in SHELLS | INTERPRETERS:
            return _deny("Dynamic batch execution through xargs or parallel is blocked.")

    if executable == "rm":
        targets = [arg for arg in args if not arg.startswith("-")]
        if "--no-preserve-root" in lowered:
            return _deny("Recursive forced deletion of a root, system, or traversal path is blocked.")
        return _deletion_decision(targets, cwd)

    if executable in {"remove-item", "del", "erase", "rd", "rmdir"}:
        known_flags = {
            "-confirm",
            "-force",
            "-literalpath",
            "-path",
            "-recurse",
            "-r",
            "/f",
            "/q",
            "/s",
        }
        targets = [arg for arg in args if arg.casefold() not in known_flags and not arg.startswith("-")]
        return _deletion_decision(targets, cwd)

    if executable == "find":
        joined = " ".join(lowered)
        destructive_exec = any(marker in lowered for marker in {"-exec", "-execdir"}) and bool(
            re.search(r"(?i)(?:^|[\s/\\])(?:rm|rmdir|shred|truncate|unlink)(?:\s|$)", joined)
        )
        if "-delete" in lowered or destructive_exec:
            decision = _deletion_decision(_find_search_roots(args), cwd)
            if decision.get("permissionDecision") == "deny":
                return decision
            return _ask("Destructive find actions require explicit human approval.")

    if executable in {"shred", "truncate", "unlink"}:
        targets = [arg for arg in args if not arg.startswith("-") and not arg.isdigit()]
        return _deletion_decision(targets, cwd)

    if executable in {"clear-disk", "diskpart", "format", "format-volume", "mkfs", "new-partition", "wipefs"}:
        return _deny("Disk formatting, partitioning, and destructive storage commands are blocked.")
    if executable == "dd" and any(arg.casefold().startswith("of=/dev/") for arg in args):
        return _deny("Raw writes to device storage are blocked.")
    if executable == "diskutil" and any(action in lowered for action in {"erasedisk", "erasevolume", "partitiondisk", "zerodisk"}):
        return _deny("Destructive disk operations are blocked.")

    if executable == "git" and args:
        action, action_args = _git_action(args)
        if action == "reset" and "--hard" in action_args:
            return _deny("Destructive Git reset is blocked.")
        if action == "clean" and any(arg.startswith("-") and "f" in arg for arg in action_args):
            return _deny("Forced Git clean is blocked.")
        if action == "restore" or (action == "checkout" and "--" in action_args):
            return _deny("Discarding working-tree changes is blocked.")
        if action == "branch" and any(arg in {"-d", "--delete"} for arg in action_args):
            return _deny("Deleting Git branches is blocked.")
        if action == "push":
            return _ask("Pushing or rewriting a remote requires explicit human approval.")
        if action in GIT_REVIEW_ACTIONS:
            return _ask("A Git state-changing operation requires explicit human approval.")

    if executable == "adb":
        joined = " ".join(lowered)
        if lowered[:1] and lowered[0] in {"uninstall", "root", "remount", "disable-verity"}:
            return _deny("Destructive or privileged Android device operations are blocked.")
        if " shell pm clear " in f" {joined} " or re.search(r"\bshell\s+rm\b", joined):
            return _deny("Commands that erase Android app/device data are blocked.")
    if executable == "fastboot" and any(action in lowered for action in {"erase", "flash", "flashing", "format", "oem", "unlock"}):
        return _deny("Fastboot flashing, erasing, formatting, and unlocking are blocked.")
    if executable in {"emulator", "emulator.exe"} and "-wipe-data" in lowered:
        return _deny("Emulator data wipes are blocked.")
    if executable == "avdmanager" and lowered[:1] == ["delete"]:
        return _deny("Deleting Android virtual devices is blocked.")
    if executable == "xcrun" and len(lowered) > 1 and lowered[0] == "simctl" and lowered[1] in {"delete", "erase"}:
        return _deny("Deleting or erasing Apple simulators is blocked.")

    if executable in {"docker", "podman"} and lowered[:2] in (["system", "prune"], ["volume", "prune"]):
        return _deny("Broad container or volume pruning is blocked.")

    package_decision = _package_decision(executable, args)
    if package_decision:
        return package_decision
    return None


def _command_decision(command: str, cwd: str, depth: int = 0) -> dict[str, str]:
    if depth > 4:
        return _deny("Nested shell execution exceeds the safe inspection depth.")
    normalized = unicodedata.normalize("NFKC", command).strip()
    if not normalized or "\x00" in normalized:
        return _deny("The shell command is empty or malformed.")

    for nested in re.findall(r"\$\(([^()]*)\)|`([^`]*)`", normalized):
        nested_command = nested[0] or nested[1]
        decision = _command_decision(nested_command, cwd, depth + 1)
        if decision:
            return decision

    segments, operators = _split_top_level(normalized)
    if not segments:
        return _deny("The shell command could not be parsed safely.")
    if "|" in operators:
        executables = [_executable(_tokens(segment)[0]) for segment in segments if _tokens(segment)]
        if any(executable in {"curl", "wget"} for executable in executables) and any(
            executable in SHELLS | INTERPRETERS for executable in executables
        ):
            return _deny("Download-and-execute pipelines are blocked.")

    pending_ask: dict[str, str] | None = None
    for segment in segments:
        decision = _segment_decision(segment, cwd, depth)
        if decision and decision.get("permissionDecision") == "deny":
            return decision
        if decision:
            pending_ask = decision
    return pending_ask or {}


def evaluate(payload: Any) -> dict[str, str]:
    if not isinstance(payload, dict):
        return _deny("Malformed hook input: expected a JSON object.")
    tool_name = payload.get("toolName", payload.get("tool_name"))
    tool_args = payload.get("toolArgs", payload.get("tool_input"))
    cwd = payload.get("cwd", "")
    if not isinstance(tool_name, str) or tool_name.casefold() not in {"bash", "execute", "powershell", "shell"}:
        return _deny("Malformed hook input: expected a shell tool call.")
    if not isinstance(cwd, str):
        return _deny("Malformed hook input: invalid working directory.")
    command = _extract_command(tool_args)
    if command is None:
        return _deny("Malformed hook input: missing shell command.")
    return _command_decision(command, cwd)


def main() -> int:
    raw = sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        result = _deny("Malformed hook input: invalid JSON.")
    else:
        result = evaluate(payload)
    sys.stdout.write(json.dumps(result, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
