---
name: supply-chain-ci-release-assurance
description: Use for dependency, SBOM, provenance, CI/CD, build, sensitive configuration, and release assurance review.
user-invocable: true
allowed-tools:
  - read_file
  - grep
  - ask_user_question
---

# Supply Chain CI Release Assurance

Inventory manifests, lockfiles, build definitions, pipeline files, artifact controls, release gates, and owners. Review dependency governance, SBOM expectations, provenance, branch controls, artifact integrity, environment separation, sensitive configuration handling, rollback criteria, blockers, residual risk, and human release decisions. Do not run tools.
