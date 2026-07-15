# Native Source Verification

Official sources checked on 2026-07-16:

- ChatGPT Projects: `https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt`
- Creating and editing GPTs: `https://help.openai.com/en/articles/8554397-creating-a-gpt`
- Skills in ChatGPT: `https://help.openai.com/en/articles/20001066-skills-in-chatgpt`

## Decisions

- Project instructions, uploaded knowledge files, templates, and workflow guidance are represented as copy-ready repository artifacts.
- Custom GPT instructions and knowledge can use the same project instruction and knowledge files.
- ChatGPT Skills are represented as `skills/<skill-name>/SKILL.md` packages.
- Repository agents, subagents, hooks, MCP servers, local execution, and automated workflows are omitted because they are not ChatGPT-native repository configuration surfaces.
