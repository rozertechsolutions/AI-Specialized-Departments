from __future__ import annotations

from dataclasses import dataclass


STANDARD_STAGES = (
    "intake",
    "requirements",
    "context_analysis",
    "risk_classification",
    "design_or_plan",
    "human_checkpoint",
    "implementation_if_applicable",
    "validation",
    "independent_code_review",
    "engineering_risk_review_if_triggered",
    "documentation_and_readiness",
    "lead_evidence_aggregation",
)


@dataclass(frozen=True)
class WorkflowDefinition:
    id: str
    purpose: str
    risk_triggers: tuple[str, ...]
    exclusive_focus: tuple[str, ...]
    stages: tuple[str, ...] = STANDARD_STAGES


WORKFLOWS = {
    "new-feature-development": {
        "purpose": "Deliver a new capability from validated requirements through independent review and documentation.",
        "risk_triggers": ("public behavior", "new data flow", "new dependency", "architecture boundary"),
        "exclusive_focus": ("validated user/system requirements", "acceptance criteria", "architecture fit", "implementation slices", "integration evidence", "feature-specific documentation"),
    },
    "bug-investigation-and-correction": {
        "purpose": "Correct a defect by proving root cause and preventing regression without suppressing symptoms.",
        "risk_triggers": ("security defect", "data corruption", "production impact", "uncertain reproduction"),
        "exclusive_focus": ("observable symptom", "reproducibility", "affected versions/paths", "root cause", "minimal fix", "regression evidence", "symptom-not-suppressed confirmation"),
    },
    "controlled-refactoring": {
        "purpose": "Improve internal design while preserving behavior and compatibility.",
        "risk_triggers": ("cross-module change", "public API", "persistence model", "large change surface"),
        "exclusive_focus": ("explicit invariants", "unchanged external behavior", "bounded transformation", "compatibility evidence", "rollback or reversal plan"),
    },
    "architecture-change": {
        "purpose": "Change architecture with a decision record, migration controls, and independent approval.",
        "risk_triggers": ("boundary change", "new architectural pattern", "migration", "compatibility risk"),
        "exclusive_focus": ("decision record", "alternatives", "boundaries", "contracts", "migration stages", "compatibility", "risk review", "rollback", "independent architecture approval"),
    },
    "api-or-library-evolution": {
        "purpose": "Evolve a public contract with compatibility, versioning, migration, and examples.",
        "risk_triggers": ("breaking change", "external consumers", "semantic versioning impact", "deprecation"),
        "exclusive_focus": ("consumer impact", "contract/schema changes", "source/binary/behavioral compatibility", "versioning", "deprecation", "migration", "examples"),
    },
    "dependency-update": {
        "purpose": "Change dependencies only after need, provenance, compatibility, and rollback are known.",
        "risk_triggers": ("new transitive dependencies", "major version", "license change", "security advisory"),
        "exclusive_focus": ("demonstrated need", "provenance", "maintenance status", "transitive changes", "license signals", "vulnerability context", "compatibility", "lockfile impact", "rollback"),
    },
    "security-remediation": {
        "purpose": "Fix a weakness without exposing sensitive details or expanding scope.",
        "risk_triggers": ("credential exposure", "authorization", "injection", "unsafe deserialization", "sensitive data"),
        "exclusive_focus": ("threat/weakness", "affected trust boundary", "exploitability assumptions", "secret-safe handling", "least-change remediation", "regression evidence", "disclosure-safe reporting"),
    },
    "performance-and-reliability-improvement": {
        "purpose": "Improve performance or resilience from a baseline or documented absence of one.",
        "risk_triggers": ("concurrency", "resource consumption", "failure handling", "data integrity"),
        "exclusive_focus": ("observed baseline or absence", "hypothesis", "resource/concurrency/failure analysis", "correctness guardrails", "evidence", "regression risk"),
    },
    "technical-debt-reduction": {
        "purpose": "Reduce prioritized debt with bounded scope and measurable maintainability benefit.",
        "risk_triggers": ("wide change surface", "architecture drift", "weak test safety net"),
        "exclusive_focus": ("identified debt and impact", "prioritization rationale", "bounded scope", "preserved behavior", "measurable improvement", "unrelated-cleanup prevention"),
    },
    "maintenance-and-compatibility-update": {
        "purpose": "Perform maintenance while preserving supported environments and contracts.",
        "risk_triggers": ("runtime compatibility", "toolchain change", "platform support change", "config or data migration"),
        "exclusive_focus": ("supported environments/contracts", "compatibility matrix", "migrations", "deprecations", "data/config implications", "fallback"),
    },
    "release-readiness-review": {
        "purpose": "Aggregate readiness evidence for a human release decision without releasing anything.",
        "risk_triggers": ("missing evidence", "known critical issue", "unreviewed change", "incomplete documentation"),
        "exclusive_focus": ("acceptance evidence", "unresolved defects/risks", "documentation/changelog/migration readiness", "artifact/version implications", "rollback readiness", "stop before publication/deployment/signing/release"),
    },
}


def definitions() -> tuple[WorkflowDefinition, ...]:
    return tuple(
        WorkflowDefinition(
            id=key,
            purpose=value["purpose"],
            risk_triggers=tuple(value["risk_triggers"]),
            exclusive_focus=tuple(value["exclusive_focus"]),
        )
        for key, value in WORKFLOWS.items()
    )
