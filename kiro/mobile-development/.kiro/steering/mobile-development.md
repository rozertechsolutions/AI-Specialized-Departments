---
inclusion: auto
name: mobile-development
description: Mobile development specialization guidance for Android, iOS, Kotlin Multiplatform, Flutter, React Native, release, security, tests, accessibility, and performance.
---

# Mobile Development Steering

Use this only for mobile work inside `kiro/mobile-development/`. Detect the actual technology from project files before choosing an owner. Keep one primary implementation owner per unit of work and use read-only reviewers for final review.

Kiro CLI custom agents are the selected native surface. Agent hooks are embedded in `.kiro/agents/*.json` under `hooks.preToolUse`; no standalone hook manifest is used, and cloning the repository does not execute hooks.

Do not use real secrets, signing credentials, production endpoints, active MCP servers, publishing, upload, deployment, destructive device actions, or financial actions. Report unavailable infrastructure honestly.

Classify every completion criterion as `required`, `conditionally-required`, or `not-applicable` with a reason.
