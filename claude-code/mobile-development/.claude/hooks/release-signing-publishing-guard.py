#!/usr/bin/env python3
"""Block release/signing/publication and ask before release-preparation commands."""

from __future__ import annotations

import re
from typing import Optional, Tuple

from hook_common import HookInputError, emit_pretool_decision, read_event, tool_input


BLOCK_PATTERNS: Tuple[Tuple[str, str], ...] = (
    ("package publication", r"\b(?:npm|pnpm|cargo)\s+publish\b|\byarn(?:\s+npm)?\s+publish\b|\bgem\s+push\b|\bdotnet\s+nuget\s+push\b"),
    ("Dart or Flutter package publication", r"\b(?:dart|flutter)\s+pub\s+publish\b"),
    ("CocoaPods publication", r"\bpod\s+trunk\s+push\b"),
    ("Gradle publication or store upload", r"\bgradlew?\b[^;&|]*(?:publish|appdistributionupload|uploadcrashlyticssymbolfile|publishreleasebundle|publishbundle)"),
    ("Gradle signing task", r"\bgradlew?\b[^;&|]*(?:sign|validateSigning)[A-Za-z0-9_-]*Release[A-Za-z0-9_-]*\b"),
    ("Fastlane release or distribution automation", r"\bfastlane\b[^;&|]*(?:deliver|supply|pilot|release|upload_to_app_store|upload_to_play_store|upload_to_testflight|firebase_app_distribution|upload_symbols_to_crashlytics|precheck)\b"),
    ("Apple upload, notarization, provisioning, or export", r"\bxcrun\s+(?:altool|notarytool|iTMSTransporter|stapler)\b|\bxcodebuild\b[^;&|]*(?:-exportArchive|-allowProvisioningUpdates|-allowProvisioningDeviceRegistration)\b"),
    ("Expo or EAS release automation", r"\b(?:(?:npx|pnpm\s+(?:exec|dlx)|yarn\s+dlx)\s+)?(?:eas|eas-cli)\s+(?:build|submit|update|deploy|credentials)\b|\b(?:npx\s+)?expo\s+(?:publish|upload)\b"),
    ("GitHub release mutation", r"\bgh\s+release\s+(?:create|upload|edit|delete)\b"),
    ("Firebase deployment, distribution, or symbol upload", r"\bfirebase(?:-tools)?\s+(?:deploy|appdistribution:distribute|crashlytics:symbols:upload)\b|\bupload-symbols\b"),
    ("Sentry release or debug-artifact upload", r"\bsentry-cli\b[^;&|]*(?:releases\s+(?:new|finalize|set-commits|deploys|files)|upload-dif\b|debug-files\s+upload\b|sourcemaps\s+upload\b)"),
    ("App Center or CodePush distribution", r"\bappcenter\s+(?:distribute\s+release|codepush\s+release(?:-react)?)\b|\bcode-push\s+release(?:-react)?\b"),
    ("Flutter patch distribution", r"\bshorebird\s+(?:release|patch)\b"),
    ("artifact upload", r"\b(?:scp|sftp|rsync|rclone)\b|\baws\s+(?:s3\s+(?:cp|mv|sync)|s3api\s+put-object)\b|\b(?:gcloud\s+storage|gsutil)\s+cp\b|\baz\s+(?:storage\s+blob\s+upload|artifacts\s+universal\s+publish)\b"),
    ("container publication", r"\bdocker\s+(?:push|login)\b"),
    ("HTTP upload", r"\bcurl\b[^;&|]*(?:--upload-file(?:\s|=)|-T\s|--request(?:\s|=)(?:POST|PUT|PATCH)|-X\s*(?:POST|PUT|PATCH)|(?:-F|--form|-d|--data(?:-ascii|-binary|-raw|-urlencode)?)(?:\s|=))|\bwget\b[^;&|]*(?:--post-file|--post-data)|\bhttps?\b\s+(?:POST|PUT|PATCH)\b|\bInvoke-(?:WebRequest|RestMethod)\b[^;&|]*(?:-InFile|-Method\s+(?:POST|PUT|PATCH))\b"),
    ("deployment command", r"\b(?:vercel|netlify)\s+(?:deploy|--prod)\b|\bkubectl\s+(?:apply|replace|create)\b"),
    ("release automation script", r"\b(?:npm|pnpm|yarn)\s+(?:run\s+)?(?:release|deploy|publish)\b"),
    ("credential import or export", r"\bsecurity\s+(?:import|export|add-|delete-|find-identity|find-generic-password|unlock-keychain|create-keychain|set-keychain-settings|add-trusted-cert)\b|\b(?:Import-PfxCertificate|Import-Certificate)\b|\bcertutil\b[^;&|]*-importPFX\b|\bgpg\b[^;&|]*(?:--import|--export-secret-keys)\b"),
    ("Apple code signing", r"(?<![-\w])codesign\b"),
    ("Android or Java signing", r"\b(?:jarsigner|apksigner)\b"),
    ("bundletool signing", r"\bbundletool\b[^;&|]*build-apks\b[^;&|]*(?:--ks|--ks-key-alias|--ks-pass|--key-pass)\b"),
    ("signed Apple package creation", r"\b(?:productbuild|pkgbuild)\b[^;&|]*--sign\b"),
    ("private-key generation or packaging", r"\bopenssl\b[^;&|]*(?:genrsa|genpkey|pkcs12)\b|\bkeytool\b[^;&|]*(?:-genkey|-genkeypair|-importkeystore|-importcert)\b"),
    ("Fastlane credential management", r"\bfastlane\b[^;&|]*(?:match|cert|sigh)\b"),
)


