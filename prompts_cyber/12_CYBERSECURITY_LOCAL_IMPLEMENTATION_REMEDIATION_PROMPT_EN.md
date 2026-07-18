# AI Specialized Departments — Cybersecurity
## Platform Implementation and Remediation Prompt: Local provider-independent implementation

You are working inside the existing open-source repository **AI-Specialized-Departments**.

This prompt applies to exactly one platform:

```text
local/
```

Your writable scope is limited to:

```text
local/cybersecurity/
```

The platform already exists in the audited package. Audit, correct, deepen, and complete it in place.

Implement and validate all eight Cybersecurity areas for this platform. Do not work on any other platform.

This is not a cross-platform master prompt.

---

# Objective

Create a professional, adaptable, organization-neutral Cybersecurity baseline that is functionally specialized and implemented exclusively through the current native capabilities of **Local provider-independent implementation**.

The result must correct the audited defects:

- missing platform or area coverage;
- unsupported or legacy formats;
- invalid schemas;
- shallow agents, Skills, and workflows;
- unadapted cross-platform copies;
- simulated MCP or connectors;
- incomplete independent review;
- missing evidence, failure, stop, and human-approval rules;
- inconsistent native wiring.

The result is a reusable baseline. It must not contain company-specific assets, policies, tools, SLAs, laws, risk appetite, endpoints, identities, or secrets.

---

# Current Official Product Surface to Verify

The expected current native surfaces are:

- Provider-neutral specifications
- Runtime-neutral agent and Skill definitions
- Workflow schemas
- Permission and human-approval policies
- Provider/runtime/model example configurations disabled by default
- Optional interface contracts for tools and MCP without active connections

Before changing files, verify these surfaces and their exact current paths, schemas, discovery, precedence, limitations, and plan availability against current official documentation.

## Required official sources

- Project-defined local-platform policy
- Agent Skills open specification where used
- JSON Schema or equivalent stable open specifications selected by the project
- MCP specification only for disabled interface definitions when genuinely required

Official documentation is the source of truth. Use official release notes and official repositories when needed. Do not rely on remembered behavior or third-party examples.

---

# Platform-Native Implementation Direction

- Treat `local/` as an open, configurable reference package, not as Ollama, LM Studio, or any specific runtime.
- Define neutral schemas and complete human-readable agent, Skill, workflow, evidence, output, and permission contracts.
- Create safe example provider configurations only when disabled, redacted, and clearly non-authoritative.
- Add the missing defensive-operations area with the same professional coverage as other areas.

## Explicit platform exclusions and corrections

- Do not bind to a provider, runtime, model, endpoint, vector database, orchestration framework, or operating system.
- Do not create runnable servers, installers, launch scripts, package manifests, or dependencies.
- Do not assume tool names or permission semantics from a single vendor.
- Do not create active MCP servers or real provider examples.

## Platform-specific audit requirements

- The audited package lacks area 05; create it.
- Review all schemas for true provider neutrality and explicit extension points.
- Ensure the package clearly distinguishes normative contracts, optional examples, and implementation-defined behavior.

---

# Required Repository Structure

Each implemented area must remain under:

```text
local/cybersecurity/<area>/
```

The eight required area directories are:

```text
governance-risk-compliance-assurance/
security-architecture-engineering/
application-product-devsecops-security/
exposure-vulnerability-hardening/
defensive-security-operations-detection-intelligence/
incident-response-dfir-recovery/
offensive-security-authorized-validation/
cyber-resilience-specialized-technologies/
```

Inside each area, use the established conceptual order only for component types that are genuinely native:

```text
agents/
subagents/
skills/
hooks/
mcp/
workflows/
```

Do not create empty directories or cosmetic parity. Use the platform's exact current native paths even when those paths differ from the conceptual names above.

A platform-level coverage or native-capability record may be created under `local/cybersecurity/` only when it provides substantive traceability and does not simulate a platform feature.

---

# Eight-Area Professional Coverage

