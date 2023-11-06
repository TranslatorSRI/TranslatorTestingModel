"""
This module provides a high level parent class interface/API
for Translator TestRunner implementations.
"""
from src.translator_testing_model.adaptor.test_case_generator import (
    TestSuiteInputException,
    TestCaseGenerator
)
from src.translator_testing_model.datamodel.pydanticmodel import (
    TestEntity,
    TestMetadata,
    TestSuite,
    AcceptanceTestSuite,
    BenchmarkTestSuite,
    StandardsComplianceTestSuite,
    OneHopTestSuite,
    TestSuiteSpecification,
    FileFormatEnum
)


class TestResult:
    """
    Wrapper of a Translator TestRunner result
    TODO: this class *might* belong inside the TranslatorTestingModel?
    """
    pass


class TestRunner:
    """
    Abstract Wrapper Class for "plug and play" TestRunner implementations
    for the Translator Testing Infrastructure. Complying with this
    specification allows for easy execution of TestRunners by the TestHarness.
    """

    def __init__(self):
        pass

    def run(self, input: TestEntity) -> TestResult:
        pass
