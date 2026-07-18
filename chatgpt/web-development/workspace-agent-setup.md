# Workspace Agent Manual Setup

Use this guide only where ChatGPT Workspace Agents are available for the user's Business or Enterprise workspace and enabled by the workspace administrator. A Workspace Agent is a managed ChatGPT agent created in the Agents builder; it is not loaded from this repository folder.

## Availability And Governance

- Workspace Agents are controlled by workspace plan, role permissions, administrator settings, region, and staged rollout.
- Enterprise workspaces may have Workspace Agents off by default until an admin enables them for eligible roles.
- Agent sharing, editing, Apps, tools, scheduled runs, API triggers, and Slack use depend on workspace policy and the agent owner's permissions.
- Collaborators can only use or edit agents according to their assigned access level.

## Agent Configuration

| Agent field | Value |
| --- | --- |
| Name | Web Development Department |
| Description | Plans, reviews, and supports web-development work with strict safety, evidence, and human-review boundaries. |
| Instructions | Paste `project-instructions.md` when the Workspace Agent is the primary surface, then add workspace-specific policy if approved. |
| Files | Add the files in `knowledge/` as controlled reference material. |
| Skills | Attach the Skills in `skills/` only if Skills are available in the agent builder and the workspace allows them. Review each Skill before use. |
| Apps and connectors | Disabled by default. Add only reviewed Apps with least-privilege access. |
| Custom MCPs, tools, schedules, API triggers, Slack | Disabled by default unless the workspace owner approves the exact use case, permissions, and external effects. |

## Setup Steps

1. Open Agents in ChatGPT and create a new agent or start from a blank builder.
2. Configure the agent fields above.
3. Add reference files and Skills only after reviewing their contents.
4. Keep permissions minimal. Prefer chat-only access for users who do not need edit rights.
5. Preview the agent with safe tasks that exercise planning, review, blocked-state reporting, and human-approval refusal.
6. Publish only after workspace policy, sharing audience, Apps, tools, and external actions have been reviewed.

## Human Review Points

Require explicit human review before enabling Apps, external write actions, schedules, API triggers, Slack operation, production access, authentication or authorization changes, dependency changes, sensitive data handling, publication, deployment, Git mutation, spending, signing, or destructive actions.

## Validation

Record what was actually tested in Preview. Runtime builds, tests, browser checks, integrations, schedules, API triggers, Slack behavior, and deployment remain NOT EXECUTED unless verified in the real workspace.
