# Customization

1. Select a provider/runtime without changing the neutral department specification.
2. Copy the example configuration and keep `enabled: false` until reviewed.
3. Choose a model and endpoint locally; never commit secrets.
4. Map only the capabilities the runtime can enforce.
5. Require human approval for repository writes and deny shell, network, MCP, and external writes by default.
6. Validate configuration with the user's chosen tooling outside this inert package.
