---
name: review-mobile-architecture
description: Review mobile architecture, ownership boundaries, modules, navigation, state, migrations, and validation risks without editing source by default.
compatibility: opencode
metadata:
  owner: mobile-architect
---

# review-mobile-architecture

- Objective: assess architecture and produce actionable findings or an implementation plan.
- Trigger: user asks for architecture review, migration review, module design, or boundary decisions.
- Inputs: project layout, requirements, manifests, dependency graph, docs, current diff.
- Supported technologies: Android, iOS, KMP, Flutter, React Native.
- Preconditions: target scope and review depth are known.
- Primary owner: `mobile-architect`.
- Reviewers: `mobile-security-reviewer`, `mobile-performance-reviewer`, `mobile-code-reviewer` when relevant.
- Steps: inspect structure; classify platforms; map modules and dependencies; identify owners; check cycles/conflicts; assess migration risks; produce findings or plan.
- Conditional steps: request implementation approval before edits.
- Validation gates: every finding references evidence; public contracts and persistent formats are identified.
- Failures: report missing docs, unavailable build graph, ambiguous ownership.
- Stop conditions: request requires implementation without approval, secrets, production access.
- Evidence: files, dependency paths, command output, unsupported assumptions.
- Outputs: architecture findings, owner matrix, validation plan, risks.
- Acceptance criteria: no overlapping authority, no self-review, actionable next steps.
- Human approvals: API changes, data migration, auth/privacy/security architecture, dependencies.
- Prohibited actions: source edits by default, release approval, signing, publishing, destructive commands.
