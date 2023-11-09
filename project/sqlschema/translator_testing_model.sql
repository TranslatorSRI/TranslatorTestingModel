

CREATE TABLE "AcceptanceTestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_env VARCHAR(4), 
	query_type VARCHAR(6), 
	preconditions TEXT, 
	trapi_template VARCHAR(24), 
	PRIMARY KEY (id)
);

CREATE TABLE "ComplianceTestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_env VARCHAR(4), 
	query_type VARCHAR(6), 
	test_assets TEXT NOT NULL, 
	preconditions TEXT, 
	trapi_template VARCHAR(24), 
	PRIMARY KEY (id)
);

CREATE TABLE "KnowledgeGraphNavigationTestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_env VARCHAR(4), 
	query_type VARCHAR(6), 
	test_assets TEXT NOT NULL, 
	preconditions TEXT, 
	trapi_template VARCHAR(24), 
	PRIMARY KEY (id)
);

CREATE TABLE "OneHopTestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_env VARCHAR(4), 
	query_type VARCHAR(6), 
	test_assets TEXT NOT NULL, 
	preconditions TEXT, 
	trapi_template VARCHAR(24), 
	PRIMARY KEY (id)
);

CREATE TABLE "Precondition" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "QuantitativeTestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_env VARCHAR(4), 
	query_type VARCHAR(6), 
	test_assets TEXT NOT NULL, 
	preconditions TEXT, 
	trapi_template VARCHAR(24), 
	PRIMARY KEY (id)
);

CREATE TABLE "TestAsset" (
	name TEXT, 
	description TEXT, 
	input_id TEXT, 
	input_name TEXT, 
	predicate TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	expected_output VARCHAR(25), 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	test_reference TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestCase" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_env VARCHAR(4), 
	query_type VARCHAR(6), 
	test_assets TEXT NOT NULL, 
	preconditions TEXT, 
	trapi_template VARCHAR(24), 
	PRIMARY KEY (id)
);

CREATE TABLE "TestEdgeData" (
	name TEXT, 
	description TEXT, 
	input_id TEXT, 
	input_name TEXT, 
	predicate TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	expected_output VARCHAR(25), 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	test_reference TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestEntityParameter" (
	parameter_name TEXT NOT NULL, 
	parameter_value TEXT NOT NULL, 
	PRIMARY KEY (parameter_name, parameter_value)
);

CREATE TABLE "TestMetadata" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_source VARCHAR(18), 
	test_reference TEXT, 
	test_objective VARCHAR(16), 
	test_annotations TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestRunnerConfiguration" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_run_parameters TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestRunSession" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_runner_name TEXT, 
	timestamp DATETIME, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestSuiteSpecification" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_data_file_locator TEXT, 
	test_data_file_format VARCHAR(4), 
	PRIMARY KEY (id)
);

CREATE TABLE "AcceptanceTestAsset" (
	name TEXT, 
	description TEXT, 
	input_id TEXT, 
	input_name TEXT, 
	predicate TEXT, 
	output_id TEXT, 
	output_name TEXT, 
	expected_output VARCHAR(25), 
	test_issue VARCHAR(20), 
	semantic_severity VARCHAR(13), 
	in_v1 BOOLEAN, 
	well_known BOOLEAN, 
	test_reference TEXT, 
	id TEXT NOT NULL, 
	must_pass_date DATE, 
	must_pass_environment VARCHAR(4), 
	scientific_question TEXT, 
	string_entry TEXT, 
	direction VARCHAR(9), 
	answer_informal_concept TEXT, 
	expected_result VARCHAR(12), 
	top_level INTEGER, 
	query_node VARCHAR(7), 
	notes TEXT, 
	"AcceptanceTestCase_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AcceptanceTestCase_id") REFERENCES "AcceptanceTestCase" (id)
);

CREATE TABLE "AcceptanceTestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_suite_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification) REFERENCES "TestSuiteSpecification" (id)
);

CREATE TABLE "OneHopTestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_suite_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification) REFERENCES "TestSuiteSpecification" (id)
);

CREATE TABLE "StandardsComplianceTestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_suite_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification) REFERENCES "TestSuiteSpecification" (id)
);

CREATE TABLE "TestCaseResult" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_suite_id TEXT, 
	test_case TEXT, 
	test_case_result VARCHAR(12), 
	"TestRunSession_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_case) REFERENCES "TestCase" (id), 
	FOREIGN KEY("TestRunSession_id") REFERENCES "TestRunSession" (id)
);

CREATE TABLE "TestSuite" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	test_metadata TEXT, 
	test_persona VARCHAR(11), 
	test_cases TEXT, 
	test_suite_specification TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(test_metadata) REFERENCES "TestMetadata" (id), 
	FOREIGN KEY(test_suite_specification) REFERENCES "TestSuiteSpecification" (id)
);

