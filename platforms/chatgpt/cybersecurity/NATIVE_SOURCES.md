# Native Sources

Documentation review date: 2026-07-21.

Product surface: ChatGPT web and desktop Projects, Custom GPTs, Skills, project files/sources, apps/plugins/connectors, and Workspace Agents where enabled.

## Official Source Checks

### Check 1 - Current reference documentation

- Projects in ChatGPT: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- Creating and editing GPTs: https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Apps in ChatGPT: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt
- Workspace agents Academy: https://openai.com/academy/workspace-agents/

### Check 2 - Release notes or changelog

- ChatGPT release notes: https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- Workspace Agents announcement: https://openai.com/index/introducing-workspace-agents-in-chatgpt/

Current notes checked for Projects, Skills, plugins/apps, Workspace Agents, custom GPTs, app permissions, workspace controls, and plan limitations.

### Check 3 - Current product behavior and schema

- ChatGPT Projects group chats, files/sources, memory, and project instructions. Project instructions apply only inside that Project and override global custom instructions.
- ChatGPT does not auto-load repository files; import is manual through Project, GPT, Skill, or Workspace Agent UI.
- Skills are reusable workflows. ChatGPT Skills can be created, uploaded, installed, shared, or published depending on plan and workspace permissions, and uploaded Skills are scanned before use.
- Apps/plugins/connectors are external integrations with separate connection, authentication, role, and action controls.
- Workspace Agents are governed workflows in eligible workspaces and use per-agent tools, approvals, triggers, schedules, and sharing controls set by builders and admins.

## Current Native Facts

- Area path: `chatgpt/cybersecurity/<area>/`.
- Primary instructions: `PROJECT_INSTRUCTIONS.md`.
- Knowledge: `knowledge/*.md`.
- Skills: `skills/<skill>/SKILL.md`.
- Workflow guidance: `workflows/*.md`.
- Output templates: `templates/*.md`.
- Discovery: manual import only; no repository autoload.
- Apps/plugins/connectors: absent by default and optional only through separately approved ChatGPT settings.
- Workspace Agents: not represented as repository code; builders must create them manually in ChatGPT if eligible.

## Discovery, Precedence, And Trust

- Project instructions apply inside the selected Project and override global custom instructions.
- Project files and sources are available only after upload or source addition.
- Shared project visibility depends on owner/admin sharing controls and plan limits.
- Skills must be uploaded, created, installed, shared, or published through ChatGPT.
- App permissions do not connect an app or grant new external access; they only control approval prompts for already-connected app capabilities.
- Workspace Agents use per-agent and workspace controls, not repository-local config.

## File Classification

- Retained: eight `PROJECT_INSTRUCTIONS.md` files, eight knowledge files, 34 Skills, eight workflow files, and eight template files.
- Retained because operational: area knowledge, workflow, and template files are uploaded as Project/GPT/Workspace Agent context and are not repository-autoload claims.
- Omitted: repository-discovered agents, hooks, MCP runtime, coding-agent config, scanner connectors, cloud integrations, schedules, Slack deployment, and production actions.
- Deleted: none for this stage; no exact duplicate Project/knowledge pairs were found.

## Removed Or Deprecated Field Handling

- No repository-discovered agents are claimed.
- No hooks, MCP runtime, coding-agent permissions, or app connections are simulated.
- Workspace Agents are documented as a manual eligible-workspace setup, not as files loaded from this repository.
- Apps/plugins/connectors are documented as optional manual integrations with separate permissions.

## Validation Method

- Inventory of all eight ChatGPT Cybersecurity areas.
- Markdown frontmatter checks for retained Skills.
- Duplicate check for `PROJECT_INSTRUCTIONS.md` versus knowledge files.
- Confirmation that no fake repository agents, hooks, MCP runtime, executable workflows, or credentials are present.
- README review for manual import, plan/workspace limitations, project-dependent values, user/organization-dependent values, fixed safety baseline, removal, and security notice.
