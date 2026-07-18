# Web Development - ChatGPT

This directory is a manual ChatGPT configuration package for a Web Development specialization. ChatGPT does not auto-discover or load repository files from this folder. Copy or upload the relevant files into the ChatGPT UI surface named below.

## Supported Surfaces

| File or folder | ChatGPT surface | Use |
| --- | --- | --- |
| `project-instructions.md` | Project settings > Instructions | Paste as the Project instruction body for recurring web-development work. |
| `knowledge/*.md` | Project sources or GPT Knowledge | Upload as factual reference material. These files are not hidden instructions. |
| `skills/*/SKILL.md` | Plugins > Skills in ChatGPT | Upload or create each Skill where Skills are available for the user, plan, and workspace. |
| `custom-gpt-setup.md` | GPT builder | Manual setup guide for a Custom GPT. |
| `workspace-agent-setup.md` | Workspace Agent builder | Manual setup guide for eligible Business or Enterprise workspaces. |

## Native Capability Map

| Capability | Status in this package |
| --- | --- |
| Project instructions | Native, manual paste into a ChatGPT Project. |
| Knowledge uploads | Native, manual upload as Project sources or GPT Knowledge. |
| Custom GPT | Native for users who can create/edit GPTs; manual configuration only. |
| ChatGPT Skills | Conditionally native; availability depends on plan, workspace role, admin controls, region, device surface, and rollout. |
| Workspace Agents | Conditionally native for eligible Business or Enterprise workspaces with admin enablement. |
| Apps/connectors | Manual-only optional integrations discovered through plugins or workspace settings; none are configured, connected, or trusted by default. |
| Actions | Manual-only optional Custom GPT integrations; none are configured. |
| Repository auto-discovery | Unsupported. |
| Repository subagents, hooks, MCP files, deployments, Git automation | Unsupported and intentionally omitted. |

## Manual Setup Sequence

1. Choose one primary surface: Project, Custom GPT, or Workspace Agent. Do not install the same full instruction body into multiple active surfaces for the same task unless you intentionally want those surfaces to behave alike.
2. Review the files locally before copying or uploading them.
3. Paste `project-instructions.md` only into the intended instruction field.
4. Upload the files in `knowledge/` only as reference sources.
5. Install or create Skills only if the Plugins > Skills UI is available on the intended ChatGPT surface and the workspace allows it.
6. Leave Apps, Actions, connectors, custom MCPs, external APIs, sync, write actions, schedules, API triggers, Slack channels, deployment, and publication disabled until a human reviews data access, scopes, retention, and approval requirements.
7. Test with safe representative prompts and record what was actually verified.

## Limitations

- This package cannot run commands, inspect a repository, open a browser, install dependencies, mutate Git, deploy, publish, authenticate, or connect services by itself.
- Availability can vary by ChatGPT plan, workspace role, administrator policy, region, and staged rollout.
- Project and GPT knowledge files are retrievable reference material, not a security boundary and not executable configuration.
- Apps may require plugin installation, user connection, OAuth, workspace enablement, and explicit confirmation before external actions. Workspace Agents use per-agent controls for app actions, and Enterprise/Edu defaults can differ from Business defaults.
- Runtime, browser, integration, build, test, and deployment behavior must be verified separately in the real project environment.

## Static Verification Checklist

- PASS: Every retained file maps to a current ChatGPT UI surface.
- PASS: No file implies repository auto-loading from this directory.
- PASS: No hooks, MCP configuration, action schemas, credentials, endpoints, or enabled connectors are included.
- PASS: Knowledge files contain factual reference material and avoid becoming a second instruction source.
- PASS: Skills use a folder containing `SKILL.md` with required `name` and `description` frontmatter, and each retained skill contains only static instructions.
- PASS: Human review remains required for production, auth, sensitive data, dependencies, external systems, publication, deployment, Git mutation, spending, signing, and destructive actions.
- NOT EXECUTED: Runtime checks, builds, tests, browser checks, app connections, Skill upload, GPT creation, Workspace Agent publishing, and integrations.

## Official Documentation Baseline

Accessed July 18, 2026:

- OpenAI Help Center: Projects in ChatGPT - https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- OpenAI Help Center: Creating and editing GPTs - https://help.openai.com/en/articles/8554397-creating-a-gpt
- OpenAI Help Center: GPTs in ChatGPT - https://help.openai.com/en/articles/8554407-gpts-in-chatgpt
- OpenAI Help Center: Skills in ChatGPT - https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- OpenAI Help Center: Apps in ChatGPT - https://help.openai.com/en/articles/11487775-connectors-in
- OpenAI Help Center: ChatGPT Workspace Agents for Enterprise and Business - https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business
- Agent Skills: Specification - https://agentskills.io/specification
