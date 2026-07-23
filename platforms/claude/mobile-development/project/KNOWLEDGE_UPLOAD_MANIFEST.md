# Knowledge Upload Manifest

Use this manifest to configure one Claude Mobile Development Project. It is an installation checklist, not Project knowledge itself.

## Required setup

1. Paste project/PROJECT_INSTRUCTIONS.md into the Project's Set project instructions field. Do not upload it only as knowledge; the non-negotiable rules must remain Project instructions.
2. Upload these four files to Project knowledge:
   - knowledge/MOBILE_DEVELOPMENT_SCOPE.md
   - knowledge/RESPONSIBILITY_MODEL.md
   - knowledge/QUALITY_AND_COMPLETION_STANDARDS.md
   - knowledge/SECURITY_AND_HUMAN_REVIEW.md
3. Confirm that all four filenames appear in Project knowledge and are readable in a new chat.
4. Ask Claude to summarize the responsibility matrix and identify the release prohibition. Compare the response with the source before relying on the Project.

## Do not upload as Project knowledge

- README.md and this manifest: retain them as installation documentation.
- connectors/CONNECTOR_SETUP_AND_SAFETY.md: consult it manually before connecting a service; upload it only if connector administration is the active task.
- The skills directory: custom Skills are separate native packages, not knowledge documents.
- The master repository or unrelated specializations: add only the application files needed for the current task.
- Secrets, credentials, local environment files, signing material, production exports, private keys, certificates, provisioning profiles, keystores, service-account files, or sensitive logs.

## Skill installation

Each direct child of skills is one independent custom Skill source. Review it, compress that named folder as the root of its own ZIP, and upload it through Customize > Skills > Create skill > Upload a skill. The root folder name and the name field in SKILL.md must match.

Install only required workflows. Keep prepare-mobile-release disabled until a user deliberately needs release-readiness work; even when enabled, it cannot sign, upload, submit, deploy, distribute, publish, or spend money.

Custom Skills require code execution to be enabled and may be governed by organization settings. If the live account does not show Skills, record the capability as unavailable. Do not substitute an ad hoc prompt and call it the native Skill.

## Application context

For each mobile task, provide current, scoped application evidence by one of these methods:

- upload the relevant source and configuration files;
- add selected GitHub files or folders to the Project and sync before work;
- use another explicitly approved read-only connector;
- paste a small non-sensitive excerpt with its repository path and revision.

Record branch or revision, sync time, platform targets, build-tool versions, and omitted areas. Project knowledge does not automatically inherit context from other chats. A connected source does not imply edit, build, test, device, signing, or publication access.

## RAG verification

If the Project displays a RAG indicator, verify that named-file retrieval works by asking a question whose answer appears in only one knowledge file. If no indicator is shown, continue without assuming RAG. Workflow correctness must not depend on automatic retrieval; explicitly name the needed knowledge file.

## Acceptance check

Setup is ready only when:

- Project instructions are saved;
- all four required knowledge files are present and current;
- Claude can retrieve the exact role boundaries and safety prohibitions;
- the needed Skills are visible and enabled;
- the actual account surface, plan or workspace, code-execution state, and connector state are recorded;
- no secret or unrelated repository content was uploaded;
- no connector was activated implicitly.
