"""
Unit Tests for TestSuiteFactory functionality
"""
import unittest

from src.translator_testing_model.adaptor.test_suite_factory import (
    TestSuiteInputException,
    TestCaseGenerator
)
from src.translator_testing_model.datamodel.pydanticmodel import (
    TestMetadata,
    TestSuite,
    TestSuiteSpecification,
    FileFormatEnum
)


# temporary hack access to some TestAsset data online
SAMPLE_TEST_ASSET_FILE = "https://raw.githubusercontent.com/TranslatorSRI/TranslatorTestingModel/" +\
                         "main/src/data/examples/SampleTestAssetList.json"


def create_test_case_generator() -> TestCaseGenerator:
    """
    Shared mock TestCaseGenerator constructor
    """
    test_suite_specification = TestSuiteSpecification(
        id="example:json_sample_test_assets",
        test_data_file_locator=SAMPLE_TEST_ASSET_FILE,
        test_data_file_format=FileFormatEnum.JSON
    )
    test_suite = TestSuite(
        id="example:TestSuite",
        test_suite_specification=test_suite_specification
    )
    tests = TestCaseGenerator(
        test_suite=test_suite
    )
    return tests


class TestTestCaseGenerator(unittest.TestCase):
    """Testing Test Suite Factory functionality."""

    def test_factory_creation(self):
        """Test Suite Factory creation test."""
        create_test_case_generator()

    def test_case_generator_load(self):
        """Test Suite load test."""
        tests = create_test_case_generator()
        for test in tests.load():
            assert test
