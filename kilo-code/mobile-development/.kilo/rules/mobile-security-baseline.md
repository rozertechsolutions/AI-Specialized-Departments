# Mobile Security Baseline

- Never read, copy, log, commit, transmit, or embed secrets, private keys, signing certificates, provisioning profiles, keystores, service-account files, local environment files, or production credentials.
- Public client configuration, such as bundle identifiers, package names, URL schemes, app IDs, and documented Firebase client fields, is not automatically a secret; still require human control before changing security-sensitive behavior.
- Require human approval before changing authentication, authorization, privacy declarations, manifests, entitlements, network security, deep links, WebViews, analytics, telemetry, dependencies, lockfiles, build/signing configuration, external writes, publishing, deployment, credential import, destructive commands, or financial actions.
- Review roles are read-only. Implementation roles must ask for independent review when security, privacy, release, architecture, performance, or accessibility risk is material.
- Local plugins may block unsafe tool calls, but they must not mutate source files automatically.

