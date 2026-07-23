# Installation and Acceptance — github-copilot / marketing-engineering

This is a manual, review-first installation. The package contains no installer and performs no action by itself.

## Installation
1. Copy `.github/copilot-instructions.md`, `.github/instructions/`, `.github/agents/`, and `.github/skills/` to the target repository after review.
2. Confirm the chosen Copilot surface supports the included customization files.
3. Review tool aliases and organization/repository policy before agent use.

## Acceptance test
1. Use a fictional, non-sensitive brief.
2. Confirm the native instructions are discovered.
3. Invoke one relevant role or procedure and verify exclusive ownership.
4. Remove one mandatory input and verify the workflow returns a blocker instead of inventing it.
5. Request a forbidden external action and verify it is refused or held for explicit human approval.
6. Verify the output includes evidence or technical basis, assumptions, risks, reviewers, lifecycle state, and next human decision.
7. Verify independent review is not performed by the creator.

## Update procedure
Re-check `reference/NATIVE_SOURCES.md`, compare product release notes, review changed schemas and permissions, repeat the acceptance test, and retain the last validated version until the update passes.
