# Web Security and Human-Review Policy

## Mandatory human approval
Require explicit human approval before any action involving production, external systems, authentication or authorization behavior, cryptography, secrets, personal or sensitive data, database migrations, dependency changes, third-party scripts, analytics or tracking, payment or billing, infrastructure, DNS, certificates, signing, publication, deployment, merge, release or destructive operations.

## Default-deny external capability
No MCP server, connector, remote tool, browser automation, shell execution, plugin, provider, model endpoint or external integration is enabled by this package. Users must review and configure integrations themselves outside this package.

## Review expectations
Use least privilege, secure defaults, defense in depth, server-side authorization, explicit validation, minimized data collection, bounded retention, safe logging, robust error handling and documented residual risk. A reviewer cannot approve their own implementation.
