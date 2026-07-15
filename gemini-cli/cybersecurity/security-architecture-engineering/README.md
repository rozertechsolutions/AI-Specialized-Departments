# Gemini CLI Cybersecurity Security Architecture Engineering

This package configures Gemini CLI native static guidance for Cybersecurity Area 02: Security Architecture Engineering.

## Native Artifacts

- `GEMINI.md` defines area scope, mission, routing, safety boundaries, and structured output requirements.
- `.gemini/agents/*.md` defines project-level local subagents for architecture governance, solution architecture, identity/cloud/network, data/container/automation, and independent review.
- `.gemini/skills/*/SKILL.md` defines reusable workspace Agent Skills for architecture review, reference patterns, identity/cloud/network/data design, container/IaC/automation review, and independent architecture assurance.
- `reference/NATIVE_SOURCES.md` records official Gemini CLI documentation checked for native feature support.

## Scope Boundaries

The package supports design, review, documentation, governance, and independent assurance of security architectures. It does not approve architectures, accept risk, publish standards, deploy controls, operate production systems, authenticate to services, run scans, or manage incidents.

Use the structured output header in `GEMINI.md` for every deliverable and route high-impact artifacts to the independent reviewer.
