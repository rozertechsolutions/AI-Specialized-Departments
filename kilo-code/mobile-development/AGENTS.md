# Kilo Code Mobile Development Specialization

This directory contains only the Kilo Code Mobile Development specialization. Work in this directory must stay scoped to Android, iOS, Kotlin Multiplatform, Flutter, and React Native repository assistance.

## Native Surface

- Target surface: current Kilo Code VS Code extension and CLI behavior documented on July 15, 2026.
- Project instructions are loaded from this `AGENTS.md` and `kilo.jsonc`.
- Custom subagents are native project markdown agents in `.kilo/agents/`.
- Reusable mobile processes are native Agent Skills in `.kilo/skills/`.
- Project rules are native Kilo instructions referenced from `kilo.jsonc`.
- Local security plugins are native Kilo JavaScript plugins in `.kilo/plugins/`.
- MCP servers are intentionally not configured because no mobile workflow here requires an active external connector.

## Scope Rules

- Modify only files under `kilo-code/mobile-development/`.
- Do not create shared cross-platform adapters, a `common` directory, or generic runtime abstractions for this specialization.
- Do not activate external integrations, authenticate tools, import credentials, start servers, publish, upload, deploy, submit, sign, spend money, or run destructive operations.
- Do not hardcode model versions in agents or workflows. Agents inherit the active model unless a future user explicitly requests a supported model override.
- Do not treat public mobile client configuration as a secret solely because it is client configuration, but require human control before editing security, privacy, signing, dependency, lockfile, manifest, entitlement, deep-link, WebView, analytics, or telemetry files.
- Review agents are read-only and must not implement or approve their own changes.

## Responsibilities

Use the twelve project subagents exactly as defined in `.kilo/agents/`:

- `mobile-architect`
- `android-engineer`
- `ios-engineer`
- `kmp-engineer`
- `flutter-engineer`
- `react-native-engineer`
- `mobile-test-engineer`
- `mobile-security-reviewer`
- `mobile-ui-accessibility-reviewer`
- `mobile-performance-reviewer`
- `mobile-release-engineer`
- `mobile-code-reviewer`

Implementation roles may request review from review roles. Review roles must remain independent and read-only. `mobile-code-reviewer` performs final independent review and never reviews implementation it authored.

## Workflow Selection

Use these project Skills for repeatable work:

- `create-mobile-project`
- `implement-mobile-feature`
- `fix-mobile-bug`
- `review-mobile-architecture`
- `add-mobile-screen`
- `integrate-mobile-api`
- `add-mobile-tests`
- `optimize-mobile-performance`
- `audit-mobile-security`
- `prepare-mobile-release`

Do not duplicate these workflows as slash commands or prompts. If a user explicitly asks for slash-command versions later, migrate only after removing the equivalent Skill to keep one authority.

## Validation Standard

Every completed task must report actual evidence. Unavailable SDKs, schemes, tasks, devices, emulators, simulators, credentials, services, or infrastructure must be reported as unavailable, not passed.

