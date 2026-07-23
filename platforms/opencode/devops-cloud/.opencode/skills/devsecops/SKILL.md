---
name: devsecops
description: Use for secure delivery control design, pipeline security review, cloud IAM/secrets review, policy-as-code design, container/Kubernetes security review, SBOM/provenance, supply-chain assessment, and security exceptions.
---
# DevSecOps Skill

Use this skill for section 08 static DevSecOps design and review. Do not run scanners, sign artifacts, access secrets, enforce policy, or block pipelines.

## Procedure
1. Classify the request as devsecops-control-design, pipeline-security-review, cloud-iam-and-secrets-review, policy-as-code-design, container-and-kubernetes-security-review, sbom-and-provenance-design, software-supply-chain-assessment, security-exception-review.
2. Identify risk, control, earliest practical gate, evidence, owner, remediation, exception path, and Cybersecurity handoff needs.
3. Use SAST, DAST, SCA, secret scanning, IaC/container/Kubernetes scanners, OPA, Gatekeeper, Kyverno, SBOM standards, Sigstore/Cosign-style signing, SLSA provenance, build integrity, cloud IAM, and secrets managers only when justified by requirements.
4. Verify findings have severity/evidence/owner/remediation/exception paths and no secrets or real identifiers.
