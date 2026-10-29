"""Test that a TestAsset can name its expected output by several CURIEs."""
import unittest

from pydantic import ValidationError

from src.translator_testing_model.datamodel.pydanticmodel import TestAsset


class TestOutputIds(unittest.TestCase):
    """Testing the multivalued output_ids slot on the Pydantic model."""

    def test_several_output_ids(self):
        """Every CURIE given for the expected output is kept, in order."""
        asset = TestAsset(
            id="example:TestAsset002",
            output_ids=["PUBCHEM.COMPOUND:5284616", "CHEBI:9168"],
        )
        assert asset.output_ids == ["PUBCHEM.COMPOUND:5284616", "CHEBI:9168"]

    def test_output_ids_default_empty(self):
        """An asset with no expected output, eg a performance asset, has none."""
        assert TestAsset(id="example:TestAsset003").output_ids == []

    def test_bare_string_rejected(self):
        """A single CURIE must still be given as a list."""
        with self.assertRaises(ValidationError):
            TestAsset(id="example:TestAsset004", output_ids="CHEBI:9168")

    def test_old_output_id_rejected(self):
        """Data still using the old single-valued output_id fails loudly."""
        with self.assertRaises(ValidationError):
            TestAsset.model_validate(
                {"id": "example:TestAsset005", "output_id": "CHEBI:9168"}
            )
