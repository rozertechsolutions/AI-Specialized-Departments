# Native Gemini CLI Sources

Official Gemini CLI documentation checked on 2026-07-15:

- Gemini CLI repository: `https://github.com/google-gemini/gemini-cli`
- Gemini CLI docs: `https://www.geminicli.com/docs/`
- Context files: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/gemini-md.md`
- Subagents: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/core/subagents.md`
- Agent Skills: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md`
- Using Agent Skills: `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/using-agent-skills.md`

Implementation decision: use `GEMINI.md`, project `.gemini/agents/*.md`, and workspace `.gemini/skills/*/SKILL.md`. Omit hooks, MCP servers, custom commands, extensions, executable scripts, active settings, and live integrations because this package is static guidance only.
