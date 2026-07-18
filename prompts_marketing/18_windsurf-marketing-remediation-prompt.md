# AI Specialized Departments — Windsurf Marketing Remediation Prompt

## Mission

Correct only the Marketing specialization for `windsurf/` in the existing
`AI-Specialized-Departments` repository.

Required branches:

```text
windsurf/marketing/
├── marketing-professional/
└── marketing-engineering/
```

This is a corrective task. Preserve useful existing content and make the minimum
changes required to obtain an accurate, native, safe, internally consistent
implementation.

## Absolute scope and execution restrictions

You may read and edit only:

```text
windsurf/marketing/**
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

1. Inventory every file under `windsurf/marketing/`.
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

- https://docs.windsurf.com/windsurf/cascade/agents-md
- https://docs.windsurf.com/windsurf/cascade/skills
- https://docs.windsurf.com/windsurf/cascade/workflows
- https://docs.windsurf.com/windsurf/cascade/memories

## Verified defects to correct

Top-level workflows are exact duplicates of native `.windsurf/workflows/`, generated audit metadata remains, and approval states are unsafe.

## Deletion allowlist

- `windsurf/marketing/AUDIT.md`
- `windsurf/marketing/marketing-professional/workflows/`
- `windsurf/marketing/marketing-engineering/workflows/`

No other file or directory may be deleted.

## Additions and migrations

- No replacement workflow files are needed: the exact native copies already exist under
  each branch's `.windsurf/workflows/`.

## Required modifications

- Keep `AGENTS.md`, `.windsurf/skills/`, and `.windsurf/workflows/`.
- Verify that the 26 top-level workflow files are exact duplicates of the native
  `.windsurf/workflows/` files before deleting the two authorized directories.
- Update all references so only `.windsurf/workflows/` is named as the manually invoked
  workflow location.
- Explain the distinction:
  - AGENTS.md: directory-scoped persistent guidance;
  - Skills: model-discovered or explicitly invoked reusable procedures;
  - Workflows: manually invoked slash-command prompt templates.
- Do not add active Cascade hooks because the safe default package must not execute
  shell commands.
- Update AGENTS, Skills, native workflows, catalogs, README, installation, governance,
  handoff, templates, source notes, and approval states.

## Platform-specific acceptance criteria

- Both `windsurf/marketing/marketing-professional/` and
  `windsurf/marketing/marketing-engineering/` remain present and independently usable.
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
