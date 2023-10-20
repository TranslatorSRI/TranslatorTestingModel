
# Class: Precondition


Represents a precondition for a TestCase

URI: [ttm:Precondition](https://w3id.org/TranslatorSRI/TranslatorTestingModel/Precondition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[TestCase]-%20preconditions%200..*>[Precondition&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestEntity]^-[Precondition],[TestCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[TestCase]-%20preconditions%200..*>[Precondition&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestEntity]^-[Precondition],[TestCase])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Referenced by Class

 *  **None** *[preconditions](preconditions.md)*  <sub>0..\*</sub>  **[Precondition](Precondition.md)**

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
