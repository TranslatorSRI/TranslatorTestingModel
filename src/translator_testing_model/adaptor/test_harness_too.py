#!/usr/bin/env python3
"""
2nd generation implementation of the
Translator SRI Automated Test Harness using the
TestRunner class and TranslatorTestingModel.
"""
from argparse import ArgumentParser
from typing import Iterator, Dict
from urllib.parse import urlparse
import json

from translator_testing_model.adaptor.testrunner import TestRunner
from translator_testing_model.adaptor.test_respository import access_tests
from translator_testing_model.datamodel.pydanticmodel import (
    TestRunnerConfiguration,
    TestRunSession,
    TestEntity,
    TestCase
)

from logging import Logger, getLogger

logger: Logger = getLogger()


def url_type(candidate_url: str):
    url = urlparse(candidate_url)
    if all((url.scheme, url.netloc)):
        return url
    raise TypeError("Invalid URL")


def load_testrunners(args: Dict) -> Dict[str, TestRunner]:
    """
    Load the catalog of available instances of configured TestRunner.
    :param args: Dict, parameters pertinent to the selection of TestRunner configurations
    :return: Dict[str, TestRunnerConfiguration], catalog of available TestRunners, indexed by name
    """
    # TODO: stub... need to retrieve the TestRunner configurations from somewhere
    tr_config: Dict = dict()
    runners: Dict[str, TestRunner] = dict()
    for name, config in tr_config.items():
        runners[name] = TestRunner(config=config)
    return runners


def main(args: Dict):
    """Main Test Harness entrypoint."""

    # Load catalog of specified configured instances of TestRunner
    testrunner_catalog: Dict[str, TestRunner] = load_testrunners(args)

    # Access TestCase data (as a 'just-in-time' Iterator)
    tests: Iterator[TestCase] = access_tests(args, logger=logger)

    # sessions: Dict[str, TestRunSession] = dict()
    # for name in runners.keys():
    #     sessions[name] = runners[name].run(tests=tests)
    #
    # if kwargs["save_to_dashboard"]:
    #     logger.info("Saving to Testing Dashboard...")
    #     raise NotImplementedError()
    #
    # if kwargs["json_output"]:
    #     logger.info("Saving report as JSON...")
    #     for name in sessions.keys():
    #         with open(f"{name}_test_report.json", "w") as f:
    #             json.dump(sessions[name].test_case_results, f)

    logger.info("All testing has completed!")


def cli():
    """Parse args and run tests."""
    parser = ArgumentParser(description="Translator SRI Automated Test Harness")

    subparsers = parser.add_subparsers()

    download_parser = subparsers.add_parser(
        "download",
        help="Download tests to run from a URL",
    )

    download_parser.add_argument(
        "suite",
        type=str,
        help="The name/id of the suite(s) to run. Once tests have been downloaded, the test cases in this suite(s) will be run.",
    )

    download_parser.add_argument(
        "--tests_url",
        type=url_type,
        default="https://github.com/NCATSTranslator/Tests/archive/refs/heads/main.zip",
        help="URL to download in order to find the test files",
    )

    run_parser = subparsers.add_parser("run", help="Run a given set of tests")

    run_parser.add_argument(
        "tests",
        type=json.loads,
        help="Path to a file of tests to be run. This would be the same output from retrieving a test generator via `access_tests()`",
    )

    parser.add_argument(
        "--save_to_dashboard",
        action="store_true",
        help="Have the Test Harness send the test results to the Testing Dashboard",
    )

    parser.add_argument(
        "--json_output",
        action="store_true",
        help="Save the test results locally in json",
    )

    parser.add_argument(
        "--log_level",
        type=str,
        choices=["ERROR", "WARNING", "INFO", "DEBUG"],
        help="Level of the logs.",
        default="WARNING",
    )

    args = parser.parse_args()
    main(vars(args))


if __name__ == "__main__":
    cli()
