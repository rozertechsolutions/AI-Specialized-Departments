# Claude Project Manual Setup

Use this guide in Claude web or Claude Desktop. This directory is not loaded automatically and is not a local repository-agent package.

## Availability

- Claude Projects are available on paid Claude plans.
- Project sharing and organization-wide visibility depend on Team or Enterprise workspace settings.
- Custom Skills require Skills availability, code execution being enabled, and any applicable workspace owner or admin permissions.
- Connectors are optional integrations. Remote web connectors require paid-plan availability; desktop extensions require Claude Desktop and local installation. This package does not configure either type.

## Setup Steps

1. Open Claude and create a new Project named `Web Development Department`.
2. Add a short Project description for humans. Do not rely on the description as model instructions.
3. Paste the full contents of `project-instructions.md` into Set project instructions and save.
4. Upload only the reviewed files from `project-knowledge/` to Project Knowledge.
5. If Skills are available, review each folder in `skills/`, package one skill folder at a time, upload it through Customize > Skills, and enable only the skills needed for this Project.
6. Leave connectors, MCP connections, desktop extensions, external tools, scripts, write actions, deployment, publication, and Git mutation disabled unless a human approves the exact provider, permissions, data flow, retention, and external effects.
7. Start a safe Project chat and verify that Claude distinguishes uploaded knowledge from instructions, marks unexecuted checks as NOT EXECUTED, and asks for approval before external or destructive actions.
8. Share the Project only with the intended audience and only after workspace policy, Project Knowledge contents, Skills, and connector status are reviewed.

## Completion Criteria

- Project instructions were pasted into the Project instruction field.
- Project Knowledge contains only factual reference files from `project-knowledge/`.
- Skills, if used, were reviewed, uploaded, enabled, and tested individually.
- Connectors remain disabled unless explicitly approved and configured outside this package.
- No local repository-agent files, shell permissions, credentials, endpoints, or automated repository controls were added.
