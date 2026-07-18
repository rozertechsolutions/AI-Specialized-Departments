---
name: stack-discovery
description: Detect and document the actual web stack before proposing changes.
---

# Stack Discovery

## Mission
Detect and document the actual web stack before proposing changes.

## Warp invocation
Invoke manually as `/stack-discovery` or let the local Warp agent load it before planning or implementation in an unfamiliar repository.

## Inputs
Approved project scope, available file evidence, known constraints, and user-stated goals.

## Expected output
Stack inventory, architecture map, conventions, constraints, assumptions, unresolved questions, and NOT EXECUTED checks.

## Stop conditions
Stop with BLOCKED when the approved scope is unclear or evidence is insufficient to identify the stack safely.

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
