# DevOps and Cloud Routing Rule

Use this rule for every DevOps and Cloud request. Classify the request, assign one primary section owner, name supporting dependencies, and keep work static unless a human explicitly approves an out-of-package action.

Primary routing starts with Leadership and Architecture for intake, ownership, architecture decisions, ADRs, standards, exceptions, and handoffs. Use the matching `.kilo/skills/` Skill when detailed procedure is needed.

Preserve Assurance independence. The Assurance Reviewer may review and block completion, but must not implement the reviewed work, self-review, or approve its own output.

Do not run or authorize shell commands, platform tools, infrastructure mutation, deployment, scanners, failovers, restores, signing, publication, spending, external integrations, hooks, MCP, or runtime validation from this package.
