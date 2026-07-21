# DevOps and Cloud for OpenAI Agents SDK

This package is an SDK-based Python representation of the DevOps and Cloud department for the OpenAI Agents SDK. It constructs static agents, typed role definitions, guardrails, handoffs, skills, and workflows for DevOps, Cloud, Platform Engineering, SRE, resilience, performance, DevSecOps, FinOps, sustainability, and independent assurance without configuring tools or external model execution by default.

The package is static and safe by default. The OpenAI Agents SDK implementation is a SDK-based Python package; it provides platform-appropriate instructions, roles, Skills, rules, workflows, or source files without activating infrastructure, CI/CD systems, cloud access, scanners, billing actions, deployments, or runtime checks.

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

- `pyproject.toml`: Python package metadata and dependencies.
- `src/devops_cloud_department/*.py`: typed sections, roles, workflows, guardrails, and SDK `Agent` construction.
- `tests/test_static_contracts.py`: deterministic offline tests for construction, topology, guardrails, boundaries, and exports.
- No tools, MCP servers, hosted tools, shell access, server, deployment, API key, or runtime session is configured.

## Installation and Setup

Use Python 3.11 or newer. For local validation, create an isolated virtual environment outside the repository, install the package plus `openai-agents` and `pytest`, disable hosted tracing with `OPENAI_AGENTS_DISABLE_TRACING=1`, and do not set an OpenAI API key.

This package is importable source code only. It does not start a server, contact a model, or run an Agent session unless a separate program does so.

## Usage

Import the package to inspect role definitions, Skills, workflows, and constructed SDK `Agent` objects. Use the entry agent for routing to specialists and request one section by name in the surrounding application design.

Use the Assurance agent only after primary output exists. Do not run real `Runner` sessions or external tools for static validation; deterministic tests should inspect construction and topology only.

## Practical Example

Safe prompt using placeholders:

```text
Import the package locally and inspect the static agent registry for <role-name>. Do not run a real Agent session, start a server, or call a model.
```

## Customization Matrix

| Category | Meaning | OpenAI Agents SDK Examples |
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

Remove `openai-agents-sdk/devops-cloud/` from the consuming repository or uninstall the local package from the isolated environment. Do not delete unrelated virtual environments or Python packages.
