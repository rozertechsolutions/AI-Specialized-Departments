# DevSecOps

Use this rule for static DevSecOps design and review inside DevOps workflows. Do not run scanners, sign artifacts, access secret stores, enforce policy, block pipelines, mutate cloud or security settings, or perform Cybersecurity-owned work.

## Owners

- DevSecOps Engineer: secure delivery controls, pipeline security requirements, security gate placement, findings routing, developer-facing remediation.
- Cloud Security Controls Engineer: technical cloud IAM, workload identity, secrets controls, policy as code, cloud hardening, least privilege.
- Software Supply Chain Security Engineer: dependency and artifact integrity, SBOM, provenance, signing strategy, verification, build isolation, SLSA-aligned controls.

## Capabilities

Use the `devsecops` Skill and workflow for devsecops-control-design, pipeline-security-review, cloud-iam-and-secrets-review, policy-as-code-design, container-and-kubernetes-security-review, sbom-and-provenance-design, software-supply-chain-assessment, and security-exception-review.

## Technology Knowledge

Cover SAST, DAST, SCA, secret scanning, IaC/container/Kubernetes scanning, OPA, Gatekeeper, Kyverno, SBOM standards, Sigstore/Cosign-style signing, SLSA provenance, build integrity, cloud IAM, and secrets managers only as static design references.

## Boundaries

DevSecOps integrates security into delivery and infrastructure but does not own pentesting, SOC/SIEM, threat intelligence, forensics, enterprise GRC, or general security incident response. Hand those to Cybersecurity.

## Quality Gates

- Controls are risk-based, traceable, and placed at the earliest practical stage.
- Findings include severity, evidence, owner, remediation, and exception path.
- No secret values or real identifiers are committed.
- Human review is required for blocking gates, policy enforcement, exceptions, signing trust, secret handling, least-privilege changes, and risk acceptance.
