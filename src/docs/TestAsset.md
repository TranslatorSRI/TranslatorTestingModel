
# Class: TestAsset


Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing the specification of a Translator test target with inputs and (expected) outputs.

URI: [ttm:TestAsset](https://w3id.org/TranslatorSRI/TranslatorTestingModel/TestAsset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[TestEdgeData],[TestAsset&#124;input_id:uriorcurie%20%3F;input_name:string%20%3F;output_id:uriorcurie%20%3F;output_name:string%20%3F;expected_output:ExpectedOutputEnum%20%3F;test_issue:TestIssueEnum%20%3F;semantic_severity:SemanticSeverityEnum%20%3F;in_v1:boolean%20%3F;well_known:boolean%20%3F;id:uriorcurie;name(i):string%20%3F;description(i):string%20%3F]^-[TestEdgeData],[TestAsset]^-[QueryAnswerPair],[TestEntity]^-[TestAsset],[QueryAnswerPair])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestEntity],[TestEdgeData],[TestAsset&#124;input_id:uriorcurie%20%3F;input_name:string%20%3F;output_id:uriorcurie%20%3F;output_name:string%20%3F;expected_output:ExpectedOutputEnum%20%3F;test_issue:TestIssueEnum%20%3F;semantic_severity:SemanticSeverityEnum%20%3F;in_v1:boolean%20%3F;well_known:boolean%20%3F;id:uriorcurie;name(i):string%20%3F;description(i):string%20%3F]^-[TestEdgeData],[TestAsset]^-[QueryAnswerPair],[TestEntity]^-[TestAsset],[QueryAnswerPair])

## Parents

 *  is_a: [TestEntity](TestEntity.md) - Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.

## Children

 * [QueryAnswerPair](QueryAnswerPair.md) - Represents a QueryAnswerPair specification of a Test Asset
 * [TestEdgeData](TestEdgeData.md) - Represents a single Biolink Model compliant instance of an edge that can be used for testing.

## Referenced by Class


## Attributes


### Own

 * [input_id](input_id.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [input_name](input_name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [output_id](output_id.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [output_name](output_name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [expected_output](expected_output.md)  <sub>0..1</sub>
     * Range: [ExpectedOutputEnum](ExpectedOutputEnum.md)
 * [test_issue](test_issue.md)  <sub>0..1</sub>
     * Range: [TestIssueEnum](TestIssueEnum.md)
 * [semantic_severity](semantic_severity.md)  <sub>0..1</sub>
     * Range: [SemanticSeverityEnum](SemanticSeverityEnum.md)
 * [in_v1](in_v1.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [well_known](well_known.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [TestAsset➞id](TestAsset_id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Test Entity
     * Range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from TestEntity:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