ASK_PATTERNS: Tuple[Tuple[str, str], ...] = (
    ("Android release build preparation", r"\bgradlew?\b[^;&|]*(?:(?:assemble|bundle)[A-Za-z0-9_-]*Release|signingReport)\b"),
    ("React Native release bundle preparation", r"\breact-native\s+bundle\b|\b(?:npx|bunx)\b[^;&|]*\breact-native\s+bundle\b|\b(?:npm\s+exec|pnpm\s+(?:exec|dlx)|yarn\s+dlx)\b[^;&|]*\breact-native\s+bundle\b"),
    ("Expo local export preparation", r"\bexpo\s+export\b"),
    ("Android package preparation", r"\bbundletool\b[^;&|]*build-apks\b"),
    ("device or simulator installation", r"\badb\s+(?:install|push)\b|\bbundletool\b[^;&|]*install-apks\b|\bxcrun\s+simctl\s+(?:install|uninstall)\b|\bios-deploy\b"),
    ("version or tag mutation", r"\b(?:agvtool|npm\s+version|git\s+(?:tag|branch|switch|checkout|stash|cherry-pick|revert|worktree))\b"),
    ("GitHub external write", r"\bgh\s+(?:pr\s+(?:create|edit|merge|review|comment|close|reopen)|issue\s+(?:create|edit|comment|close|reopen)|repo\s+(?:create|edit|delete|fork)|api\b[^;&|]*(?:--method|-X)\s*(?:POST|PUT|PATCH|DELETE))\b"),
    ("external repository write", r"\bgit\s+push\b"),
)


