#!/usr/bin/env python3
import json
import os
import sys


ROOT = os.path.realpath(os.getcwd())
PROTECTED_PARTS = {
    ".git",
    ".ssh",
    ".gnupg",
    ".aws",
    ".azure",
    ".gcloud",
    ".gradle/caches",
    "DerivedData",
}


def block(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def candidate_paths(data):
    info = data.get("tool_info", {})
    path = info.get("file_path") or info.get("path")
    if isinstance(path, str):
        yield path


def main():
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError as exc:
        block(f"scope_guard: malformed hook JSON: {exc}")

    if data.get("agent_action_name") != "pre_write_code":
        return

    for raw_path in candidate_paths(data):
        if "\x00" in raw_path:
            block("scope_guard: blocked path with null byte")
        normalized = os.path.realpath(os.path.join(ROOT, raw_path) if not os.path.isabs(raw_path) else raw_path)
        rel = os.path.relpath(normalized, ROOT)
        if rel == os.pardir or rel.startswith(os.pardir + os.sep):
            block(f"scope_guard: blocked write outside workspace: {raw_path}")
        rel_posix = rel.replace(os.sep, "/")
        for protected in PROTECTED_PARTS:
            if rel_posix == protected or rel_posix.startswith(protected + "/") or f"/{protected}/" in rel_posix:
                block(f"scope_guard: blocked write to protected path: {raw_path}")


if __name__ == "__main__":
    main()
