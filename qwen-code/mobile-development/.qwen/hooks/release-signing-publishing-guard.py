#!/usr/bin/env python3
"""Qwen Code PreToolUse guard for signing, publishing, upload, and deployment."""

from __future__ import annotations

import json
import ntpath
import re
import shlex
import sys
from typing import Any, Iterable


class PolicyInputError(ValueError):
    """Raised when the hook input cannot be evaluated safely."""


SHELL_TOOLS = {"bash", "shell", "run_shell_command"}
CONTROL_TOKENS = {";", "&&", "||", "|", "&", ">", ">>", "<", "<<", "<<<"}
SHELL_INTERPRETERS = {"sh", "bash", "zsh", "fish", "dash", "ksh"}
EXPLICIT_RELEASE_ACTIONS = {
    "deliver",
    "pilot",
    "supply",
    "upload_to_app_store",
    "upload_to_play_store",
    "firebase_app_distribution",
    "match",
    "gym",
}


def _decision(kind: str, reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": kind,
            "permissionDecisionReason": reason,
        }
    }


def _validate_payload(payload: Any) -> tuple[str, dict[str, Any]]:
    if not isinstance(payload, dict):
        raise PolicyInputError("input must be a JSON object")
    if payload.get("hook_event_name") != "PreToolUse":
        raise PolicyInputError("unexpected hook event")
    tool_name = payload.get("tool_name")
    tool_input = payload.get("tool_input")
    if not isinstance(tool_name, str) or not tool_name.strip():
        raise PolicyInputError("tool_name must be a non-empty string")
    if not isinstance(tool_input, dict):
        raise PolicyInputError("tool_input must be an object")
    return tool_name.strip().lower(), tool_input


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


def _unwrap(segment: list[str]) -> list[str]:
    result = list(segment)
    while result:
        while result and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", result[0]):
            result.pop(0)
        if not result:
            break
        executable = _executable(result[0])
        if executable in {"command", "builtin", "env"}:
            result.pop(0)
            while executable == "env" and result:
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
        if executable == "bundle" and len(result) >= 3 and result[1].lower() == "exec":
            result = result[2:]
            continue
        if executable == "npx" and len(result) >= 2:
            index = 1
            while index < len(result) and result[index].startswith("-"):
                if result[index] in {"-p", "--package"} and index + 1 < len(result):
                    index += 2
                else:
                    index += 1
            if index < len(result):
                result = result[index:]
                package = _executable(result[0])
                if package.startswith("firebase-tools"):
                    result[0] = "firebase"
                elif package.startswith("eas-cli"):
                    result[0] = "eas"
                elif package in {"@sentry/cli", "sentry-cli"}:
                    result[0] = "sentry-cli"
                continue
        if executable in {"pnpm", "yarn"} and len(result) >= 3 and result[1].lower() == "dlx":
            result = result[2:]
            continue
        if executable == "bunx" and len(result) >= 2:
            result = result[1:]
            continue
        break
    return result


def _has_active_substitution(command: str) -> bool:
    single_quoted = False
    double_quoted = False
    escaped = False
    index = 0
    while index < len(command):
        character = command[index]
        if escaped:
            escaped = False
            index += 1
            continue
        if character == "\\" and not single_quoted:
            escaped = True
            index += 1
            continue
        if character == "'" and not double_quoted:
            single_quoted = not single_quoted
            index += 1
            continue
        if character == '"' and not single_quoted:
            double_quoted = not double_quoted
            index += 1
            continue
        if not single_quoted and (character == "`" or command.startswith("$(", index)):
            return True
        index += 1
    return False


def _nested_shell(segment: list[str], depth: int) -> tuple[str, str] | None:
    executable = _executable(segment[0])
    if executable not in SHELL_INTERPRETERS:
        return None
    args = segment[1:]
    for flag in ("-c", "--command"):
        if flag in args:
            index = args.index(flag)
            if index + 1 >= len(args):
                return "deny", "Nested shell input is malformed."
            return _analyze_command(args[index + 1], depth + 1)
    return None


