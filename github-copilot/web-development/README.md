# Web Development — GitHub Copilot

This directory is an independent, platform-native Web Development specialization. Treat this directory as the package root when copying its contents into a target repository or configuring the product UI.

## Native components included
- Repository custom instructions
- Path-specific web instructions
- Custom agent profiles
- Agent Skills
- Reusable prompt files

## Intentionally omitted or disabled
- No MCP servers are embedded
- No GitHub Actions, workflows, hooks or automatic PR behavior
- No model is pinned

## Platform notes
The files target repository-scoped Copilot customization and must be copied into the target repository root. Reviewer profiles expose only read/search tools. Prompt files never instruct Copilot to push, merge, or deploy.

## Support matrix
| Component | GitHub.com cloud agent | Copilot CLI | VS Code | Visual Studio | JetBrains IDEs |
| --- | --- | --- | --- | --- | --- |
| `.github/copilot-instructions.md` | Supported | Supported | Supported | Supported | Supported |
| `.github/instructions/*.instructions.md` | Supported where repository custom instructions are enabled | Supported where repository custom instructions are loaded | Supported | Supported | Preview |
| `.github/agents/*.agent.md` | Supported | Supported | Supported | Supported | Preview |
| `.github/prompts/*.prompt.md` | Not supported | Not supported | Supported | Supported | Preview |
| `.github/skills/*/SKILL.md` | Supported | Supported | Supported | Supported | Preview |

## Manual invocation
- Select `web-development-lead` manually for multi-step coordination. It can use the `agent` tool only on surfaces where subagents are supported; otherwise manually select the specialist profiles.
- Use prompt files from supported IDE prompt pickers only. They include expected input, output, and evidence requirements in the prompt body.
- Skills are selected automatically when relevant by supported Copilot surfaces, or manually where the surface provides skill invocation.
- GitHub Actions, MCP, hooks, tokens, automatic PR creation, deployment, and publication are intentionally not configured.

## Safety baseline
- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Official sources reviewed
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/create-custom-agents
- https://docs.github.com/en/copilot/reference/custom-agents-configuration
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills
- https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/customization-cheat-sheet
