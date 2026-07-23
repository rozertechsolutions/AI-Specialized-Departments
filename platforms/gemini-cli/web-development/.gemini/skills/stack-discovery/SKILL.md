---
name: stack-discovery
description: Detect and document the actual web stack before proposing changes.
---

# Stack Discovery

## Mission
Detect and document the actual web stack before proposing changes.

## Trigger boundary
Use at the start of unclear or non-trivial work when the stack, tooling, ownership, or constraints are not already verified from repository evidence. Do not use to make changes.

## Procedure
1. Inspect only files within the approved project scope.
2. Identify languages, frameworks, package managers, runtime versions, build systems, test tools, deployment descriptors, browser targets, and existing conventions from evidence.
3. Distinguish confirmed facts from assumptions and unresolved questions.
4. Do not install, upgrade, execute, or reconfigure anything during discovery.
5. Output a concise stack inventory, architectural map, constraints, and uncertainty list.

## Output
State scope, evidence, facts, assumptions, risks, unresolved questions, and PASS, FAIL, BLOCKED, or NOT APPLICABLE gates.
