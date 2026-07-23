from __future__ import annotations

from dataclasses import dataclass

from mobile_development_agents.context import MobileTechnology, WorkflowRequest


@dataclass(frozen=True, slots=True)
class WorkflowSpec:
    name: str
    objective: str
    trigger: str
    inputs: tuple[str, ...]
    supported_technologies: frozenset[MobileTechnology]
    preconditions: tuple[str, ...]
    primary_owner: str
    reviewers: tuple[str, ...]
    ordered_steps: tuple[str, ...]
    conditional_steps: tuple[str, ...]
    validation_gates: tuple[str, ...]
    failures: tuple[str, ...]
    stop_conditions: tuple[str, ...]
    evidence: tuple[str, ...]
    outputs: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    human_approvals: tuple[str, ...]
    prohibited_actions: tuple[str, ...]
    manually_initiated: bool = False

    def validate_request(self, request: WorkflowRequest) -> tuple[str, ...]:
        issues: list[str] = []
        if request.workflow != self.name:
            issues.append(f"request workflow {request.workflow!r} does not match {self.name!r}")
        unsupported = request.technologies - self.supported_technologies
        if unsupported:
            issues.append("unsupported technologies: " + ", ".join(sorted(t.value for t in unsupported)))
        if request.cancellation_requested:
            issues.append("cancellation requested")
        if self.manually_initiated and "manual-initiation" not in request.human_approvals:
            issues.append("manual initiation approval is required")
        missing_approvals = set(self.human_approvals) - set(request.human_approvals)
        if missing_approvals:
            issues.append("missing approvals: " + ", ".join(sorted(missing_approvals)))
        return tuple(issues)


ALL_TECHNOLOGIES = frozenset(MobileTechnology)
IMPLEMENTATION_REVIEWERS = (
    "mobile-test-engineer",
    "mobile-security-reviewer",
    "mobile-ui-accessibility-reviewer",
    "mobile-code-reviewer",
)


