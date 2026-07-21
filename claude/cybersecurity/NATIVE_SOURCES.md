# Native Sources

Documentation review date: 2026-07-21.

Product surface: Claude web and Claude Desktop Projects, project instructions, project knowledge, Claude Skills, memory, sharing controls, and optional connectors.

## Official Source Checks

### Check 1 - Current reference documentation

- What are Projects: https://support.anthropic.com/en/articles/9517075-what-are-projects
- How to create and manage Projects: https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Personalization features, including project instructions and Skills: https://support.anthropic.com/en/articles/10185728-understanding-claude-s-personalization-features
- Use connectors to extend Claude's capabilities: https://support.anthropic.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp

### Check 2 - Release notes or recent product notes

- Claude project and sharing articles were checked for current plan, sharing, RAG, and memory behavior.
- Claude connector articles were checked for remote connector and remote MCP behavior.
- Claude Skills support articles were checked for current Skill availability and manual setup behavior.

### Check 3 - Current product behavior and schema

- Claude Projects are self-contained workspaces with project instructions, project knowledge, project chats, sharing controls, and project-scoped memory behavior.
- Project instructions are added through `Set project instructions`; they are not repository files discovered from disk.
- Project knowledge requires manual upload or source addition. Paid plans may enable RAG mode when knowledge approaches the context limit.
- Skills customize Claude behavior and can be created, uploaded, installed, or shared only through the supported Claude Skill surface.
- Connectors are separate integrations. Claude inherits the user's permissions from the connected service and can access or act only according to the configured connector.

## Current Native Facts

- Area path: `claude/cybersecurity/<area>/`.
- Primary instructions: `PROJECT_INSTRUCTIONS.md`.
- Skills: `skills/<skill>/SKILL.md`.
- Workflow guidance: `workflows/*.md`.
- Output templates: `templates/*.md`.
- Unique area knowledge retained: `governance-risk-compliance-assurance/knowledge/GOVERNANCE.md` and `security-architecture-engineering/knowledge/ARCHITECTURE_GOVERNANCE.md`.
- Discovery: manual import only; no repository autoload for Claude web or Desktop.
- Connectors and remote MCP: absent by default and optional only through separately approved Claude settings.

## Discovery, Precedence, And Trust

- Project instructions apply inside the selected Claude Project.
- Project knowledge is separate from instructions and is available only after upload or source addition.
- Shared project visibility depends on owner/admin sharing controls and plan limits.
- Skills must be created, uploaded, installed, or shared through Claude.
- Connectors require explicit configuration and inherit source-system permissions.

## File Classification

- Retained: eight `PROJECT_INSTRUCTIONS.md` files, 47 Skills, 16 workflow files, eight template files, and two unique knowledge files.
- Retained workflow pairs: one file provides area-specific procedure guidance and one provides a compact manual workflow entry point; they are not exact duplicates.
- Deleted: eight exact duplicate `knowledge/RESPONSIBILITY_MODEL.md` files because each matched its area's `PROJECT_INSTRUCTIONS.md` byte-for-byte and did not add independent Project knowledge value.
- Omitted: repository-discovered agents, hooks, MCP runtime, coding-agent config, scanner connectors, cloud integrations, schedules, and production actions.

## Removed Or Deprecated Field Handling

- No repository-discovered agents are claimed.
- No hooks, MCP runtime, coding-agent permissions, connector access, or app connections are simulated.
- Project knowledge files are documented as manual uploads, not auto-loaded repository artifacts.
- Connectors and remote MCP are documented as optional manual integrations with separate permissions.

## Validation Method

- Inventory of all eight Claude Cybersecurity areas.
- Markdown frontmatter checks for retained Skills.
- Exact duplicate comparison for `PROJECT_INSTRUCTIONS.md` versus `knowledge/RESPONSIBILITY_MODEL.md`.
- Removal of exact duplicate knowledge files and empty directories.
- Confirmation that no fake repository agents, hooks, MCP runtime, executable workflows, or credentials are present.
- README review for manual import, plan/workspace limitations, project-dependent values, user/organization-dependent values, fixed safety baseline, removal, and security notice.
