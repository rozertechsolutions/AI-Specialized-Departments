#!/usr/bin/env python3
"""Block signing, release publication, upload, submission, and distribution commands."""

from __future__ import annotations

import json
import re
import shlex
import sys
import unicodedata
from typing import Any


COMMAND_KEYS = {"command", "cmd", "script", "shell_command", "shellcommand"}
SHELLS = {"bash", "cmd", "cmd.exe", "dash", "powershell", "powershell.exe", "pwsh", "sh", "zsh"}
FASTLANE_BLOCKED = {
    "app_store_build_number",
    "build_app",
    "cert",
    "deliver",
    "download_dsyms",
    "gym",
    "match",
    "pem",
    "pilot",
    "precheck",
    "produce",
    "sigh",
    "supply",
    "upload_to_app_store",
    "upload_to_play_store",
    "upload_to_testflight",
}
FASTLANE_READ_ONLY = {"action", "actions", "env", "lanes", "lint", "scan", "test", "tests", "version"}
ARTIFACT_PATTERN = re.compile(
    r"(?i)(?:^|[=@/\\])[^\s]*\.(?:aab|apk|appx|dSYM|ipa|msix|pkg|xcarchive)(?:$|[?#&])"
)


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


def _split_top_level(command: str) -> list[str]:
    segments: list[str] = []
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
            if index + 1 < len(command) and command[index + 1] == char and char in {"|", "&"}:
                index += 1
            index += 1
            continue
        buffer.append(char)
        index += 1
    segment = "".join(buffer).strip()
    if segment:
        segments.append(segment)
    return segments


def _tokens(segment: str) -> list[str]:
    stripped = segment.strip().strip("() ")
    windows_like = bool(re.search(r"[A-Za-z]:\\", stripped)) or "powershell" in stripped.casefold()
    try:
        tokens = shlex.split(stripped, posix=not windows_like)
    except ValueError:
        return []
    return [token.strip("\"'") for token in tokens]


def _executable(token: str) -> str:
    return token.replace("\\", "/").rstrip("/").rsplit("/", 1)[-1].casefold()


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
        if executable in {"npx", "pnpx"} and len(remaining) > 1:
            remaining = remaining[1:]
            continue
        if executable in {"pnpm", "yarn"} and len(remaining) > 2 and remaining[1].casefold() in {"dlx", "exec"}:
            remaining = remaining[2:]
            continue
        break
    return remaining


def _is_remote_location(value: str) -> bool:
    cleaned = value.strip("\"'")
    if re.match(r"^[A-Za-z]:[\\/]", cleaned):
        return False
    return bool(
        re.match(r"(?i)^(?:https?|s3|gs|rsync)://", cleaned)
        or re.match(r"^(?:[^/@\s:]+@)?[^/\\\s:]+:.+", cleaned)
    )


def _last_positional(args: list[str]) -> str:
    positional = [arg for arg in args if not arg.startswith("-")]
    return positional[-1] if positional else ""


def _contains_artifact(args: list[str]) -> bool:
    return any(ARTIFACT_PATTERN.search(arg) for arg in args)


def _gradle_decision(args: list[str]) -> dict[str, str] | None:
    pending_release = False
    for arg in args:
        if arg.startswith("-") or "=" in arg:
            continue
        task = arg.rsplit(":", 1)[-1].casefold()
        if task == "signingreport":
            continue
        if any(marker in task for marker in ("publish", "upload", "promote", "artifactregistry", "appdistribution")):
            return _deny("Gradle publication, upload, promotion, and distribution tasks are blocked.")
        if any(marker in task for marker in ("sign", "release", "bundle")):
            pending_release = True
    if pending_release:
        return _ask("A Gradle release/bundle task may sign an artifact and requires explicit human review.")
    return None


