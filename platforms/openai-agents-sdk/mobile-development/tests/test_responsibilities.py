import unittest

from mobile_development_agents.agents.definitions import (
    READ_ONLY_REVIEWERS,
    ROLE_SPECS,
    SPECIALIST_NAMES,
)
from mobile_development_agents.app import responsibility_matrix


class ResponsibilityTests(unittest.TestCase):
    def test_all_twelve_specialists_are_defined(self) -> None:
        self.assertEqual(tuple(ROLE_SPECS), SPECIALIST_NAMES)
        self.assertEqual(len(ROLE_SPECS), 12)

    def test_every_role_has_required_operational_fields(self) -> None:
        for spec in ROLE_SPECS.values():
            self.assertEqual(spec.native_classification, "native")
            self.assertTrue(spec.mission)
            self.assertTrue(spec.exclusive_scope)
            self.assertTrue(spec.inputs)
            self.assertTrue(spec.preconditions)
            self.assertTrue(spec.outputs)
            self.assertTrue(spec.evidence)
            self.assertTrue(spec.tools)
            self.assertTrue(spec.permissions)
            self.assertTrue(spec.dependencies or spec.name == "mobile-code-reviewer")
            self.assertTrue(spec.invocation)
            self.assertTrue(spec.stop_conditions)
            self.assertTrue(spec.errors)
            self.assertTrue(spec.fail_safe_behavior)
            self.assertTrue(spec.completion_criteria)
            self.assertTrue(spec.human_review)
            self.assertTrue(spec.prohibited_actions)

    def test_review_roles_are_read_only(self) -> None:
        matrix = responsibility_matrix()
        for name in READ_ONLY_REVIEWERS:
            self.assertIs(matrix[name]["read_only"], True)
