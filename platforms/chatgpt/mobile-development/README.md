# ChatGPT Mobile Development Specialization

This directory is a manual source package for configuring ChatGPT for mobile development work across Android, iOS, Kotlin Multiplatform, Flutter, and React Native.

Cloning this repository does not install, publish, share, enable, authenticate, schedule, connect, or deploy anything in ChatGPT. Copy the relevant source text into ChatGPT's native interfaces manually.

## Verified ChatGPT Surface

Verified on 2026-07-15 from current OpenAI Help Center documentation:

- Projects in ChatGPT: native. Projects can hold chats, files, and project instructions. Project availability and file limits vary by plan and workspace controls.
- Custom GPTs: native for paid ChatGPT users and permitted managed-workspace users. GPT building and editing is web-only; mobile apps can use GPTs but do not build them.
- GPT knowledge uploads: native. Use uploaded knowledge files as reference material, not behavior rules.
- Personal Skills: native for eligible ChatGPT Business, Enterprise, Healthcare, and Edu users. ChatGPT supports creating, editing, installing, sharing, downloading, and uploading Skills, and OpenAI documents that Skills follow the Agent Skills open standard.
- Workspace Agents: native only for eligible Business and Enterprise workspaces when enabled by admins. This package provides optional builder source text only.
- Apps, connectors, custom MCP, schedules, API triggers, Slack channels, and actions: native surfaces in some contexts, but unsupported in this package because the prompt forbids configuring active integrations and because setup is account, workspace, and approval dependent.

Actual account plan, workspace type, enabled tools, installed apps, and admin controls cannot be detected from this repository. The user configuring ChatGPT must verify those in ChatGPT before using the source text.

## Official Documentation Consulted

- https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business
- https://help.openai.com/en/articles/11487775-connectors-in-chatgpt

## Native Setup Options

1. ChatGPT Project: create a project named `Mobile Development` and paste `project/PROJECT_INSTRUCTIONS.md` into Project instructions. Upload the files listed in `project/KNOWLEDGE_UPLOAD_MANIFEST.md` only as project sources.
2. Custom GPT: create a GPT in the web GPT builder. Use `custom-gpt/GPT_BUILDER_CONFIGURATION.md`, paste `custom-gpt/GPT_INSTRUCTIONS.md` into Instructions, and add starters from `custom-gpt/CONVERSATION_STARTERS.md`. Upload the knowledge files listed in the GPT configuration.
3. Workspace Agent: only in an eligible, admin-enabled Business or Enterprise workspace. Use `workspace-agent/WORKSPACE_AGENT_CONFIGURATION.md` and `workspace-agent/AGENT_INSTRUCTIONS.md` as builder source. Keep visibility private by default.
4. Skills: if Skills are available in the target account, review one workflow directory under `skills/`, zip that single directory as the top-level Skill package, and upload it through ChatGPT's native Skills page. Install only the workflows the user intends to use.

## Native Components

| Component | Classification | Use in this package |
| --- | --- | --- |
| Project instructions | native | Primary configuration for advisory, planning, review, and supplied-file analysis. |
| Project knowledge files | native | Reference files uploaded manually. |
| Custom GPT builder fields | native | Manual source for a private GPT. |
| Workspace Agent builder fields | native, conditional | Optional source for eligible workspaces only. |
| Skills | native, conditional | Ten source-controlled Agent Skills are provided under `skills/`; upload is manual and account/workspace dependent. |
| Apps/connectors | native, conditional | Recommended read-only constraints only; not configured. |
| Custom MCP | native, conditional | Not configured. Mentioned only as a later manual option requiring approval. |
| Repository agents, subagents, hooks, workflows, MCP folders | unsupported | Omitted because ChatGPT does not discover repository folders as native configuration. |
| Shell, local build, device, simulator, signing, store publication | unsupported without separate enabled tools and evidence | Never claimed or assumed. |

## Files

- `project/PROJECT_INSTRUCTIONS.md`: Project instruction source.
- `project/KNOWLEDGE_UPLOAD_MANIFEST.md`: Files to upload as project knowledge and the reason for each.
- `custom-gpt/GPT_BUILDER_CONFIGURATION.md`: Exact builder field source.
- `custom-gpt/GPT_INSTRUCTIONS.md`: GPT behavior instructions.
- `custom-gpt/CONVERSATION_STARTERS.md`: Starter prompts.
- `workspace-agent/WORKSPACE_AGENT_CONFIGURATION.md`: Optional workspace-agent builder source.
- `workspace-agent/AGENT_INSTRUCTIONS.md`: Optional workspace-agent instructions.
- `workspace-agent/FILES_MANIFEST.md`: Optional workspace-agent file attachment list.
- `workspace-agent/CONNECTOR_CONSTRAINTS.md`: Recommended connector constraints for later manual setup.
- `skills/README.md`: Manual packaging and upload instructions for ChatGPT Skills.
- `skills/*/SKILL.md`: Ten instruction-only workflow Skills.
- `knowledge/MOBILE_DEVELOPMENT_SCOPE.md`: Scope, platform detection, and native/unsupported boundaries.
- `knowledge/RESPONSIBILITY_MODEL.md`: Twelve-role responsibility model and matrix.
- `knowledge/QUALITY_AND_COMPLETION_STANDARDS.md`: Ten workflows, validation gates, and completion criteria.
- `knowledge/SECURITY_AND_HUMAN_REVIEW.md`: Security baseline, approval rules, and fail-safe behavior.

## Omitted Components

- No connector, app, MCP, action, schedule, Slack, API trigger, or publication configuration is included.
- No secrets, tokens, keys, certificates, signing material, private endpoints, or real environment values are included.
- No automatic install or activation script is included.