def _segment_decision(segment: str, depth: int) -> dict[str, str] | None:
    tokens = _unwrap(_tokens(segment))
    if not tokens:
        return _deny("The shell command could not be parsed safely.")
    executable = _executable(tokens[0])
    args = tokens[1:]
    lowered = [arg.casefold() for arg in args]

    if executable in SHELLS:
        for index, arg in enumerate(lowered):
            if arg in {"-c", "--command", "/c", "-command"} and index + 1 < len(args):
                return _command_decision(args[index + 1], depth + 1)

    if executable in {"gradle", "gradle.bat", "gradlew", "gradlew.bat"}:
        return _gradle_decision(args)

    if executable == "xcodebuild":
        joined = " ".join(lowered)
        actions = {"analyze", "archive", "build", "build-for-testing", "clean", "test", "test-without-building"}
        read_only_flags = {"-help", "-list", "-showdestinations", "-showsdks", "-version"}
        if any(flag in lowered for flag in read_only_flags) and not any(action in lowered for action in actions):
            return None
        if any(marker in lowered for marker in {"archive", "-exportarchive", "-allowprovisioningupdates", "-allowprovisioningdeviceRegistration".casefold()}):
            return _deny("Xcode archive, export, and automatic provisioning operations are blocked.")
        if any(
            marker in joined
            for marker in (
                "code_sign_identity=",
                "code_signing_allowed=yes",
                "development_team=",
                "provisioning_profile",
            )
        ):
            return _deny("Explicit Xcode signing or provisioning configuration is blocked.")
        if "code_signing_allowed=no" not in joined and "iphonesimulator" not in joined:
            return _ask("An Xcode device build may sign; use an explicit no-signing or simulator configuration.")
        return None

    if executable == "codesign":
        signing_flags = {"--force", "--generate-entitlement-der", "--options", "--preserve-metadata", "--requirements", "--sign", "-f", "-o", "-r", "-s"}
        inspection_flags = {"--display", "--verify", "-d", "-v"}
        if any(arg in signing_flags for arg in lowered) or not any(arg in inspection_flags for arg in lowered):
            return _deny("Code signing is blocked; only signature display or verification is allowed.")
    if executable == "jarsigner" and "-verify" not in lowered:
        return _deny("JAR/APK signing is blocked.")
    if executable in {"apksigner", "apksigner.bat"} and lowered[:1] != ["verify"]:
        return _deny("APK signing is blocked.")
    if executable == "keytool" and any(
        arg in lowered for arg in {"-genkey", "-genkeypair", "-genseckey", "-import", "-importcert", "-importkeystore"}
    ):
        return _deny("Signing key generation or import is blocked.")
    if executable == "security" and lowered[:1] == ["import"]:
        return _deny("Importing signing credentials into a keychain is blocked.")

    if executable == "fastlane":
        lane = lowered[1] if lowered[:1] == ["run"] and len(lowered) > 1 else (lowered[0] if lowered else "")
        if lane in FASTLANE_BLOCKED or any(marker in lane for marker in ("deploy", "distribute", "publish", "release", "submit", "upload")):
            return _deny("Fastlane signing, distribution, upload, or store operations are blocked.")
        if lane and lane not in FASTLANE_READ_ONLY and not lane.startswith("--"):
            return _ask("An unclassified Fastlane lane requires explicit human review because it may publish or sign.")
        return None

    if executable == "xcrun" and lowered:
        if lowered[0] in {
            "altool",
            "notarytool",
            "stapler",
            "transporter",
            "itmstransporter",
            "upload-symbols",
        }:
            return _deny("Apple notarization, transport, upload, and submission operations are blocked.")
        if lowered[:3] == ["devicectl", "device", "install"]:
            return _ask("Installing an application on a physical Apple device requires explicit human approval.")
    if executable in {"altool", "notarytool", "transporter", "itmstransporter", "upload-symbols"}:
        return _deny("Apple notarization, transport, upload, and submission operations are blocked.")

    if executable == "flutter" and lowered[:1] == ["build"]:
        target = lowered[1] if len(lowered) > 1 else ""
        if target == "ios" and "--no-codesign" in lowered:
            return None
        if target in {"ipa", "appbundle"} or "--release" in lowered:
            return _ask("A Flutter release artifact may be signed and requires explicit human review.")
    if executable == "flutter" and lowered[:1] == ["install"]:
        return _ask("Installing a Flutter application on a device requires explicit human approval.")

    if executable == "eas" and lowered[:1] and lowered[0] in {"build", "submit", "update"}:
        return _deny("EAS remote build, submission, and update operations are blocked.")
    if executable == "expo" and lowered[:1] and lowered[0] in {"publish", "publish:history", "publish:rollback", "update"}:
        return _deny("Expo publication and update operations are blocked.")

    if executable in {"npm", "pnpm"} and "publish" in lowered[:2]:
        return _deny("Package publication is blocked.")
    if executable == "yarn" and lowered[:2] in (["npm", "publish"], ["publish"]):
        return _deny("Package publication is blocked.")
    if executable in {"dart", "flutter"} and lowered[:2] == ["pub", "publish"]:
        return _deny("Dart package publication is blocked.")
    if executable == "pod" and lowered[:2] == ["trunk", "push"]:
        return _deny("CocoaPods trunk publication is blocked.")
    if executable == "cargo" and lowered[:1] == ["publish"]:
        return _deny("Package publication is blocked.")
    if executable == "gem" and lowered[:1] == ["push"]:
        return _deny("Package publication is blocked.")
    if executable == "twine" and lowered[:1] == ["upload"]:
        return _deny("Package publication is blocked.")
    if executable == "dotnet" and lowered[:2] == ["nuget", "push"]:
        return _deny("Package publication is blocked.")
    if executable == "mvn" and any(arg.casefold() == "deploy" for arg in args if not arg.startswith("-")):
        return _deny("Package publication is blocked.")
    if executable == "swift" and lowered[:2] == ["package-registry", "publish"]:
        return _deny("Package publication is blocked.")

    if executable == "curl":
        explicit_upload = any(
            arg == "-T" or arg.startswith("-T") or arg.casefold().startswith("--upload-file") for arg in args
        )
        form_upload = any(
            arg.startswith("-F")
            or arg.casefold() in {"--form", "--form-string", "--data-binary"}
            or arg.casefold().startswith(("--form=", "--form-string=", "--data-binary="))
            for arg in args
        ) and _contains_artifact(args)
        if explicit_upload or form_upload:
            return _deny("Uploading artifacts with curl is blocked.")
    if executable == "scp" and _is_remote_location(_last_positional(args)):
        return _deny("Remote artifact transfer is blocked.")
    if executable == "sftp" and any(not arg.startswith("-") for arg in args):
        return _ask("An interactive remote transfer session requires explicit human approval.")
    if executable == "rsync" and _is_remote_location(_last_positional(args)):
        return _deny("Remote artifact transfer is blocked.")
    if executable == "aws" and any(
        lowered[index : index + 2] in (["s3", "cp"], ["s3", "mv"], ["s3", "sync"])
        for index in range(max(0, len(lowered) - 1))
    ) and _is_remote_location(_last_positional(args)):
        return _deny("Uploading artifacts to remote object storage is blocked.")
    if executable == "gsutil" and any(action in lowered[:3] for action in {"cp", "mv", "rsync"}):
        if _is_remote_location(_last_positional(args)):
            return _deny("Uploading artifacts to remote object storage is blocked.")
    if executable == "gcloud" and any(
        lowered[index : index + 2] == ["storage", "cp"] for index in range(max(0, len(lowered) - 1))
    ) and _is_remote_location(_last_positional(args)):
        return _deny("Uploading artifacts to remote object storage is blocked.")

    if executable == "adb" and lowered[:1] and lowered[0] in {"install", "install-multi-package", "install-multiple"}:
        return _ask("Installing an application on an Android device requires explicit human approval.")
    if executable == "bundletool" and lowered[:1] == ["install-apks"]:
        return _ask("Installing an Android application bundle requires explicit human approval.")
    if executable in {"ideviceinstaller", "ios-deploy"}:
        return _ask("Installing an application on a physical Apple device requires explicit human approval.")

    joined = " ".join(lowered)
    if executable == "firebase" and ("deploy" in lowered or "appdistribution:distribute" in lowered):
        return _deny("Firebase deployment and app distribution are blocked.")
    if executable in {"appcenter", "appcenter-cli"} and any(marker in joined for marker in ("codepush release", "distribute release", "distribute upload")):
        return _deny("App Center distribution and CodePush release operations are blocked.")
    if executable == "sentry-cli" and any(marker in joined for marker in ("upload", "releases new", "releases finalize", "deploys new")):
        return _deny("Sentry upload, release, and deployment operations are blocked.")
    if executable == "gh" and lowered[:1] == ["release"] and len(lowered) > 1:
        if lowered[1] in {"create", "delete", "edit", "upload"}:
            return _deny("Remote release creation, modification, deletion, and upload are blocked.")
    if executable in {"gcloud", "vercel", "netlify"} and any(marker in lowered for marker in {"deploy", "publish", "release"}):
        return _deny("Remote deployment and publication operations are blocked.")
    return None


def _command_decision(command: str, depth: int = 0) -> dict[str, str]:
    if depth > 4:
        return _deny("Nested shell execution exceeds the safe inspection depth.")
    normalized = unicodedata.normalize("NFKC", command).strip()
    if not normalized or "\x00" in normalized:
        return _deny("The shell command is empty or malformed.")
    pending_ask: dict[str, str] | None = None
    for nested in re.findall(r"\$\(([^()]*)\)|\x60([^\x60]*)\x60", normalized):
        nested_command = nested[0] or nested[1]
        decision = _command_decision(nested_command, depth + 1)
        if decision.get("permissionDecision") == "deny":
            return decision
        if decision:
            pending_ask = decision
    segments = _split_top_level(normalized)
    if not segments:
        return _deny("The shell command could not be parsed safely.")
    for segment in segments:
        decision = _segment_decision(segment, depth)
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
    if not isinstance(tool_name, str) or tool_name.casefold() not in {"bash", "execute", "powershell", "shell"}:
        return _deny("Malformed hook input: expected a shell tool call.")
    command = _extract_command(tool_args)
    if command is None:
        return _deny("Malformed hook input: missing shell command.")
    return _command_decision(command)


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