def release_decision(command: str) -> Optional[Tuple[str, str]]:
    if "\x00" in command:
        return "deny", "command contains a NUL byte"

    if "\n" in command or "\r" in command:
        return "deny", "multiline commands cannot be inspected as one release action"
    if re.search(r"`|\$\(|<\(|>\(", command):
        return "deny", "command or process substitution may conceal a release action"

    normalized = " ".join(command.split())

    for label, pattern in BLOCK_PATTERNS:
        if re.search(pattern, normalized, flags=re.IGNORECASE):
            return "deny", f"{label} is prohibited in this specialization"

    xcode_command = re.search(r"\bxcodebuild\b([^;&|]*)", normalized, flags=re.IGNORECASE)
    xcode_signing_path = False
    if xcode_command:
        xcode_arguments = xcode_command.group(1)
        xcode_signing_path = bool(
            re.search(
                r"\barchive\b|-configuration(?:\s+|=)[\"']?Release[\"']?(?=\s|$)|-sdk(?:\s+|=)[\"']?iphoneos(?:\d+(?:\.\d+)*)?[\"']?(?=\s|$)|\b(?:CODE_SIGN_IDENTITY|DEVELOPMENT_TEAM|PROVISIONING_PROFILE(?:_SPECIFIER)?|OTHER_CODE_SIGN_FLAGS)\s*=|\bCODE_SIGNING_(?:ALLOWED|REQUIRED)\s*=\s*[\"']?YES[\"']?(?=\s|$)",
                xcode_arguments,
                flags=re.IGNORECASE,
            )
        )
        for destination in re.finditer(
            r"-destination(?:\s+|=)(?:\"([^\"]*)\"|'([^']*)'|(\S+))",
            xcode_arguments,
            flags=re.IGNORECASE,
        ):
            value = next(item for item in destination.groups() if item is not None)
            if re.search(r"(?:platform\s*=\s*iOS(?:,|$)|generic/platform=iOS)", value, re.IGNORECASE) and not re.search(
                r"simulator", value, re.IGNORECASE
            ):
                xcode_signing_path = True

    if xcode_signing_path:
        signing_disabled = re.search(
            r"\bCODE_SIGNING_ALLOWED\s*=\s*[\"']?NO[\"']?(?=\s|$)", normalized, flags=re.IGNORECASE
        )
        if not signing_disabled:
            return "deny", "the Apple device, archive, or Release path may sign; CODE_SIGNING_ALLOWED=NO is required"
        return "ask", "explicitly non-signing Apple release preparation still requires human confirmation"

    flutter_build = re.search(
        r"\bflutter\s+build\s+(aar|apk|appbundle|bundle|ios|ios-framework|ipa|macos|windows|linux|web)\b([^;&|]*)",
        normalized,
        flags=re.IGNORECASE,
    )
    if flutter_build:
        target = flutter_build.group(1).lower()
        flags = flutter_build.group(2)
        if target in {"ios", "ipa"}:
            if not re.search(r"--no-codesign(?:\s|$)", flags, flags=re.IGNORECASE):
                return "deny", f"flutter build {target} may sign; --no-codesign is required"
            return "ask", f"unsigned Flutter {target} preparation requires explicit human confirmation"
        explicit_non_release = re.search(r"--(?:debug|profile)\b", flags, flags=re.IGNORECASE)
        if not explicit_non_release:
            return (
                "ask",
                f"Flutter {target} defaults to a release build; confirm the project path cannot use signing material",
            )

    fastlane_build = re.search(
        r"\bfastlane\b[^;&|]*(?:gym|build_app)\b([^;&|]*)", normalized, flags=re.IGNORECASE
    )
    if fastlane_build:
        if not re.search(
            r"\bskip_codesigning\s*(?::|=)\s*true\b",
            fastlane_build.group(0),
            flags=re.IGNORECASE,
        ):
            return "deny", "Fastlane build automation may sign; skip_codesigning:true is required"
        return "ask", "explicitly unsigned Fastlane build preparation requires human confirmation"

    for label, pattern in ASK_PATTERNS:
        if re.search(pattern, normalized, flags=re.IGNORECASE):
            return "ask", f"{label} requires explicit human confirmation and must remain non-signing/non-publishing"
    return None


def main() -> int:
    try:
        event = read_event()
        if event.get("hook_event_name") != "PreToolUse" or event.get("tool_name") not in {
            "Bash",
            "PowerShell",
        }:
            raise HookInputError("expected a PreToolUse Bash or PowerShell event")
        payload = tool_input(event)
        command = payload.get("command")
        if not isinstance(command, str) or not command.strip():
            raise HookInputError("shell command is required")
        decision = release_decision(command)
        if decision:
            mode, reason = decision
            return emit_pretool_decision(mode, f"Release guard: {reason}.")
        return 0
    except HookInputError as exc:
        return emit_pretool_decision("deny", f"Release guard failed closed: {exc}.")
    except Exception:
        return emit_pretool_decision("deny", "Release guard failed closed because validation could not complete.")


if __name__ == "__main__":
    raise SystemExit(main())
