"""
This module provides a 'facade' layer to access (Pydantic 1) TestSuites
and their corresponding TestCase entries, in a source-agnostic manner.
"""
from typing import Optional, Generator
from src.translator_testing_model.datamodel.pydanticmodel import (
    TestMetadata,
    TestSuite,
    AcceptanceTestSuite,
    BenchmarkTestSuite,
    StandardsComplianceTestSuite,
    OneHopTestSuite,
    TestSuiteSpecification
)


class TestSuiteInputException(RuntimeError):
    pass


class TestCaseGenerator:

    def __init__(
            self,
            test_suite: TestSuite,
            test_metadata: Optional[TestMetadata] = None
    ):
        self.test_suite = test_suite
        self.metadata = test_metadata
        self.bind_test_suite()

    def bind_test_suite(self):
        """
        Perform TestSuite (child-class-specific) input configuration here
        """
        if isinstance(self.test_suite, TestSuite):
            pass
        elif isinstance(self.test_suite, AcceptanceTestSuite):
            pass
        elif isinstance(self.test_suite, BenchmarkTestSuite):
            pass
        elif isinstance(self.test_suite, StandardsComplianceTestSuite):
            pass
        elif isinstance(self.test_suite, OneHopTestSuite):
            pass

    def load(self) -> Generator:
        pass

