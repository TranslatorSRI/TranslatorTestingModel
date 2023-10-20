
# Class: Input


Represents an input to a TestCase

URI: [ttm:Input](https://w3id.org/TranslatorSRI/TranslatorTestingModel/Input)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[SemanticSmokeTestInput],[TestCase]-%20inputs%200..*>[Input&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Input]^-[SemanticSmokeTestInput],[TestEntity]^-[Input],[TestCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[SemanticSmokeTestInput],[TestCase]-%20inputs%200..*>[Input&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Input]^-[SemanticSmokeTestInput],[TestEntity]^-[Input],[TestCase])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Children

 * [SemanticSmokeTestInput](SemanticSmokeTestInput.md) - Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.

## Referenced by Class

 *  **None** *[inputs](inputs.md)*  <sub>0..\*</sub>  **[Input](Input.md)**

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
