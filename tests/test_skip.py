"""Test that assets and test cases can be skipped."""
import unittest

from src.translator_testing_model.datamodel.pydanticmodel import (
    PathfinderTestAsset,
    PathfinderTestCase,
    PerformanceTestCase,
    TestAsset,
    TestCase,
)


class TestSkip(unittest.TestCase):
    """skip defaults to false, and skip_reason says why a test is skipped."""

    def test_not_skipped_by_default(self):
        for entity in (
            TestAsset(id="Asset_1"),
            PathfinderTestAsset(id="Asset_2", minimum_required_path_nodes=1),
            TestCase(id="TestCase_1"),
            PathfinderTestCase(id="TestCase_2"),
        ):
            assert entity.skip is False
            assert entity.skip_reason is None

    def test_skipped_with_a_reason(self):
        asset = TestAsset.model_validate(
            {"id": "Asset_1", "skip": True, "skip_reason": "always fails: Tests#140"}
        )
        assert asset.skip is True
        assert asset.skip_reason == "always fails: Tests#140"

    def test_subclasses_can_be_skipped(self):
        case = PerformanceTestCase(
            id="TestCase_1", test_run_time=20, spawn_rate=0.1, skip=True
        )
        assert case.skip is True
