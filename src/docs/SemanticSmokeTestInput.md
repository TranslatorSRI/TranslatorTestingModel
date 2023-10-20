
# Class: SemanticSmokeTestInput


Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.

URI: [ttm:SemanticSmokeTestInput](https://w3id.org/TranslatorSRI/TranslatorTestingModel/SemanticSmokeTestInput)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AcceptanceTestCase]-%20inputs%201..*>[SemanticSmokeTestInput&#124;must_pass_date:date%20%3F;must_pass_environment:EnvironmentEnum%20%3F;query:string%20%3F;string_entry:string%20%3F;direction:DirectionEnum%20%3F;answer_informal_concept:string%20%3F;expected_result:ExpectedResultsEnum%20%3F;curie:curie%20%3F;top_level:string%20%3F;node:string%20%3F;notes:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Input]^-[SemanticSmokeTestInput],[Input],[AcceptanceTestCase])](https://yuml.me/diagram/nofunky;dir:TB/class/[AcceptanceTestCase]-%20inputs%201..*>[SemanticSmokeTestInput&#124;must_pass_date:date%20%3F;must_pass_environment:EnvironmentEnum%20%3F;query:string%20%3F;string_entry:string%20%3F;direction:DirectionEnum%20%3F;answer_informal_concept:string%20%3F;expected_result:ExpectedResultsEnum%20%3F;curie:curie%20%3F;top_level:string%20%3F;node:string%20%3F;notes:string%20%3F;id(i):uriorcurie;name(i):string%20%3F;description(i):string%20%3F],[Input]^-[SemanticSmokeTestInput],[Input],[AcceptanceTestCase])

## Parents

 *  is_a: [Input](Input.md) - Represents an input to a TestCase

## Referenced by Class

 *  **[AcceptanceTestCase](AcceptanceTestCase.md)** *[AcceptanceTestCase➞inputs](AcceptanceTestCase_inputs.md)*  <sub>1..\*</sub>  **[SemanticSmokeTestInput](SemanticSmokeTestInput.md)**

## Attributes


### Own

 * [must_pass_date](must_pass_date.md)  <sub>0..1</sub>
     * Description: The date by which this test must pass
     * Range: [Date](types/Date.md)
     * Example: 2023-09-01 None
 * [must_pass_environment](must_pass_environment.md)  <sub>0..1</sub>
     * Description: The environment in which this test must pass
     * Range: [EnvironmentEnum](EnvironmentEnum.md)
     * Example: PROD None
     * Example: CI None
     * Example: TEST None
 * [query](query.md)  <sub>0..1</sub>
     * Description: The question a SME would ask
     * Range: [String](types/String.md)
     * Example: What drugs may treat multiple sclerosis? None
     * Example: What gene is upregulated? None
 * [string_entry](string_entry.md)  <sub>0..1</sub>
     * Description: The object of the core triple to be tested
     * Range: [String](types/String.md)
     * Example: multiple sclerosis None
     * Example: Castlemans None
 * [direction](direction.md)  <sub>0..1</sub>
     * Description: The direction of the expected query result triple
     * Range: [DirectionEnum](DirectionEnum.md)
 * [answer_informal_concept](answer_informal_concept.md)  <sub>0..1</sub>
     * Description: An answer that is returned from the test case, note: this must be combined with the expected_result to form a complete answer.  It might make sense to couple these in their own object instead of strictly sticking to the flat schema introduced by the spreadsheet here: https://docs.google.com/spreadsheets/d/1yj7zIchFeVl1OHqL_kE_pqvzNLmGml_FLbHDs-8Yvig/edit#gid=0
     * Range: [String](types/String.md)
     * Example: fingolimod None
     * Example: natalizumab None
     * Example: lead None
     * Example: great answer here None
 * [expected_result](expected_result.md)  <sub>0..1</sub>
     * Description: The expected result of the query
     * Range: [ExpectedResultsEnum](ExpectedResultsEnum.md)
 * [curie](curie.md)  <sub>0..1</sub>
     * Description: The curie of the query
     * Range: [Curie](types/Curie.md)
 * [top_level](top_level.md)  <sub>0..1</sub>
     * Description: The answer must return in these many results
     * Range: [String](types/String.md)
 * [node](node.md)  <sub>0..1</sub>
     * Description: The node of the TRAPI query to replace.
     * Range: [String](types/String.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Description: The notes of the query
     * Range: [String](types/String.md)

### Inherited from Input:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Test Entity
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for a Test Entity
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: A human-readable description for a Test Entity
     * Range: [String](types/String.md)
