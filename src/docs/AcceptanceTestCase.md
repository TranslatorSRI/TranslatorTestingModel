
# Class: AcceptanceTestCase


Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.

URI: [ttm:AcceptanceTestCase](https://w3id.org/TranslatorSRI/TranslatorTestingModel/AcceptanceTestCase)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestCase],[SemanticSmokeTestOutput],[SemanticSmokeTestInput],[Precondition],[SemanticSmokeTestOutput]<outputs%201..*-%20[AcceptanceTestCase&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[SemanticSmokeTestInput]<inputs%201..*-%20[AcceptanceTestCase],[TestCase]^-[AcceptanceTestCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestCase],[SemanticSmokeTestOutput],[SemanticSmokeTestInput],[Precondition],[SemanticSmokeTestOutput]<outputs%201..*-%20[AcceptanceTestCase&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[SemanticSmokeTestInput]<inputs%201..*-%20[AcceptanceTestCase],[TestCase]^-[AcceptanceTestCase])

## Parents

 *  is_a: [TestCase](TestCase.md) - Represents a single enumerated instance of Test Case, derived from a  given TestAsset and used to probe a particular test condition.

## Referenced by Class


## Attributes


### Own

 * [AcceptanceTestCase➞inputs](AcceptanceTestCase_inputs.md)  <sub>1..\*</sub>
     * Range: [SemanticSmokeTestInput](SemanticSmokeTestInput.md)
 * [AcceptanceTestCase➞outputs](AcceptanceTestCase_outputs.md)  <sub>1..\*</sub>
     * Range: [SemanticSmokeTestOutput](SemanticSmokeTestOutput.md)

### Inherited from TestCase:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Test Entity
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
 * [preconditions](preconditions.md)  <sub>0..\*</sub>
     * Range: [Precondition](Precondition.md)
