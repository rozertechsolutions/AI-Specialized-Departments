#!/usr/bin/env python3
"""Request specialist review after evidence of a sensitive mobile file change."""

from __future__ import annotations

import re
from typing import Dict, List, Set

from hook_common import (
    HookInputError,
    emit_context,
    first_string,
    normalize_target,
    project_root,
    read_event,
    tool_input,
)


PATH_KEYS = {
    "Edit": ("file_path",),
    "Write": ("file_path",),
    "NotebookEdit": ("notebook_path", "file_path"),
}

DEPENDENCY_FILES = {
    "package.json",
    "package-lock.json",
    "npm-shrinkwrap.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "pubspec.yaml",
    "pubspec.lock",
    "podfile",
    "podfile.lock",
    "package.swift",
    "package.resolved",
    "gradle.lockfile",
    "libs.versions.toml",
}


def changed_text(payload: Dict[str, object]) -> str:
    values: List[str] = []
    for key in ("content", "old_string", "new_string", "cell", "new_source", "text"):
        value = payload.get(key)
        if isinstance(value, str):
            values.append(value[:200_000])
    return "\n".join(values)


def review_requirements(relative: str, text: str) -> Set[str]:
    path = relative.replace("\\", "/")
    basename = path.rsplit("/", 1)[-1].lower()
    lower_text = text.lower()
    reviews: Set[str] = set()

    if basename in DEPENDENCY_FILES or basename.endswith((".lock", ".lockfile")):
        reviews.update({"mobile-security-reviewer", "mobile-code-reviewer"})

    if basename in {"build.gradle", "build.gradle.kts", "settings.gradle", "settings.gradle.kts"}:
        if re.search(
            r"dependencies|plugins|repositories|maven\s*\{|implementation\s*\(?|api\s*\(?|compileonly\s*\(?|runtimeonly\s*\(?|classpath\s*\(?|kapt\s*\(?|ksp\s*\(?|alias\s*\(\s*libs\.|signingconfig|buildtypes|productflavors|applicationid|minsdk|targetsdk|compilesdk|namespace",
            lower_text,
        ):
            reviews.update({"mobile-security-reviewer", "mobile-release-engineer"})

    if basename in {"package.json", "pubspec.yaml"} and re.search(
        r"(?:^|[\s\"'])version[\s\"':=]|scripts|release|publish|deploy|build", lower_text
    ):
        reviews.add("mobile-release-engineer")

    if basename == "androidmanifest.xml":
        if re.search(
            r"uses-permission|android:exported|intent-filter|networksecurityconfig|usescleartexttraffic|<provider|<service|<receiver|<queries",
            lower_text,
        ):
            reviews.update({"android-engineer", "mobile-security-reviewer", "mobile-release-engineer"})

    if basename == "info.plist":
        if re.search(
            r"usageDescription|cfbundleurltypes|nsapptransportsecurity|uibackgroundmodes|associateddomains|nsallowsarbitraryloads",
            text,
            flags=re.IGNORECASE,
        ):
            reviews.update({"ios-engineer", "mobile-security-reviewer", "mobile-release-engineer"})

    if basename.endswith(".entitlements"):
        reviews.update({"ios-engineer", "mobile-security-reviewer", "mobile-release-engineer"})
    if basename in {"privacyinfo.xcprivacy", "network_security_config.xml"}:
        reviews.update({"mobile-security-reviewer", "mobile-release-engineer"})

    if basename == "project.pbxproj" and re.search(
        r"code_sign|development_team|product_bundle_identifier|code_sign_entitlements|marketing_version|current_project_version",
        lower_text,
    ):
        reviews.update({"ios-engineer", "mobile-release-engineer", "mobile-security-reviewer"})

    if (basename.endswith(".xcconfig") or basename in {"exportoptions.plist", "gradle.properties"}) and re.search(
        r"code[_-]?sign|development_team|provisioning_profile|signing|keystore|storepassword|keypassword|keyalias|certificate|distribution|release",
        lower_text,
    ):
        reviews.update({"mobile-security-reviewer", "mobile-release-engineer"})

    if re.search(
        r"oauth|openid|authorization|bearer|access[_-]?token|refresh[_-]?token|biometric|keychain|keystore|securestorage",
        lower_text,
    ):
        reviews.add("mobile-security-reviewer")
    if re.search(
        r"webview|wkwebview|setjavascriptenabled|javascriptmode|originwhitelist|mixedcontentmode|addjavascriptinterface",
        lower_text,
    ):
        reviews.update({"mobile-security-reviewer", "mobile-ui-accessibility-reviewer"})
    if re.search(
        r"deep.?link|app.?link|universal.?link|url.?scheme|intent-filter|associated.?domains",
        lower_text,
    ):
        reviews.update({"mobile-security-reviewer", "mobile-ui-accessibility-reviewer"})
    if re.search(
        r"signingconfig|code[_-]?sign|provisioning_profile|development_team|keystore|storepassword|keypassword|keyalias",
        lower_text,
    ):
        reviews.update({"mobile-security-reviewer", "mobile-release-engineer"})

    return reviews


def main() -> int:
    try:
        event = read_event()
        if event.get("hook_event_name") != "PostToolUse":
            raise HookInputError("expected a PostToolUse event")
        name = event.get("tool_name")
        if not isinstance(name, str) or name not in PATH_KEYS:
            raise HookInputError("expected an Edit, Write, or NotebookEdit tool")
        payload = tool_input(event)
        raw_path = first_string(payload, PATH_KEYS[name])
        if raw_path is None:
            raise HookInputError(f"{name} target path is required")
        root = project_root(event)
        cwd = event.get("cwd") if isinstance(event.get("cwd"), str) else root
        target = normalize_target(raw_path, root, cwd=cwd)
        if target.traversal or not target.within_root:
            return emit_context(
                "Sensitive-change hook could not establish an in-project path. Treat specialist review as unresolved before completion."
            )

        reviews = review_requirements(target.relative, changed_text(payload))
        if not reviews:
            return 0
        ordered = ", ".join(sorted(reviews))
        return emit_context(
            f"Sensitive mobile change detected in {target.relative}. Required independent review before completion: {ordered}. Re-run affected validation after any correction."
        )
    except HookInputError as exc:
        return emit_context(
            f"Sensitive-change hook failed safely: {exc}. Treat specialist review as unresolved before completion."
        )
    except Exception:
        return emit_context(
            "Sensitive-change hook could not complete validation. Treat specialist review as unresolved before completion."
        )


if __name__ == "__main__":
    raise SystemExit(main())
