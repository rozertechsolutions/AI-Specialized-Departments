# OpenCode - Software Development

This directory implements the Software Development specialization for OpenCode using repository-scoped native content. The primary OpenCode session is the Software Development Lead through `AGENTS.md`; there is intentionally no `.opencode/agents/software-development-lead.md` subagent.

## Native content

- `AGENTS.md` defines the primary Software Development Lead behavior.
- `opencode.jsonc` sets explicit project permissions: broad fallback ask, Bash denied, web fetch denied, edits ask.
- `.opencode/agents/` contains seven specialist subagents.
- `.opencode/skills/` contains fourteen preserved capability Skills.
- `.opencode/commands/` contains eleven prompt-only workflow commands.

## Permission rationale

OpenCode tools may otherwise be broadly available, so this package uses explicit least-privilege permissions. Planners, architects, testers, reviewers, risk reviewers, and documentation/release specialists deny edit, Bash, and web. The implementation specialist may request edits only after the primary Lead has approved scope; it still denies Bash, web, Git, MCP, deployment, publication, signing, release, and external actions.

The project configuration contains no MCP server, provider pin, model pin, endpoint, credential, plugin, hook, global path, script, wrapper, launcher, deployment automation, publication automation, signing automation, release automation, or executable asset.

## Operating model

Commands and user requests route through the primary Lead. The Lead may call specialists for bounded responsibilities, but specialists return evidence to the Lead, cannot recursively delegate, cannot expand scope, and cannot claim final completion. Implementation, code-quality review, engineering-risk review, and release-readiness assessment remain distinct.

Human approval is mandatory before destructive, sensitive, external, architectural, dependency, permission, trust-boundary, migration, or irreversible actions. Final completion must list validation evidence, checks not run, independent review outcomes, risk findings when triggered, documentation/readiness status, limitations, and human decisions.

## Intentionally omitted

- `.opencode/agents/software-development-lead.md`
- MCP configuration, plugins, hooks, scripts, wrappers, global paths, provider/model pins, endpoints, and credentials
- Bash, web, Git, deployment, publication, signing, release, submission, account, purchase, spending, or external communication authority