## Area 01 — `governance-risk-compliance-assurance`

**Professional scope**

- Cybersecurity governance and strategy
- Policy, standards, and control governance
- Cyber-risk management
- Compliance and control mapping
- Evidence and assurance management
- Third-party and supply-chain cyber risk
- Exceptions, findings, remediation governance, maturity, metrics, and executive reporting
- Independent assurance review

**Minimum workflow coverage**

- governance review
- policy review
- cyber-risk assessment
- risk-register maintenance
- control mapping and gap assessment
- evidence validation
- third-party assessment
- exception management
- remediation closure review
- maturity assessment
- executive reporting
- framework-change impact assessment

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

## Area 02 — `security-architecture-engineering`

**Professional scope**

- Security architecture governance and decision records
- Enterprise and solution security architecture
- Identity, access, privileged-access, and Zero Trust architecture
- Cloud, platform, network, endpoint, workspace, and data security architecture
- Cryptography, keys, certificates, and secrets architecture
- Container, Kubernetes, and infrastructure-as-code security architecture
- Reusable security engineering patterns and safe automation boundaries
- Independent architecture assurance

**Minimum workflow coverage**

- security architecture review
- reference architecture design
- identity and privileged-access architecture review
- cloud and platform review
- network segmentation review
- data-protection and cryptography review
- container, Kubernetes, and IaC review
- security-control pattern design
- architecture-remediation validation

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

## Area 03 — `application-product-devsecops-security`

**Professional scope**

- Secure SDLC and product-security governance
- Application security requirements
- Threat modeling and abuse-case analysis
- Application, API, web, mobile, backend, and distributed-system design review
- Static secure-code review guidance
- Dependency, SBOM, provenance, and software-supply-chain review
- CI/CD, build, artifact, and release security
- Application-security testing governance
- PSIRT and coordinated product-vulnerability handling
- Independent application-security assurance

**Minimum workflow coverage**

- secure-SDLC review
- threat modeling
- application design review
- static secure-code review
- dependency and supply-chain review
- CI/CD review
- finding triage
- release-readiness assessment
- product-vulnerability coordination
- remediation validation

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

## Area 04 — `exposure-vulnerability-hardening`

**Professional scope**

- Exposure-management governance
- Asset and attack-surface context normalization
- Vulnerability intake, normalization, provenance, and deduplication
- Risk-based prioritization using exploitability, exposure, reachability, criticality, and confidence
- Remediation, mitigation, compensating-control, and exception tracking
- Hardening baselines and configuration-deviation assessment
- External attack-surface review from supplied passive evidence
- Patch, lifecycle, and end-of-support risk governance
- Independent remediation validation and exposure assurance

**Minimum workflow coverage**

- exposure-program review
- finding normalization and triage
- backlog prioritization
- hardening-baseline design
- configuration-deviation review
- passive attack-surface assessment
- patch and end-of-life risk review
- vulnerability exception management
- remediation-evidence validation
- exposure reporting

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

## Area 05 — `defensive-security-operations-detection-intelligence`

**Professional scope**

- SOC operating model, service boundaries, and escalation
- Telemetry and logging coverage requirements
- Detection engineering lifecycle
- Alert triage and case-analysis methods
- Threat-hunting design and review
- Cyber threat-intelligence requirements and assessments
- Defensive malware-analysis planning and report interpretation
- SOAR playbook design with human approval gates
- Detection coverage and adversary-behavior mapping
- SOC metrics, quality, and independent assurance
- Explicit handoff to Incident Response when an incident is declared

**Minimum workflow coverage**

- SOC operating-model review
- telemetry-source onboarding design
- detection design and review
- supplied-alert triage
- threat-hunt planning
- threat-intelligence assessment
- defensive malware-analysis planning
- SOAR playbook design
- detection-coverage assessment
- SOC quality review
- incident escalation

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

## Area 06 — `incident-response-dfir-recovery`

**Professional scope**

