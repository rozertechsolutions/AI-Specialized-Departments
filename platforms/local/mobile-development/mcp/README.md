# MCP Lifecycle

MCP is supported only as a disabled example in this specialization. The Model Context Protocol is an open standard for connecting AI applications to external systems such as data sources, tools, and workflows. This repository does not start, authenticate, trust, or connect any MCP server by default.

Before enabling an MCP server, a human must review:

- Server identity, source, transport, and command or URL.
- Exposed tools, resources, prompts, roots, sampling, and elicitation behavior.
- Data that can be read or written.
- Approval requirements for external writes and sensitive actions.
- Credential storage and revocation.
- Audit logging and failure behavior.

All example servers must keep `enabled: false`.
