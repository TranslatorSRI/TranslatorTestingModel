"""Data test."""
import os
import glob
import unittest
from typing import List, Dict

from linkml_runtime.loaders import yaml_loader
from src.translator_testing_model.datamodel.translator_testing_model import (
    TestEntity,
    TestMetadata,
    TestAsset,
    TestCase,
    TestSuite
)


ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

model_classes: List[str] = ["TestEntity", "TestMetadata", "TestAsset", "TestCase", "TestSuite"]
good_model_example_data_files: Dict[str, str] = {
    model_class_name: glob.glob(os.path.join(DATA_DIR, f'Good-{model_class_name}-*.yaml'))
    for model_class_name in model_classes
}

bad_model_example_data_files: Dict[str, str] = {
    model_class_name: glob.glob(os.path.join(DATA_DIR, f'Bad-{model_class_name}-*.yaml'))
    for model_class_name in model_classes
}


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_good_test_entity(self):
        """Good TestEntity test."""
        for path in good_model_example_data_files["TestEntity"]:
            obj = yaml_loader.load(path, target_class=TestEntity)
            assert obj

    def test_bad_test_entity(self):
        """Bad TestEntity test."""
        for path in bad_model_example_data_files["TestEntity"]:
            with self.assertRaises(ValueError):
                yaml_loader.load(path, target_class=TestEntity)

    def test_good_test_metadata(self):
        """Good TestMetadata test."""
        for path in good_model_example_data_files["TestMetadata"]:
            obj = yaml_loader.load(path, target_class=TestMetadata)
            assert obj

    def test_bad_test_metadata(self):
        """Bad TestMetadata test."""
        for path in bad_model_example_data_files["TestMetadata"]:
            with self.assertRaises(ValueError):
                yaml_loader.load(path, target_class=TestMetadata)

    def test_good_test_asset(self):
        """Good TestAsset test."""
        for path in good_model_example_data_files["TestAsset"]:
            obj = yaml_loader.load(path, target_class=TestAsset)
            assert obj

    def test_bad_test_asset(self):
        """Bad TestAsset test."""
        for path in bad_model_example_data_files["TestAsset"]:
            with self.assertRaises(ValueError):
                yaml_loader.load(path, target_class=TestAsset)

    def test_good_test_case(self):
        """Good TestCase test."""
        for path in good_model_example_data_files["TestCase"]:
            obj = yaml_loader.load(path, target_class=TestCase)
            assert obj

    def test_bad_test_case(self):
        """Bad TestCase test."""
        for path in bad_model_example_data_files["TestCase"]:
            with self.assertRaises(ValueError):
                yaml_loader.load(path, target_class=TestCase)

    def test_good_test_suite(self):
        """Good TestSuite test."""
        for path in good_model_example_data_files["TestCase"]:
            obj = yaml_loader.load(path, target_class=TestCase)
            assert obj

    def test_bad_test_suite(self):
        """Bad TestSuite test."""
        for path in bad_model_example_data_files["TestCase"]:
            with self.assertRaises(ValueError):
                yaml_loader.load(path, target_class=TestCase)
