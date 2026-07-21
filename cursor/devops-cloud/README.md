# DevOps and Cloud for Cursor

This package is a repository-native DevOps and Cloud department for Cursor. It covers cloud architecture, cloud foundations, CI/CD, containers, platform engineering, SRE, observability, resilience, performance, DevSecOps, FinOps, sustainability, and independent Assurance.

The Cursor implementation provides `AGENTS.md`, Cursor Project Rules, native project custom subagents, Agent Skills, and static workflow references. It is static and safe by default: it does not install dependencies, configure MCP, connect to cloud accounts, execute commands, run CI/CD, deploy, scan, mutate infrastructure, or validate runtime state.

## Possible Uses

- Cloud architecture design and static Well-Architected review.
- Landing-zone, account, subscription, project, and environment-boundary review.
- IaC design/review for Terraform, OpenTofu, Pulumi, CloudFormation, Bicep, and Ansible.
- CI/CD pipeline, release, promotion, rollback, and DORA-metric design/review.
- Docker, OCI image, Kubernetes, Helm, Kustomize, registry, and platform-engineering review.
- SLI, SLO, error-budget, observability, alerting, incident, and postmortem design.
- Rollback, backup/restore, RTO/RPO, disaster-recovery, HA, and failover/failback planning.
- Performance, capacity, scaling, autoscaling, bottleneck, and efficiency review.
- DevSecOps, cloud security control, policy-as-code, SBOM, provenance, signing-strategy, and software supply-chain review.
- FinOps, cost allocation, forecasting, rightsizing, commitments, utilization, and sustainability analysis.
- Independent Assurance after primary DevOps and Cloud work exists.

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

- `AGENTS.md`: concise persistent Cursor guidance for department identity, global routing, safety, DevSecOps boundaries, Assurance requirements, completion rules, and native asset discovery. Cursor supports `AGENTS.md` at the project root and in subdirectories.
- `.cursor/agents/*.md`: twenty project-scoped Cursor custom subagents, one per professional role. Cursor discovers Markdown files in `.cursor/agents/`, reads YAML frontmatter, and exposes custom subagents as available Agent tools.
- `.cursor/rules/*.mdc`: Cursor Project Rules with YAML frontmatter. The routing/safety rule is always applied; section rules use `alwaysApply: false` and descriptions so Cursor can apply them when relevant.
- `.cursor/skills/*/SKILL.md`: ten Agent Skills with supported `name` and `description` frontmatter. Cursor can apply relevant Skills automatically, and users can invoke them by name where their Cursor version exposes Skill invocation.
- `docs/*-workflows.md`: static workflow references used by the section Skills. They are support documents, not execution scripts.

No Cursor cloud-agent setup, MCP configuration, hooks, connector, terminal automation, or external integration is included.

## Installation and Setup

Copy the contents of `cursor/devops-cloud/` into the root of the repository opened in Cursor. The expected project paths are:

- `AGENTS.md`
- `.cursor/agents/*.md`
- `.cursor/rules/*.mdc`
- `.cursor/skills/*/SKILL.md`
- `docs/*-workflows.md`

Open the repository as a Cursor workspace. Native discovery depends on the installed Cursor version, workspace trust/settings, and account or plan availability for Agent, custom subagents, and Agent Skills. The package installs no extension, dependency, plugin, MCP server, cloud connector, or provider configuration.

## Usage

Ask Cursor Agent for a DevOps and Cloud outcome and name the section or role when useful, for example: "Use the `performance-capacity-engineer` to review autoscaling risks for `<service-name>` from these manifests." Cursor may also delegate automatically based on custom subagent descriptions, current context, task complexity, and available tools.

Use `devops-cloud-orchestrator` for intake, classification, dependency coordination, and role selection. Use specialist subagents for primary role work. Use section Skills for repeatable procedures and the `docs/*-workflows.md` references for detailed static workflow steps.

Invoke `devops-cloud-assurance-reviewer` only after a primary artifact, review, or evidence set exists. Assurance may block completion but must not implement the primary artifact, approve its own work, silently edit reviewed work, or claim runtime validation from static inspection.

