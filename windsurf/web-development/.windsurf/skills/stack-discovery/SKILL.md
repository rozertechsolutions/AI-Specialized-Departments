---
name: stack-discovery
description: Detect and document the actual web stack before proposing changes.
---

# Stack Discovery

## Mission
Detect and document the actual web stack before proposing changes.

## Invocation and surface
- Cascade: Invoke with `@stack-discovery` or allow Cascade to select it before planning or implementation in an unfamiliar repository.
- Devin Local: Compatible as a project skill; invoke with `/stack-discovery` when using Devin Local.
- Not a setup script, installer, scanner service, MCP server, or custom agent.

## Inputs and preconditions
Approved project scope, available file evidence, known constraints, user-stated goals, and any prohibited paths or operations.

## Expected output and evidence
Stack inventory, architecture map, conventions, constraints, assumptions, unresolved questions, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED when approved scope is unclear, evidence is insufficient to identify the stack safely, or sensitive files would be required without authorization.

## Required procedure
1. Inspect only files within the approved project scope.
2. Identify languages, frameworks, package managers, runtime versions, build systems, test tools, deployment descriptors, browser targets, and existing conventions from evidence.
3. Distinguish confirmed facts from assumptions and unresolved questions.
4. Do not install, upgrade, execute, or reconfigure anything during discovery.
5. Output a concise stack inventory, architectural map, constraints, and uncertainty list.

## Output contract
- State confirmed scope and evidence.
- Separate facts, assumptions, risks, and unresolved decisions.
- List files or components affected or reviewed.
- State which quality gates are PASS, FAIL, BLOCKED, or NOT APPLICABLE.
- Do not claim execution or success without direct evidence.

## Prohibited actions
- Do not run commands, install packages, mutate Git state, deploy, publish, authenticate, handle secrets, spend money, sign artifacts, or perform destructive operations without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
