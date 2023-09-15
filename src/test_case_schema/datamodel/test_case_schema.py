# Auto generated from test_case_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-09-15T10:46:18
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
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

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



class TestCase(YAMLRoot):
    """
    Represents a TestCase
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestCase
    class_class_curie: ClassVar[str] = "test_case_schema:TestCase"
    class_name: ClassVar[str] = "TestCase"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestCase


@dataclass
class TestCaseCollection(YAMLRoot):
    """
    A holder for TestCase objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestCaseCollection
    class_class_curie: ClassVar[str] = "test_case_schema:TestCaseCollection"
    class_name: ClassVar[str] = "TestCaseCollection"
    class_model_uri: ClassVar[URIRef] = TEST_CASE_SCHEMA.TestCaseCollection

    entries: Optional[Union[Union[dict, TestCase], List[Union[dict, TestCase]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.entries, list):
            self.entries = [self.entries] if self.entries is not None else []
        self.entries = [v if isinstance(v, TestCase) else TestCase(**as_dict(v)) for v in self.entries]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=TEST_CASE_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=TEST_CASE_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=TEST_CASE_SCHEMA.description, domain=None, range=Optional[str])

slots.testCaseCollection__entries = Slot(uri=TEST_CASE_SCHEMA.entries, name="testCaseCollection__entries", curie=TEST_CASE_SCHEMA.curie('entries'),
                   model_uri=TEST_CASE_SCHEMA.testCaseCollection__entries, domain=None, range=Optional[Union[Union[dict, TestCase], List[Union[dict, TestCase]]]])