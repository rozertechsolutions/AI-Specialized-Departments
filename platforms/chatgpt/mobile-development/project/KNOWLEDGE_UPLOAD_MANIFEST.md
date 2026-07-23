# Knowledge Upload Manifest

Upload these files as ChatGPT Project sources when configuring the Mobile Development project. Files are reference material only; behavior rules belong in Project instructions.

| File | Required | Purpose |
| --- | --- | --- |
| `knowledge/MOBILE_DEVELOPMENT_SCOPE.md` | yes | Defines supported mobile platforms, platform detection evidence, native ChatGPT boundaries, and unsupported capabilities. |
| `knowledge/RESPONSIBILITY_MODEL.md` | yes | Defines the twelve exact responsibilities, ownership matrix, delegation rules, and no-self-review constraints. |
| `knowledge/QUALITY_AND_COMPLETION_STANDARDS.md` | yes | Defines the ten workflows, validation gates, evidence standards, and completion criteria. |
| `knowledge/SECURITY_AND_HUMAN_REVIEW.md` | yes | Defines security baseline, human approval gates, connector constraints, and fail-safe behavior. |
| `custom-gpt/CONVERSATION_STARTERS.md` | optional | Useful examples for project users; not required for behavior. |

Do not upload secrets, credentials, private repositories, signing files, provisioning profiles, keystores, service-account files, local `.env` files, production data, or private endpoints as knowledge.

Do not upload Skill folders as ordinary project knowledge. If Skills are enabled, package and upload each reviewed workflow Skill through ChatGPT's native Skill upload flow instead.
