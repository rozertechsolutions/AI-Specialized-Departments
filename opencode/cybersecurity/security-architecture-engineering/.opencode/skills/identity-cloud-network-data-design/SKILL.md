---
name: identity-cloud-network-data-design
description: Use for identity, privileged access, cloud, platform, network, communications, data protection, or cryptography architecture.
compatibility: opencode
metadata:
  owner: identity-cloud-network-agent
---

# identity-cloud-network-data-design

- Objective: draft target-state architecture across identity, cloud, network, communications, data protection, cryptography, keys, and restricted material.
- Trigger: user asks for target-state design or review in these domains.
- Inputs: identity flows, privilege model, cloud topology, network paths, connectivity needs, data classes, cryptography requirements.
- Primary owner: `identity-cloud-network-agent`.
- Reviewers: `independent-architecture-reviewer`.
- Steps: confirm environment scope; map administration paths; map cloud and network boundaries; map data classes; document dependencies and decisions.
- Validation gates: administration paths, cloud boundaries, network paths, and data protection expectations are documented.
- Stop conditions: access change, live configuration, key operation, monitoring operation, or sensitive material exposure.
- Outputs: target-state design, control pattern map, segmentation review, data protection notes, dependency log.
- Human approvals: design acceptance, access changes, environment changes.
- Prohibited actions: granting access, changing configuration, operating controls, or rotating keys.

