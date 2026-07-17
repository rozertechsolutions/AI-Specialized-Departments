#!/usr/bin/env python3
import json
import re
import shlex
import sys


FASTLANE_RELEASE_ACTIONS = {
    "cert",
    "deliver",
    "match",
    "pem",
    "pilot",
    "precheck",
    "produce",
    "sigh",
    "supply",
    "upload_symbols_to_crashlytics",
    "upload_to_app_store",
    "upload_to_play_store",
}
RELEASE_WORDS = (
    "appstore",
    "app_store",
    "crashlytics",
    "deploy",
    "distribute",
    "distribution",
    "playstore",
    "play_store",
    "production",
    "publish",
    "release",
    "submit",
    "upload",
)
GRADLE_RELEASE_TASK_RE = re.compile(
    r"(?i)(publish|upload|deploy|bundleRelease|assembleRelease|appDistributionUpload|"
    r"crashlyticsUpload|publish.*Release|upload.*Release|publish.*Bundle|"
    r"publish.*Apk|publish.*Aab|play.*Publish)"
)
FLUTTER_RELEASE_RE = re.compile(
    r"(?i)\bflutter\s+(build|deploy)\b.*\b(release|appbundle|ipa|apk|ios|aab)\b"
)
EAS_RELEASE_RE = re.compile(r"(?i)\beas\s+(build|submit|update)\b")
FIREBASE_RELEASE_RE = re.compile(
    r"(?i)\bfirebase\s+(deploy|appdistribution:distribute|crashlytics:symbols:upload)\b"
)
APP_CENTER_RELEASE_RE = re.compile(r"(?i)\b(appcenter|appcenter-cli)\s+distribute\b")
SENTRY_RELEASE_RE = re.compile(r"(?i)\bsentry-cli\s+(releases|upload)\b")
NPM_PUBLISH_RE = re.compile(r"(?i)\b(npm|pnpm|yarn|bun)\s+(publish|npm\s+publish)\b")
GITHUB_RELEASE_RE = re.compile(r"(?i)\bgh\s+release\s+(create|upload)\b")
GOOGLE_PLAY_RE = re.compile(r"(?i)\b(google-play|play\s+store|supply)\b")
APP_STORE_RE = re.compile(r"(?i)\b(app-store-connect|appstoreconnect|altool|notarytool)\b")
BLOCK_PATTERNS = [
    r"(?i)\brm\s+-[^\n]*[rf]",
    r"(?i)\bsudo\b",
    r"(?i)\bchmod\s+(-R\s+)?777\b",
    r"(?i)\b(chown|mkfs|diskutil|dd)\b",
    r"(?i)\bgit\s+(reset|clean|checkout|restore|push|pull|merge|rebase|branch|switch|commit|tag)\b",
    r"(?i)\bxcodebuild\b.*\b(archive|-exportArchive|CODE_SIGN_IDENTITY=)\b",
    r"(?i)\b(codesign|jarsigner|apksigner\s+sign|keytool\s+-genkey|notarytool|altool)\b",
    r"(?i)\bsecurity\s+(import|unlock-keychain|set-key-partition-list)\b",
    r"(?i)\b(npm|pnpm|yarn|bun|pip|gem|bundle|brew)\b.*\b(install|add|update|upgrade)\b",
]
SHELL_OPERATOR_RE = re.compile(r"(\|\||&&|;|\||`|\$\(|<\(|>|>>|<<)")
ENCODED_RE = re.compile(
    r"(?i)(base64\s+-d|frombase64string|certutil\s+-decode|powershell.+-enc|"
    r"%3b|%7c|%26|%60|\\x[0-9a-f]{2}|\\u[0-9a-f]{4})"
)


def block(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def executable_name(token):
    cleaned = token.replace("\\", "/").rstrip("/")
    return cleaned.rsplit("/", 1)[-1].lower()


def is_gradle_executable(token):
    name = executable_name(token)
    return name in {"gradle", "gradlew"} or name.endswith("gradlew")


def is_fastlane_executable(token):
    name = executable_name(token)
    return name == "fastlane" or name.endswith("fastlane")


def fastlane_invocation(tokens):
    for index, token in enumerate(tokens):
        if executable_name(token) == "bundle" and index + 2 < len(tokens):
            if tokens[index + 1].lower() == "exec" and is_fastlane_executable(tokens[index + 2]):
                return index + 2
        if is_fastlane_executable(token):
            return index
    return None


def fastlane_actions(tokens, fastlane_index):
    actions = []
    for token in tokens[fastlane_index + 1 :]:
        lower = token.lower()
        if lower.startswith("-"):
            continue
        if lower == "run":
            continue
        actions.append(lower)
    return actions


def blocks_fastlane(tokens):
    index = fastlane_invocation(tokens)
    if index is None:
        return False
    for action in fastlane_actions(tokens, index):
        normalized = action.replace("-", "_")
        if normalized in FASTLANE_RELEASE_ACTIONS:
            return True
        if any(word in normalized for word in RELEASE_WORDS):
            return True
    return False


def blocks_gradle_release(tokens):
    for index, token in enumerate(tokens):
        if not is_gradle_executable(token):
            continue
        return any(GRADLE_RELEASE_TASK_RE.search(task) for task in tokens[index + 1 :])
    return False


def blocks_release_tool(command, tokens):
    if blocks_fastlane(tokens) or blocks_gradle_release(tokens):
        return True
    release_patterns = (
        FLUTTER_RELEASE_RE,
        EAS_RELEASE_RE,
        FIREBASE_RELEASE_RE,
        APP_CENTER_RELEASE_RE,
        SENTRY_RELEASE_RE,
        NPM_PUBLISH_RE,
        GITHUB_RELEASE_RE,
        GOOGLE_PLAY_RE,
        APP_STORE_RE,
    )
    return any(pattern.search(command) for pattern in release_patterns)


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError as exc:
        block(f"command_guard: malformed hook JSON: {exc}")

    if data.get("agent_action_name") != "pre_run_command":
        return

    command = str(data.get("tool_info", {}).get("command_line") or "")
    if not command.strip():
        block("command_guard: missing command_line")

    if "\x00" in command:
        block("command_guard: blocked command with null byte")
    if SHELL_OPERATOR_RE.search(command):
        block("command_guard: blocked shell chaining, redirection, pipe, or substitution")
    if ENCODED_RE.search(command):
        block("command_guard: blocked encoded or decoded command execution")

    try:
        tokens = shlex.split(command, posix=True)
    except ValueError as exc:
        block(f"command_guard: malformed command quoting: {exc}")
    if not tokens:
        block("command_guard: missing command_line")

    for pattern in BLOCK_PATTERNS:
        if re.search(pattern, command):
            block("command_guard: blocked command requiring explicit human approval")
    if blocks_release_tool(command, tokens):
        block(
            "command_guard: blocked release, publication, upload, signing, or distribution command"
        )


if __name__ == "__main__":
    main()
