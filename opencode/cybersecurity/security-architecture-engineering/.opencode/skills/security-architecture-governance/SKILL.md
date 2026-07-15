---
name: security-architecture-governance
description: Use for security architecture governance, reference models, standards mappings, decision records, and review gates.
compatibility: opencode
metadata:
  owner: architecture-governance-agent
---

# security-architecture-governance

- Objective: produce source-backed security architecture governance and decision material for Cybersecurity Area 02.
- Trigger: user asks for architecture governance, reference model, standards mapping, design review gate, ownership, or decision record work.
- Inputs: scope, standards, architecture principles, control catalog, owner list, decision history, constraints.
- Primary owner: `architecture-governance-agent`.
- Reviewers: `independent-architecture-reviewer`.
- Steps: confirm scope; inventory source artifacts; map standards to decisions; identify owners and review gates; record gaps and assumptions; prepare decision-ready output.
- Validation gates: every architecture claim has a source; every owner assignment is supported; every approval dependency is explicit.
- Stop conditions: policy approval, risk acceptance, unsupported claim, missing authority, or external submission.
- Outputs: governance model, reference index, standards map, decision record, approval questions.
- Acceptance criteria: scope, source basis, ownership, gaps, residual risk, and approval dependencies are explicit.
- Human approvals: governance approval, architecture acceptance, external distribution.
- Prohibited actions: approving policy, accepting risk, certifying architecture, or changing live records.

