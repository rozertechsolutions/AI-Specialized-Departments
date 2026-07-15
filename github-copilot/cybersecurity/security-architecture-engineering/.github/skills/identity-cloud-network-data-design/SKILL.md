---
name: identity-cloud-network-data-design
description: Use for IAM, PAM, cloud, platform, network, communications, endpoint, workspace, data protection, cryptography, key, and protected material architecture.
---

# Identity, Cloud, Network, and Data Design

Objective: create or review architecture designs for identity, cloud/platform, network, endpoint/workspace, data protection, and cryptographic control domains.

Primary owner: `identity-cloud-network-agent` for identity/cloud/network/endpoint outputs; `data-container-automation-agent` for data protection, cryptography, and protected material outputs.

Workflow:

1. Confirm authorized scope, owner, reviewer, approver, source versions, evidence limitations, and decision needed.
2. Map identities, privileges, administrative paths, trust zones, data classes, interfaces, and management planes.
3. Define target controls, inherited controls, boundary controls, monitoring handoff expectations, and failure modes.
4. Document design findings, required changes, recommended patterns, dependencies, residual risk, and human-only decisions.
5. Produce implementation handoff criteria without granting access, configuring controls, or handling real sensitive material.
6. Route high-impact designs to `independent-architecture-reviewer`.

Stop for privileged access approval, cryptographic authority decision, production control operation, tenant/network change, sensitive material exposure, or deployment.
