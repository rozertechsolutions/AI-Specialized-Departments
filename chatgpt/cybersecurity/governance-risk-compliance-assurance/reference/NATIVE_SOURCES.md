# Native Configuration Sources

Official sources checked on 2026-07-15:

- OpenAI Help Center: Projects in ChatGPT, `https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt`.
- OpenAI Help Center: GPTs in ChatGPT, `https://help.openai.com/en/articles/8554407`.
- OpenAI Help Center: Creating and editing GPTs, `https://help.openai.com/en/articles/8554397-creating-a-gpt`.
- OpenAI Help Center: Skills in ChatGPT, `https://help.openai.com/en/articles/20001066-skills-in-chatgpt`.

## Current native surface

ChatGPT Projects support project instructions, uploaded files, project sources, project memory behavior, project sharing, and use of connected apps subject to workspace settings. Custom GPTs support instructions, conversation starters, knowledge files, selected capabilities, apps or actions, preview, save/update, and version history. ChatGPT Skills are reusable workflows that can include instructions, examples, and code, and can be created, uploaded, installed, shared, or managed when the workspace enables Skills.

## Implementation decision

This package uses only manual ChatGPT project/GPT instructions, uploadable knowledge files, uploadable Skill definitions, workflow knowledge files, and output templates. It does not define repository-local agents, subagents, hooks, MCP servers, action schemas, apps, or connector configuration because those would require unsupported or externally connected behavior for this static package.

