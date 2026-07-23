# Application Security Workflows

## Secure SDLC

Confirm product types, criticality, delivery model, lifecycle, and boundaries. Map security activities, evidence, owners, and approval gates. Tailor depth by risk and exposure without removing safeguards. Define entry, exit, exception, and escalation criteria. Route approval to humans after independent review.

## Threat Modeling

Confirm scope, context, assets, actors, data flows, trust boundaries, dependencies, and assumptions. Identify threats, abuse cases, failure modes, and attacker objectives. Prioritize mitigations and validation. Link mitigations to requirements, owners, and validation. State limitations and route independent review.

## Application Security Design Review

Confirm product context, architecture, interfaces, identities, data, tenancy, integrations, and operations. Review requirements and threat model. Analyze control placement, bypass paths, error handling, observability, resilience, and privacy dependencies. Produce findings, remediation, residual risk, and validation criteria. Route approval and exceptions to humans.

## Static Secure Code Review

Confirm authorized repository scope and objective. Read only the minimum relevant source and configuration. Trace security-sensitive data and control paths. Record evidence with file and location references. Separate confirmed issues from hypotheses requiring runtime validation. Propose remediation and static validation criteria. Do not execute code or tools.

## Dependency and Supply-Chain Review

Confirm manifests, lockfiles, SBOMs, build definitions, artifact sources, and provenance evidence. Identify unsupported, unpinned, untrusted, vulnerable, abandoned, or opaque components from supplied evidence. Assess build identity, artifact integrity, signing, and promotion controls. Record uncertainty where external verification was not performed. Produce prioritized remediation and independent review.

## CI/CD and Release Security

Confirm pipeline scope, identities, permissions, sensitive values, runners, artifacts, environments, approvals, and deployment path. Analyze privilege, isolation, trust, tamper resistance, provenance, rollback, and evidence controls. Identify unsafe defaults and bypass paths. Assess release evidence against explicit criteria. Do not run pipelines or approve release.

## Finding Triage

Preserve source, scanner, version, scope, and evidence. Normalize duplicates and classify confirmed, probable, not reproduced, false positive, or needs validation. Assess exploitability, impact, reachability, exposure, and confidence. Assign remediation and validation criteria. Require human review for critical findings and closure.

## Release Readiness

Confirm release scope, changes, threats, open findings, exceptions, test evidence, dependencies, and operational readiness. Validate required evidence and unresolved risk. Separate blocking, conditional, accepted, and informational items. Provide recommendation with confidence and limitations. Leave approval to authorized humans.

## Product Vulnerability Coordination

Confirm intake authorization, affected product, reporter information handling, evidence, and confidentiality. Create a validation plan without accessing unauthorized systems. Assess severity, affected versions, exposure, and customer impact from supplied evidence. Coordinate remediation, retest, disclosure, and communication dependencies. Require legal and human approval before disclosure.

## Remediation Validation

Confirm original finding, affected scope, approved fix, and closure criteria. Review supplied code, design, and test evidence statically. Check root cause, variants, bypass paths, and regression risk. Record confirmed, partial, insufficient, or not-verifiable status. Require independent human closure for high-impact findings.

