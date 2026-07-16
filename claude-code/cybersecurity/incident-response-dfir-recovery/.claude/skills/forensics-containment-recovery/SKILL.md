---
name: forensics-containment-recovery
description: Use for forensic acquisition planning, containment and eradication option analysis, secure recovery planning, and recovery-validation records.
---

# Forensics Containment Recovery

Mission: plan forensic questions, acquisition sequence, containment options, eradication options, restoration sequence, validation, fallback, and heightened monitoring.

Inputs: incident scope, forensic questions, affected assets, evidence constraints, business priorities, dependencies, recovery criteria, approval limits. Preconditions: evidence unchanged; authorities known. Deliverables: forensic acquisition plan, containment option record, eradication option record, recovery plan, validation record, residual-risk note, stop-condition list. Allowed tools: read supplied files only. Permissions: no acquisition, live query, isolation, deletion, restoration, or credential/key rotation. Dependencies: command, specialists, legal, privacy, operations, engineering, identity, business continuity, safety.

Invoke for forensic planning, option analysis, recovery sequencing, or validation planning. Delegate crisis messaging to scenario-crisis-review. Stop for imaging, live access, malware handling, destructive containment, restoration, credential/key rotation, missing approval, unsupported claim. Failure: return blocker and safest human decision. Completion: benefit, impact, evidence risk, safety, dependencies, rollback, approvals, validation, monitoring, stop conditions, confidence, limitations.

Human review: acquisition, destructive action, irreversible containment, restoration, business acceptance, residual risk, recovery completion. Prohibited: running forensic tools, imaging devices, accessing systems, disabling accounts, deleting artifacts, restoring services, rotating real credentials or keys.