All output remains advisory and static unless a human separately authorizes an action outside this package.

## Practical Example

Safe prompt using placeholders:

```text
Use devops-cloud-orchestrator to route this request, then use infrastructure-as-code-engineer for primary review:
review the Terraform module under <repo-path> for environment separation, state ownership, rollback assumptions, and missing human approval gates.
Do not run terraform, cloud CLIs, scanners, or tests. End with whether Assurance is ready to review.
```

## Customization Matrix

| Category | Meaning | Cursor Examples |
|---|---|---|
| Repository-generic | Must remain reusable and committed safely to the open-source repository. | Professional role boundaries, `.cursor/agents/` schema, `.cursor/rules/` paths, Skill names, static safety rules, no-secret rules, human-approval gates, DevSecOps/Cybersecurity boundary. |
| Project-specific | Must be adapted by the project using the department. | Repository paths, service names, environments, cloud providers, regions, IaC layout, image names, Kubernetes namespaces, CI/CD provider, artifact registry, branch policies, SLO targets, RTO/RPO, cost centers, tagging conventions, security policies. |
| User-specific | Depends on the local user, account, installation, workspace, provider/runtime, or local environment and must not be hard-coded globally. | Cursor version, workspace trust, enabled Agent/Skills/subagent availability, model access, local workspace path, manually configured connectors, optional MCP outside this package, selected cloud account outside the repository. |

### Project-Specific Values

Replace placeholders such as `<repo-path>`, `<service-name>`, `<environment>`, `<cloud-provider>`, `<region>`, `<namespace>`, `<pipeline-name>`, `<artifact-registry>`, `<slo-target>`, `<rto>`, `<rpo>`, `<cost-center>`, and `<tagging-standard>` with values from the adopting repository. Do not commit real secrets, credentials, private endpoints, account IDs, production identifiers, or organization-private URLs.

### User-Specific Values

Cursor account, plan, model availability, workspace trust, local installation path, user-level Cursor settings, user-level agents, and any user-configured MCP servers or connectors are outside this package. Keep those values in the user's environment or Cursor settings, not in the shared package.

### Repository-generic Values

Keep role ownership, section routing, static-by-default behavior, no-production-default rules, human-review gates, Assurance independence, prohibited actions, generic examples, supported native paths, and Skill/workflow names reusable across repositories.

## Safety and Limitations

Cursor subagents support `readonly: true`, which restricts file edits and state-changing shell commands, but Cursor documentation also states subagents inherit tools from the parent, including MCP tools from configured servers. This package does not configure MCP and does not claim stronger technical isolation than Cursor provides. The subagent bodies, `AGENTS.md`, and Project Rules explicitly prohibit terminal execution, MCP use, cloud access, scanners, deployments, production mutation, billing changes, signing, publishing, failover, restore, and destructive actions.

Static validation means reviewing files and reasoning about artifacts. Runtime validation requires separately authorized execution and evidence. Do not treat this package as proof that tests, builds, scans, cloud plans, deployments, failovers, restores, or cost queries were executed.

DevSecOps is limited to secure delivery controls, cloud/platform control design, IAM/secrets patterns, policy-as-code placement, SBOM, provenance, signing strategy, and software supply-chain controls inside DevOps workflows. Pentesting, Red Team, SOC/SIEM, threat intelligence, forensics, enterprise GRC, general cybersecurity incident response, and offensive security belong to the separate Cybersecurity specialization.

## Removal or Deactivation

Remove only this package's files from the target repository:

- `AGENTS.md` if it was copied only for this package.
- `.cursor/agents/devops-cloud-*.md` and the other DevOps and Cloud role files listed in `.cursor/agents/`.
- `.cursor/rules/*devops-cloud*.mdc` and the numbered DevOps and Cloud section rules.
- `.cursor/skills/*` entries copied from this package.
- `docs/*-workflows.md` entries copied from this package.

Preserve unrelated Cursor rules, user settings, workspace settings, MCP configuration, extensions, and project files.