def _gradle_action(args: list[str]) -> tuple[str, str] | None:
    tasks = [arg.lower() for arg in args if not arg.startswith("-") and "=" not in arg]
    for task in tasks:
        compact = task.replace(":", "")
        if "publish" in compact or "uploadarchives" in compact or compact.startswith("upload"):
            return "deny", "Artifact publication or upload is prohibited."
        if "sign" in compact and "signingreport" not in compact:
            return "deny", "Artifact signing is prohibited."
    if any(task.endswith("release") or "bundlerelease" in task or "assemblerelease" in task for task in tasks):
        return "ask", "A release build may use signing configuration and requires human review."
    return None


def _curl_write(args: list[str]) -> tuple[str, str] | None:
    lowered = [arg.lower() for arg in args]
    if any(
        original == "-T" or lower == "--upload-file" or lower.startswith("--upload-file=")
        for original, lower in zip(args, lowered)
    ):
        return "deny", "File upload is prohibited."
    if any(
        original == "-F"
        or original.startswith("-F")
        or lower in {"--data", "--data-raw", "--data-binary", "--json", "-d", "--form"}
        or lower.startswith(("--data=", "--data-raw=", "--data-binary=", "--json=", "--form="))
        for original, lower in zip(args, lowered)
    ):
        return "ask", "An external HTTP write requires explicit human approval."
    for index, (original, lower) in enumerate(zip(args, lowered)):
        if (original == "-X" or lower == "--request") and index + 1 < len(lowered):
            if lowered[index + 1] in {"post", "put", "patch", "delete"}:
                return "ask", "An external HTTP write requires explicit human approval."
        if lower.startswith("--request=") and lower.split("=", 1)[1] in {"post", "put", "patch", "delete"}:
            return "ask", "An external HTTP write requires explicit human approval."
    return None


def _git_subcommand(args: list[str]) -> tuple[str | None, list[str]]:
    index = 0
    options_with_value = {"-c", "-C", "--git-dir", "--work-tree", "--namespace"}
    while index < len(args):
        argument = args[index]
        if argument in options_with_value:
            index += 2
            continue
        if argument.startswith(("--git-dir=", "--work-tree=", "--namespace=")):
            index += 1
            continue
        if argument.startswith("-"):
            index += 1
            continue
        return argument.lower(), args[index + 1 :]
    return None, []


def _remote_target(argument: str) -> bool:
    lowered = argument.lower()
    if re.match(r"^[A-Za-z]:[\\/]", argument):
        return False
    return bool(
        re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", argument)
        or re.match(r"^(?:[^/@\s]+@)?[^/:\s]+:.+", argument)
        or lowered.startswith(("s3://", "gs://", "az://"))
    )


def _positional_args(args: list[str], options_with_value: set[str] | None = None) -> list[str]:
    result: list[str] = []
    value_options = options_with_value or set()
    index = 0
    while index < len(args):
        argument = args[index]
        if argument == "--":
            result.extend(args[index + 1 :])
            break
        if argument in value_options:
            index += 2
            continue
        if argument.startswith("-"):
            index += 1
            continue
        result.append(argument)
        index += 1
    return result


def _transfer_finding(executable: str, args: list[str]) -> tuple[str, str] | None:
    if executable in {"scp", "rsync"}:
        positionals = _positional_args(
            args,
            {"-B", "--block-size", "-e", "--rsh", "-P", "--port", "--rsync-path"},
        )
        if positionals and _remote_target(positionals[-1]):
            return "deny", "Uploading files to a remote destination is prohibited."
    if executable == "sftp":
        return "ask", "An authenticated remote file-transfer session requires human approval."
    if executable == "ssh":
        return "ask", "Authenticated remote command execution requires human approval."
    return None


