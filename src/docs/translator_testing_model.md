
# Translator-Testing-Model


**metamodel version:** 1.7.0

**version:** None


Data model to formalize the structure of test assets, cases, suites and related metadata
applied to run the diverse polymorphic testing objectives for the Biomedical Data Translator system.


### Classes

 * [BenchmarkTestSuite](BenchmarkTestSuite.md) - JsonObj(is_a='TestSuite')
 * [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.
     * [Input](Input.md) - Represents an input to a TestCase
         * [SemanticSmokeTestInput](SemanticSmokeTestInput.md) - Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
     * [Output](Output.md) - Represents an output from a TestCase
         * [SemanticSmokeTestOutput](SemanticSmokeTestOutput.md) - Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
     * [Precondition](Precondition.md) - Represents a precondition for a TestCase
     * [TestAsset](TestAsset.md) - Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing the specification of a Translator test target with inputs and (expected) outputs.
         * [QueryAnswerPair](QueryAnswerPair.md) - Represents a QueryAnswerPair specification of a Test Asset
         * [TestEdgeData](TestEdgeData.md) - Represents a single Biolink Model compliant instance of an edge that can be used for testing.
     * [TestCase](TestCase.md) - Represents a single enumerated instance of Test Case, derived from a  given TestAsset and used to probe a particular test condition.
         * [AcceptanceTestCase](AcceptanceTestCase.md) - Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
     * [TestCaseSpecification](TestCaseSpecification.md) - Parameterized declaration of the Test Case generator which dynamically generates a collection of Test Cases from Test Assets, using applicable heuristics.
     * [TestMetadata](TestMetadata.md) - Represents metadata related to (external SME, SMURF, Translator feedback,  large scale batch, etc.) like the provenance of test assets, cases and/or suites.
     * [TestSuite](TestSuite.md) - Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic 'test_case_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to be present.
         * [AcceptanceTestSuite](AcceptanceTestSuite.md)
         * [OneHopTestSuite](OneHopTestSuite.md) - Test case for testing the integrity of "One Hop" knowledge graph retrievals sensa legacy SRI_Testing harness.
         * [StandardsComplianceTestSuite](StandardsComplianceTestSuite.md) - Test suite for testing Translator components against releases of standards like TRAPI and the Biolink Model.

### Mixins


### Slots

 * [answer_informal_concept](answer_informal_concept.md) - An answer that is returned from the test case, note: this must be combined with the expected_result to form a complete answer.  It might make sense to couple these in their own object instead of strictly sticking to the flat schema introduced by the spreadsheet here: https://docs.google.com/spreadsheets/d/1yj7zIchFeVl1OHqL_kE_pqvzNLmGml_FLbHDs-8Yvig/edit#gid=0
 * [curie](curie.md) - The curie of the query
 * [description](description.md) - A human-readable description for a Test Entity
 * [direction](direction.md) - The direction of the expected query result triple
 * [expected_output](expected_output.md)
 * [expected_result](expected_result.md) - The expected result of the query
 * [id](id.md) - A unique identifier for a Test Entity
     * [TestAsset➞id](TestAsset_id.md)
 * [in_v1](in_v1.md)
 * [input_id](input_id.md)
 * [input_name](input_name.md)
 * [inputs](inputs.md)
     * [AcceptanceTestCase➞inputs](AcceptanceTestCase_inputs.md)
 * [must_pass_date](must_pass_date.md) - The date by which this test must pass
 * [must_pass_environment](must_pass_environment.md) - The environment in which this test must pass
 * [name](name.md) - A human-readable name for a Test Entity
 * [node](node.md) - The node of the TRAPI query to replace.
 * [notes](notes.md) - The notes of the query
 * [output_id](output_id.md)
 * [output_name](output_name.md)
 * [outputs](outputs.md)
     * [AcceptanceTestCase➞outputs](AcceptanceTestCase_outputs.md)
 * [preconditions](preconditions.md)
 * [query](query.md) - The question a SME would ask
 * [requires_trapi](requires_trapi.md) - Does this test require a TRAPI-compliant query to run?
 * [semantic_severity](semantic_severity.md)
 * [string_entry](string_entry.md) - The object of the core triple to be tested
 * [test_case_specification](test_case_specification.md) - Declarative specification of a set of Test Cases generated elsewhere (i.e. within a Test Runner)
 * [test_cases](test_cases.md) - List of explicitly enumerated Test Cases.
 * [test_issue](test_issue.md)
 * [test_metadata](test_metadata.md) - Test metadata describes the external provenance, cross-references and objectives for a given test.
 * [test_objective](test_objective.md) - Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative)
 * [test_persona](test_persona.md) - A Test persona describes the user or operational context of a given test.
 * [test_reference](test_reference.md) - Source documentation where original test particulars are registered (e.g. Github repo)
 * [test_source](test_source.md) - Provenance of a specific set of test assets, cases and/or suites.
 * [top_level](top_level.md) - The answer must return in these many results
 * [well_known](well_known.md)

### Enums

 * [DirectionEnum](DirectionEnum.md)
 * [EnvironmentEnum](EnvironmentEnum.md)
 * [ExpectedOutputEnum](ExpectedOutputEnum.md) - Expected output values for instances of Test Asset or Test Cases(?). (Note: does this Enum overlap with 'ExpectedResultsEnum' below?)
 * [ExpectedResultsEnum](ExpectedResultsEnum.md) - Does this Enum overlap with 'ExpectedOutputEnum' above?
 * [SemanticSeverityEnum](SemanticSeverityEnum.md) - From Jenn's worksheet, empty or ill defined (needs elaboration)
 * [TestIssueEnum](TestIssueEnum.md)
 * [TestObjectiveEnum](TestObjectiveEnum.md)
 * [TestPersonaEnum](TestPersonaEnum.md)
 * [TestSourceEnum](TestSourceEnum.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
