
# Class: TestSuite


Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic 'test_case_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to be present.

URI: [ttm:TestSuite](https://w3id.org/TranslatorSRI/TranslatorTestingModel/TestSuite)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestCaseSpecification]<test_case_specification%200..1-%20[TestSuite&#124;test_persona:TestPersonaEnum%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestCase]<test_cases%200..*-++[TestSuite],[TestMetadata]<test_metadata%200..1-%20[TestSuite],[TestSuite]^-[StandardsComplianceTestSuite],[TestSuite]^-[OneHopTestSuite],[TestSuite]^-[AcceptanceTestSuite],[TestEntity]^-[TestSuite],[TestMetadata],[TestEntity],[TestCaseSpecification],[TestCase],[StandardsComplianceTestSuite],[OneHopTestSuite],[AcceptanceTestSuite])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestCaseSpecification]<test_case_specification%200..1-%20[TestSuite&#124;test_persona:TestPersonaEnum%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestCase]<test_cases%200..*-++[TestSuite],[TestMetadata]<test_metadata%200..1-%20[TestSuite],[TestSuite]^-[StandardsComplianceTestSuite],[TestSuite]^-[OneHopTestSuite],[TestSuite]^-[AcceptanceTestSuite],[TestEntity]^-[TestSuite],[TestMetadata],[TestEntity],[TestCaseSpecification],[TestCase],[StandardsComplianceTestSuite],[OneHopTestSuite],[AcceptanceTestSuite])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Children

 * [AcceptanceTestSuite](AcceptanceTestSuite.md)
 * [OneHopTestSuite](OneHopTestSuite.md) - Test case for testing the integrity of "One Hop" knowledge graph retrievals sensa legacy SRI_Testing harness.
 * [StandardsComplianceTestSuite](StandardsComplianceTestSuite.md) - Test suite for testing Translator components against releases of standards like TRAPI and the Biolink Model.

## Referenced by Class


## Attributes


### Own

 * [test_metadata](test_metadata.md)  <sub>0..1</sub>
     * Description: Test metadata describes the external provenance, cross-references and objectives for a given test.
     * Range: [TestMetadata](TestMetadata.md)
 * [test_persona](test_persona.md)  <sub>0..1</sub>
     * Description: A Test persona describes the user or operational context of a given test.
     * Range: [TestPersonaEnum](TestPersonaEnum.md)
 * [test_cases](test_cases.md)  <sub>0..\*</sub>
     * Description: List of explicitly enumerated Test Cases.
     * Range: [TestCase](TestCase.md)
 * [test_case_specification](test_case_specification.md)  <sub>0..1</sub>
     * Description: Declarative specification of a set of Test Cases generated elsewhere (i.e. within a Test Runner)
     * Range: [TestCaseSpecification](TestCaseSpecification.md)

### Inherited from TestEntity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Test Entity
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
