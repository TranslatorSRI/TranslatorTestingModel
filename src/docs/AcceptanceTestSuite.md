
# Class: AcceptanceTestSuite




URI: [ttm:AcceptanceTestSuite](https://w3id.org/TranslatorSRI/TranslatorTestingModel/AcceptanceTestSuite)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestSuite],[TestMetadata],[TestCaseSpecification],[TestCase],[TestSuite]^-[AcceptanceTestSuite&#124;test_persona(i):TestPersonaEnum%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestSuite],[TestMetadata],[TestCaseSpecification],[TestCase],[TestSuite]^-[AcceptanceTestSuite&#124;test_persona(i):TestPersonaEnum%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [TestSuite](TestSuite.md) - Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic 'test_case_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to be present.

## Attributes


### Inherited from TestSuite:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Test Entity
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
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