def _analyze_segment(segment: list[str], depth: int) -> tuple[str, str] | None:
    if depth > 3:
        return "deny", "Nested command evaluation exceeded the safe inspection limit."
    segment = _unwrap(segment)
    if not segment:
        return None
    nested = _nested_shell(segment, depth)
    if nested:
        return nested

    executable = _executable(segment[0])
    args = segment[1:]
    lowered = [arg.lower() for arg in args]
    joined = " ".join(lowered)

    transfer_finding = _transfer_finding(executable, args)
    if transfer_finding:
        return transfer_finding

    if executable == "codesign":
        if any(arg in {"-s", "--sign"} or arg.startswith("--sign=") for arg in args):
            return "deny", "Code signing is prohibited."
        if any(
            arg in {"--verify", "--display"} or bool(re.fullmatch(r"-[vd]+", arg))
            for arg in args
        ):
            return None
        return "deny", "Code signing is prohibited."
    if executable == "jarsigner":
        return None if "-verify" in lowered else ("deny", "JAR signing is prohibited.")
    if executable == "apksigner":
        return None if lowered[:1] == ["verify"] else ("deny", "APK signing is prohibited.")
    if executable == "signtool":
        return None if lowered[:1] == ["verify"] else ("deny", "Package signing is prohibited.")
    if executable == "security" and lowered[:1] in (["import"], ["create-keychain"], ["unlock-keychain"]):
        return "deny", "Signing-credential or keychain mutation is prohibited."
    if executable in {"notarytool", "altool", "transporter", "itmstransporter"}:
        return "deny", "Notarization or store transport is prohibited."

    if executable == "xcrun" and lowered:
        if lowered[0] in {"notarytool", "altool", "itmstransporter"}:
            return "deny", "Notarization or store upload is prohibited."
    if executable == "xcodebuild":
        if "archive" in lowered or "-exportarchive" in lowered or "-allowprovisioningupdates" in lowered:
            return "deny", "Archiving, export, or provisioning mutation is prohibited."
        signing_disabled = any(
            arg.upper() in {"CODE_SIGNING_ALLOWED=NO", "CODE_SIGNING_REQUIRED=NO"} for arg in args
        )
        if not signing_disabled and "release" in lowered:
            return "ask", "A release build may sign and requires human review."

    if executable in {"gradle", "gradlew"}:
        finding = _gradle_action(args)
        if finding:
            return finding
    if executable == "flutter":
        if lowered[:2] == ["pub", "publish"]:
            return "deny", "Package publication is prohibited."
        if lowered[:2] == ["build", "ipa"]:
            if "--no-codesign" not in lowered:
                return "deny", "IPA building with code signing is prohibited."
            return "ask", "Unsigned release-package preparation requires human review."
        if lowered[:1] == ["build"] and any(
            target in lowered for target in {"appbundle", "apk", "ios", "macos"}
        ):
            return "ask", "Release-package building may use signing configuration and requires review."
    if executable == "dart" and lowered[:2] == ["pub", "publish"]:
        return "deny", "Package publication is prohibited."
    if executable in {"npm", "pnpm"} and lowered[:1] == ["publish"]:
        return "deny", "Package publication is prohibited."
    if executable == "yarn" and (lowered[:1] == ["publish"] or lowered[:2] == ["npm", "publish"]):
        return "deny", "Package publication is prohibited."
    if executable == "pod" and lowered[:2] == ["trunk", "push"]:
        return "deny", "CocoaPods publication is prohibited."
    if executable == "cargo" and lowered[:1] == ["publish"]:
        return "deny", "Package publication is prohibited."
    if executable == "gem" and lowered[:1] in (["push"], ["publish"]):
        return "deny", "Package publication is prohibited."
    if executable in {"twine"} and lowered[:1] == ["upload"]:
        return "deny", "Package publication is prohibited."
    if executable in {"mvn", "mvnw"} and any(
        argument == "deploy" or argument.endswith(":deploy") for argument in lowered
    ):
        return "deny", "Artifact deployment is prohibited."
    if executable == "dotnet" and lowered[:2] == ["nuget", "push"]:
        return "deny", "Package publication is prohibited."

    if executable in EXPLICIT_RELEASE_ACTIONS:
        return "deny", "Signing or store publication action is prohibited."
    if executable == "fastlane":
        if any(action in joined for action in EXPLICIT_RELEASE_ACTIONS):
            return "deny", "Fastlane signing or publication action is prohibited."
        return "ask", "Fastlane may perform signing or external release actions and requires human review."
    if executable == "eas" and lowered:
        if lowered[0] == "build" and "--local" in lowered:
            return "ask", "Local release-package preparation requires human review."
        if lowered[0] in {"build", "submit", "update"}:
            return "deny", "Cloud build, upload, submission, or update is prohibited."
    if executable in {"expo"} and lowered[:1] and lowered[0] in {"publish", "upload", "update"}:
        return "deny", "Application publication or upload is prohibited."

    if executable == "firebase" and any(action in lowered for action in {"deploy", "appdistribution:distribute"}):
        return "deny", "Firebase deployment or distribution is prohibited."
    if executable == "appcenter" and lowered[:1] == ["distribute"]:
        return "deny", "Application distribution is prohibited."
    if executable == "vercel" and (not lowered or lowered[0] not in {"whoami", "help", "--help", "ls", "inspect", "logs"}):
        return "deny", "Deployment is prohibited."
    if executable == "netlify" and lowered[:1] in (["deploy"], ["sites:create"], ["link"]):
        return "deny", "Deployment or remote site mutation is prohibited."
    if executable == "fly" and lowered[:1] == ["deploy"]:
        return "deny", "Deployment is prohibited."
    if executable == "gcloud" and "deploy" in lowered:
        return "deny", "Deployment is prohibited."
    if executable == "gcloud" and lowered[:2] == ["storage", "cp"]:
        positionals = _positional_args(args[2:])
        if positionals and _remote_target(positionals[-1]):
            return "deny", "Cloud artifact upload is prohibited."
    if executable == "aws" and lowered[:2] in (["s3", "cp"], ["s3", "sync"]):
        positionals = _positional_args(args[2:])
        if positionals and _remote_target(positionals[-1]):
            return "deny", "Cloud artifact upload is prohibited."
    if executable == "aws" and lowered[:1] == ["s3api"] and len(lowered) > 1 and lowered[1].startswith(
        ("put-", "create-", "delete-")
    ):
        return "deny", "Cloud storage mutation is prohibited."
    if executable == "gsutil" and lowered[:1] in (["cp"], ["rsync"]):
        positionals = _positional_args(args[1:])
        if positionals and _remote_target(positionals[-1]):
            return "deny", "Cloud artifact upload is prohibited."
    if executable == "az" and joined.startswith("storage blob ") and any(
        action in lowered for action in {"upload", "upload-batch", "sync"}
    ):
        return "deny", "Cloud artifact upload is prohibited."
    if executable == "kubectl" and lowered[:1] in (["apply"], ["create"], ["delete"], ["replace"]):
        return "deny", "Deployment or remote cluster mutation is prohibited."
    if executable == "helm" and lowered[:1] in (["install"], ["upgrade"], ["uninstall"]):
        return "deny", "Deployment or remote cluster mutation is prohibited."
    if executable == "sentry-cli" and any(
        marker in joined for marker in {"upload-dif", "sourcemaps upload", "releases new", "releases finalize"}
    ):
        return "deny", "Debug-symbol, source-map, or release upload is prohibited."
    if executable == "upload-symbols" or (executable == "bugsnag-cli" and "upload" in lowered) or (
        executable == "datadog-ci" and "sourcemaps upload" in joined
    ):
        return "deny", "Debug-symbol or source-map upload is prohibited."

    if executable == "gh":
        if lowered[:1] == ["release"] and any(action in lowered for action in {"create", "upload", "edit", "delete"}):
            return "deny", "GitHub release publication or upload is prohibited."
        if lowered[:2] in (
            ["pr", "create"],
            ["pr", "edit"],
            ["pr", "merge"],
            ["pr", "close"],
            ["pr", "reopen"],
            ["issue", "create"],
            ["issue", "edit"],
            ["issue", "close"],
            ["issue", "reopen"],
            ["issue", "comment"],
        ):
            return "ask", "An authenticated external GitHub write requires human approval."
        if lowered[:1] == ["api"]:
            method = "get"
            for index, argument in enumerate(lowered):
                if argument in {"-x", "--method"} and index + 1 < len(lowered):
                    method = lowered[index + 1]
                elif argument.startswith("--method="):
                    method = argument.split("=", 1)[1]
            if method in {"post", "put", "patch", "delete"} or any(
                argument in {"-f", "-F", "--field", "--raw-field", "--input"}
                or argument.startswith(("--field=", "--raw-field=", "--input="))
                for argument in args
            ):
                return "ask", "An authenticated external GitHub write requires human approval."
    if executable == "git":
        subcommand, rest = _git_subcommand(args)
        rest_lowered = [argument.lower() for argument in rest]
        if subcommand == "push":
            return "ask", "A Git remote or release-reference write requires human approval."
        if subcommand == "tag" and rest and not any(
            flag in rest_lowered for flag in {"-l", "--list", "--contains", "--points-at"}
        ):
            return "ask", "A Git release-reference write requires human approval."
    if executable == "curl":
        return _curl_write(args)
    if executable == "wget":
        if any(
            arg.startswith(
                (
                    "--post",
                    "--method=post",
                    "--method=put",
                    "--method=patch",
                    "--method=delete",
                    "--body-data",
                    "--body-file",
                )
            )
            for arg in lowered
        ) or any(
            argument == "--method"
            and index + 1 < len(lowered)
            and lowered[index + 1] in {"post", "put", "patch", "delete"}
            for index, argument in enumerate(lowered)
        ):
            return "ask", "An external HTTP write requires explicit human approval."
    if executable in {"http", "https"} and any(
        argument in {"post", "put", "patch", "delete"} for argument in lowered[:2]
    ):
        return "ask", "An external HTTP write requires explicit human approval."
    return None


