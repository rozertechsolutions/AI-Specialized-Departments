---
trigger: always_on
---

# Safety and Human Review

Use least privilege and the minimum context needed. Never expose secrets, credentials, tokens, private keys, personal data, private endpoints, or environment values. Never silently expand scope or invent evidence.

Stop for explicit human approval before editing sensitive scope, changing architecture or dependencies, running commands, accessing external systems, deploying, publishing, signing, releasing, performing destructive operations, mutating Git, changing permissions, changing trust boundaries, migrating data/configuration, spending money, changing accounts, or sending external communications.

Hooks, MCP, shell helpers, auto-run configuration, background jobs, external integrations, fake custom agents, and automatic approval mechanisms are intentionally absent.
