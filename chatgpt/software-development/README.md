# ChatGPT - Software Development

The Software Development department is a human-reviewed specialization for requirements, planning, architecture, implementation support, testing, code review, engineering risk review, documentation, and release-readiness assessment. This ChatGPT package represents the department as manual Project, Custom GPT, Skill, Workspace Agent, and connector-policy source material because ChatGPT does not load files directly from this repository. It is safe by default: integrations remain off, actions require human review, and no file here authenticates, deploys, publishes, signs, releases, or mutates Git.

## Department Overview

Use this department for stack-agnostic software engineering work across backend services, APIs, desktop apps, CLIs, libraries, SDKs, maintenance, debugging, refactoring, quality, security, dependencies, performance, reliability, compatibility, and technical documentation. Browser-specific frontend product work belongs in Web Development; mobile-platform implementation belongs in Mobile Development. The material is language-, framework-, database-, provider-, and model-neutral.

## Possible Uses

- Turn a feature idea into requirements, acceptance criteria, and an implementation plan.
- Investigate a defect and propose a bounded correction.
- Review an architecture change, API evolution, dependency update, security remediation, performance issue, reliability issue, or technical-debt reduction.
- Prepare maintenance, compatibility, migration, documentation, and release-readiness evidence.

## Included Components

- `project/project-instructions.md`: manual-import Project instructions; paste into a ChatGPT Project when Projects are available for the account or workspace.
- `project/knowledge/`: manual Project knowledge files; upload or attach selected files through the ChatGPT Project UI.
- `custom-gpt/`: manual Custom GPT source; use only where Custom GPT creation is available and allowed.
- `skills/`: conditional Skill source packages; import only where ChatGPT Skills or plugin-packaged Skills are supported for the account/workspace.
- `workspace-agent/`: conditional manual Workspace Agent definition for Business, Enterprise, Edu, or other workspaces where Workspace Agents are available.
- `apps-connectors/`: auxiliary policy source for apps/connectors; it does not enable connectors, MCP, or apps.

None of these files auto-load from a repository checkout.

## Prerequisites

You need access to ChatGPT on a surface that supports the chosen component: Projects for Project material, Custom GPT creation for `custom-gpt/`, Skills support for `skills/`, and an eligible workspace/admin policy for Workspace Agents or connectors. You also need repository or project context you are authorized to share with ChatGPT. Human approval is expected before any external action, connector authorization, code change, Git operation, release action, or destructive step.

## Installation or Setup

1. Open the destination ChatGPT Project, Custom GPT builder, workspace-agent builder, or Skill-management UI.
2. Paste `project/project-instructions.md` into Project instructions for a Project setup.
3. Upload selected `project/knowledge/*.md` files as Project knowledge only if they are appropriate for that workspace.
4. For a Custom GPT, manually adapt `custom-gpt/instructions.md`, `custom-gpt/conversation-starters.md`, and `custom-gpt/capability-policy.md`.
5. For Skills, import each supported folder under `skills/<skill-name>/` according to the current ChatGPT Skills or plugin UI.
6. Treat `apps-connectors/apps-connectors-policy.md` as policy text only; enable no app, connector, or MCP server unless a human explicitly approves it in ChatGPT.

Do not paste secrets, private endpoints, account IDs, or credentials into any setup field.

## Usage

Start in the Project, GPT, Skill-enabled chat, or Workspace Agent surface you configured. Ask the Lead to clarify scope, route work through the responsibility areas, separate implementation from independent review, and report evidence before completion.

Example requests:

- "Analyze this maintenance request and produce acceptance criteria, risks, and a validation plan."
- "Review this proposed API change for compatibility and migration risk; do not edit anything."
- "Plan a safe bug fix and list the evidence needed before I approve implementation."

## Operating Model

The Software Development Lead owns intake, scope, routing, approvals, dependency control, and final evidence aggregation. Specialists cover requirements/planning, architecture, implementation/maintenance, test/quality, code quality review, engineering risk review, and documentation/release readiness. A role that implements substantive work must not certify its own work.

## Safety and Human Review

Use least privilege and share only the context needed for the task. Connectors, apps, browsing, file creation, code execution, Git mutation, dependency changes, deployment, publication, signing, release, spending, submissions, and destructive actions require explicit human authorization in the active task. Text instructions reduce risk but do not replace ChatGPT account controls, workspace admin policy, or user review.

## Platform Limitations

ChatGPT does not automatically read this repository package. Projects, Custom GPTs, Skills, Workspace Agents, apps, and connectors are account-, plan-, workspace-, region-, and admin-policy dependent. Workspace Agents and plugin/Skill behavior can vary by product surface. This package includes no fake `.chatgpt/` directory, hooks, MCP config, active connector config, or repository-loaded agent file.

## Updating and Removal

To update, compare your existing Project/GPT/Skill/workspace text with the new package and preserve local customizations before replacing content. To remove, delete the pasted Project instructions, uploaded knowledge, imported Skills, Custom GPT text, Workspace Agent definition, and any manually copied policy text for this department only. No integrations, credentials, or account settings are stored in this package.
