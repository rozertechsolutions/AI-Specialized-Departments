# Native GitHub Copilot Sources

Official GitHub documentation checked on 2026-07-15:

- Repository custom instructions: `https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions`
- Custom instructions support: `https://docs.github.com/en/copilot/reference/custom-instructions-support`
- Copilot cloud agent environment: `https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment`
- GitHub Docs LLM index: `https://docs.github.com/llms.txt`

Implementation decision: use `.github/copilot-instructions.md`, `.github/agents/*.agent.md`, and `.github/skills/*/SKILL.md`. Omit cloud-agent setup, Actions workflows, hooks, MCP servers, extensions, executable scripts, active automations, external connectors, and live integrations because this package is static guidance only.
