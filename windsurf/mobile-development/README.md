# Windsurf Mobile Development Specialization

This specialization is configured for Devin Desktop Cascade when `windsurf/mobile-development/` is opened as the workspace root.

## Verified Surface

- Selected surface: Cascade in Devin Desktop.
- Installed local app or CLI: not detected in `/Applications` or `PATH` during repository implementation.
- Product plan and account settings: unavailable locally; no assumption is made.
- Official docs checked: `AGENTS.md`, Skills, Workflows, Hooks, MCP, and Devin Local documentation at `docs.devin.ai`.

## Native Components

- `AGENTS.md`: native directory-scoped coordinator instructions.
- `.windsurf/skills/*/SKILL.md`: native workspace Skills for repeatable, automatically selected procedures.
- `.windsurf/workflows/prepare-mobile-release.md`: native manual Workflow for release preparation.
- `.windsurf/hooks.json`: native workspace hook configuration.
- `.windsurf/hooks/*.py`: local hook scripts called by Cascade hooks.

## Unsupported Components Omitted

- Custom project agent files are omitted because current Cascade documentation does not define a stable project-scoped custom-agent schema.
- Custom project subagent files are omitted for the same reason.
- MCP servers are omitted because no inactive, approval-controlled server is required for this mobile specialization.
- Legacy generic folders are omitted; only native Cascade configuration is kept.

## Security Posture

The configuration does not contain secrets, tokens, endpoints, signing credentials, provisioning profiles, keystores, certificates, or service-account files. Hooks block suspicious secret writes, out-of-scope file writes, risky shell commands, publishing/signing/deployment commands, and MCP tool use by default.

Static hook tests are provided in `.windsurf/hooks/tests/test_hooks.py` for manual execution with `python3 -m unittest discover -s .windsurf/hooks/tests`. They are dependency-free and were not executed during static generation.

## Limitations

Cascade must load this directory as a workspace root for workspace Skills and hooks to resolve from `.windsurf/`. Android, iOS, KMP, Flutter, and React Native build commands are discovered inside the target mobile application repository at task time; this specialization does not claim build, test, security, accessibility, performance, or release evidence without running the relevant project commands.
