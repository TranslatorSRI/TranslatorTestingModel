
# Class: TestCaseSpecification


Parameterized declaration of the Test Case generator which dynamically generates a collection of Test Cases from Test Assets, using applicable heuristics.

URI: [ttm:TestCaseSpecification](https://w3id.org/TranslatorSRI/TranslatorTestingModel/TestCaseSpecification)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[TestSuite]-%20test_case_specification%200..1>[TestCaseSpecification&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestEntity]^-[TestCaseSpecification],[TestSuite])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[TestSuite]-%20test_case_specification%200..1>[TestCaseSpecification&#124;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[TestEntity]^-[TestCaseSpecification],[TestSuite])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Referenced by Class

 *  **None** *[test_case_specification](test_case_specification.md)*  <sub>0..1</sub>  **[TestCaseSpecification](TestCaseSpecification.md)**

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
