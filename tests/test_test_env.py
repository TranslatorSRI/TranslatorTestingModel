"""Test that test cases no longer carry an environment."""
import unittest

from pydantic import ValidationError

from src.translator_testing_model.datamodel.pydanticmodel import (
    PathfinderTestCase,
    TestCase,
    TestRunSession,
)


class TestNoTestEnv(unittest.TestCase):
    """The same suite runs in every environment; the TestHarness picks one."""

    def test_test_case_rejects_test_env(self):
        with self.assertRaises(ValidationError):
            TestCase.model_validate({"id": "TestCase_1", "test_env": "ci"})

    def test_pathfinder_test_case_rejects_test_env(self):
        with self.assertRaises(ValidationError):
            PathfinderTestCase.model_validate({"id": "TestCase_1", "test_env": "ci"})

    def test_test_run_session_keeps_test_env(self):
        """A record of a run still says where it ran."""
        session = TestRunSession(id="session_1", test_env="prod")
        assert session.test_env == "prod"
