"""
Accessor to tests documented in the Tests repository.
"""
from typing import Iterator, Dict, List
from translator_testing_model.datamodel.pydanticmodel import TestCase


def access_tests(test_specs: Dict, logger) -> Iterator[TestCase]:
    """
    Access a stream of TestCase instances for processing.

    :param test_specs: Dict of parameters locating tests
    :param logger: Logger instance for error messages
    :return: Iterator[TestCase]
    """
    # TODO: elaborate this stub tests accessor
    tests: List[TestCase] = list()
    if "tests_url" in test_specs:
        suite = test_specs["suite"]
        tests_url = test_specs["tests_url"]
    elif "tests" in test_specs:
        tests = test_specs["tests"]
    else:
        logger.error("Available tests unspecified.")
        raise StopIteration

    for testcase in tests:
        yield testcase
