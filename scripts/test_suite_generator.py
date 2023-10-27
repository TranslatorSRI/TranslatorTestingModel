#!/usr/bin/env python3
"""
CLI Script to generate a TestSuite of TestCases from specified TestAssets
"""
from argparse import ArgumentParser
import json
from urllib.parse import urlparse


def url_type(arg):
    url = urlparse(arg)
    if all((url.scheme, url.netloc)):
        return arg
    raise TypeError("Invalid URL")


def main(args):
    test_suite_id = args["test_suite_id"]
    test_suite_name = args["test_suite_name"]
    test_assets_url = args["test_assets_url"]
    test_assets_format = args["test_assets_format"]
    test_suite_url = args["test_suite_url"]


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
        help="Input source URL location of test assets.",
    )

    parser.add_argument(
        "-f", "--test_assets_format",
        type=str,
        choices=["tsv", "json", "yaml"],
        default="tsv",
        help="File format of test assets (Default: 'tsv').",
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

