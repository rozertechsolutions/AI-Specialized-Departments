---
trigger: model_decision
description: Apply for Docker, OCI, Compose, Kubernetes, Helm, Kustomize, registries, internal developer platforms, catalogs, portals, and golden paths.
---

# Containers and Platform Engineering Rule

Use for Section 04 container and platform product work. Primary owners:

- Container and Orchestration Engineer: Docker, OCI images, Docker Compose static topology, registries, Kubernetes workload design, Helm, Kustomize, tenancy, limits, probes, disruption, and lifecycle.
- Platform Product and Developer Experience Engineer: internal developer platforms, catalogs, portals, templates, golden paths, controlled self-service, platform-as-a-product feedback, and lifecycle.

Outputs must expose ownership, limits, security posture, lifecycle, platform metrics, and handoffs. Keep self-service policy bounded and human-reviewed for privileged access.

Do not run Docker, Compose, Kubernetes, Helm, Kustomize, registry operations, portal APIs, platform APIs, hooks, MCP, deployments, or generated configurations.

Use `@containers-platform-engineering` for detailed procedures.
