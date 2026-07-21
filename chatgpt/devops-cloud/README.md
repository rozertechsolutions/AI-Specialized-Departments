# DevOps and Cloud for ChatGPT

This package is a manual/import-only DevOps and Cloud department for ChatGPT Projects, Custom GPTs, project knowledge, and ChatGPT Skills where the workspace supports Skills. It covers DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance without enabling apps, actions, connectors, or automation.

The package is static and safe by default. The ChatGPT implementation is a manual/import-only ChatGPT package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

## Possible Uses

- Designing a cloud target architecture.
- Reviewing landing zones and environment separation.
- Designing or auditing IaC.
- Designing Jenkins, GitHub Actions, GitLab CI/CD, Azure Pipelines, CircleCI, Tekton, Argo CD, or Flux workflows.
- Designing Docker, OCI, Kubernetes, Helm, and Kustomize configurations.
- Creating SLI, SLO, error-budget, alerting, and observability plans.
- Preparing incident, rollback, backup, restore, RTO, RPO, and disaster-recovery plans.
- Reviewing performance, capacity, scaling, and resource efficiency.
- Performing static DevSecOps and software supply-chain reviews.
- Performing FinOps, cost allocation, forecasting, rightsizing, and sustainability analysis.
- Performing independent operational-readiness and assurance reviews.

## Department Coverage

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

## Native Assets

- `project/project-instructions.md`: Project-level instructions for routing, safety, and completion.
- `project/knowledge/*.md`: ten section knowledge files for manual upload as Project sources.
- `custom-gpt/instructions.md`: separate Custom GPT instruction text.
- `skills/*/SKILL.md`: Agent Skill bundles for workspaces that support ChatGPT Skills.
- No repository-native agents, hooks, MCP, actions, apps, or connector configuration is included.

## Installation and Setup

Create or open a ChatGPT Project in the ChatGPT UI, add `project/project-instructions.md` as Project instructions, and upload only the relevant files from `project/knowledge/` or `skills/` that fit the current plan and workspace limits. Repository files are not loaded automatically by ChatGPT.

For a Custom GPT, use `custom-gpt/instructions.md` in the GPT builder and attach selected knowledge files only if the GPT configuration and workspace policy allow it. Project setup and GPT setup are separate; neither one configures the other.

## Usage

Start a chat in the configured Project or Custom GPT and ask for the needed section, for example "use DevOps and Cloud: SRE, Observability, and Operations to draft SLOs." Use the knowledge files for broad context and Skills for section procedures when available.

Request independent Assurance only after primary work exists, for example "run Assurance and Independent Review on the CI/CD design." Output remains advisory and static unless a human separately authorizes an action outside this package.

## Practical Example

Safe prompt using placeholders:

```text
Use the project instructions and knowledge files to review <service-name> for CI/CD rollback and SLO risks. Do not claim that ChatGPT has run tests, scans, deployments, or cloud commands.
```

## Customization Matrix

| Category | Meaning | ChatGPT Examples |
|---|---|---|
| Repository-generic | Must remain reusable and committed safely to the open-source repository. | Department sections, professional role boundaries, safety rules, no-secret rules, human-approval gates, DevSecOps/Cybersecurity boundary, platform-native package paths. |
| Project-specific | Must be adapted by the project using the department. | Repository paths, service names, environments, cloud providers, cloud regions, IaC layout, container image names, Kubernetes namespaces, CI/CD provider, artifact registry, SLO targets, RTO/RPO, cost centers, tagging conventions, branch policies, security policies. |
| User-specific | Depends on the local user, account, installation, workspace, provider/runtime, or local environment and must not be hard-coded globally. | Local installation, account or plan availability, workspace trust, selected model/provider/runtime, local paths, manually configured connectors, optional permissions, user-selected tools. |

### Project-Specific Values

Adapt placeholders such as `<repo-path>`, `<service-name>`, `<environment>`, `<cloud-provider>`, `<region>`, `<namespace>`, `<pipeline-name>`, `<artifact-registry>`, `<slo-target>`, `<rto>`, `<rpo>`, `<cost-center>`, and `<tagging-standard>` in the adopting project. Do not commit real secrets, credentials, account IDs, subscription IDs, private endpoints, private URLs, production names, or organization data.

### User-Specific Values

Keep user account, local installation, selected provider/runtime/model, workspace trust, local interpreter, local SDK installation, manually configured connectors, optional permissions, and selected cloud account outside the shared package.

### Repository-generic Values

Keep professional role boundaries, safety requirements, human-approval gates, no-secret rules, no-production-default rules, Assurance independence, platform-native paths and schemas, generic examples, and reusable Skills/workflows repository-generic.

## Safety and Limitations

The default behavior is static-only design, planning, review, and documentation. The package contains no secrets, credentials, account identifiers, private endpoints, production bindings, active integrations, or automatic production changes.

Human approval is required before privileged, destructive, costly, externally visible, compliance-sensitive, production-impacting, signing, spending, publishing, failover, restore, deployment, scanner, or irreversible actions. Static validation means reviewing files and reasoning about artifacts; runtime validation requires separately authorized execution and evidence. This package must not be used as proof of runtime success.

DevSecOps is limited to secure delivery, cloud/platform control design, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls. Pentesting, SOC/SIEM operations, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove uploaded Project sources, delete the Project instructions, remove the Custom GPT draft/configuration, or uninstall imported Skills in the ChatGPT UI. This does not affect repository files.
