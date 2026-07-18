---
name: stack-discovery
description: Detect and document the actual web stack before proposing changes.
---

# Stack Discovery

Use this skill at the start of unclear or non-trivial work when the stack, tooling, ownership, or constraints are not already verified from repository evidence. Do not use it to make changes.

1. Inspect only files within the approved project scope.
2. Identify languages, frameworks, package managers, runtime versions, build systems, test tools, deployment descriptors, browser targets, and conventions from evidence.
3. Distinguish confirmed facts from assumptions and unresolved questions.
4. Do not install, upgrade, execute, or reconfigure anything during discovery.
5. Output a concise stack inventory, architectural map, constraints, uncertainty list, and PASS, FAIL, BLOCKED, NOT APPLICABLE, or NOT EXECUTED gates.
