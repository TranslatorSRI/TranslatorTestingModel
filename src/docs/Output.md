
# Class: Output


Represents an output from a TestCase

URI: [ttm:Output](https://w3id.org/TranslatorSRI/TranslatorTestingModel/Output)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[SemanticSmokeTestOutput],[TestCase]-%20outputs%200..*>[Output&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Output]^-[SemanticSmokeTestOutput],[TestEntity]^-[Output],[TestCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[SemanticSmokeTestOutput],[TestCase]-%20outputs%200..*>[Output&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Output]^-[SemanticSmokeTestOutput],[TestEntity]^-[Output],[TestCase])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Children

 * [SemanticSmokeTestOutput](SemanticSmokeTestOutput.md) - Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.

## Referenced by Class

 *  **None** *[outputs](outputs.md)*  <sub>0..\*</sub>  **[Output](Output.md)**

## Attributes


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
