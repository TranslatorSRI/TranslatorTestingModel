

CREATE TABLE "SemanticSmokeTestCase" (
	name TEXT, 
	id TEXT NOT NULL, 
	description TEXT, 
	preconditions TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestCase" (
	name TEXT, 
	id TEXT NOT NULL, 
	description TEXT, 
	preconditions TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestSuite" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "Input" (
	"TestCase_id" TEXT, 
	PRIMARY KEY ("TestCase_id"), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id)
);

CREATE TABLE "Output" (
	"TestCase_id" TEXT, 
	PRIMARY KEY ("TestCase_id"), 
	FOREIGN KEY("TestCase_id") REFERENCES "TestCase" (id)
);

CREATE TABLE "SemanticSmokeTestInput" (
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
	"SemanticSmokeTestCase_id" TEXT, 
	PRIMARY KEY (must_pass_date, must_pass_environment, "query", string_entry, direction, answer_informal_concept, expected_result, curie, top_level, node, notes, "SemanticSmokeTestCase_id"), 
	FOREIGN KEY("SemanticSmokeTestCase_id") REFERENCES "SemanticSmokeTestCase" (id)
);

CREATE TABLE "SemanticSmokeTestOutput" (
	"SemanticSmokeTestCase_id" TEXT, 
	PRIMARY KEY ("SemanticSmokeTestCase_id"), 
	FOREIGN KEY("SemanticSmokeTestCase_id") REFERENCES "SemanticSmokeTestCase" (id)
);