- Incident-response preparedness, activation, and governance
- Incident classification, scope, command support, and decision logging
- Evidence preservation, provenance, and chain of custody
- Digital-forensic questions, acquisition planning, and specialist coordination
- Containment and eradication option planning
- Secure recovery and restoration assurance
- Ransomware, data exposure, identity, cloud, supply-chain, insider, malware, and destructive-incident scenarios
- Legal, privacy, crisis, communications, and business-continuity handoffs
- Post-incident review and corrective-action governance
- Independent incident and recovery assurance

**Minimum workflow coverage**

- incident-readiness review
- incident triage and declaration support
- active-incident coordination plan
- evidence-preservation plan
- forensic-acquisition plan
- containment and eradication options
- secure-recovery plan
- ransomware coordination
- data-exposure coordination
- tabletop exercise
- post-incident review

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

## Area 07 — `offensive-security-authorized-validation`

**Professional scope**

- Written authorization, exact scope, rules of engagement, dates, permitted techniques, exclusions, and emergency stop
- Penetration-test planning without active execution
- Adversary-emulation and Red Team campaign design
- Purple Team and control-validation coordination
- Social-engineering assessment governance
- Evidence, finding, severity, exploitability, impact, and confidence quality
- White-team deconfliction, safety, cleanup, and artifact assurance
- Breach-and-attack-simulation governance
- Authorized retest and remediation validation
- Independent scope, safety, and offensive-assessment assurance

**Minimum workflow coverage**

- authorization and scoping
- rules-of-engagement review
- penetration-test planning
- adversary-emulation campaign design
- Purple Team exercise design
- social-engineering assessment planning
- offensive finding documentation
- BAS design
- cleanup assurance
- authorized retest planning
- offensive quality and safety review

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

## Area 08 — `cyber-resilience-specialized-technologies`

**Professional scope**

- Cyber-resilience strategy, critical services, dependencies, and disruption scenarios
- Backup, restoration, immutability, and ransomware resilience
- Cyber exercises and recovery exercises
- OT and ICS security
- IoT and embedded-system security
- AI, machine-learning, agent, tool, retrieval, memory, and model-supply-chain security
- Hardware and firmware security
- Cryptographic agility and post-quantum transition planning
- Critical-infrastructure and safety-relevant cybersecurity
- Independent specialist and resilience assurance

**Minimum workflow coverage**

- cyber-resilience program review
- backup and ransomware-resilience assessment
- resilience or recovery exercise design
- OT or ICS assessment
- IoT or embedded review
- AI-system security review
- hardware or firmware review
- cryptographic-agility planning
- critical-infrastructure resilience assessment
- specialized-security quality review

**Required outcome**

Implement this area using only the platform mechanisms declared native in this prompt. Preserve the same professional coverage even when the platform represents it through instructions, Skills, knowledge, commands, schemas, or SDK code rather than agents. Include an independent reviewer for high-impact outputs.

Special rule: OT/ICS, IoT/embedded, hardware/firmware, critical-infrastructure, and other specialist modules must be created only when they provide substantive reusable value. Never create empty or nominal specialist artifacts.


---


# Mandatory Artifact Quality Contract

Every artifact must be professionally complete. Short placeholder agents, one-sentence Skills, and nominal workflows are forbidden.

## Agent or subagent contract

Every native agent or subagent must define, directly or through an unambiguous referenced instruction file:

1. Exact mission.
2. Exclusive responsibility and ownership.
3. Explicit non-goals and boundary with other Cybersecurity areas.
4. Required inputs.
5. Preconditions and authorization requirements.
6. Expected outputs and output structure.
7. Native tools available.
8. Tool and file permissions.
9. Dependencies.
10. Invocation conditions.
11. Delegation and handoff conditions.
12. Stop conditions.
13. Errors and uncertainty handled.
14. Failure behavior.
15. Evidence and confidence requirements.
16. Completion criteria.
17. Mandatory human-review conditions.
18. Explicit prohibited actions.

Do not create one agent for every small capability. Use the minimum complete responsibility model, with a distinct independent reviewer for high-impact outputs.