WORKFLOW_SPECS: dict[str, WorkflowSpec] = {
    "create-mobile-project": WorkflowSpec(
        name="create-mobile-project",
        objective="Create a mobile project skeleton using the requested native technology conventions.",
        trigger="Explicit request to create a new Android, iOS, KMP, Flutter, or React Native project.",
        inputs=("project name", "technology", "package identifiers", "target platforms"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("target directory scoped", "technology tooling detected", "no conflicting project exists"),
        primary_owner="mobile-architect",
        reviewers=("mobile-security-reviewer", "mobile-test-engineer", "mobile-code-reviewer"),
        ordered_steps=("inspect destination", "select native project structure", "create scoped files", "discover validation commands", "validate"),
        conditional_steps=("request approval before dependencies, lockfiles, signing, or external templates"),
        validation_gates=("project configuration", "dependency resolution when local", "non-publishing build when available"),
        failures=("tooling unavailable", "destination conflict", "approval missing"),
        stop_conditions=("out-of-scope path", "credentials required", "external integration activation requested"),
        evidence=("created file list", "commands run", "unavailable infrastructure"),
        outputs=("project files", "validation report", "limitations"),
        acceptance_criteria=("native project opens/builds when tooling is available", "no secrets", "no active external integration"),
        human_approvals=("project-edit",),
        prohibited_actions=("publish", "upload", "sign with real credentials", "activate integrations"),
    ),
    "implement-mobile-feature": WorkflowSpec(
        name="implement-mobile-feature",
        objective="Implement a bounded mobile feature in existing project conventions.",
        trigger="Explicit feature request.",
        inputs=("feature requirements", "target technology", "acceptance criteria"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("existing project inspected", "owner selected", "tests and validation commands discovered"),
        primary_owner="mobile-architect",
        reviewers=IMPLEMENTATION_REVIEWERS,
        ordered_steps=("inspect", "route implementation owner", "plan", "edit scoped files", "add tests", "validate", "final review"),
        conditional_steps=("security review for auth/privacy/network/dependencies", "accessibility review for UI", "performance review for hot paths"),
        validation_gates=("format/lint/type/build where configured", "relevant tests", "independent final review"),
        failures=("ambiguous requirement", "validation failure", "approval missing"),
        stop_conditions=("public contract change not approved", "external write needed", "unsafe credential use"),
        evidence=("diff", "test output", "review findings"),
        outputs=("implementation", "tests", "validation report"),
        acceptance_criteria=("feature satisfies requirements", "regression coverage present or justified", "review complete"),
        human_approvals=("project-edit",),
        prohibited_actions=("scope expansion", "unapproved dependencies", "self-review"),
    ),
    "fix-mobile-bug": WorkflowSpec(
        name="fix-mobile-bug",
        objective="Reproduce, diagnose, and fix a mobile bug with regression coverage.",
        trigger="Bug report or failing test.",
        inputs=("bug description", "reproduction steps", "affected technology"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("reproduction attempted", "affected files inspected", "expected behavior known"),
        primary_owner="mobile-test-engineer",
        reviewers=("mobile-security-reviewer", "mobile-code-reviewer"),
        ordered_steps=("reproduce or explain unavailable", "localize cause", "apply minimal fix", "add regression test", "validate"),
        conditional_steps=("route platform-specific code to technology owner", "security review for sensitive bug classes"),
        validation_gates=("regression test", "affected test suite", "static checks where configured"),
        failures=("cannot reproduce", "unclear expected behavior", "unrelated failure"),
        stop_conditions=("fix requires behavior change outside scope", "test weakening required", "approval missing"),
        evidence=("reproduction result", "test output", "diff"),
        outputs=("minimal fix", "regression test", "known limitations"),
        acceptance_criteria=("bug fixed", "regression covered", "unrelated failures reported"),
        human_approvals=("project-edit",),
        prohibited_actions=("broad refactor", "test weakening", "fabricated reproduction"),
    ),
    "review-mobile-architecture": WorkflowSpec(
        name="review-mobile-architecture",
        objective="Review architecture, boundaries, dependency direction, state, navigation, and migrations.",
        trigger="Architecture review request or architecture-sensitive change.",
        inputs=("architecture files", "module graph", "target constraints"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("project inspected", "technology matrix known", "dependency direction understood"),
        primary_owner="mobile-architect",
        reviewers=("mobile-security-reviewer", "mobile-performance-reviewer", "mobile-code-reviewer"),
        ordered_steps=("inspect structure", "map responsibilities", "identify conflicts", "document findings", "review evidence"),
        conditional_steps=("request implementation approval only if remediation is explicitly requested"),
        validation_gates=("responsibility matrix", "conflict check", "security/performance risk review"),
        failures=("unavailable dependency graph", "ambiguous ownership", "unsupported architecture assumption"),
        stop_conditions=("requested remediation exceeds review scope", "public API change needed"),
        evidence=("file references", "dependency notes", "findings"),
        outputs=("architecture review", "risk list", "recommended next steps"),
        acceptance_criteria=("unique ownership", "no duplicated authority", "limitations stated"),
        human_approvals=(),
        prohibited_actions=("implementation without approval", "release approval"),
    ),
    "add-mobile-screen": WorkflowSpec(
        name="add-mobile-screen",
        objective="Add a mobile screen using native UI conventions and complete UI states.",
        trigger="Request for a new screen or view.",
        inputs=("screen requirements", "navigation target", "states", "technology"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("UI framework detected", "navigation pattern known", "state-management convention known"),
        primary_owner="mobile-architect",
        reviewers=("mobile-ui-accessibility-reviewer", "mobile-test-engineer", "mobile-code-reviewer"),
        ordered_steps=("inspect UI patterns", "route platform owner", "implement screen", "cover states", "validate UI tests"),
        conditional_steps=("security review for forms/auth/private data", "localization review when text changes"),
        validation_gates=("loading/empty/error/retry/cancellation states", "accessibility", "navigation tests where available"),
        failures=("missing design requirements", "state convention unclear", "accessibility blocker"),
        stop_conditions=("unapproved data collection", "incomplete required UI states", "external assets with unclear rights"),
        evidence=("screen files", "test output", "accessibility checklist"),
        outputs=("screen implementation", "state coverage", "validation report"),
        acceptance_criteria=("screen works in target navigation", "states complete", "accessibility reviewed"),
        human_approvals=("project-edit",),
        prohibited_actions=("hardcoded private data", "unapproved telemetry", "incomplete UI states"),
    ),
    "integrate-mobile-api": WorkflowSpec(
        name="integrate-mobile-api",
        objective="Integrate a mobile API client without embedding secrets or activating private services by default.",
        trigger="Request to add or modify API integration.",
        inputs=("API contract", "auth model", "error behavior", "offline requirements"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("endpoint classification complete", "secret handling defined", "network security reviewed"),
        primary_owner="mobile-architect",
        reviewers=("mobile-security-reviewer", "mobile-test-engineer", "mobile-code-reviewer"),
        ordered_steps=("inspect networking conventions", "define client boundary", "implement safe config", "add tests", "validate"),
        conditional_steps=("human approval for auth, privacy, dependencies, analytics, telemetry, or lockfiles"),
        validation_gates=("no real endpoints unless public and intended", "no secrets", "error/offline states tested"),
        failures=("secret required", "auth flow unclear", "network policy violation"),
        stop_conditions=("credential import requested", "private endpoint value missing approval", "dependency approval missing"),
        evidence=("client files", "secret scan", "network/security review", "test output"),
        outputs=("API integration", "configuration docs", "validation evidence"),
        acceptance_criteria=("safe configuration", "errors handled", "security approval satisfied"),
        human_approvals=("project-edit", "security-sensitive"),
        prohibited_actions=("commit secrets", "activate real external integration by default", "log sensitive data"),
    ),
    "add-mobile-tests": WorkflowSpec(
        name="add-mobile-tests",
        objective="Add deterministic mobile regression coverage at the appropriate test level.",
        trigger="Request for tests or uncovered behavior.",
        inputs=("behavior under test", "target technology", "test level"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("test framework detected", "fixtures reviewed", "commands discovered"),
        primary_owner="mobile-test-engineer",
        reviewers=("mobile-code-reviewer",),
        ordered_steps=("inspect tests", "choose level", "add deterministic fixtures", "run targeted tests", "record evidence"),
        conditional_steps=("security review for sensitive fixtures", "UI reviewer for accessibility snapshots"),
        validation_gates=("targeted test pass", "flakiness risk", "no production weakening"),
        failures=("test infra unavailable", "nondeterminism", "sensitive fixture risk"),
        stop_conditions=("production behavior change needed merely for tests", "external service required", "approval missing"),
        evidence=("test files", "test command output", "unavailable infrastructure"),
        outputs=("tests", "coverage rationale", "limitations"),
        acceptance_criteria=("tests are deterministic", "relevant commands run or unavailable", "no production weakening"),
        human_approvals=("project-edit",),
        prohibited_actions=("weaken validation", "fabricate passing tests", "use real private data"),
    ),
    "optimize-mobile-performance": WorkflowSpec(
        name="optimize-mobile-performance",
        objective="Improve or assess mobile performance using measured evidence.",
        trigger="Performance issue or optimization request.",
        inputs=("performance goal", "baseline", "target technology", "measurement method"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("baseline available or unavailable stated", "measurement command approved when costly", "hot path identified"),
        primary_owner="mobile-performance-reviewer",
        reviewers=("mobile-test-engineer", "mobile-code-reviewer"),
        ordered_steps=("define metric", "measure baseline", "identify cause", "apply scoped optimization if approved", "remeasure"),
        conditional_steps=("route implementation to technology owner", "request approval for long-running profiling"),
        validation_gates=("baseline", "post-change measurement", "regression tests"),
        failures=("measurement unavailable", "flaky benchmark", "unapproved resource-intensive run"),
        stop_conditions=("cannot measure", "optimization requires architecture change without approval", "battery/privacy risk"),
        evidence=("profiling output", "benchmark result", "test output"),
        outputs=("optimization or findings", "measurement comparison", "risks"),
        acceptance_criteria=("improvement measured or limitation stated", "no unsupported claim", "tests still pass"),
        human_approvals=("project-edit", "performance-measurement"),
        prohibited_actions=("claim improvement without measurements", "run costly profiling without approval"),
    ),
    "audit-mobile-security": WorkflowSpec(
        name="audit-mobile-security",
        objective="Audit mobile security, privacy, permissions, storage, network, deep links, WebViews, logging, telemetry, and dependency risks.",
        trigger="Security audit request or security-sensitive change.",
        inputs=("target scope", "manifests/entitlements", "dependency files", "network/storage/auth code"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("scope inspected", "secrets protected", "approval state known"),
        primary_owner="mobile-security-reviewer",
        reviewers=("mobile-code-reviewer",),
        ordered_steps=("map sensitive surfaces", "scan for secrets", "review policies", "classify findings", "report blockers"),
        conditional_steps=("request approval before remediation edits", "route remediation to implementation owner"),
        validation_gates=("secret scan", "permission review", "dependency risk review", "privacy review"),
        failures=("secret detected", "unapproved auth/privacy change", "missing evidence"),
        stop_conditions=("credential exposure", "private data risk", "remediation requested without approval"),
        evidence=("findings", "file references", "scan output", "approval requirements"),
        outputs=("security audit", "blockers", "approved remediation plan if requested"),
        acceptance_criteria=("risks classified", "secrets absent or blocked", "human approvals identified"),
        human_approvals=(),
        prohibited_actions=("modify source by default", "suppress risks", "import credentials"),
    ),
    "prepare-mobile-release": WorkflowSpec(
        name="prepare-mobile-release",
        objective="Prepare release readiness without publishing, uploading, submitting, distributing, spending money, or using real signing credentials.",
        trigger="Manual release preparation request only.",
        inputs=("release target", "variant/flavor/scheme", "versioning", "readiness checklist"),
        supported_technologies=ALL_TECHNOLOGIES,
        preconditions=("manual initiation", "target version known", "signing prerequisites separated from credentials"),
        primary_owner="mobile-release-engineer",
        reviewers=("mobile-security-reviewer", "mobile-test-engineer", "mobile-code-reviewer"),
        ordered_steps=("inspect versioning", "review variants/schemes/flavors", "run non-publishing validation", "document readiness", "list blockers"),
        conditional_steps=("request approval for version/build config edits", "stop before real signing or external distribution"),
        validation_gates=("non-publishing build when available", "test evidence", "security release checklist"),
        failures=("manual initiation missing", "credentials required", "publishing requested"),
        stop_conditions=("real signing credential needed", "external release action requested", "spend money requested"),
        evidence=("version review", "non-publishing command output", "readiness checklist"),
        outputs=("release readiness report", "blockers", "non-publishing validation evidence"),
        acceptance_criteria=("manual initiation present", "no release action performed", "readiness gaps explicit"),
        human_approvals=("manual-initiation", "release-sensitive"),
        prohibited_actions=("publish", "upload", "submit", "deploy", "distribute", "spend money", "sign with real credentials"),
        manually_initiated=True,
    ),
}


def get_workflow(name: str) -> WorkflowSpec:
    try:
        return WORKFLOW_SPECS[name]
    except KeyError as exc:
        raise ValueError(f"unsupported workflow: {name}") from exc


def workflows_for_technology(technology: MobileTechnology) -> tuple[WorkflowSpec, ...]:
    return tuple(spec for spec in WORKFLOW_SPECS.values() if technology in spec.supported_technologies)
