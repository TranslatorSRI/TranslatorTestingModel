from sys import stderr
import unittest
from typing import Dict

from translator_testing_model.adaptor.testrunner import TestRunner
from translator_testing_model.datamodel.pydanticmodel import (
    TestRunnerConfiguration,
    TestEntityParameter, TestEntity, TestRunSession
)


def _mock_config():
    test_parameter_1 = TestEntityParameter(
        parameter_name="name",
        parameter_value="MockTestRunner"
    )
    test_parameter_2 = TestEntityParameter(
        parameter_name="some_other_parameters",
        parameter_value="42"
    )
    trc = TestRunnerConfiguration(
        id="mock testrunner configuration",
        test_run_parameters=[test_parameter_1, test_parameter_2],
        tags=["MockTestRunner"]
    )
    return trc


def _test_config(trc: TestRunnerConfiguration):
    assert trc
    assert trc.id == "mock testrunner configuration"
    assert trc.test_run_parameters
    for parameter in trc.test_run_parameters:
        assert parameter.parameter_name == "name"
        assert parameter.parameter_value == "MockTestRunner"
    assert "MockTestRunner" in trc.tags


def _mock_test_data() -> TestEntity:
    return TestEntity(id="mock_entity")


class TestTestRunner(unittest.TestCase):
    """Testing Translator TestRunner library."""

    def test_testrunner_config_construction(self):
        trc: TestRunnerConfiguration = _mock_config()
        assert trc
        assert trc.id == "mock testrunner configuration"
        assert trc.test_run_parameters
        for parameter in trc.test_run_parameters:
            assert parameter.parameter_name in ["name", "some_other_parameters"]
            if parameter.parameter_name == "name":
                assert parameter.parameter_value == "MockTestRunner"
            else:
                assert parameter.parameter_value == "42"
        assert "MockTestRunner" in trc.tags

    def test_testrunner_construction_with_get_config_and_empty_session(self):
        trc: TestRunnerConfiguration = _mock_config()
        runner = TestRunner(config=trc)
        assert runner.get_name() == "MockTestRunner"
        config: Dict = runner.get_config()
        assert config["some_other_parameters"] == "42"

    def test_testrunner_run_and_get_session(self):
        trc: TestRunnerConfiguration = _mock_config()
        runner = TestRunner(config=trc)

        # Simple TestEntity as test input
        trs: TestRunSession = runner.run(tests=TestEntity(id="mock_entity"))
        assert trs.id
        assert runner.get_session(trs.id) is not None
        print(file=stderr)
        print(trs.json(indent="\t"), file=stderr)

        # List[TestEntity] as test input
        trs = runner.run(tests=[TestEntity(id="mock_entity-1"), TestEntity(id="mock_entity-2")])
        print(file=stderr)
        print(trs.json(indent="\t"), file=stderr)