def _analyze_command(command: str, depth: int = 0) -> tuple[str, str] | None:
    if not command.strip() or "\x00" in command:
        raise PolicyInputError("shell command must be a non-empty valid string")
    if _has_active_substitution(command):
        return "ask", "Dynamic command substitution prevents deterministic release-policy inspection."
    tokens = _tokenize(command)
    if not tokens:
        raise PolicyInputError("shell command contains no executable tokens")
    result: tuple[str, str] | None = None
    for segment in _segments(tokens):
        finding = _analyze_segment(segment, depth)
        if finding and finding[0] == "deny":
            return finding
        if finding and result is None:
            result = finding
    return result


def evaluate(payload: Any) -> dict[str, Any]:
    tool, tool_input = _validate_payload(payload)
    if tool not in SHELL_TOOLS:
        return {}
    command = tool_input.get("command", tool_input.get("cmd"))
    if not isinstance(command, str):
        raise PolicyInputError("shell tool input must contain a command string")
    finding = _analyze_command(command)
    return _decision(*finding) if finding else {}


def _payload(command: str) -> dict[str, Any]:
    return {
        "hook_event_name": "PreToolUse",
        "tool_name": "run_shell_command",
        "tool_input": {"command": command},
        "cwd": "/workspace/app",
    }


def _result_decision(result: dict[str, Any]) -> str | None:
    return result.get("hookSpecificOutput", {}).get("permissionDecision")


