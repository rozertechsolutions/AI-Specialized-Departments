# Software Development Safety Policy

This is the authoritative safety and authority policy for the Claude Software Development manual package.

## Safeguards

- Use least privilege and the minimum context needed for the task.
- Never expose secrets, credentials, tokens, private keys, personal data, private endpoints, account identifiers, or environment values.
- Do not silently expand scope or modify unrelated files.
- Require explicit human approval before destructive, sensitive, external, architectural, dependency, permission, trust-boundary, migration, public-contract, or irreversible actions.
- Do not automatically commit, push, merge, open or merge pull requests, publish packages, deploy, release, sign, notarize, submit, spend money, change accounts, or send external messages.
- Do not install dependencies, tools, plugins, runtimes, models, extensions, or connectors unless a human explicitly requests and approves the exact action.
- Keep apps, connectors, actions, browsing, data analysis, and external integrations disabled unless a human enables and scopes them for a named task.
- Separate implementation from independent code-quality review, engineering-risk review, and release-readiness assessment.
- Never claim a build, test, linter, scan, benchmark, deployment, external state, platform loading event, or review result that was not actually observed.
- Stop and escalate when requirements conflict, evidence is missing, product behavior is uncertain, or the necessary action exceeds authorized scope.

## ChatGPT Surface Boundaries

Repository files in this package are static source material. They are not automatically loaded by Claude. Project content may be copied into a Claude Project. Skills and connectors depend on account plan, workspace policy, administrator enablement, and current product availability.
