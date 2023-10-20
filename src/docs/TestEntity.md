
# Class: TestEntity


Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

URI: [ttm:TestEntity](https://w3id.org/TranslatorSRI/TranslatorTestingModel/TestEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestSuite],[TestMetadata],[TestEntity&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[TestSuite],[TestEntity]^-[TestMetadata],[TestEntity]^-[TestCaseSpecification],[TestEntity]^-[TestCase],[TestEntity]^-[TestAsset],[TestEntity]^-[Precondition],[TestEntity]^-[Output],[TestEntity]^-[Input],[TestCaseSpecification],[TestCase],[TestAsset],[Precondition],[Output],[Input])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestSuite],[TestMetadata],[TestEntity&#124;id:uriorcurie;name:string%20%3F;description:string%20%3F]^-[TestSuite],[TestEntity]^-[TestMetadata],[TestEntity]^-[TestCaseSpecification],[TestEntity]^-[TestCase],[TestEntity]^-[TestAsset],[TestEntity]^-[Precondition],[TestEntity]^-[Output],[TestEntity]^-[Input],[TestCaseSpecification],[TestCase],[TestAsset],[Precondition],[Output],[Input])

## Children

 * [Input](Input.md) - Represents an input to a TestCase
 * [Output](Output.md) - Represents an output from a TestCase
 * [Precondition](Precondition.md) - Represents a precondition for a TestCase
 * [TestAsset](TestAsset.md) - Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing the specification of a Translator test target with inputs and (expected) outputs.
 * [TestCase](TestCase.md) - Represents a single enumerated instance of Test Case, derived from a  given TestAsset and used to probe a particular test condition.
 * [TestCaseSpecification](TestCaseSpecification.md) - Parameterized declaration of the Test Case generator which dynamically generates a collection of Test Cases from Test Assets, using applicable heuristics.
 * [TestMetadata](TestMetadata.md) - Represents metadata related to (external SME, SMURF, Translator feedback,  large scale batch, etc.) like the provenance of test assets, cases and/or suites.
 * [TestSuite](TestSuite.md) - Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic 'test_case_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to be present.

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Test Entity
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
