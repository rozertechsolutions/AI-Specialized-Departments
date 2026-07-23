import unittest
from pathlib import PurePath

from mobile_development_agents.app import dry_run_workflow, route_workflow
from mobile_development_agents.context import MobileProjectContext, MobileTechnology, WorkflowRequest
from mobile_development_agents.outputs import CriterionStatus, WorkflowState
from mobile_development_agents.workflows.registry import WORKFLOW_SPECS


def make_request(
    workflow: str,
    technologies: frozenset[MobileTechnology],
    approvals: frozenset[str] = frozenset({"project-edit"}),
):
    context = MobileProjectContext(
        project_root=PurePath("app"),
        technologies=technologies,
        detected_commands=("pytest",),
    )
    return WorkflowRequest(
        workflow=workflow,
        objective="test objective",
        technologies=technologies,
        project_context=context,
        human_approvals=approvals,
    )


class WorkflowTests(unittest.TestCase):
    def test_ten_workflows_are_defined_once(self) -> None:
        self.assertEqual(len(WORKFLOW_SPECS), 10)
        self.assertEqual(
            set(WORKFLOW_SPECS),
            {
                "create-mobile-project",
                "implement-mobile-feature",
                "fix-mobile-bug",
                "review-mobile-architecture",
                "add-mobile-screen",
                "integrate-mobile-api",
                "add-mobile-tests",
                "optimize-mobile-performance",
                "audit-mobile-security",
                "prepare-mobile-release",
            },
        )

    def test_single_technology_feature_routes_to_platform_owner(self) -> None:
        request = make_request("implement-mobile-feature", frozenset({MobileTechnology.ANDROID}))
        routed = route_workflow(request)
        self.assertEqual(routed.primary_owner, "android-engineer")
        self.assertIn("mobile-code-reviewer", routed.reviewers)
        self.assertNotIn(routed.primary_owner, routed.reviewers)
        self.assertEqual(routed.validation_issues, ())

    def test_release_workflow_requires_manual_initiation_and_release_approval(self) -> None:
        request = make_request(
            "prepare-mobile-release",
            frozenset({MobileTechnology.IOS}),
            approvals=frozenset(),
        )
        result = dry_run_workflow(request)
        self.assertIs(result.state, WorkflowState.NEEDS_APPROVAL)
        self.assertTrue(any("manual initiation" in issue for issue in result.limitations))
        self.assertTrue(any("release-sensitive" in issue for issue in result.limitations))

    def test_not_applicable_completion_criteria_have_reasons(self) -> None:
        request = make_request("add-mobile-tests", frozenset({MobileTechnology.FLUTTER}))
        result = dry_run_workflow(request)
        not_applicable = [
            criterion
            for criterion in result.criteria
            if criterion.status is CriterionStatus.NOT_APPLICABLE
        ]
        self.assertTrue(not_applicable)
        self.assertTrue(all(criterion.reason for criterion in not_applicable))
