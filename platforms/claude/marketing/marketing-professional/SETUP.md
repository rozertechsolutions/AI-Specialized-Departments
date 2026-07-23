# Setup for claude

1. Create a dedicated claude project or workspace for this branch.
2. Paste `PROJECT_INSTRUCTIONS.md` into the platform's project instructions.
3. Add the contents of `knowledge/`, `reference/`, and `templates/` as project knowledge only when needed.
4. Import individual `skills/<name>/` packages through the platform's native Skill mechanism when available to the account.
5. Configure connectors separately with least privilege. Begin read-only; never commit credentials.
6. Test one low-risk, fictional brief before using real organizational data.
7. Keep the professional and engineering branches as separate projects when their permissions or reviewers differ.

This package performs no installation, authentication, connector activation, publication, sending, spending, audience upload, or production change.
