# Custom GPT Manual Setup

Use this guide in the GPT builder. A Custom GPT is a configured ChatGPT experience with its own instructions, knowledge, capabilities, Apps, or Actions. It is not a repository agent and does not auto-load files from this directory.

## Availability

- Creating or editing GPTs requires a paid ChatGPT plan and, in managed workspaces, the required workspace permission.
- GPT building and editing are web-only. Mobile clients can use GPTs but may not support building or editing.
- GPTs do not use the user's saved memory, global custom instructions, or previous conversations as implicit context.

## Configuration

| GPT field | Value |
| --- | --- |
| Name | Web Development Department |
| Description | A stack-agnostic web-development assistant for architecture, frontend, backend, APIs, security, privacy, accessibility, performance, SEO, testing, compatibility, and release-readiness review. |
| Instructions | Paste `project-instructions.md` when the GPT is the primary surface, then add only approved organization-specific rules that are safe to include. |
| Conversation starters | "Review this frontend change for accessibility and responsive behavior."; "Plan a safe backend API change for this requirement."; "Assess this web feature for security, privacy, and release readiness."; "Create a test and browser-compatibility checklist for this implementation." |
| Knowledge | Upload the files in `knowledge/` and only safe project documentation. Do not upload secrets, production configuration, credentials, personal data, private endpoints, or privileged logs. |
| Capabilities | Enable only the capabilities needed for the GPT's intended use. |
| Apps or Actions | Leave disabled by default. If one is required, choose Apps or Actions deliberately; a GPT cannot use both at the same time. |

## Setup Steps

1. Open the GPT builder from the GPTs area in ChatGPT.
2. Configure the fields above.
3. Upload factual knowledge files. Keep behavioral rules in the Instructions field, not in Knowledge.
4. Leave Actions, Apps, connectors, sync, and write actions off unless a human has reviewed data access, scopes, retention, confirmation prompts, and workspace restrictions. A GPT can use Apps or Actions, but not both at the same time.
5. Preview with safe representative tasks before sharing or publishing.
6. Share only with the intended audience and review workspace policy before enabling public or workspace-wide access.

## Review Checklist

- The GPT states that it cannot auto-discover repository files.
- Knowledge files are reference material, not a second instruction source.
- Apps, Actions, external APIs, and write actions are disabled unless explicitly reviewed.
- The GPT refuses unapproved deployment, publication, dependency installation, Git mutation, secret handling, and destructive actions.
- Preview outputs distinguish verified evidence from assumptions and unexecuted checks.
