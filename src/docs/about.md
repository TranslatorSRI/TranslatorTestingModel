# Translator Testing Model

This is a preliminary schema repo for defining test cases in Translator that can be reused in different test suites.  e.g. a test case in plain language might be something like _"what drugs may treat MS? I expect fingolimod to return in the top 10 results in less than 5 mins."_  

Capturing these details in metadata that is parsable and usable by test runners is the objective of this schema.  We also want to harmonize our language and nomenclature for the metadata we need (which of these data are required and which are optional for each kind of test case, etc.) so that downstream testing code can utilize a common framework for understanding.