## Skill contract

Every native Skill must define:

- valid native frontmatter;
- exact use cases and invocation conditions;
- required inputs and preconditions;
- ordered procedure;
- structured outputs;
- evidence and quality checks;
- stop and escalation conditions;
- failure behavior;
- human-review gates;
- prohibited actions;
- references or templates only when they add substantive value.

A Skill containing only a title and a sentence is invalid.

## Workflow or command contract

Every native workflow, command, prompt file, spec, or equivalent must define:

- purpose and authorized scope;
- inputs;
- prerequisites;
- ordered stages;
- stage owners or delegated capabilities;
- intermediate and final outputs;
- decision points;
- human approvals;
- stop and failure conditions;
- evidence requirements;
- completion criteria;
- explicit statement that the workflow is not executed during this implementation task.

A command may be brief only when it delegates unambiguously to a complete native Skill or agent and validates its required inputs.

## Evidence and completion

Every substantive finding or assessment must distinguish:

- confirmed;
- probable;
- hypothetical;
- not reproduced;
- false positive;
- accepted risk;
- insufficient evidence;
- not applicable.

Every high-impact conclusion requires an independent reviewer who did not create the original output.

No artifact may claim that a control, remediation, test, recovery, deployment, scan, or integration was executed unless supplied evidence explicitly proves it.


---

# Cross-Area Authority Model

- Area 01 owns governance, risk, compliance, assurance, policy, and risk-decision support.
- Area 02 owns technical security architecture and engineering patterns.
- Area 03 owns product, application, software, and DevSecOps security.
- Area 04 owns exposure, vulnerability, prioritization, hardening, and remediation governance.
- Area 05 owns monitoring design, detection, triage, hunting, intelligence, and SOC quality.
- Area 06 owns declared-incident coordination, evidence governance, DFIR planning, containment planning, recovery, and lessons learned.
- Area 07 owns only explicitly authorized offensive assessment planning and validation.
- Area 08 owns cyber resilience and specialized technologies.

No area may:

- approve its own critical output;
- accept risk;
- approve policy, architecture, release, supplier, incident closure, testing authorization, recovery completion, or legal applicability;
- absorb another area's primary ownership;
- invoke itself recursively;
- delegate in a circle;
- hide unresolved residual risk;
- claim execution or validation without evidence.

The independent reviewer must not be the author or coordinator of the artifact being reviewed.

---


# Non-Negotiable Safety and Execution Rules

This is a static repository-authoring task.

You may:

- Read files inside the repository.
- Read current official platform documentation and official release notes.
- Create, replace, or remove files only inside the target platform's `cybersecurity/` directory.
- Inspect Git status and diffs.
- Stage only the target platform's Cybersecurity paths.
- Create one local commit after the complete platform has passed all gates.

You must not:

- Run generated agents, subagents, Skills, workflows, hooks, scripts, commands, SDK applications, MCP servers, integrations, or tests.
- Run builds, linters, formatters, parsers, compilers, interpreters, package managers, scanners, security tools, models, containers, or applications.
- Install or update software, extensions, plugins, dependencies, runtimes, models, SDKs, or CLIs.
- Authenticate any service.
- Connect any MCP server, connector, app, API, SIEM, EDR, scanner, cloud account, repository service, identity provider, ticketing platform, or telemetry source.
- Scan, probe, enumerate, exploit, test, patch, reconfigure, deploy to, or otherwise interact with a live system or target.
- Read outside the repository.
- Modify another platform or another specialization.
- Change user-global, operating-system, IDE-global, shell, or home-directory configuration.
- Add secrets, tokens, credentials, keys, private endpoints, personal information, real target data, or organization-specific confidential values.
- Perform Git push, pull, fetch, merge, rebase, reset, checkout, restore, clean, stash, branch creation, tag creation, force operations, or remote changes.
- Change Git identity or Git configuration.
- Stage or commit unrelated files.

Only these Git operations are permitted when available and necessary:

