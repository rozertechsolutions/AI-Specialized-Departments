# Claude Mobile Development

This directory is a manual source package for a Claude Project that supports Android, iOS, Kotlin Multiplatform (KMP), Flutter, and React Native work. It targets Claude chat on the hosted web, desktop, and mobile surfaces. It is not a Claude Code configuration and is not discovered automatically from a repository checkout.

The package was checked against current official documentation on 2026-07-15. Claude is a hosted product, so this repository cannot detect the user's plan, organization policy, application build, enabled capabilities, or connected accounts. Confirm those items in the destination account before installation and again at the start of each task.

## Native implementation

| Component | Classification | How it is used |
| --- | --- | --- |
| Claude Project | Native | Create it manually in Projects. |
| Project instructions | Native | Paste project/PROJECT_INSTRUCTIONS.md into Set project instructions. |
| Project knowledge | Native | Upload the four files listed in project/KNOWLEDGE_UPLOAD_MANIFEST.md. |
| Project RAG | Native when available | Claude activates it automatically; this package does not enable or control it. |
| Ten custom Skills | Native when Skills and code execution are enabled | Package and upload each skills subdirectory separately. |
| Conversational responsibility boundaries | Native | Project instructions and knowledge make one Claude session adopt one bounded responsibility at a time. |
| GitHub and Google Drive project content | Native and optional | A human may connect them manually with least privilege. |
| Directory connectors such as Figma and Sentry | Native and optional | A human may install and enable only required read tools. |
| Remote custom MCP connector | Native beta, not installed here | Documented only; no server, URL, or credentials are configured. |
| Repository agents or subagents | Unsupported on this target | No agents or subagents directory is included. |
| Repository hooks or executable permission guards | Unsupported on this target | No hooks are included or simulated. |
| Repository workflow files or commands | Unsupported on this target | Each reusable process exists exactly once as a custom Skill. |
| Local MCP configuration | Unsupported for the cross-surface target | No mcp directory or Claude Desktop configuration is included. |
| Automatic repository discovery, local builds, devices, signing, or publication | Unsupported as an inherent Project capability | Claude may use only tools explicitly enabled in the current chat and must report their limits. |

## Package layout

    mobile-development/
    ├── README.md
    ├── project/
    │   ├── PROJECT_INSTRUCTIONS.md
    │   └── KNOWLEDGE_UPLOAD_MANIFEST.md
    ├── knowledge/
    │   ├── MOBILE_DEVELOPMENT_SCOPE.md
    │   ├── RESPONSIBILITY_MODEL.md
    │   ├── QUALITY_AND_COMPLETION_STANDARDS.md
    │   └── SECURITY_AND_HUMAN_REVIEW.md
    ├── skills/
    │   ├── create-mobile-project/SKILL.md
    │   ├── implement-mobile-feature/SKILL.md
    │   ├── fix-mobile-bug/SKILL.md
    │   ├── review-mobile-architecture/SKILL.md
    │   ├── add-mobile-screen/SKILL.md
    │   ├── integrate-mobile-api/SKILL.md
    │   ├── add-mobile-tests/SKILL.md
    │   ├── optimize-mobile-performance/SKILL.md
    │   ├── audit-mobile-security/SKILL.md
    │   └── prepare-mobile-release/SKILL.md
    └── connectors/
        └── CONNECTOR_SETUP_AND_SAFETY.md

## Installation

