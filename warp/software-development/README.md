# Warp - Software Development

This directory implements the Software Development specialization for Warp using honest, repository-scoped guidance. The primary Warp Agent is the Software Development Lead through `WARP.md`; there are no repository custom-agent files. Specialist responsibilities are represented as routing stages, review gates, Skills, and workflows.

## Native and manual-import content

- `WARP.md`: project guidance for the primary Warp Agent when the workspace supports project guidance loading.
- `.agents/skills/`: fourteen repository Skills automatically discoverable by Warp from the project.
- `warp-drive/rules/`: source material for Warp Drive rules or manual import.
- `warp-drive/workflows/`: eleven differentiated workflow references for manual import or supported Warp Drive surfaces.

Do not claim workflow source files are automatically loaded in every repository. Use `warp-drive/workflows/` only where the target Warp account/product surface explicitly supports them or import them manually.

## Safety boundary

The package contains no cloud-agent schedule, Oz/background job, terminal script, launcher, MCP configuration, connector, external integration, hook, auto-approval setting, model/provider pin, endpoint, credential, deployment automation, publication automation, signing automation, release automation, or fake repository agent.

Interactive human approval is required before any terminal command, edit, Git action, external action, deployment, publication, signing, release, destructive operation, dependency change, permission change, trust-boundary change, migration, or irreversible action.

## Operating model

The primary Lead confirms scope, routes responsibility stages, requires independent review after implementation, triggers engineering-risk review when needed, and aggregates evidence. Implementation, code-quality review, engineering-risk review, and release-readiness assessment remain distinct.
