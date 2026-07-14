# AI Specialized Departments

AI Specialized Departments is a multi-platform collection of professional AI configurations organized by department and specialty.

Each department contains the agents, subagents, skills, hooks, MCP integrations, and workflows required for its specific field.

## Purpose

The project provides focused AI configurations for professional areas such as:

* Software development
* Web development
* Cybersecurity
* Marketing
* Medicine
* Legal
* Finance
* Education

Each specialty is designed independently so it only contains the components it actually requires.

## Supported Platforms

The project may include native configurations for platforms such as:

* OpenAI Codex
* Claude Code
* Gemini CLI
* GitHub Copilot
* Qwen Code
* Mistral Vibe
* Ollama
* LM Studio

Support depends on the native capabilities of each platform.

## Structure

```text
ai-specialized-departments/
├── codex/
│   ├── software-development/
│   │   ├── agents/
│   │   ├── subagents/
│   │   ├── skills/
│   │   ├── hooks/
│   │   ├── mcp/
│   │   └── workflows/
│   ├── cybersecurity/
│   ├── marketing/
│   └── medicine/
├── claude-code/
├── gemini-cli/
├── github-copilot/
├── qwen-code/
├── mistral-vibe/
├── ollama/
└── lm-studio/
```

## Design Principles

* Platform-native configurations
* Independent professional departments
* No mandatory shared layer
* No project-specific business rules
* No real secrets or credentials
* No external services enabled by default
* Security-focused permissions
* Clear separation between specialties
* Components added only when supported by the platform

## Department Components

A department may contain:

* **Agents:** primary professional roles
* **Subagents:** specialized supporting roles
* **Skills:** reusable capabilities for the department
* **Hooks:** optional lifecycle or validation events
* **MCP:** safe integration configurations
* **Workflows:** structured collaboration and execution processes

Not every platform or department must implement every component.

## Current Scope

This repository contains specialized configurations for individual AI platforms.

It is not currently intended to provide:

* A universal AI framework
* A shared runtime
* A cross-platform execution engine
* Automatic conversion between platforms
* Universal compatibility guarantees

These capabilities may be developed separately in the future.

## Security

* Never commit real API keys, tokens, passwords, or credentials.
* External integrations must remain disabled until explicitly configured.
* Permissions should follow the principle of least privilege.
* High-impact actions should require explicit user approval.
* Medical, legal, financial, and security-related departments must include appropriate validation and human-review rules.

## Contributing

Contributions should:

1. Target a specific platform and department.
2. Use the native format supported by that platform.
3. Avoid unnecessary duplication.
4. Document required capabilities and limitations.
5. Include no private data or real credentials.
6. Clearly identify unsupported or degraded functionality.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
