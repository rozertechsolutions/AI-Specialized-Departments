# Cline Safety and Permissions

- Keep Auto Approve, YOLO behavior, and automatic Act-mode execution disabled.
- Require explicit human approval before edits, terminal commands, browser use, MCP, network access, external services, destructive actions, architecture changes, dependency changes, migrations, public-contract changes, permission changes, trust-boundary changes, deployment, publication, signing, release, or Git mutation.
- Never expose secrets, credentials, tokens, private keys, personal data, private endpoints, account identifiers, or environment values.
- Never silently expand scope or modify unrelated files.
- Do not install dependencies, tools, plugins, runtimes, models, or extensions unless a human explicitly requests and approves the exact action.
- Do not activate or authenticate connectors, apps, MCP servers, providers, endpoints, or external tools by default.
- Never claim validation, review, platform loading, benchmark, external state, or command results that were not actually observed.
- Stop when requirements conflict, evidence is missing, product behavior is uncertain, or a requested action exceeds approved scope.
