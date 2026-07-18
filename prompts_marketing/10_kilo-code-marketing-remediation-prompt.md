# AI Specialized Departments — Kilo Code Marketing Remediation Prompt

## Mission

Correct only the Marketing specialization for `kilo-code/` in the existing
`AI-Specialized-Departments` repository.

Required branches:

```text
kilo-code/marketing/
├── marketing-professional/
└── marketing-engineering/
```

This is a corrective task. Preserve useful existing content and make the minimum
changes required to obtain an accurate, native, safe, internally consistent
implementation.

## Absolute scope and execution restrictions

You may read and edit only:

```text
kilo-code/marketing/**
```

You must not:

- modify another platform or specialization;
- modify repository-root files;
- use Git;
- run shell or terminal commands;
- run scripts, tests, builds, linters, formatters, package managers, installers,
  applications, servers, models, hooks, generated code, or external integrations;
- authenticate to any service;
- access production systems, private URLs, accounts, credentials, or live APIs;
- create a universal runtime, common compatibility layer, cross-platform adapter,
  converter, or `common/` directory;
- create empty files, placeholder-only files, simulated native capabilities, or
  implementation prompts for later work;
- claim that a test, runtime, hook, integration, approval, or external action was
  executed when only static inspection was performed.

Web consultation is allowed only for current documentation. Official documentation
is authoritative. Reputable Reddit discussions may be consulted only when official
documentation is ambiguous and must never override it.

## Closed deletion policy

The only files or directories you are authorized to delete are listed in
**Deletion allowlist** below.

- Do not delete any other path.
- A move is allowed only when the source path is explicitly listed for deletion and
  its destination is explicitly required under **Additions and migrations**.
- If another deletion appears beneficial, report it in the final response but do not
  perform it.
- Never recreate a deleted `AUDIT.md`, setup duplicate, generic workflow duplicate,
  governance duplicate, migration note, or implementation prompt.

## Global corrections required in both Marketing branches

1. Search all Markdown, JSON, YAML, TOML, Python, schemas, catalogs, templates,
   instructions, agent files, Skills, workflows, and documentation for
   `human_approved`.
2. Remove `human_approved` from every model-generated state enum, output contract,
   example, completion criterion, and agent instruction.
3. Agent-generated states may be only:
   - `draft`
   - `blocked`
   - `review_required`
   - `ready_for_human_approval`
4. `ready_for_release_approval` may be used in Marketing Engineering only when it
   clearly means readiness for a later human decision.
5. A real approval must be represented only by an externally supplied human decision
   record containing:
   - decision;
   - approver identity or authorized role;
   - timestamp;
   - exact scope;
   - conditions;
   - artifact version or hash.
6. Update every `templates/HUMAN_DECISION_PACKAGE.md` so the agent prepares evidence
   but leaves the decision fields blank. State explicitly that an authorized human
   completes them after reviewing the exact artifact version.
7. Ensure the creator cannot approve or independently review its own work.
8. Engineering leads coordinate and delegate; they do not implement or approve.
9. Independent quality, compliance, security, and QA reviewers must be read-only
   whenever the platform provides enforceable per-agent permissions.
10. Implementers may receive only the minimum native editing capability required for
    bounded workspace changes. Do not enable unrestricted execution, automatic
    external actions, publishing, sending, spending, deployment, destructive changes,
    credential access, or production modification.
11. Update README, installation instructions, role/Skill/workflow catalogs,
    governance, handoff contracts, schemas, templates, and source notes so they match
    the final file inventory and do not contain stale paths.
12. Preserve both Marketing branches as independently usable packages. Do not create
    shared cross-branch content.

## Required working method

1. Inventory every file under `kilo-code/marketing/`.
2. Verify the current native capabilities, paths, formats, permissions, and discovery
   rules from the official sources listed below.
3. Apply only the additions, modifications, migrations, and deletions authorized by
   this prompt.
4. Perform three independent static reviews:
   - native paths, formats, discovery, references, and syntax;
   - responsibilities, permissions, review separation, and completion behavior;
   - security, minimality, duplicates, stale references, and documentation accuracy.
5. Compare the three reviews, correct every issue, and repeat all three until they
   pass.
6. Do not create a repository audit file. Return the audit summary only in the final
   response.

## Completion report

Return:

- files added;
- files modified;
- files moved;
- files deleted, matching the deletion allowlist exactly;
- permission corrections;
- workflow or knowledge migrations;
- approval-state corrections;
- remaining procedural limitations;
- confirmation that no unlisted deletion occurred;
- confirmation that all three static reviews passed.

Do not report success while any requirement remains unresolved.

## Official documentation to verify

- https://kilo.ai/docs/customize/custom-subagents
- https://kilo.ai/docs/customize/skills
- https://kilo.ai/docs/customize/custom-rules
- https://kilo.ai/docs/customize/custom-modes
- https://kilo.ai/docs/customize/agents-md

## Verified defects to correct

Engineering lead/reviewer may edit, governance is duplicated, procedure representations overlap, and approval states are unsafe.

## Deletion allowlist

- `kilo-code/marketing/AUDIT.md`
- `kilo-code/marketing/marketing-professional/reference/GOVERNANCE.md`
- `kilo-code/marketing/marketing-engineering/reference/GOVERNANCE.md`
- `kilo-code/marketing/marketing-professional/workflows/`
- `kilo-code/marketing/marketing-engineering/workflows/`

No other file or directory may be deleted.

## Additions and migrations

- Merge each unique workflow procedure into the existing native `.kilo/skills/` or the
  corresponding manually invoked `.kilo/commands/` file before deleting top-level
  workflows.
- Do not add another representation when a command or Skill already owns the procedure.

## Required modifications

- Keep `.kilo/rules/marketing-approval.md` as the sole governance/approval source in
  each branch and update all references.
- In Engineering agent configurations set `edit: deny` for:
  - `marketing-engineering-lead`;
  - `marketing-engineering-security-qa-reviewer`.
- Keep implementation specialists at `edit: ask` or a narrower documented path rule.
- Keep shell denied by default for all packaged agents.
- Preserve sensitive-file and external-directory denials.
- Distinguish commands (explicit user invocation) from Skills (discoverable reusable
  procedures) and remove content duplication by editing retained files, not by deleting
  any additional command or Skill.
- Update `kilo.jsonc`, agents, rules, commands, Skills, catalogs, README, installation,
  handoff, templates, sources, and approval states.

## Platform-specific acceptance criteria

- Both `kilo-code/marketing/marketing-professional/` and
  `kilo-code/marketing/marketing-engineering/` remain present and independently usable.
- Every deletion matches the allowlist exactly.
- Every retained reference resolves to an existing final path.
- No `human_approved` remains as an agent-generated state.
- Human decision templates require an external authorized human and an artifact
  version/hash.
- Leads and independent reviewers are non-editing wherever native permissions exist.
- Implementer capabilities truthfully match their role contracts.
- No active integration, hook, server, credential, production endpoint, deployment,
  publishing, sending, spending, or destructive operation is enabled.
- Native files follow current official syntax and placement by static inspection.
- No implementation prompt, temporary audit report, generation note, or placeholder is
  added.
