#!/usr/bin/env python3
"""
CLI Script to generate a TestSuite of TestCases from specified TestAssets
"""
from typing import List
from argparse import ArgumentParser
from urllib.parse import urlparse
from linkml_runtime.loaders import tsv_loader, json_loader, yaml_loader
from src.translator_testing_model.datamodel.translator_testing_model import (
    TestAsset,
    TestCase,
    TestSuite
)


def url_type(arg):
    url = urlparse(arg)
    if all((url.scheme, url.netloc)):
        return arg
    raise TypeError("Invalid URL")


def main(args):
    test_suite_id = args["test_suite_id"]
    test_suite_name = args["test_suite_name"]
    test_assets_url = args["test_assets_url"]
    test_assets_format = test_assets_url.split('.')[-1]
    test_suite_url = args["test_suite_url"]

    if test_assets_format == "tsv":
        test_assets: List[TestAsset] = tsv_loader.load(test_assets_url, target_class=TestAsset)
    elif test_assets_format == "json":
        test_assets: List[TestAsset] = json_loader.load(test_assets_url, target_class=TestAsset)
    elif test_assets_format == "yaml":
        test_assets: List[TestAsset] = yaml_loader.load(test_assets_url, target_class=TestAsset)
    else:
        raise RuntimeError(f"Unknown TestAsset file format: {test_assets_format}")


def cli():
    """Parse args and run tests."""
    parser = ArgumentParser(description="Translator Testing Test Suite Generator")

    parser.add_argument(
        "-i", "--test_suite_id",
        type=str,
        required=True,
        help="CURIE of Test Suite to create.",
    )

    parser.add_argument(
        "-n", "--test_suite_name",
        type=str,
        required=True,
        help="Human readable name of Test Suite to create.",
    )

    parser.add_argument(
        "-a", "--test_assets_url",
        type=url_type,
        required=True,
        help="Input source URL location of test assets file. " +
             "File format discerned from file extension " +
             "(One of 'tsv', 'json' or 'yaml' assumed).",
    )

    parser.add_argument(
        "-s", "--test_suite_url",
        type=url_type,
        default="https://github.com/NCATSTranslator/Tests",
        help="Target storage URL location of resulting Test Suite and related data" +
             " (Default: 'https://github.com/NCATSTranslator/Tests')",
    )

    # parser.add_argument(
    #     "--log_level",
    #     type=str,
    #     choices=["ERROR", "WARNING", "INFO", "DEBUG"],
    #     help="Level of the logs.",
    #     default="WARNING",
    # )

    args = parser.parse_args()

    main(vars(args))


if __name__ == "__main__":
    cli()