1. In Claude, verify the active surface, plan, workspace type, organization policy, Skills availability, code execution setting, and tool access. Record anything that cannot be verified as unknown.
2. Create a new Project. On Team or Enterprise, choose the intended visibility deliberately; private is the safe default.
3. Paste the full contents of project/PROJECT_INSTRUCTIONS.md into Set project instructions.
4. Follow project/KNOWLEDGE_UPLOAD_MANIFEST.md and upload the four knowledge files. Do not upload secrets, local environment files, signing material, production data, or this entire repository.
5. If custom Skills are available, enable Code execution and file creation as required by the account or organization. Review every Skill source before upload.
6. Compress each direct child of skills as its own ZIP. The ZIP must contain the named Skill folder at its root, and that folder must contain SKILL.md. Do not combine the ten Skills into one ZIP.
7. In Customize > Skills, choose Create skill, then Upload a skill. Upload and enable only the workflows needed. Organization provisioning or sharing must be a deliberate owner-controlled action where available.
8. Leave all connectors disconnected. If repository or design context is needed, follow connectors/CONNECTOR_SETUP_AND_SAFETY.md and approve the minimum read access manually.
9. Start a fresh Project chat and ask Claude to report its detected surface, available tools, connected sources, repository snapshot, mobile technologies, and evidence limitations before doing work.

No generated ZIP archives are committed because the Markdown sources are reviewable, portable, and can be packaged without introducing opaque binary artifacts.

## Project knowledge and RAG

Project knowledge is shared across chats only when content is added to the Project. Conversation context from one chat is not automatically shared with another. Upload descriptive, focused files and reference filenames explicitly in requests.

Claude may automatically use retrieval augmented generation when project knowledge approaches context limits. Official Help Center pages currently disagree about whether expanded RAG is available on every plan or only paid plans. Treat RAG as plan- and account-dependent, verify the indicator in the actual Project, and never make workflow correctness depend on RAG being active.

RAG retrieves relevant excerpts rather than guaranteeing that every uploaded sentence is present in each response. Project instructions therefore contain the non-negotiable coordinator and safety rules; knowledge files contain detailed routing and evidence guidance. Ask Claude to retrieve a named knowledge file whenever its details matter.

## Plan and surface limitations

- Projects are documented for all Claude users; the current Help Center states that Free accounts may create up to five Projects.
- Custom Skills are documented for Free, Pro, Max, Team, and Enterprise accounts, but require code execution and may require organization-owner enablement.
- A hosted Project has no repository-local version file or SDK. App version, plan, workspace type, model choice, and enabled tools cannot be inferred from this package.
- Skills uploaded on one product surface may not synchronize automatically to another. Confirm availability in the surface where the task will run.
- A GitHub Project source supplies selected file names and contents from a branch; it does not inherently provide local edit, build, device, commit-history, pull-request, or publication access.
- Code execution is a sandboxed environment, not proof of access to the user's local checkout, installed mobile SDKs, simulators, devices, signing identities, or stores.
- The conversational roles in this package are responsibility boundaries, not independent Claude agents. For high-risk work, an independent human or separate authorized review session remains required.

## Documentation corrections and conservative choices

Current official pages contain several inconsistencies. This package applies the narrowest format that satisfies all of them:

- Some Help Center text says skill.md, while Claude Platform documentation and organization provisioning require SKILL.md. Every package uses uppercase SKILL.md.
- Help Center guidance gives a 200-character description limit, while Platform documentation allows 1,024 characters. Every description here is below 200 characters.
- Recent Help Center guidance documents Skills on all plans and organization sharing controls; older Platform text describes narrower plan and sharing support. Installation requires checking the live account instead of assuming either state.
- Project pages disagree on RAG plan coverage. RAG is treated as automatic but optional.
- Remote custom connectors are documented as beta. This stable package does not configure one; it provides safety guidance only.

## Official documentation consulted

- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [Create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Retrieval augmented generation for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)
- [Claude personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)
- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Use connectors to extend Claude](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Use the GitHub integration](https://support.claude.com/en/articles/10167454-use-the-github-integration)
- [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [Custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Interactive connectors](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
- [Figma MCP documentation](https://developers.figma.com/docs/figma-mcp-server/)
- [Sentry connector directory entry](https://claude.com/connectors/sentry)
- [Firebase MCP server](https://firebase.google.com/docs/ai-assistance/mcp-server)

## Baseline state

Nothing in this package creates a Project, uploads knowledge, enables a Skill, connects an account, authenticates a connector, invokes an external tool, edits an application, runs a build, signs an artifact, or publishes anything. Every such action remains visible and human-controlled.
