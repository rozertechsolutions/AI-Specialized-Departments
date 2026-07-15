# Cybersecurity Governance, Risk, Compliance & Assurance for ChatGPT

This package defines a ChatGPT-native cybersecurity governance, risk, compliance, and assurance workspace. It is intended for manual setup in a ChatGPT Project, Custom GPT, or ChatGPT Skills library where the user's plan and workspace settings support those features.

## Native mechanisms used

- `PROJECT_INSTRUCTIONS.md`: copy into ChatGPT Project instructions or Custom GPT instructions.
- `knowledge/`: upload as project or GPT knowledge files.
- `skills/*/SKILL.md`: upload or recreate as ChatGPT Skills when Skills are enabled for the workspace.
- `workflows/`: upload as project or GPT knowledge files and reference from instructions.
- `templates/`: upload as knowledge files for structured outputs.

## Unsupported mechanisms intentionally omitted

ChatGPT does not provide a repository-native agent tree, subagent tree, hook runner, MCP server configuration, local workflow runner, or local permission policy for this package. External apps, actions, and connectors are not configured by default.

## Safety baseline

The assistant supports governance and assurance analysis only. It must not approve strategy, publish policy, accept risk, grant exceptions, approve suppliers, make legal determinations, claim compliance or certification, close critical findings by self-review, contact external parties, connect to security tools, scan systems, retrieve secrets, or execute active security operations.

