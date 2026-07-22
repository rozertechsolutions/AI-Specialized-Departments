# Warp - Software Development

The Software Development department is a human-reviewed Warp package for requirements, planning, architecture, implementation, validation, independent code review, engineering-risk review, documentation, and release readiness. It can be used for stack-agnostic software work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, debugging, refactoring, testing, security, dependencies, performance, reliability, compatibility, migrations, and documentation.

Warp represents this package with a native Project Rules file and native project Skills. The safety model keeps humans in control of sensitive actions: no automatic Git mutation, dependency change, deployment, publication, signing, release, credential use, external integration, or destructive operation is authorized by installing this package.

## Included components

- `WARP.md`: the native Warp Project Rules file for this package. Current Warp supports `WARP.md` for Project Rules, applies it automatically when in scope, and gives it priority over `AGENTS.md` if both files exist in the same directory. This package intentionally retains `WARP.md` as the backwards-compatible Project Rules filename and does not duplicate the same rules in `AGENTS.md`.
- `.agents/skills/*/SKILL.md`: native Warp project Skills in the current recommended project Skill location. Warp discovers in-scope Skills automatically based on working-directory/project scope. Warp Agent can invoke relevant Skills automatically, and Skills may also be invoked directly with Warp slash-command behavior such as `/{skill-name}`.
- `docs/workflows/*.md`: auxiliary Software Development process references. These Markdown files are not native Warp Drive Workflows, are not executed automatically, are not imported automatically, and are not auto-loaded as Project Rules or Skills.

There are no repository custom-agent files, cloud agents, schedules, triggers, MCP configuration, credentials, provider/model pins, or deployment/release automation.

## Installation

Copy the contents of `warp/software-development/` into the target repository root, preserving:

- `WARP.md`
- `.agents/skills/`
- `docs/workflows/`

If the target repository already has `WARP.md`, manually merge the Software Development rules into the existing file instead of overwriting project-specific rules. If the target repository already has `AGENTS.md`, Warp still supports `WARP.md`; when both `WARP.md` and `AGENTS.md` exist in the same directory, Warp gives `WARP.md` priority. Merge intentionally so the active rule precedence is clear.

If the target already has `.agents/skills/`, merge Skill directories safely and do not overwrite project-specific Skills blindly. Skill names should remain unique unless the team intentionally accepts Warp's documented name-conflict behavior.

Do not authenticate Warp Drive, create cloud objects, enable MCP, configure credentials, select a provider/model, configure private endpoints, or create automation while installing this generic package.

## Usage

Use Warp Agent from the target repository. Warp receives applicable Project Rules from `WARP.md` and automatically discovers in-scope Skills under `.agents/skills/`. Skills complement persistent Rules: Rules define always-on constraints and operating expectations; Skills define focused procedures for specific tasks. Warp may select relevant Skills automatically, and users may invoke Skills directly with supported slash-command behavior.

Use `docs/workflows/` as reference documentation only. Those files describe process gates and evidence expectations for common Software Development work, but they are not Warp Drive Workflow objects and do not introduce an executable command mechanism.

Safe example requests:

- "Analyze this feature request, produce requirements and architecture considerations first, and do not implement until the plan is approved."
- "Review this implementation with independent code-quality and engineering-risk stages; report findings and do not edit files."

## Operating model

The Software Development Lead owns intake, scope, routing, approvals, dependency control, separation of duties, and final evidence aggregation. Specialist responsibilities are represented through Project Rules, Skills, auxiliary process references, and requested review stages rather than custom repository agents. Implementation, independent code-quality review, engineering-risk review, and release readiness remain separate.

## Project-dependent configuration

The target project must provide repository/module paths, source/test/resource directories, languages, frameworks, package manager, build/test/lint/type-check commands, architecture, APIs, database/storage, CI/CD, supported runtime versions, project quality gates, generated-code areas, documentation paths, test strategy, and security/compliance requirements.

These values must come from repository files, project documentation, maintainers, and review evidence. Do not store them as generic defaults in this package.

## User- or organization-dependent configuration

The user or team controls Warp account/workspace, plan availability, model/provider selection, agent profile, permissions, credentials, integrations, MCP, private endpoints, reviewers, deployment/release authorization, billing/spending authority, and privacy/telemetry preferences.

Do not store these values in this generic package. Do not configure credentials, MCP, integrations, private endpoints, billing, or release authority during package installation.

## Limitations

`WARP.md` is supported even though Warp recommends `AGENTS.md` for new projects. `.agents/skills/` is this package's selected native Skill path. `docs/workflows/*.md` are auxiliary references, not Warp Drive Workflow objects. The package includes no cloud agents, schedules, triggers, MCP configuration, credentials, provider/model pinning, custom inference endpoints, terminal hooks, installers, or deployment/release automation.
