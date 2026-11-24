"""Test the ExternalRepurposing test source and the questionable test issue."""
import unittest

from src.translator_testing_model.datamodel.pydanticmodel import (
    TestAsset,
    TestIssueEnum,
    TestSourceEnum,
)


class TestExternalRepurposing(unittest.TestCase):
    """An asset can come from an external repurposing source and be flagged."""

    def test_external_repurposing_source(self):
        asset = TestAsset.model_validate(
            {
                "id": "Asset_1",
                "test_metadata": {
                    "id": "1",
                    "test_source": "ExternalRepurposing",
                    "test_reference": "https://everycure.org/portfolio/",
                    "test_annotations": [
                        {"parameter": "source", "value": "Every Cure portfolio"}
                    ],
                },
            }
        )
        assert asset.test_metadata.test_source == TestSourceEnum.ExternalRepurposing

    def test_questionable_issue(self):
        asset = TestAsset.model_validate(
            {"id": "Asset_1", "test_issue": "questionable"}
        )
        assert asset.test_issue == TestIssueEnum.questionable
