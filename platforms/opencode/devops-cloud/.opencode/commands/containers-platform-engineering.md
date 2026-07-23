---
description: Static container, Kubernetes, platform product, golden path, and developer experience workflows.
agent: container-and-orchestration-engineer
subtask: true
---

# Containers and Platform Engineering Workflows

## containerize-service
1. Capture runtime, dependency, build context, base image, non-root, secret, registry, and lifecycle constraints.
2. Design static OCI image guidance without building or running images.
3. Define handoffs for CI/CD, security review, and runtime ownership.

## kubernetes-readiness-review
1. Review ownership, namespace/tenancy, configuration, limits, probes, disruption, scaling, rollout, and lifecycle assumptions.
2. Verify no manifests are applied and no cluster state is claimed.
3. Return readiness findings and blockers.

## workload-manifest-review
1. Review Kubernetes, Helm, and Kustomize structure for clarity, policy boundaries, secrets handling, lifecycle, and portability.
2. Identify missing limits, probes, disruption handling, ownership, and rollback assumptions.
3. Do not run template, diff, apply, or validation commands.

## internal-platform-capability
1. Define user, problem, service contract, policy boundary, operational model, and support lifecycle.
2. Confirm self-service does not hide critical operational or security constraints.
3. Require human approval for sensitive actions.

## golden-path-publication-review
1. Review template, paved-road scope, ownership, documentation, support model, adoption metric, and escape hatch.
2. Confirm product feedback and lifecycle management are defined.
3. Publish guidance only as static repository content.

## platform-product-feedback-cycle
1. Define platform users, outcomes, feedback channels, product metrics, review cadence, and deprecation path.
2. Convert feedback into prioritized static recommendations.
3. Do not install, connect, or mutate platform products.
