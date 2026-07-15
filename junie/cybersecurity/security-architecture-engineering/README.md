# Junie Cybersecurity Security Architecture Engineering

This package configures Junie-native static guidance for Cybersecurity Area 02: Security Architecture Engineering.

## Native Artifacts

- `.junie/AGENTS.md` defines area scope, mission, routing, safety boundaries, and structured output requirements.
- `.junie/config.json` describes the static area package.
- `.junie/agents/*.md` defines custom subagents for architecture governance, solution architecture, identity/cloud/network, data/container/automation, and independent review.
- `.junie/skills/*/SKILL.md` defines reusable skills for architecture review, reference patterns, identity/cloud/network/data design, container/IaC/automation review, and independent architecture assurance.
- `.junie/commands/*.md` provides thin command entry points that route to the matching skill.
- `reference/NATIVE_SOURCES.md` records official Junie documentation checked for native feature support.

## Scope Boundaries

The package supports design, review, documentation, governance, and independent assurance of security architectures. It does not approve architectures, accept risk, publish standards, deploy controls, operate production systems, authenticate to services, run scans, or manage incidents.
