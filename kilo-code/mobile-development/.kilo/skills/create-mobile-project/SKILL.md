---
name: create-mobile-project
description: Use when creating or structuring a new Android, iOS, Kotlin Multiplatform, Flutter, or React Native mobile project with safe native setup and validation gates.
---

# create-mobile-project

- Objective: Create or structure a mobile project using only stable native project capabilities for the selected technology.
- Trigger: User asks to create a mobile project, app skeleton, module layout, or initial mobile repository structure.
- Inputs: Target technology, app purpose, package or bundle identifiers, minimum platform versions, UI framework, state/navigation preferences, test expectations, and release constraints.
- Supported technologies: Android, iOS, Kotlin Multiplatform, Flutter, React Native.
- Preconditions: Confirm target technology, inspect existing repository, discover installed SDK/tool versions when relevant, and avoid overwriting existing files.
- Primary owner: `mobile-architect`.
- Reviewers: Owning platform engineer, `mobile-test-engineer`, `mobile-security-reviewer` when permissions/privacy are involved, and `mobile-code-reviewer`.
- Steps: Inspect current files; classify existing content as native or unsupported; choose the smallest native project structure; ask before dependency, lockfile, signing, privacy, or external integration changes; create only necessary files; discover validation commands; run non-publishing checks when available; record evidence and limitations.
- Validation gates: Project opens with native tooling, dependency resolution is verified when applicable, basic compile/analyze/lint/test checks run or are unavailable, and no credentials or signing material are used.
- Failures: Stop on overwrite risk, unsupported platform request, missing SDK that prevents safe generation, validation failures caused by changes, or credential/signing requirement.
- Stop conditions: User requests publishing, signing, deployment, external integration activation, destructive commands, or a universal runtime.
- Evidence: Files created, tools/versions discovered, commands run, outputs summarized, and not-applicable criteria with reasons.
- Outputs: Project structure, configuration files, tests where appropriate, validation report, and follow-up risks.
- Acceptance criteria: The created project is minimal, native, scoped, validated where possible, and independently reviewed.
- Human approvals: Required for dependencies, lockfiles, signing/build config, privacy, permissions, external writes, and any destructive or credentialed action.
- Prohibited actions: Publishing, upload, deploy, submit, sign with real credentials, spend money, activate connectors, invent unsupported capabilities, or fabricate validation.

