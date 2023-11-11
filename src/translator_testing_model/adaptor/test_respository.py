"""
Access methods to tests documented in the Tests repository.
"""
from typing import Iterator, Union, List, Dict
from pathlib import Path
from logging import Logger
from translator_testing_model.datamodel.pydanticmodel import TestCase


def access_tests(kwargs: Dict, logger) -> Iterator[TestCase]:
    tests = []
    if "tests_url" in kwargs:
        tests = access_tests(kwargs["suite"], kwargs["tests_url"], logger)
    elif "tests" in kwargs:
        tests = kwargs["tests"]
    else:
        return logger.error(
            "Please run this command with `-h` to see the available options."
        )
