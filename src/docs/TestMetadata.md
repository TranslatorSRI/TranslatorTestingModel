
# Class: TestMetadata


Represents metadata related to (external SME, SMURF, Translator feedback,  large scale batch, etc.) like the provenance of test assets, cases and/or suites.

URI: [ttm:TestMetadata](https://w3id.org/TranslatorSRI/TranslatorTestingModel/TestMetadata)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestSuite]-%20test_metadata%200..1>[TestMetadata&#124;test_source:TestSourceEnum%20%3F;test_reference:uriorcurie%20%3F;test_objective:TestObjectiveEnum%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestEntity]^-[TestMetadata],[TestSuite],[TestEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestSuite]-%20test_metadata%200..1>[TestMetadata&#124;test_source:TestSourceEnum%20%3F;test_reference:uriorcurie%20%3F;test_objective:TestObjectiveEnum%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestEntity]^-[TestMetadata],[TestSuite],[TestEntity])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Referenced by Class

 *  **None** *[test_metadata](test_metadata.md)*  <sub>0..1</sub>  **[TestMetadata](TestMetadata.md)**

## Attributes


### Own

 * [test_source](test_source.md)  <sub>0..1</sub>
     * Description: Provenance of a specific set of test assets, cases and/or suites.
     * Range: [TestSourceEnum](TestSourceEnum.md)
 * [test_reference](test_reference.md)  <sub>0..1</sub>
     * Description: Source documentation where original test particulars are registered (e.g. Github repo)
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [test_objective](test_objective.md)  <sub>0..1</sub>
     * Description: Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative)
     * Range: [TestObjectiveEnum](TestObjectiveEnum.md)

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
