# DevSecOps Workflows

## secure-pipeline-design
1. Map stages, runners, permissions, secrets, artifacts, gates, and findings routing.
2. Place controls at the earliest practical stage without automatic enforcement.

## security-gate-review
1. Review risk, evidence, severity, owner, remediation, exception, and human approval.
2. Do not block pipelines or enforce production policy.

## iac-container-kubernetes-security-review
1. Review IaC, image, and workload security control design and ownership.
2. Do not execute scanners or validators.

## sbom-and-provenance-workflow
1. Define SBOM, provenance, signing, verification, build isolation, and artifact integrity requirements.
2. Do not sign or upload artifacts.

## secret-exposure-response-plan
1. Define containment, rotation owner, evidence handling, notification, and Cybersecurity handoff.
2. Do not read or expose secret values.

## security-finding-remediation
1. Capture finding, severity, evidence, owner, remediation, due date, exception path, and verification need.
2. Hand off independent assurance to Cybersecurity.

## devsecops-exception-approval
1. Record control, exception rationale, compensating controls, risk owner, expiry, and approval.
2. Require human approval.
