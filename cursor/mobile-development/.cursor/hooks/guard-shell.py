#!/usr/bin/env python3
import json
import os
import re
import shlex
import sys


DENY_SUBCOMMANDS = {
    "git": {"commit", "push", "pull", "merge", "rebase", "reset", "clean", "checkout", "restore", "switch", "branch", "tag"},
    "gh": {"release", "workflow", "run"},
    "firebase": {"deploy"},
    "fastlane": {"deliver", "pilot", "supply", "upload_to_testflight", "upload_to_play_store", "release"},
    "eas": {"submit", "build"},
    "xcrun": {"altool", "notarytool"},
}

DENY_WORDS = {
    "rm", "rmdir", "shred", "srm", "mkfs", "dd", "diskutil", "adb", "fastboot",
    "xcodebuild -exportArchive", "gradle publish", "./gradlew publish",
    "pod trunk", "npm publish", "yarn publish", "pnpm publish",
}

ASK_WORDS = {
    "curl", "wget", "scp", "rsync", "ssh", "openssl", "security",
    "keytool", "jarsigner", "codesign", "xcodebuild", "gradle", "./gradlew",
    "npm", "yarn", "pnpm", "bundle", "pod", "flutter", "react-native",
}

CONTROL_PATTERNS = [
    r";", r"\|\|?", r"&&", r">\s*", r"<\s*", r"`", r"\$\(", r"\${",
    r"\bbase64\b", r"\bpython\s+-c\b", r"\bpython3\s+-c\b", r"\bperl\s+-e\b",
    r"\bruby\s+-e\b", r"\bnode\s+-e\b", r"\bpowershell\b", r"\bcmd\.exe\b",
]


def decision(permission, user_message, agent_message=None):
    out = {"continue": True, "permission": permission, "user_message": user_message}
    if agent_message:
        out["agent_message"] = agent_message
    print(json.dumps(out))


def load_payload():
    try:
        return json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        decision("deny", "Shell command blocked: malformed hook input.")
        sys.exit(0)


def tokenize(command):
    try:
        return shlex.split(command, posix=True)
    except ValueError:
        decision("deny", "Shell command blocked: malformed quoting.")
        sys.exit(0)


def has_control_operator(command):
    return any(re.search(pattern, command) for pattern in CONTROL_PATTERNS)


def specialization_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def path_escape(tokens):
    workspace = specialization_root()
    for token in tokens:
        if token.startswith("-"):
            continue
        looks_path = "/" in token or "\\" in token or token.startswith(".")
        if not looks_path:
            continue
        normalized = os.path.abspath(token if os.path.isabs(token) else os.path.join(workspace, token))
        if token.startswith("..") or not normalized.startswith(workspace):
            return token
    return None


def main():
    payload = load_payload()
    command = str(payload.get("command") or "").strip()
    if not command:
        decision("deny", "Shell command blocked: empty command.")
        return

    lowered = command.lower()
    tokens = tokenize(command)
    if not tokens:
        decision("deny", "Shell command blocked: empty command.")
        return

    escaped = path_escape(tokens)
    if escaped:
        decision("ask", f"Shell command touches a path outside the specialization or uses traversal: {escaped}")
        return

    if has_control_operator(command):
        decision("ask", "Shell command uses chaining, redirection, substitution, encoding, or platform shell syntax; human review is required.")
        return

    executable = os.path.basename(tokens[0]).lower()
    subcommand = tokens[1].lower() if len(tokens) > 1 else ""

    if executable in DENY_SUBCOMMANDS and subcommand in DENY_SUBCOMMANDS[executable]:
        decision("deny", f"Shell command blocked: `{executable} {subcommand}` is prohibited for this specialization.")
        return

    if any(word in lowered for word in DENY_WORDS):
        decision("deny", "Shell command blocked: destructive, publishing, signing, or distribution behavior is prohibited.")
        return

    if executable in ASK_WORDS or any(word in lowered for word in ASK_WORDS):
        decision("ask", "Shell command may affect dependencies, SDKs, network, signing, or generated state; human review is required.")
        return

    decision("allow", "Shell command allowed by mobile-development guard.")


if __name__ == "__main__":
    main()