- `git status`
- `git diff`
- `git diff --cached`
- path-scoped `git add`
- `git commit`

Never use a terminal or shell for any other purpose.

All MCP, connector, app, remote-tool, telemetry, hosted-tool, and provider examples must be absent or explicitly disabled by default. Do not create fake endpoints such as `example.invalid` merely to fill a configuration.


---


# Required Working Method

## Gate 1 — Repository boundary and audit

1. Confirm the exact platform target.
2. Inspect existing Cybersecurity content for all eight areas.
3. Preserve unrelated work.
4. Identify missing areas, obsolete paths, invalid schemas, duplicate responsibilities, superficial artifacts, placeholder files, simulated components, and cross-platform copies that are not adapted.
5. Produce a private correction plan before writing.

## Gate 2 — Three independent official-documentation checks

Perform three separate reviews of current official documentation.

Each review must independently determine:

- current product and surface;
- project-scoped, version-controlled native paths;
- supported instructions, agents, subagents, Skills, workflows, commands, hooks, MCP, permissions, knowledge, schemas, and SDK mechanisms;
- required fields and schemas;
- discovery, precedence, inheritance, activation, and trust behavior;
- plan, account, workspace, IDE, CLI, cloud, preview, and version limitations;
- legacy or deprecated formats;
- whether every proposed component is truly native.

Compare the three results. Resolve every discrepancy using official documentation. If a material discrepancy cannot be resolved, stop and report the blocker. Do not guess.

## Gate 3 — Platform-native design

1. Classify every proposed component internally as `native` or `unsupported`.
2. Omit unsupported components completely.
3. Do not create `unsupported` files, simulated agents, fake hooks, dummy MCP servers, or cosmetic folder parity.
4. Preserve equivalent professional coverage without forcing identical structures.
5. Use the minimum complete set of platform-native components.
6. Separate creator, coordinator, and independent-review responsibilities.

## Gate 4 — Area-by-area implementation

Process areas 01 through 08 in order.

Do not begin the next area until the current area has passed:

- professional-coverage review;
- native-format review;
- safety review;
- responsibility-overlap review;
- static file review.

Do not leave an area partially implemented.

## Gate 5 — Platform audit

After all eight areas:

1. Verify every area is implemented or has an explicit, evidence-based omission.
2. Verify no professional responsibility disappeared because a native component type was unsupported.
3. Verify the defensive-operations area is present; it must not be silently omitted.
4. Verify no short or nominal agents, Skills, or workflows remain.
5. Verify there is no self-review, circular delegation, or conflicting authority.
6. Verify every path, filename, frontmatter field, schema, and permission is current and native.
7. Verify no fake MCP or connector exists.
8. Verify no generated content was executed.
9. Repeat the complete audit three times independently and reconcile the results.

## Gate 6 — Local commit

After the platform passes every gate:

1. Stage only the target platform's `cybersecurity/` directory.
2. Review the staged diff.
3. Create the exact commit specified in this prompt.
4. Do not amend.
5. Do not push.

If a safe local commit is impossible, leave the verified files uncommitted and report the exact reason. Do not modify Git configuration.


---

# Platform Commit

After all eight areas and the complete platform audit pass, create one local commit with this exact subject:

```text
fix(local): complete and harden provider-neutral cybersecurity specialization
```

Stage only:

```text
local/cybersecurity/
```

Do not push.

---


# Required Final Response

Return a concise report with:

- Platform and exact product surface selected.
- Official documentation and release notes consulted.
- Current platform version or documentation date where available.
- Eight-area coverage table.
- Native component types used.
- Unsupported component types omitted.
- Files created, replaced, or removed per area.
- Specific audit defects corrected.
- Remaining limitations.
- Triple-verification result.
- Local commit hash, or the exact reason the commit was safely skipped.
- Explicit confirmation that no generated content was executed, no software was installed, no service was authenticated or connected, no unrelated files were changed, and no push occurred.

Do not claim success unless the repository state supports every statement.
