from __future__ import annotations

from dataclasses import dataclass


STANDARD_STAGES = (
    "intake", "requirements", "analysis", "risk_classification", "design_if_applicable",
    "plan", "human_checkpoint", "implementation_if_applicable", "validation",
    "independent_code_review", "engineering_risk_review_if_triggered", "documentation",
    "release_readiness", "close",
)


@dataclass(frozen=True)
class WorkflowDefinition:
    id: str
    purpose: str
    risk_triggers: tuple[str, ...]
    stages: tuple[str, ...] = STANDARD_STAGES


WORKFLOWS = {'new-feature-development': {'purpose': 'Deliver a new capability from requirements through independent review and release-readiness assessment.', 'risk_triggers': ('public behavior', 'new data flow', 'new dependency', 'architecture boundary')}, 'bug-investigation-and-correction': {'purpose': 'Identify root cause, make the smallest safe correction, and prevent regression.', 'risk_triggers': ('security defect', 'data corruption', 'production impact', 'uncertain reproduction')}, 'controlled-refactoring': {'purpose': 'Improve internal structure while preserving documented behavior and compatibility.', 'risk_triggers': ('cross-module change', 'public API', 'persistence model', 'large change surface')}, 'architecture-change': {'purpose': 'Evaluate alternatives, document a decision, obtain approval, migrate safely, and review independently.', 'risk_triggers': ('boundary change', 'new architectural pattern', 'migration', 'compatibility risk')}, 'api-or-library-evolution': {'purpose': 'Evolve public contracts with compatibility, versioning, migration, testing, and documentation controls.', 'risk_triggers': ('breaking change', 'external consumers', 'semantic versioning impact', 'deprecation')}, 'dependency-update': {'purpose': 'Assess necessity and supply-chain risk before a controlled dependency change.', 'risk_triggers': ('new transitive dependencies', 'major version', 'license change', 'security advisory')}, 'security-remediation': {'purpose': 'Correct a verified software weakness without exposing sensitive details or creating regressions.', 'risk_triggers': ('credential exposure', 'authorization', 'injection', 'unsafe deserialization', 'sensitive data')}, 'performance-and-reliability-improvement': {'purpose': 'Improve measurable performance or resilience with explicit baselines and evidence.', 'risk_triggers': ('concurrency', 'resource consumption', 'failure handling', 'data integrity')}, 'technical-debt-reduction': {'purpose': 'Reduce prioritized debt with bounded scope, preserved behavior, and measurable maintainability benefit.', 'risk_triggers': ('wide change surface', 'architecture drift', 'weak test safety net')}, 'maintenance-and-compatibility-update': {'purpose': 'Perform bounded maintenance while preserving supported environments and contracts.', 'risk_triggers': ('runtime compatibility', 'toolchain change', 'platform support change')}, 'release-readiness-review': {'purpose': 'Aggregate evidence, reviews, documentation, migrations, and risks for a human release decision.', 'risk_triggers': ('missing evidence', 'known critical issue', 'unreviewed change', 'incomplete documentation')}}


def definitions() -> tuple[WorkflowDefinition, ...]:
    return tuple(WorkflowDefinition(id=key, purpose=value["purpose"], risk_triggers=tuple(value["risk_triggers"])) for key, value in WORKFLOWS.items())
