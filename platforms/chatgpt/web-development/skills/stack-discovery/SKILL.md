---
name: stack-discovery
description: Use to identify the actual web stack, conventions, constraints, and unknowns before planning or changing a project.
---

# Stack Discovery

## Mission
Detect and document the actual web stack before recommending or changing anything. This Skill uses only evidence the user provides or explicitly makes available.

## Use When

- The stack, framework, package manager, build system, routes, test tools, deployment model, or conventions are unknown.
- A task starts in a repository or codebase that has not been inspected.
- A recommendation depends on current architecture or tooling.

## Inputs

- File tree, package/config files, source snippets, lockfiles, framework config, deployment descriptors, README excerpts, test output, or user-provided project facts.

## Procedure

1. Inspect only files within the approved project scope.
2. Identify languages, frameworks, package managers, runtime versions, build systems, test tools, deployment descriptors, browser targets, and existing conventions from evidence.
3. Distinguish confirmed facts from assumptions and unresolved questions.
4. Do not install, upgrade, execute, or reconfigure anything during discovery.
5. Output a concise stack inventory, architectural map, constraints, and uncertainty list.

## Output Contract

- Stack inventory with evidence for each claim.
- Architecture and responsibility map at the level supported by available files.
- Constraints, conventions, risks, and unknowns.
- Recommended next specialist Skill or review path when appropriate.

## Stop Conditions

Stop and report BLOCKED when the user has not provided enough project evidence to identify the stack safely.

## Prohibited Actions

- Do not infer frameworks, package managers, test tools, deployment targets, or browser support without evidence.
- Do not install, execute, authenticate, mutate Git, deploy, publish, or perform destructive actions.
