"""
This module provides a high level parent class interface/API
for Translator TestRunner implementations.
"""
from typing import Union, List
from datetime import datetime

from src.translator_testing_model.datamodel.pydanticmodel import (
    TestEntity,
    TestCase,
    TestCaseResult,
    TestCaseResultEnum
)


class TestResults:
    """
    Wrapper of a Translator TestRunner result
    """

    def __init__(self, test_id: str):
        """
        TestResult constructor
        """
        self.id = test_id
        self.test_case_results: List[TestCaseResult] = list()

    def add_test_case_result(self, test_case: TestCase, test_case_result: TestCaseResultEnum):
        self.test_case_results.append(
            TestCaseResult(
                test_suite_id=self.id,
                test_case=test_case,
                test_case_result=test_case_result,
                timestamp=datetime.now()
            )
        )

    def get_test_case_results(self) -> List[TestCaseResult]:
        return self.test_case_results


class TestRunner:
    """
    Abstract Wrapper Class for "plug and play" TestRunner implementations
    for the Translator Testing Infrastructure. Complying with this
    specification allows for easy execution of TestRunners by the TestHarness.
    """

    def __init__(self, *args, **kwargs):
        """
        TestRunner constructor
        """
        raise NotImplementedError

    def run(self, tests: Union[TestEntity, List[TestEntity]]) -> TestResults:
        """

        :param tests: Union[TestEntity, List[TestEntity]], may be any reasonable (TestRunner-specific) -
                      possibly a List of - instance(s) of test data entity but generally constrained to
                      be of a TestSuite, TestCase or TestAsset derived data type.
        :return: TestResults, data wrapper for (full) reporting of the (TestSuite of) TestCase result(s).
        """
        raise NotImplementedError
