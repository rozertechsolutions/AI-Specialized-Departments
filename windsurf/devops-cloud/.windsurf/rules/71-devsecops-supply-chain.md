---
trigger: model_decision
description: Apply for dependency, artifact, SBOM, provenance, signing-design, build integrity, and software supply-chain controls.
---

# DevSecOps Supply Chain Rule

Use for Section 08 supply-chain work. Primary owner:

- Software Supply Chain Security Engineer: dependency and artifact integrity, SAST, DAST, SCA integration design, secret scanning design, IaC/container/Kubernetes scanning design, SBOM, provenance, signing design, verification, build isolation, and SLSA-aligned controls.

Findings must include severity, evidence, owner, remediation, exception path, and independent review handoff. Signing and provenance may be designed statically but must not be executed by this package.

Do not run scanners, sign artifacts, publish packages, upload SBOMs, mutate build systems, access secrets, or use external services.

Use `@devsecops` for detailed procedures.
