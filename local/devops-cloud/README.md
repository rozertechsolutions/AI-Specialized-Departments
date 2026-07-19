# DevOps and Cloud Local Specification

This package is a provider-, runtime-, model-, endpoint-, and tool-neutral declarative specification for the complete DevOps and Cloud specialization. It is static configuration and reference material only; it does not implement a runtime, choose a model, connect to services, execute tools, mutate infrastructure, deploy, publish, sign, spend, or validate live state.

## Native Assets
- `spec/department.yaml`: department identity, scope, sections, role references, Skill references, workflow references, policies, and disabled-by-default integration flags.
- `spec/roles/*.yaml`: twenty role contracts with exclusive ownership, boundaries, handoffs, stop conditions, human-review requirements, and prohibited actions.
- `spec/skills/*.yaml`: ten section Skill specifications.
- `spec/workflows/*.yaml`: ten static workflow specifications.
- `spec/policies/*.yaml`: safety and quality-gate policies.

## Department Coverage
1. Leadership and Architecture
2. Cloud Foundation and Infrastructure
3. CI/CD and Release Engineering
4. Containers and Platform Engineering
5. SRE, Observability, and Operations
6. Resilience and Disaster Recovery
7. Performance, Capacity, and Efficiency
8. DevSecOps
9. FinOps and Sustainability
10. Assurance and Independent Review

## Neutral Operating Model
The specification preserves the twenty-role responsibility model without binding it to any hosted provider, local model server, model, runtime, tool runner, or endpoint. Providers, runtimes, models, endpoints, tools, permissions, and integrations are user-configurable and disabled by default.

Each responsibility has one primary owner. Supporting roles may provide evidence through explicit handoffs, but they must not silently take over ownership or create circular delegation. The DevOps and Cloud Assurance Reviewer remains independent and non-implementing.

## Safety Model
The package forbids secrets, credentials, real endpoints, account identifiers, private URLs, production mutation, destructive operations, external integrations, and runtime-success claims. Human review is required before privileged, destructive, costly, externally visible, compliance-sensitive, or irreversible actions.
