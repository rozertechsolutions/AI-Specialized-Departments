# Web Development - Claude

This directory is a manual Claude web/desktop Project package for a Web Development specialization. Claude does not auto-discover or load repository files from this folder. Review the files, then paste or upload them through the Claude UI surface named below.

## File-To-UI Mapping

| File or folder | Claude surface | Use |
| --- | --- | --- |
| `project-instructions.md` | Claude Project > Set project instructions | Paste as the Project instruction body for recurring web-development work. |
| `project-knowledge/*.md` | Claude Project Knowledge | Upload as factual reference material. These files are not hidden instructions. |
| `skills/*/SKILL.md` | Customize > Skills or organization-provisioned Skills | Package each skill folder and upload only where Skills are enabled and allowed. |
| `claude-project-setup.md` | Human setup checklist | Follow manually before sharing or using the Project. |

## Native Capability Map

| Capability | Status in this package |
| --- | --- |
| Project instructions | Native, manual paste into a Claude Project. |
| Project knowledge | Native, manual upload to the Project knowledge base. |
| Custom Skills | Conditionally native; availability depends on plan, code execution, workspace settings, user permissions, and rollout. |
| Organization-provisioned Skills | Conditionally native for Team and Enterprise owners or admins. |
| Connectors | Manual-only optional integrations; none are configured, authenticated, or trusted by default. |
| Local repository-agent files, executable lifecycle automation, shell permissions, and repository automation | Unsupported for this package and intentionally omitted. |
| Automatic MCP connections | Unsupported in this package; connectors/MCP require separate user or workspace setup. |

## Manual Setup Sequence

1. Create a Claude Project on a paid plan that supports Projects.
2. Paste `project-instructions.md` into Set project instructions.
3. Upload only the reviewed files in `project-knowledge/` to Project Knowledge.
4. Package and upload Skills only if Customize > Skills is available and code execution plus workspace policy allow custom Skills.
5. Leave connectors, MCP connections, external tools, scripts, write actions, deployments, publication, and Git mutation disabled unless a human approves the exact provider, scopes, data flow, retention, and action risk.
6. Test with safe representative prompts and record only what was actually verified.

## Safety baseline

- No credentials, tokens, endpoints, private URLs, executable lifecycle automation, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Static Verification Checklist

- PASS: Every retained file maps to Claude web/desktop Projects, Project Knowledge, Skills, or human setup.
- PASS: No local repository-agent file mechanism, permission file, shell configuration, or repository automation is included.
- PASS: Knowledge files contain factual reference material and avoid becoming a second instruction source.
- PASS: Skills are distinct on-demand workflows, use required name and description metadata, and include no scripts or executable resources.
- PASS: Connectors are optional and unconfigured by default.
- NOT EXECUTED: Runtime checks, builds, tests, browser checks, connector setup, Skill upload, Project creation, and integrations.

## Official Documentation Baseline

Accessed July 18, 2026:

- Claude Help Center: What are projects? - https://support.claude.com/en/articles/9517075-what-are-projects
- Claude Help Center: How can I create and manage projects? - https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude Help Center: What are skills? - https://support.claude.com/en/articles/12512176-what-are-skills
- Claude Help Center: How to create custom skills - https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Claude Help Center: Use skills in Claude - https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Claude Docs: Skills overview - https://claude.com/docs/skills/overview
- Claude Help Center: When to use desktop and web connectors - https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors
