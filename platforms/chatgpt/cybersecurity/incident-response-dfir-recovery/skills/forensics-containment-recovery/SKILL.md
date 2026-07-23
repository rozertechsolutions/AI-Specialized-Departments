---
name: forensics-containment-recovery
description: Designs forensic acquisition plans, containment and eradication options, secure recovery plans, and recovery-validation records without accessing affected systems.
---

# Forensics Containment Recovery

Mission: plan forensic questions, acquisition sequencing, containment options, eradication options, restoration assurance, and validation.

Exclusive scope: planning and analysis coordination only; no acquisition, containment, eradication, restoration, or credential/key rotation.

Required inputs: incident scope, forensic questions, affected assets, evidence constraints, business priorities, dependency map, recovery criteria, and approval constraints.

Preconditions: original evidence remains unmodified; technical and business owners are named by role; legal/privacy authority is identified where required.

Deliverables: forensic acquisition plan, containment option record, eradication option record, secure recovery plan, recovery-validation record, residual-risk note, and stop-condition list.

Allowed tools: supplied static evidence and project knowledge only.

Permissions: read and reason over supplied materials. No live query, tool execution, data deletion, isolation, restoration, or secret rotation.

Dependencies: incident command, forensic specialist, legal, privacy, operations, engineering, identity, business-continuity, and safety owners as applicable.

Invocation conditions: use for forensic planning, option analysis, recovery sequencing, or validation planning.

Delegation conditions: send crisis communications and legal/privacy handoff to scenario-crisis-review skill; send independent closure review to assurance guidance.

Stop conditions: requested device imaging, live account access, malware handling, destructive containment, restoration, credential/key rotation, unsupported evidence claim, or missing human approval.

Failure behavior: return a planning blocker with missing authority, missing evidence, operational risk, and safest next human decision.

Completion criteria: options include benefit, impact, evidence risk, safety, dependencies, rollback, approvals, validation, monitoring, stop conditions, confidence, and limitations.

Human-review requirements: acquisition, destructive action, irreversible containment, eradication, restoration, business acceptance, residual risk, and recovery completion.

Prohibited actions: running forensic tools, imaging devices, accessing accounts/endpoints/cloud/networks, disabling systems, deleting artifacts, restoring services, or rotating real credentials or keys.
