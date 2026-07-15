# GitHub Copilot Cybersecurity Security Architecture Engineering

This package configures GitHub Copilot native static guidance for Cybersecurity Area 02: Security Architecture Engineering.

## Native Artifacts

- `.github/copilot-instructions.md` defines repository-level Copilot guidance for this area.
- `.github/agents/*.agent.md` defines custom agents for architecture governance, solution architecture, identity/cloud/network, data/container/automation, and independent review.
- `.github/skills/*/SKILL.md` defines reusable skills for architecture review, reference patterns, identity/cloud/network/data design, container/IaC/automation review, and independent architecture assurance.
- `reference/NATIVE_SOURCES.md` records official GitHub documentation checked for native feature support.

## Scope Boundaries

The package supports design, review, documentation, governance, and independent assurance of security architectures. It does not approve architectures, accept risk, publish standards, deploy controls, operate production systems, authenticate to services, run scans, or manage incidents.

Use the required output header in `.github/copilot-instructions.md` for every deliverable and route high-impact artifacts to the independent reviewer.
