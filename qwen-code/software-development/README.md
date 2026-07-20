# Qwen Code - Software Development

This directory implements the Software Development specialization for Qwen Code using repository-scoped native content. The main Qwen Code session is the Software Development Lead through `QWEN.md`; there is intentionally no `.qwen/agents/software-development-lead.md` subagent.

## Native content

- `QWEN.md` defines the main-session Software Development Lead behavior.
- `.qwen/settings.json` sets `{ "tools": { "approvalMode": "default" } }` only.
- `.qwen/agents/` contains seven specialist subagents with explicit `approvalMode`, tool allowlists, and `run_shell_command` denied.
- `.qwen/skills/` contains fourteen preserved non-executable capability Skills.
- `.qwen/commands/` contains eleven current Markdown prompt-only workflow commands.

## Parent approval-mode requirement

Start and keep the parent Qwen Code session in `default` approval mode. A permissive parent session such as `auto-edit` or `yolo` can override subagent restrictions. This package does not claim project settings can defeat explicit permissive CLI flags.

## Tool policy

Read-only specialists use `approvalMode: plan` and only `read_file`, `grep_search`, and `list_directory`. The implementation specialist uses `approvalMode: default` and only `read_file`, `grep_search`, `write_file`, and `replace`. All specialists disallow `run_shell_command` and omit MCP, browser, network, shell, Git, deployment, publication, signing, release, and external tools.

The package contains no hooks, deprecated TOML commands, scripts, provider/model/auth configuration, endpoints, credentials, environment values, MCP configuration, extensions, sandbox builders, deployment automation, publication automation, signing automation, release automation, or executable assets.

## Operating model

Commands and user requests route through the main Software Development Lead session. The Lead may call specialists for bounded responsibilities, but specialists return evidence to the Lead, never call each other, cannot expand scope, and cannot claim final completion. Implementation, code-quality review, engineering-risk review, and release-readiness assessment remain distinct.
