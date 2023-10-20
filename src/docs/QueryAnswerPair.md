
# Class: QueryAnswerPair


Represents a QueryAnswerPair specification of a Test Asset

URI: [ttm:QueryAnswerPair](https://w3id.org/TranslatorSRI/TranslatorTestingModel/QueryAnswerPair)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TestAsset],[TestAsset]^-[QueryAnswerPair&#124;input_id(i):uriorcurie%20%3F;input_name(i):string%20%3F;output_id(i):uriorcurie%20%3F;output_name(i):string%20%3F;expected_output(i):ExpectedOutputEnum%20%3F;test_issue(i):TestIssueEnum%20%3F;semantic_severity(i):SemanticSeverityEnum%20%3F;in_v1(i):boolean%20%3F;well_known(i):boolean%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[TestAsset],[TestAsset]^-[QueryAnswerPair&#124;input_id(i):uriorcurie%20%3F;input_name(i):string%20%3F;output_id(i):uriorcurie%20%3F;output_name(i):string%20%3F;expected_output(i):ExpectedOutputEnum%20%3F;test_issue(i):TestIssueEnum%20%3F;semantic_severity(i):SemanticSeverityEnum%20%3F;in_v1(i):boolean%20%3F;well_known(i):boolean%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F])

## Parents

 *  is_a: [TestAsset](TestAsset.md) - Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing the specification of a Translator test target with inputs and (expected) outputs.

## Attributes


### Inherited from TestAsset:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
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
