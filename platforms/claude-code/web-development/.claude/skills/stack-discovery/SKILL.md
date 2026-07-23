---
name: stack-discovery
description: Detect and document the actual web stack before proposing changes.
---

# Stack Discovery

## Mission
Detect and document the actual web stack before proposing changes.

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
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
