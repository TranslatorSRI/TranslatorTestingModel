"""
Unit Tests for TestSuiteFactory functionality
"""
import unittest
from unittest import skip

from src.translator_testing_model.adaptor.test_case_generator import (
    TestSuiteInputException,
    TestCaseGenerator
)
from src.translator_testing_model.datamodel.pydanticmodel import (
    TestMetadata,
    TestSuite,
    AcceptanceTestSuite,
    BenchmarkTestSuite,
    StandardsComplianceTestSuite,
    OneHopTestSuite,
    TestSuiteSpecification,
    FileFormatEnum
)


# temporary hack access to some TestAsset data online
SAMPLE_TEST_ASSET_FILE = "https://raw.githubusercontent.com/TranslatorSRI/TranslatorTestingModel/" +\
                         "main/src/data/examples/SampleTestAssetList.json"


class TestCaseGeneratorWrapper:
    
    def __init__(self, target_test_suite_class=TestSuite):
        """
        TestCaseGeneratorWrapper constructor
        """
        self.target_test_suite_class = target_test_suite_class
        self.test_suite_specification = TestSuiteSpecification(
            id="example:json_sample_test_assets",
            test_data_file_locator=SAMPLE_TEST_ASSET_FILE,
            test_data_file_format=FileFormatEnum.JSON
        )
        self.test_suite = self.target_test_suite_class(
            id=f"example:{target_test_suite_class.__class__.__name__}",
            test_suite_specification=self.test_suite_specification
        )
    
    def create_test_case_generator(self) -> TestCaseGenerator:
        """
        TestCaseGenerator factory
        """
        tests = TestCaseGenerator(
            test_suite=self.test_suite
        )
        return tests


class TestTestCaseGenerator(unittest.TestCase):
    """Testing Test Case Generator functionality."""

    @skip("Not implemented yet")
    def test_default_generator_wrapper(self):
        """Test Suite Generator creation test."""
        test_suite_wrapper = TestCaseGeneratorWrapper()
        test_suite_wrapper.create_test_case_generator()
        isinstance(test_suite_wrapper.target_test_suite_class, TestSuite)

    @skip("Not implemented yet")
    def test_acceptance_test_case_generator_wrapper(self):
        """Acceptance Test Suite Wrapper creation test."""
        test_suite_wrapper = TestCaseGeneratorWrapper(target_test_suite_class=AcceptanceTestSuite)
        test_suite_wrapper.create_test_case_generator()
        isinstance(test_suite_wrapper.target_test_suite_class, AcceptanceTestSuite)

    @skip("Not implemented yet")
    def test_generator_creation(self):
        """Test Case Generator creation test."""
        test_suite_wrapper = TestCaseGeneratorWrapper()
        print(test_suite_wrapper.test_suite_specification.name)
        tests = test_suite_wrapper.create_test_case_generator()
        isinstance(tests, TestCaseGenerator)

    @skip("Not implemented yet")
    def test_case_generator_load(self):
        """Test Case Generator load test."""
        test_suite_wrapper = TestCaseGeneratorWrapper()
        tests = test_suite_wrapper.create_test_case_generator()
        print(tests.load())
        for test in tests.load():
            assert test
