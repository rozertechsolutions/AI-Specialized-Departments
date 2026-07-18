---
name: stack-discovery
description: Identify the actual web stack, tools, architecture, conventions, constraints, and unknowns before planning or changing a project.
---

# Stack Discovery

## Mission
Detect and document the actual web stack before proposing changes.

## Use when
- The stack, framework, package manager, build system, test tools, routes, deployment model, or conventions are unknown.
- A recommendation depends on current architecture or tooling.

## Do not use when
- The stack and relevant constraints are already verified from current evidence.

## Inputs
File tree, package/config files, source snippets, lockfiles, framework config, deployment descriptors, README excerpts, test output, or user-provided project facts.

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

## Stop and failure behavior
Return BLOCKED when the user has not provided enough project evidence to identify the stack safely.

## Review requirements
Report stack inventory, architecture map, constraints, conventions, risks, unknowns, and recommended next Skill or Plan/Act transition.

## Prohibited actions
- No installation, command execution, Git mutation, deployment, publication, authentication, secret handling, spending, signing, or destructive operation without exact human authorization.
- No unsupported technology assumptions or fabricated completion evidence.
