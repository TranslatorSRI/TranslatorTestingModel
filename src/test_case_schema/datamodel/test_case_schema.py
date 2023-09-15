# Auto generated from test_case_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-09-15T11:16:49
# Schema: test-case-schema
#
# id: https://w3id.org/TranslatorSRI/test-case-schema
# description: This is the project description.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Curie, Date, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Curie, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
TEST_CASE_SCHEMA = CurieNamespace('test_case_schema', 'https://w3id.org/TranslatorSRI/test-case-schema/')
DEFAULT_ = TEST_CASE_SCHEMA


# Types

# Class references
class TestCaseId(URIorCURIE):
    pass


class SemanticSmokeTestCaseId(TestCaseId):
    pass


@dataclass
class TestCase(YAMLRoot):
    """
    Represents a TestCase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestCase
    class_class_curie: ClassVar[str] = "test_case_schema:TestCase"
    class_name: ClassVar[str] = "TestCase"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestCase

    id: Union[str, TestCaseId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    inputs: Optional[Union[Union[dict, "Input"], List[Union[dict, "Input"]]]] = empty_list()
    outputs: Optional[Union[Union[dict, "Output"], List[Union[dict, "Output"]]]] = empty_list()
    preconditions: Optional[Union[Union[dict, "Precondition"], List[Union[dict, "Precondition"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TestCaseId):
            self.id = TestCaseId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.inputs, list):
            self.inputs = [self.inputs] if self.inputs is not None else []
        self.inputs = [v if isinstance(v, Input) else Input(**as_dict(v)) for v in self.inputs]

        if not isinstance(self.outputs, list):
            self.outputs = [self.outputs] if self.outputs is not None else []
        self.outputs = [v if isinstance(v, Output) else Output(**as_dict(v)) for v in self.outputs]

        if not isinstance(self.preconditions, list):
            self.preconditions = [self.preconditions] if self.preconditions is not None else []
        self.preconditions = [v if isinstance(v, Precondition) else Precondition(**as_dict(v)) for v in self.preconditions]

        super().__post_init__(**kwargs)


@dataclass
class SemanticSmokeTestCase(TestCase):
    """
    Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.SemanticSmokeTestCase
    class_class_curie: ClassVar[str] = "test_case_schema:SemanticSmokeTestCase"
    class_name: ClassVar[str] = "SemanticSmokeTestCase"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.SemanticSmokeTestCase

    id: Union[str, SemanticSmokeTestCaseId] = None
    inputs: Union[Union[dict, "SemanticSmokeTestInput"], List[Union[dict, "SemanticSmokeTestInput"]]] = None
    outputs: Union[Union[dict, "SemanticSmokeTestOutput"], List[Union[dict, "SemanticSmokeTestOutput"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SemanticSmokeTestCaseId):
            self.id = SemanticSmokeTestCaseId(self.id)

        if self._is_empty(self.inputs):
            self.MissingRequiredField("inputs")
        if not isinstance(self.inputs, list):
            self.inputs = [self.inputs] if self.inputs is not None else []
        self.inputs = [v if isinstance(v, SemanticSmokeTestInput) else SemanticSmokeTestInput(**as_dict(v)) for v in self.inputs]

        if self._is_empty(self.outputs):
            self.MissingRequiredField("outputs")
        if not isinstance(self.outputs, list):
            self.outputs = [self.outputs] if self.outputs is not None else []
        self.outputs = [v if isinstance(v, SemanticSmokeTestOutput) else SemanticSmokeTestOutput(**as_dict(v)) for v in self.outputs]

        super().__post_init__(**kwargs)


class Input(YAMLRoot):
    """
    Represents an input to a TestCase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.Input
    class_class_curie: ClassVar[str] = "test_case_schema:Input"
    class_name: ClassVar[str] = "Input"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.Input


@dataclass
class SemanticSmokeTestInput(Input):
    """
    Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.SemanticSmokeTestInput
    class_class_curie: ClassVar[str] = "test_case_schema:SemanticSmokeTestInput"
    class_name: ClassVar[str] = "SemanticSmokeTestInput"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.SemanticSmokeTestInput

    must_pass_date: Optional[Union[str, XSDDate]] = None
    must_pass_environment: Optional[Union[str, "EnvironmentEnum"]] = None
    query: Optional[str] = None
    string_entry: Optional[str] = None
    direction: Optional[Union[str, "DirectionEnum"]] = None
    answer_informal_concept: Optional[str] = None
    expected_result: Optional[Union[str, "ExpectedResultsEnum"]] = None
    curie: Optional[Union[str, Curie]] = None
    top_level: Optional[str] = None
    node: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.must_pass_date is not None and not isinstance(self.must_pass_date, XSDDate):
            self.must_pass_date = XSDDate(self.must_pass_date)

        if self.must_pass_environment is not None and not isinstance(self.must_pass_environment, EnvironmentEnum):
            self.must_pass_environment = EnvironmentEnum(self.must_pass_environment)

        if self.query is not None and not isinstance(self.query, str):
            self.query = str(self.query)

        if self.string_entry is not None and not isinstance(self.string_entry, str):
            self.string_entry = str(self.string_entry)

        if self.direction is not None and not isinstance(self.direction, DirectionEnum):
            self.direction = DirectionEnum(self.direction)

        if self.answer_informal_concept is not None and not isinstance(self.answer_informal_concept, str):
            self.answer_informal_concept = str(self.answer_informal_concept)

        if self.expected_result is not None and not isinstance(self.expected_result, ExpectedResultsEnum):
            self.expected_result = ExpectedResultsEnum(self.expected_result)

        if self.curie is not None and not isinstance(self.curie, Curie):
            self.curie = Curie(self.curie)

        if self.top_level is not None and not isinstance(self.top_level, str):
            self.top_level = str(self.top_level)

        if self.node is not None and not isinstance(self.node, str):
            self.node = str(self.node)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


class Output(YAMLRoot):
    """
    Represents an output from a TestCase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.Output
    class_class_curie: ClassVar[str] = "test_case_schema:Output"
    class_name: ClassVar[str] = "Output"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.Output


class SemanticSmokeTestOutput(Output):
    """
    Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.SemanticSmokeTestOutput
    class_class_curie: ClassVar[str] = "test_case_schema:SemanticSmokeTestOutput"
    class_name: ClassVar[str] = "SemanticSmokeTestOutput"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.SemanticSmokeTestOutput


class Precondition(YAMLRoot):
    """
    Represents a precondition for a TestCase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.Precondition
    class_class_curie: ClassVar[str] = "test_case_schema:Precondition"
    class_name: ClassVar[str] = "Precondition"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.Precondition


@dataclass
class TestSuite(YAMLRoot):
    """
    A holder for TestCase objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestSuite
    class_class_curie: ClassVar[str] = "test_case_schema:TestSuite"
    class_name: ClassVar[str] = "TestSuite"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestSuite

    entries: Optional[Union[Dict[Union[str, TestCaseId], Union[dict, TestCase]], List[Union[dict, TestCase]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=TestCase, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class ExpectedResultsEnum(EnumDefinitionImpl):

    include_good = PermissibleValue(
        text="include_good",
        description="The query should return the result in this test case")
    exclude_bad = PermissibleValue(
        text="exclude_bad",
        description="The query should not return the result in this test case")

    _defn = EnumDefinition(
        name="ExpectedResultsEnum",
    )

class DirectionEnum(EnumDefinitionImpl):

    increased = PermissibleValue(text="increased")
    decreased = PermissibleValue(text="decreased")

    _defn = EnumDefinition(
        name="DirectionEnum",
    )

class EnvironmentEnum(EnumDefinitionImpl):

    DEV = PermissibleValue(text="DEV")
    CI = PermissibleValue(text="CI")
    TEST = PermissibleValue(text="TEST")
    PROD = PermissibleValue(text="PROD")

    _defn = EnumDefinition(
        name="EnvironmentEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=TEST_CASE_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=TEST_CASE_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=TEST_CASE_SCHEMA.description, domain=None, range=Optional[str])

slots.must_pass_date = Slot(uri=TEST_CASE_SCHEMA.must_pass_date, name="must_pass_date", curie=TEST_CASE_SCHEMA.curie('must_pass_date'),
                   model_uri=TEST_CASE_SCHEMA.must_pass_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.must_pass_environment = Slot(uri=TEST_CASE_SCHEMA.must_pass_environment, name="must_pass_environment", curie=TEST_CASE_SCHEMA.curie('must_pass_environment'),
                   model_uri=TEST_CASE_SCHEMA.must_pass_environment, domain=None, range=Optional[Union[str, "EnvironmentEnum"]])

slots.query = Slot(uri=TEST_CASE_SCHEMA.query, name="query", curie=TEST_CASE_SCHEMA.curie('query'),
                   model_uri=TEST_CASE_SCHEMA.query, domain=None, range=Optional[str])

slots.string_entry = Slot(uri=TEST_CASE_SCHEMA.string_entry, name="string_entry", curie=TEST_CASE_SCHEMA.curie('string_entry'),
                   model_uri=TEST_CASE_SCHEMA.string_entry, domain=None, range=Optional[str])

slots.direction = Slot(uri=TEST_CASE_SCHEMA.direction, name="direction", curie=TEST_CASE_SCHEMA.curie('direction'),
                   model_uri=TEST_CASE_SCHEMA.direction, domain=None, range=Optional[Union[str, "DirectionEnum"]])

slots.answer_informal_concept = Slot(uri=TEST_CASE_SCHEMA.answer_informal_concept, name="answer_informal_concept", curie=TEST_CASE_SCHEMA.curie('answer_informal_concept'),
                   model_uri=TEST_CASE_SCHEMA.answer_informal_concept, domain=None, range=Optional[str])

slots.expected_result = Slot(uri=TEST_CASE_SCHEMA.expected_result, name="expected_result", curie=TEST_CASE_SCHEMA.curie('expected_result'),
                   model_uri=TEST_CASE_SCHEMA.expected_result, domain=None, range=Optional[Union[str, "ExpectedResultsEnum"]])

slots.curie = Slot(uri=TEST_CASE_SCHEMA.curie, name="curie", curie=TEST_CASE_SCHEMA.curie('curie'),
                   model_uri=TEST_CASE_SCHEMA.curie, domain=None, range=Optional[Union[str, Curie]])

slots.top_level = Slot(uri=TEST_CASE_SCHEMA.top_level, name="top_level", curie=TEST_CASE_SCHEMA.curie('top_level'),
                   model_uri=TEST_CASE_SCHEMA.top_level, domain=None, range=Optional[str])

slots.node = Slot(uri=TEST_CASE_SCHEMA.node, name="node", curie=TEST_CASE_SCHEMA.curie('node'),
                   model_uri=TEST_CASE_SCHEMA.node, domain=None, range=Optional[str])

slots.notes = Slot(uri=TEST_CASE_SCHEMA.notes, name="notes", curie=TEST_CASE_SCHEMA.curie('notes'),
                   model_uri=TEST_CASE_SCHEMA.notes, domain=None, range=Optional[str])

slots.requires_trapi = Slot(uri=TEST_CASE_SCHEMA.requires_trapi, name="requires_trapi", curie=TEST_CASE_SCHEMA.curie('requires_trapi'),
                   model_uri=TEST_CASE_SCHEMA.requires_trapi, domain=None, range=Optional[Union[bool, Bool]])

slots.inputs = Slot(uri=TEST_CASE_SCHEMA.inputs, name="inputs", curie=TEST_CASE_SCHEMA.curie('inputs'),
                   model_uri=TEST_CASE_SCHEMA.inputs, domain=None, range=Optional[Union[Union[dict, Input], List[Union[dict, Input]]]])

slots.outputs = Slot(uri=TEST_CASE_SCHEMA.outputs, name="outputs", curie=TEST_CASE_SCHEMA.curie('outputs'),
                   model_uri=TEST_CASE_SCHEMA.outputs, domain=None, range=Optional[Union[Union[dict, Output], List[Union[dict, Output]]]])

slots.preconditions = Slot(uri=TEST_CASE_SCHEMA.preconditions, name="preconditions", curie=TEST_CASE_SCHEMA.curie('preconditions'),
                   model_uri=TEST_CASE_SCHEMA.preconditions, domain=None, range=Optional[Union[Union[dict, Precondition], List[Union[dict, Precondition]]]])

slots.testSuite__entries = Slot(uri=TEST_CASE_SCHEMA.entries, name="testSuite__entries", curie=TEST_CASE_SCHEMA.curie('entries'),
                   model_uri=TEST_CASE_SCHEMA.testSuite__entries, domain=None, range=Optional[Union[Dict[Union[str, TestCaseId], Union[dict, TestCase]], List[Union[dict, TestCase]]]])

slots.SemanticSmokeTestCase_inputs = Slot(uri=TEST_CASE_SCHEMA.inputs, name="SemanticSmokeTestCase_inputs", curie=TEST_CASE_SCHEMA.curie('inputs'),
                   model_uri=TEST_CASE_SCHEMA.SemanticSmokeTestCase_inputs, domain=SemanticSmokeTestCase, range=Union[Union[dict, "SemanticSmokeTestInput"], List[Union[dict, "SemanticSmokeTestInput"]]])

slots.SemanticSmokeTestCase_outputs = Slot(uri=TEST_CASE_SCHEMA.outputs, name="SemanticSmokeTestCase_outputs", curie=TEST_CASE_SCHEMA.curie('outputs'),
                   model_uri=TEST_CASE_SCHEMA.SemanticSmokeTestCase_outputs, domain=SemanticSmokeTestCase, range=Union[Union[dict, "SemanticSmokeTestOutput"], List[Union[dict, "SemanticSmokeTestOutput"]]])