# Codex Mobile Development

This specialization configures OpenAI Codex for Android, iOS, Kotlin Multiplatform, Flutter, and React Native work. It uses only native Codex surfaces: nested `AGENTS.md` instructions, project-scoped custom agents, repository Skills, command hooks, and project-scoped MCP configuration.

## Activation scope

Start Codex with the current working directory set to `codex/mobile-development/` or one of its descendants. Codex discovers nested `.codex/config.toml`, `.codex/agents/`, `.codex/hooks.json`, `.agents/skills/`, and `AGENTS.md` while walking from the repository root to the working directory. Starting Codex at the repository root does not activate configuration stored below that directory.

The project must be trusted before Codex loads project-scoped `.codex` configuration. Review new or changed command hooks with `/hooks`; Codex skips untrusted project hooks.

The command hooks require Python 3.9 or later. Unix-like hosts must expose it as `python3`; Windows hosts must provide the standard `py -3` launcher used by `commandWindows`.

## Native layout

```text
mobile-development/
├── AGENTS.md
├── README.md
├── .codex/
│   ├── config.toml
│   ├── hooks.json
│   ├── agents/
│   │   └── *.toml
│   └── hooks/
│       └── *.py
└── .agents/
    └── skills/
        └── */SKILL.md
```

Generic `agents/`, `subagents/`, `skills/`, `hooks/`, `mcp/`, and `workflows/` directories are not Codex configuration surfaces and must remain absent. Workflows are implemented only as repository Skills under `.agents/skills/`.

## MCP integrations

All MCP servers in `.codex/config.toml` are disabled by default, optional, non-required, restricted to read-oriented tools, and use the `prompt` mode to require approval for every tool call. Enabling a server is a deliberate local action: change only that server's `enabled` value to `true`, satisfy its prerequisite, restart Codex, authenticate if required, and inspect the resulting tools with `/mcp`. Never commit credentials or authenticated session material.

- **Firebase** uses a user-installed `firebase` CLI from `PATH`. It requires Node.js, npm, and an authenticated Firebase CLI session prepared outside this repository. No package is downloaded by cloning or by the disabled template. Its allowlist is limited to project/app metadata, security-rule inspection, Firebase resources, and Crashlytics reads. It can expose project metadata and crash data that may contain personal or production information.
- **Figma** uses `https://mcp.figma.com/mcp` with OAuth. Its allowlist covers design context, metadata, screenshots, variables, and existing Code Connect mappings. It can disclose private product designs and assets.
- **GitHub** uses `https://api.githubcopilot.com/mcp/`. It expects a least-privilege token through the local `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable; the value is never stored here. Its allowlist covers repository file and pull-request reads. It can disclose private repository content available to the token.
- **Sentry** uses `https://mcp.sentry.dev/mcp` with OAuth. Its allowlist covers organization/project discovery and issue, event, and trace reads. Telemetry can contain personal data, source context, request data, or production identifiers.

Enable only the server needed for the current task, minimize account scope, review each approval request, and disable the server again when it is no longer needed.

## Security model and limitations

- The default sandbox is `workspace-write` with outbound shell network access disabled and interactive approvals enabled.
- Publishing, store submission, signing, deployment, release creation, credential handling, and destructive device operations are prohibited by the instructions and guarded by command hooks.
- Command hooks are deterministic guardrails, not a complete security boundary. Current `PreToolUse` interception does not cover every shell execution path or non-shell tool. Repository policy, the sandbox, approvals, and human review remain authoritative.
- Only `command` hook handlers are used. Current Codex releases parse but skip `prompt`, `agent`, and asynchronous command handlers.
- Custom agents are direct subagents only. `agents.max_depth = 1` prevents recursive delegation.
- Workflows are implemented as Skills because Codex has no separate native `workflows/` file format.
- No model is pinned. Custom agents inherit the user's supported model and reasoning configuration.
- No MCP server is contacted during installation or validation of this specialization.
- Static hook tests are provided in `.codex/hooks/tests/test_hooks.py` for manual execution with `python3 -m unittest discover -s .codex/hooks/tests`; they were not executed during static generation.

## Official references

- [Codex custom agents](https://developers.openai.com/codex/subagents)
- [Codex Skills](https://developers.openai.com/codex/skills)
- [Codex hooks](https://developers.openai.com/codex/hooks)
- [Codex MCP](https://developers.openai.com/codex/mcp)
- [Firebase MCP](https://firebase.google.com/docs/ai-assistance/mcp-server)
- [Figma MCP](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [GitHub MCP for Codex](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-codex.md)
- [Sentry MCP](https://mcp.sentry.dev/)
