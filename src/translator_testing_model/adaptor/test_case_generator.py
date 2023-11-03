"""
This module provides a 'facade' layer to access (Pydantic 1) TestSuites
and their corresponding TestCase entries, in a source-agnostic manner.
"""
from typing import Optional, Generator
from src.translator_testing_model.datamodel.pydanticmodel import (
    TestMetadata,
    TestSuite,
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

    def load(self) -> Generator:
        pass
