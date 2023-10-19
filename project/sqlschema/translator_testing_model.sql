

CREATE TABLE "AcceptanceTestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	preconditions TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Precondition" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QueryAnswerPair" (
	name TEXT, 
	description TEXT, 
	input_id TEXT, 
	input_name TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	expected_output VARCHAR(16), 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestAsset" (
	name TEXT, 
	description TEXT, 
	input_id TEXT, 
	input_name TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	expected_output VARCHAR(16), 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	preconditions TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestCaseSpecification" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestEdgeData" (
	name TEXT, 
	description TEXT, 
	input_id TEXT, 
	input_name TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	expected_output VARCHAR(16), 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestMetadata" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_source VARCHAR(18), 
	test_reference TEXT, 
	test_objective VARCHAR(16), 
	PRIMARY KEY (id)
);

CREATE TABLE "AcceptanceTestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_case_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_case_specification) REFERENCES "TestCaseSpecification" (id)
);

CREATE TABLE "Input" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TestCase_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id)
);

CREATE TABLE "OneHopTestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_case_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_case_specification) REFERENCES "TestCaseSpecification" (id)
);

CREATE TABLE "Output" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"TestCase_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id)
);

CREATE TABLE "SemanticSmokeTestInput" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	must_pass_date DATE, 
	must_pass_environment VARCHAR(4), 
	"query" TEXT, 
	string_entry TEXT, 
	direction VARCHAR(9), 
	answer_informal_concept TEXT, 
	expected_result VARCHAR(12), 
	curie TEXT, 
	top_level TEXT, 
	node TEXT, 
	notes TEXT, 
	"AcceptanceTestCase_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id)
);

CREATE TABLE "SemanticSmokeTestOutput" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	"AcceptanceTestCase_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id)
);

CREATE TABLE "StandardsComplianceTestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_case_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_case_specification) REFERENCES "TestCaseSpecification" (id)
);

CREATE TABLE "TestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_case_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_case_specification) REFERENCES "TestCaseSpecification" (id)
);
