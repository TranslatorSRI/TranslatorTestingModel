
# Class: SemanticSmokeTestOutput


Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.

URI: [ttm:SemanticSmokeTestOutput](https://w3id.org/TranslatorSRI/TranslatorTestingModel/SemanticSmokeTestOutput)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AcceptanceTestCase]-%20outputs%201..*>[SemanticSmokeTestOutput&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Output]^-[SemanticSmokeTestOutput],[Output],[AcceptanceTestCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[AcceptanceTestCase]-%20outputs%201..*>[SemanticSmokeTestOutput&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Output]^-[SemanticSmokeTestOutput],[Output],[AcceptanceTestCase])

## Parents

 *  is_a: [Output](Output.md) - Represents an output from a TestCase

## Referenced by Class

 *  **[AcceptanceTestCase](AcceptanceTestCase.md)** *[AcceptanceTestCase➞outputs](AcceptanceTestCase_outputs.md)*  <sub>1..\*</sub>  **[SemanticSmokeTestOutput](SemanticSmokeTestOutput.md)**

## Attributes


### Inherited from Output:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Test Entity
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