def self_test() -> int:
    cases = [
        ("codesign --verify App.app", None),
        ("codesign -s Developer App.app", "deny"),
        ("codesign --verify --sign Developer App.app", "deny"),
        ("MODE=release codesign -s Developer App.app", "deny"),
        ("xcodebuild build CODE_SIGNING_ALLOWED=NO", None),
        ("xcodebuild archive", "deny"),
        ("./gradlew test", None),
        ("./gradlew publishReleaseBundle", "deny"),
        ("./gradlew bundleRelease", "ask"),
        ("flutter build ipa --no-codesign", "ask"),
        ("npm publish", "deny"),
        ("gem push package.gem", "deny"),
        ("mvn deploy", "deny"),
        ("gh release create v1.0.0", "deny"),
        ("gh pr view 12", None),
        ("gh api --method POST repos/acme/app/issues", "ask"),
        ("git status", None),
        ("echo '$(npm publish)'", None),
        ("git push origin main", "ask"),
        ("git -C app push origin main", "ask"),
        ("curl https://example.invalid/health", None),
        ("curl -X POST https://example.invalid/items", "ask"),
        ("curl --upload-file app.ipa https://example.invalid/upload", "deny"),
        ("curl -f https://example.invalid/health", None),
        ("scp app.ipa user@example.invalid:/releases/", "deny"),
        ("scp user@example.invalid:/logs/build.log build.log", None),
        ("aws s3 cp app.aab s3://releases/app.aab", "deny"),
        ("aws s3 cp s3://releases/report.json report.json", None),
        ("npx -y firebase-tools@latest deploy", "deny"),
        ("firebase deploy", "deny"),
    ]
    for command, expected in cases:
        actual = _result_decision(evaluate(_payload(command)))
        if actual != expected:
            raise AssertionError(f"expected {expected!r}, got {actual!r} for test case")
    print("release-signing-publishing-guard self-test: ok")
    return 0


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        return self_test()
    try:
        payload = json.load(sys.stdin)
        result = evaluate(payload)
    except (json.JSONDecodeError, PolicyInputError) as exc:
        print(f"release-signing-publishing-guard: invalid input: {exc}", file=sys.stderr)
        return 2
    except Exception:
        print("release-signing-publishing-guard: internal policy failure", file=sys.stderr)
        return 2
    if result:
        print(json.dumps(result, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