CREATE TABLE "AcceptanceTestCase_components" (
	backref_id TEXT, 
	components VARCHAR(9), 
	PRIMARY KEY (backref_id, components), 
	FOREIGN KEY(backref_id) REFERENCES "AcceptanceTestCase" (id)
);

CREATE TABLE "AcceptanceTestCase_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "AcceptanceTestCase" (id)
);

CREATE TABLE "ComplianceTestCase_components" (
	backref_id TEXT, 
	components VARCHAR(9), 
	PRIMARY KEY (backref_id, components), 
	FOREIGN KEY(backref_id) REFERENCES "ComplianceTestCase" (id)
);

CREATE TABLE "ComplianceTestCase_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "ComplianceTestCase" (id)
);

CREATE TABLE "KnowledgeGraphNavigationTestCase_components" (
	backref_id TEXT, 
	components VARCHAR(9), 
	PRIMARY KEY (backref_id, components), 
	FOREIGN KEY(backref_id) REFERENCES "KnowledgeGraphNavigationTestCase" (id)
);

CREATE TABLE "KnowledgeGraphNavigationTestCase_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "KnowledgeGraphNavigationTestCase" (id)
);

CREATE TABLE "OneHopTestCase_components" (
	backref_id TEXT, 
	components VARCHAR(9), 
	PRIMARY KEY (backref_id, components), 
	FOREIGN KEY(backref_id) REFERENCES "OneHopTestCase" (id)
);

CREATE TABLE "OneHopTestCase_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "OneHopTestCase" (id)
);

CREATE TABLE "Precondition_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "Precondition" (id)
);

CREATE TABLE "QuantitativeTestCase_components" (
	backref_id TEXT, 
	components VARCHAR(9), 
	PRIMARY KEY (backref_id, components), 
	FOREIGN KEY(backref_id) REFERENCES "QuantitativeTestCase" (id)
);

CREATE TABLE "QuantitativeTestCase_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "QuantitativeTestCase" (id)
);

CREATE TABLE "TestAsset_runner_settings" (
	backref_id TEXT, 
	runner_settings TEXT NOT NULL, 
	PRIMARY KEY (backref_id, runner_settings), 
	FOREIGN KEY(backref_id) REFERENCES "TestAsset" (id)
);

CREATE TABLE "TestAsset_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestAsset" (id)
);

CREATE TABLE "TestCase_components" (
	backref_id TEXT, 
	components VARCHAR(9), 
	PRIMARY KEY (backref_id, components), 
	FOREIGN KEY(backref_id) REFERENCES "TestCase" (id)
);

CREATE TABLE "TestCase_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestCase" (id)
);

CREATE TABLE "TestEdgeData_runner_settings" (
	backref_id TEXT, 
	runner_settings TEXT NOT NULL, 
	PRIMARY KEY (backref_id, runner_settings), 
	FOREIGN KEY(backref_id) REFERENCES "TestEdgeData" (id)
);

CREATE TABLE "TestEdgeData_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestEdgeData" (id)
);

CREATE TABLE "TestMetadata_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestMetadata" (id)
);

CREATE TABLE "TestRunnerConfiguration_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestRunnerConfiguration" (id)
);

CREATE TABLE "TestRunSession_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestRunSession" (id)
);

CREATE TABLE "TestRunSession_test_entities" (
	backref_id TEXT, 
	test_entities TEXT, 
	PRIMARY KEY (backref_id, test_entities), 
	FOREIGN KEY(backref_id) REFERENCES "TestRunSession" (id)
);

CREATE TABLE "TestSuiteSpecification_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestSuiteSpecification" (id)
);

CREATE TABLE "AcceptanceTestAsset_runner_settings" (
	backref_id TEXT, 
	runner_settings TEXT NOT NULL, 
	PRIMARY KEY (backref_id, runner_settings), 
	FOREIGN KEY(backref_id) REFERENCES "AcceptanceTestAsset" (id)
);

CREATE TABLE "AcceptanceTestAsset_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "AcceptanceTestAsset" (id)
);

CREATE TABLE "AcceptanceTestSuite_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "AcceptanceTestSuite" (id)
);

CREATE TABLE "OneHopTestSuite_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "OneHopTestSuite" (id)
);

CREATE TABLE "StandardsComplianceTestSuite_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "StandardsComplianceTestSuite" (id)
);

CREATE TABLE "TestCaseResult_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestCaseResult" (id)
);

CREATE TABLE "TestSuite_tags" (
	backref_id TEXT, 
	tags TEXT, 
	PRIMARY KEY (backref_id, tags), 
	FOREIGN KEY(backref_id) REFERENCES "TestSuite" (id)
);
