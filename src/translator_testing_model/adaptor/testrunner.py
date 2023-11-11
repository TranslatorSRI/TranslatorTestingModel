"""
This module provides a high level parent class interface/API
for Translator TestRunner implementations.
"""
from typing import Union, List, Optional, Dict, Iterator
from datetime import datetime
from uuid import uuid4

from translator_testing_model.datamodel.pydanticmodel import (
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

    def __init__(self,config: Optional[TestRunnerConfiguration]):
        """
        Constructor for an instance of TestRunner.
        :param config: TestRunnerConfiguration, general run configuration parameters for a specified TestRunner
        """
        self._config: Dict[str, str] = dict()
        if config:
            for parameter in config.test_run_parameters:
                self._config[parameter.parameter_name] = parameter.parameter_value
        self._name = self._config.pop("name") if "name" in self._config else "Unknown"

        # catalog of registered sessions of the test runner.
        self._sessions: Dict[
            str,            # session_id
            TestRunSession  # session object
        ] = dict()

    def get_name(self):
        return self._name

    def get_config(self) -> Dict[str, str]:
        return self._config

    def get_session(self, session_id: str) -> Optional[TestRunSession]:

        """
        Returns the TestRunner session corresponding to the given session identifier.

        :param session_id: valid session identifier of registered TestRunner session
        :return: Optional[TestRunSession],
                 session of a valid extant instance of TestRunner if known; None otherwise
        """
        return self._sessions[session_id] if session_id in self._sessions else None

    @staticmethod
    def is_data_type(instance, name: str) -> bool:
        return str(type(instance)).endswith(f"{name}'>")

    def run(self, tests: Iterator[TestCase]) -> TestRunSession:
        """
        Method to initiate TestRunner processing of the specified collection of tests,
        returning a session handle to manage the run and access test results.

        :param tests: Union[TestEntity, List[TestEntity]], may be any reasonable (TestRunner-specific) -
                      possibly a List of - instance(s) of test data entity but generally constrained to
                      be of a TestSuite, TestCase or TestAsset derived data type.

        :return: TestRunSession, data wrapper for an instance of TestRunner running the provided tests.
        """
        # First iteration: blind loading of tests into dictionary of 'test_entities'
        test_entities: Optional[Dict[str, TestEntity]] = dict()
        if isinstance(tests, List):
            for test in tests:
                # TODO: how do I ensure that 'tests' is a valid TestEntity here?
                test_entities[test.id] = test
        else:
            # TODO: how do I ensure that 'tests' is a valid TestEntity here?
            test_entities[tests.id] = tests

        # ...then configure and persist the TestRunner session...
        session_id = f"ttm:{str(uuid4())}"
        session = TestRunSession(
            id=session_id,
            name="TestRunnerSession",
            test_runner_name=self.get_name(),
            description="Test Runner Session",
            timestamp=str(datetime.now()),
            tags=[],
            test_entities=test_entities
            # Default initialization of empty dictionary of test_case_results
            # test_case_results: Optional[Dict[str, TestCaseResult]] = dict()
        )
        self._sessions[session_id] = session

        return session

    def get_results(self, session: TestRunSession) -> Dict[str, TestCaseResult]:
        """
        Return test results.
        TODO: may (eventually) need to be asynchronous?

        :param session: TestRunSession within which the tests are being run.
        :return: Dict[str, TestCaseResult], indexed dictionary of test case results
        """
        return dict()
