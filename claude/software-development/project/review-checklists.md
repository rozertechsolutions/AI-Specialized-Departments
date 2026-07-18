# Review Checklists

Use these checklists as Claude Project knowledge. They support the authoritative operating model and do not define separate repository agents.

## Code-Quality Review

- Requirements and scope are traceable.
- Correctness, readability, complexity, duplication, architecture fit, and compatibility are assessed.
- The reviewer did not implement the substantive change under review.
- Findings include severity, evidence, and required correction or acceptance rationale.

## Engineering-Risk Review

- Security, trust boundaries, input handling, dependencies, supply chain, performance, concurrency, failure handling, reliability, and data integrity are assessed when applicable.
- Findings distinguish verified facts from inferences.
- Sensitive details are reported without exposing secrets or exploit-enabling payloads unnecessarily.

## Release Readiness

- Validation evidence, independent reviews, documentation, migrations, versioning implications, remaining risks, and unexecuted checks are explicit.
- Artifact, compatibility, rollback, and human decision implications are clear.
- No publication, deployment, signing, submission, or release is performed.
