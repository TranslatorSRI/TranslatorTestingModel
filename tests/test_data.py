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
model_example_data_files: Dict[str, str] = {
    model_class_name: glob.glob(os.path.join(DATA_DIR, f'*{model_class_name}*.yaml'))
    for model_class_name in model_classes
}


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_test_entity(self):
        """TestEntity test."""
        for path in model_example_data_files["TestEntity"]:
            obj = yaml_loader.load(path, target_class=TestEntity)
            assert obj

    def test_test_metadata(self):
        """TestMetadata test."""
        for path in model_example_data_files["TestMetadata"]:
            obj = yaml_loader.load(path, target_class=TestMetadata)
            assert obj

    def test_test_asset(self):
        """TestAsset test."""
        for path in model_example_data_files["TestAsset"]:
            obj = yaml_loader.load(path, target_class=TestAsset)
            assert obj

    def test_test_case(self):
        """TestCase test."""
        for path in model_example_data_files["TestCase"]:
            obj = yaml_loader.load(path, target_class=TestCase)
            assert obj

    def test_test_suite(self):
        """TestSuite test."""
        for path in model_example_data_files["TestSuite"]:
            obj = yaml_loader.load(path, target_class=TestSuite)
            assert obj
