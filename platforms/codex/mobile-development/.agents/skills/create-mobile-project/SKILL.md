---
name: create-mobile-project
description: Create a new Android, iOS, Kotlin Multiplatform, Flutter, or React Native project or module with an approved identity, target matrix, architecture, and local verification. Do not use for adding a feature to an existing project.
---

# Create Mobile Project

## Objective

Create the smallest valid mobile project or module for one explicitly selected technology without overwriting existing work, inventing identifiers, installing unapproved software, signing, publishing, or connecting to production services.

## Required inputs

Obtain or derive from authoritative repository context:

- Destination path and whether this is an application, library, shared module, or host integration.
- Platform: Android, iOS, KMP, Flutter, or React Native.
- Product/module name and package, namespace, or bundle identifier.
- Supported OS targets, device classes, and required build variants or flavors.
- Language/UI choices that are not already fixed by repository convention.
- Initial functional scope and acceptance criteria.
- Approved architecture constraints and whether generated baseline dependencies are acceptable.

Ask the user for any material value that cannot be derived. Never invent organization identifiers, signing teams, store metadata, API endpoints, or credentials.

## Preconditions

1. Read applicable instructions and project documentation.
2. Inspect the destination, repository status, installed toolchain, and sibling-project conventions.
3. Confirm the destination is absent or contains no conflicting files. Do not delete or overwrite an existing project.
4. Confirm the selected generator is already installed and trusted. Get approval before network access, package installation, SDK changes, dependency resolution that changes lockfiles, or executing a downloaded generator.
5. Record which completion checks are required, conditional, or not applicable.

## Agent ownership

The coordinator owns inputs, sequencing, and final verification. Delegate architecture to `mobile-architect`, then delegate all writes to exactly one primary implementation agent: `android-engineer`, `ios-engineer`, `kmp-engineer`, `flutter-engineer`, or `react-native-engineer`. Use native platform agents only for explicitly separated host code. After implementation, use `mobile-test-engineer` for test assets and `mobile-code-reviewer` for final review. Invoke security, UI/accessibility, and performance reviewers only when the initial scope makes their domain material.

Do not run write-capable agents concurrently on overlapping files. Custom agents must not delegate further.

## Execution

1. **Define the project contract.** Write down the exact inputs, non-goals, supported target matrix, project identity, and acceptance criteria.
2. **Design.** Have `mobile-architect` inspect local conventions and return the minimal module/layer layout, dependency direction, navigation/state boundaries, and ownership map.
3. **Gate: design.** Continue only when the design uses observed conventions, has no unresolved identity or target decisions, and introduces no unapproved dependency/tool change.
4. **Preview generation.** Determine the exact generator command and expected files without running it. Identify network, overwrite, telemetry, dependency-install, signing, and post-generation behavior.
5. **Gate: command safety.** Obtain any required approval. Reject commands that can sign, publish, deploy, erase data, or write outside the destination.
6. **Generate or scaffold.** The selected implementation agent creates only the approved project. Prefer non-interactive flags with explicit values. Do not initialize Git, create branches, stage, commit, or fetch dependencies unless separately authorized.
7. **Normalize minimally.** Apply only required repository conventions. Do not reformat unrelated sibling files or add speculative infrastructure.
8. **Add tests.** `mobile-test-engineer` adds the smallest deterministic smoke/unit coverage supported by the generated project, without new test dependencies unless approved.
9. **Validate.** Run configuration checks, formatting/lint/static analysis, unit tests, and an unsigned or simulator-safe compile when locally available. Validate every declared target that can be checked without signing or external services.
10. **Review.** `mobile-code-reviewer` inspects the scoped diff. Run conditional security, UI/accessibility, or performance review when applicable. Return findings to the implementation owner, fix only in-scope defects, and rerun affected checks.
11. **Final gate.** Review the complete diff and confirm that all files are necessary, the destination is correct, identifiers are exact, no secret/signing material exists, and no required check fails.

## Error handling and stop conditions

Stop and report the blocker when the destination conflicts, an identifier/target is unknown, the toolchain is unavailable, generation requires an unapproved install/network action, the template introduces unapproved dependencies, a generated file escapes scope, signing is invoked, or a required check cannot run. Preserve partial files for review; do not delete them without approval. Never substitute placeholder production logic.

## Outputs

- Created file list and selected architecture.
- Generator/tool version and exact command, if one ran.
- Approved dependency or tool changes, if any.
- Validation matrix with required/conditional/not-applicable status and results.
- Review findings fixed or unresolved.
- Explicit human-only next steps, excluding signing and publication execution.

## Acceptance criteria

- Project identity, target matrix, and structure match approved inputs.
- The project opens/configures and compiles through a safe unsigned path when the toolchain is available.
- Required lint/static checks and tests pass.
- No existing file was overwritten, no unrelated file changed, no secret was added, and no MCP/server connection occurred.
- Any unrun conditional check has a concrete reason; no failing required check is hidden.

## Prohibited actions

Do not sign, archive for distribution, publish, deploy, create store records, initialize authenticated services, erase devices, install tools/dependencies without approval, fabricate identifiers, initialize or mutate Git state, or delete conflicting files.
