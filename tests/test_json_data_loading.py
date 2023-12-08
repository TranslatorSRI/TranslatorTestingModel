"""Data test."""
import os
import glob
import unittest
from typing import List, Dict

from linkml_runtime.loaders import json_loader
from src.translator_testing_model.datamodel.translator_testing_model import (
    TestEntity,
    TestMetadata,
    TestAsset,
    AcceptanceTestAsset,
    TestCase,
    AcceptanceTestCase,
    TestSuite
)


ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

model_classes: List[str] = [
    "TestEntity",
    "TestMetadata",
    "TestAsset",
    "AcceptanceTestAsset",
    "TestCase",
    "AcceptanceTestCase",
    "TestSuite"
]
good_model_example_data_files: Dict[str, str] = {
    model_class_name: glob.glob(os.path.join(DATA_DIR, f'Good-{model_class_name}-*.json'))
    for model_class_name in model_classes
}

bad_model_example_data_files: Dict[str, str] = {
    model_class_name: glob.glob(os.path.join(DATA_DIR, f'Bad-{model_class_name}-*.json'))
    for model_class_name in model_classes
}


class TestData(unittest.TestCase):
    """Testing sample JSON data and TranslatorTestingModel schema."""

    def test_good_test_entity(self):
        """Good TestEntity test."""
        for path in good_model_example_data_files["TestEntity"]:
            obj = json_loader.load(path, target_class=TestEntity)
            assert obj

    def test_bad_test_entity(self):
        """Bad TestEntity test."""
        for path in bad_model_example_data_files["TestEntity"]:
            with self.assertRaises(ValueError):
                json_loader.load(path, target_class=TestEntity)

    def test_good_test_metadata(self):
        """Good TestMetadata test."""
        for path in good_model_example_data_files["TestMetadata"]:
            obj = json_loader.load(path, target_class=TestMetadata)
            assert obj

    def test_bad_test_metadata(self):
        """Bad TestMetadata test."""
        for path in bad_model_example_data_files["TestMetadata"]:
            print(path)
            with self.assertRaises(ValueError):
                json_loader.load(path, target_class=TestMetadata)

    def test_good_test_asset(self):
        """Good TestAsset test."""
        for path in good_model_example_data_files["TestAsset"]:
            print(path)
            obj = json_loader.load(path, target_class=TestAsset)
            assert obj

    def test_bad_test_asset(self):
        """Bad TestAsset test."""
        for path in bad_model_example_data_files["TestAsset"]:
            print(path)
            with self.assertRaises(ValueError):
                json_loader.load(path, target_class=TestAsset)

    def test_good_acceptance_test_asset(self):
        """Good TestAsset test."""
        for path in good_model_example_data_files["AcceptanceTestAsset"]:
            obj = json_loader.load(path, target_class=AcceptanceTestAsset)
            assert obj

    def test_bad_acceptance_test_asset(self):
        """Bad AcceptanceTestAsset test."""
        for path in bad_model_example_data_files["AcceptanceTestAsset"]:
            print(path)
            with self.assertRaises(ValueError):
                json_loader.load(path, target_class=AcceptanceTestAsset)

    def test_good_test_case(self):
        """Good TestCase test."""
        for path in good_model_example_data_files["TestCase"]:
            print(path)
            obj = json_loader.load(path, target_class=TestCase)
            assert obj

    def test_bad_test_case(self):
        """Bad TestCase test."""
        for path in bad_model_example_data_files["TestCase"]:
            print(path)
            with self.assertRaises(ValueError):
                json_loader.load(path, target_class=TestCase)

    def test_good_acceptance_test_case(self):
        """Good AcceptanceTestCase test."""
        for path in good_model_example_data_files["AcceptanceTestCase"]:
            print(path)
            obj = json_loader.load(path, target_class=AcceptanceTestCase)
            assert obj

    def test_bad_acceptance_test_case(self):
        """Bad AcceptanceTestCase test."""
        for path in bad_model_example_data_files["AcceptanceTestCase"]:
            with self.assertRaises(ValueError):
                json_loader.load(path, target_class=AcceptanceTestCase)

    def test_good_test_suite(self):
        """Good TestSuite test."""
        for path in good_model_example_data_files["TestSuite"]:
            obj = json_loader.load(path, target_class=TestSuite)
            assert obj

    def test_bad_test_suite(self):
        """Bad TestSuite test."""
        for path in bad_model_example_data_files["TestSuite"]:
            with self.assertRaises(ValueError):
                json_loader.load(path, target_class=TestSuite)
