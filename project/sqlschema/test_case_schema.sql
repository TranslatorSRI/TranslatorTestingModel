

CREATE TABLE "TestCase" (
	name TEXT, 
	id TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TestCaseCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);
