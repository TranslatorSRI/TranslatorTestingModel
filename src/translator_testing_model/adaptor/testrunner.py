"""
This module provides a high level parent class interface/API
for Translator TestRunner implementations.
"""
from typing import Union, List, Optional, Dict
from datetime import datetime
from uuid import uuid4

from src.translator_testing_model.datamodel.pydanticmodel import (
    TestRunnerConfiguration,
    TestEntity,
    TestCase,
    TestCaseResult,
    TestCaseResultEnum,
    TestRunSession
)


class TestRunner:
    """
    Abstract Wrapper Class for "plug and play" TestRunner implementations for
    the Translator Testing Infrastructure. Complying with this specification
    facilitates uniform execution of TestRunners by the TestHarness.
    """

    def __init__(self, name: str, config: Optional[TestRunnerConfiguration]):
        """
        Constructor for an instance of TestRunner.

        :param name: str, Global system name of a TestRunner
        :param config: TestRunnerConfiguration, general run configuration parameters for a specified TestRunner
        """
        self._name = name
        self._config: Optional[TestRunnerConfiguration] = config

        # catalog of registered sessions of the test runner.
        self._sessions: Dict[
            str,            # session_id
            TestRunSession  # session object
        ] = dict()

    def get_name(self):
        return self._name

    def get_config(self) -> Optional[TestRunnerConfiguration]:
        return self._config

    def get_session(self, session_id: str) -> Optional[TestRunSession]:

        """
        Returns the TestRunner session corresponding to the given session identifier.

        :param session_id: valid session identifier of registered TestRunner session
        :return: Optional[TestRunSession],
                 session of a valid extant instance of TestRunner if known; None otherwise
        """
        return self._sessions[session_id] if session_id in self._sessions else None

    def run(self, tests: Union[TestEntity, List[TestEntity]]) -> TestRunSession:
        """
        Method to initiate TestRunner processing of the specified collection of tests,
        returning a session handle to manage the run and access test results.

        :param tests: Union[TestEntity, List[TestEntity]], may be any reasonable (TestRunner-specific) -
                      possibly a List of - instance(s) of test data entity but generally constrained to
                      be of a TestSuite, TestCase or TestAsset derived data type.

        :return: TestRunSession, data wrapper for an instance of TestRunner running the provided tests.
        """
        session = TestRunSession(
            id=f"ttm:{str(uuid4())}",
            name="TestRunnerSession",
            test_runner_name=self._name,
            description="Test Runner Session",
            timestamp=str(datetime.now()),
            tags=[],
            # test_entities=tests
            # test_case_results: Optional[Dict[str, TestCaseResult]] = Field(default_factory=dict, description="""One or more instances of TestCaseResult.""")
        )
        return session
