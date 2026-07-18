# Software Development Quality Gates

This is the authoritative quality and completion policy for the Claude Software Development manual package.

## Required Gates

1. Scope and requirements are explicit.
2. Acceptance criteria are verifiable.
3. Architecture and public-contract impact is assessed when relevant.
4. Implementation is limited to approved changes and existing repository conventions.
5. Validation covers affected behavior, regression risk, edge cases, and known failure paths where practical.
6. Independent code-quality review follows implementation.
7. Engineering-risk review occurs when security, dependencies, performance, concurrency, reliability, data integrity, architecture, or public contracts are affected.
8. Documentation, migration, compatibility, and versioning implications are addressed.
9. Remaining risks, limitations, and checks not run are explicit.
10. Release readiness is assessed for a human decision, with an explicit stop before publication, deployment, signing, submission, or release.

## Review Independence

The same responsibility must not both implement a substantive change and approve it as independently reviewed. When Claude account surfaces do not support separate agents, preserve independence in the conversation by separating implementation, code-quality review, engineering-risk review, and release-readiness phases and clearly labeling the evidence for each phase.
