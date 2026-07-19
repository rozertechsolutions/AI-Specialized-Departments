# DevOps and Cloud for ChatGPT

This is a manual/import package for ChatGPT Projects, Custom GPTs, project knowledge, and ChatGPT Skills. It is not repository-native automation: ChatGPT will not automatically read these files, run tools, connect apps, or validate runtime state.

## Native Surfaces

- `project/project-instructions.md`: concise persistent Project guidance for routing, safety, and completion.
- `project/knowledge/*.md`: detailed section knowledge for the ten DevOps and Cloud sections.
- `skills/*/SKILL.md`: reusable Skill procedures where ChatGPT Skills are available to the workspace.
- `custom-gpt/instructions.md`: concise Custom GPT behavior and boundary instructions.

Apps, connectors, MCP, hooks, permissions, and repository-native agents are intentionally absent.

## Sections Covered

1. Leadership and Architecture.
2. Cloud Foundation and Infrastructure.
3. CI/CD and Release Engineering.
4. Containers and Platform Engineering.
5. SRE, Observability, and Operations.
6. Resilience and Disaster Recovery.
7. Performance, Capacity, and Efficiency.
8. DevSecOps.
9. FinOps and Sustainability.
10. Assurance and Independent Review.

## Setup

For a ChatGPT Project, create or open a Project in the ChatGPT UI, add the contents of `project/project-instructions.md` as Project instructions, and upload only the relevant knowledge and Skill files that fit the active plan limits. Current ChatGPT Projects support custom instructions and project sources; file limits vary by plan and the UI limits how many files can be uploaded at once.

For a Custom GPT, use `custom-gpt/instructions.md` as the GPT instruction source and add selected knowledge or Skill files only if the GPT builder and workspace plan support them.

Project setup and Custom GPT setup are separate. A Project instruction file does not configure a GPT, and a GPT instruction file does not automatically configure a Project.

## Safety

All outputs are static design, review, and planning artifacts. Do not use this package to execute builds, tests, scans, deployments, failovers, restores, infrastructure plans, signing, publishing, billing changes, cloud actions, or production operations. Human review is required for privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible decisions.
