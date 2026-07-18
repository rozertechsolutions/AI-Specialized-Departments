# Web Development - Cline

This directory is a static Cline Web Development specialization for workspace rules and Agent Skills. Copy the contents into a target repository root only after review.

## Native Components

| Component | Cline surface | Activation |
| --- | --- | --- |
| `.clinerules/*.md` | Workspace Rules | Always loaded when enabled in the Rules panel. |
| `.cline/skills/*/SKILL.md` | Workspace Skills | Experimental, on-demand; Cline loads matching Skills with `use_skill` when enabled. |
| User task prompts | Cline Plan/Act chat | Manual entry by the user. |

## Omitted Mechanisms

- Custom agents: not included because this package targets Cline rules and Skills, not simulated multi-agent orchestration.
- Hooks and plugins: omitted because they execute code or extend runtime behavior.
- MCP, connectors, cron, scripts, terminal automation, deployment workflows, provider setup, and model configuration: omitted because they require external setup, credentials, or execution.

## Manual Use

1. Place `.clinerules/` and `.cline/skills/` at the repository root.
2. Enable Skills in Settings > Features if the workspace should use Skills.
3. Review and toggle rules and Skills in the Cline UI before starting work.
4. Use Plan mode for discovery, architecture, reviews, and unclear changes; switch to Act mode only after approving the implementation approach.
5. Keep hooks, plugins, MCP, terminal execution, deployment, publication, and destructive actions disabled unless a human approves the exact use.

## Safety Baseline

- No credentials, tokens, endpoints, private URLs, executable hooks, installation scripts, deployment scripts, or active MCP connections are included.
- Repository edits may be proposed only within explicit task scope. Command execution, installation, Git mutation, publication, deployment, authentication, external side effects and destructive actions require exact human approval.
- Review the files before enabling or copying them into a real project.

## Static Verification Checklist

- PASS: Always-on rules are short and do not contain long task procedures.
- PASS: Skills are discoverable under `.cline/skills/<name>/SKILL.md` with matching `name` metadata.
- PASS: README does not promise custom agents or automated orchestration.
- PASS: Safety statements are model instructions and human gates, not claimed technical enforcement.
- NOT EXECUTED: Runtime checks, builds, tests, browser checks, hooks, plugins, MCP, terminal commands, Skill triggering, and Cline UI loading.

## Official Documentation Baseline

Accessed July 18, 2026:

- https://docs.cline.bot/customization/cline-rules
- https://docs.cline.bot/customization/skills
- https://docs.cline.bot/core-workflows/plan-and-act
- https://docs.cline.bot/features/auto-approve
- https://docs.cline.bot/customization/hooks
- https://docs.cline.bot/customization/plugins
