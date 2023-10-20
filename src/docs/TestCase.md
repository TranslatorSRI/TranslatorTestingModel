
# Class: TestCase


Represents a single enumerated instance of Test Case, derived from a  given TestAsset and used to probe a particular test condition.

URI: [ttm:TestCase](https://w3id.org/TranslatorSRI/TranslatorTestingModel/TestCase)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[Precondition]<preconditions%200..*-%20[TestCase&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Output]<outputs%200..*-%20[TestCase],[Input]<inputs%200..*-%20[TestCase],[TestSuite]++-%20test_cases%200..*>[TestCase],[TestCase]^-[AcceptanceTestCase],[TestEntity]^-[TestCase],[TestSuite],[Precondition],[Output],[Input],[AcceptanceTestCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[Precondition]<preconditions%200..*-%20[TestCase&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Output]<outputs%200..*-%20[TestCase],[Input]<inputs%200..*-%20[TestCase],[TestSuite]++-%20test_cases%200..*>[TestCase],[TestCase]^-[AcceptanceTestCase],[TestEntity]^-[TestCase],[TestSuite],[Precondition],[Output],[Input],[AcceptanceTestCase])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Children

 * [AcceptanceTestCase](AcceptanceTestCase.md) - Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.

## Referenced by Class

 *  **None** *[test_cases](test_cases.md)*  <sub>0..\*</sub>  **[TestCase](TestCase.md)**

## Attributes


### Own

 * [inputs](inputs.md)  <sub>0..\*</sub>
     * Range: [Input](Input.md)
 * [outputs](outputs.md)  <sub>0..\*</sub>
     * Range: [Output](Output.md)
 * [preconditions](preconditions.md)  <sub>0..\*</sub>
     * Range: [Precondition](Precondition.md)

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
