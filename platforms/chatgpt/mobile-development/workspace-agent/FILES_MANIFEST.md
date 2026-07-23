# Workspace Agent Files Manifest

Attach these files to the Workspace Agent:

| File | Required | Reason |
| --- | --- | --- |
| `knowledge/MOBILE_DEVELOPMENT_SCOPE.md` | yes | Platform scope, detection evidence, native boundaries, and unsupported capabilities. |
| `knowledge/RESPONSIBILITY_MODEL.md` | yes | Role definitions, matrix, delegation, permissions, and no-self-review rules. |
| `knowledge/QUALITY_AND_COMPLETION_STANDARDS.md` | yes | Ten workflows, validation gates, evidence, and completion criteria. |
| `knowledge/SECURITY_AND_HUMAN_REVIEW.md` | yes | Security baseline, human approval requirements, and connector constraints. |
| `workspace-agent/CONNECTOR_CONSTRAINTS.md` | optional | Only attach if apps/connectors are later approved for manual setup. |
| `skills/<workflow>/SKILL.md` | optional | Attach or install only through the native Skills surface when Skills are enabled and the exact workflow is approved. |

Do not attach secrets, credentials, signing material, private endpoints, production data, service-account files, provisioning profiles, keystores, certificates, local environment files, or unreviewed third-party Skill packages.
