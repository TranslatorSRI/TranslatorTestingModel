"""
Unit tests for (TranslatorTestingModel-driven) TestHarness components
"""
import unittest
from translator_testing_model.adaptor.test_harness_too import url_type


class TestTestHarness(unittest.TestCase):
    """Testing Translator TestHarness module."""

    def test_valid_url_type(self):
        """Test for valid URL"""
        assert url_type("https://github.com")

    def test_invalid_url_type(self):
        """Test for invalid URL"""
        with self.assertRaises(TypeError):
            url_type("not-a-url")

    def test_load_testrunners(self):
        """Test loading of test runners from retrieved test runner configurations"""
        raise NotImplementedError

