# Native Configuration Sources

Official source checked on 2026-07-15:

- OpenAI Codex Manual: `https://developers.openai.com/codex/codex-manual.md`.

## Current native surface

The Codex manual documents durable repository instructions through `AGENTS.md`, local configuration through `config.toml` and project `.codex/config.toml`, custom local agents/subagent workflows, skills, MCP, hooks, plugins, and approval/sandbox settings. It also describes `agents.max_depth` for subagent nesting.

## Implementation decision

This package uses `AGENTS.md`, `.codex/config.toml`, and `.codex/agents/*.toml` custom agents. It omits MCP, hooks, plugins, external integrations, and generated executable files because this static cybersecurity governance area must not connect external systems or execute generated integration logic.

