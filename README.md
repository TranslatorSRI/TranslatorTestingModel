# test-case-schema

This is a preliminary schema repo for defining test cases in Translator that can be reused in many different test suites.  e.g. a test case in plain language might be something like "what drugs may treat MS? I expect fingolimod to return in the top 10 results in less than 5 mins. "  Capturing these details in metadata that is parsable and usable by test runners is the objective of this schema.  We also want to harmonize our language and nomenclature for the metadata we need (which of these data are required and which are optional for each kind of test case, etc) so that downstream testing code can utilize a common framework for understanding.

## Website

[https://TranslatorSRI.github.io/test-case-schema](https://TranslatorSRI.github.io/test-case-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [test_case_schema](src/test_case_schema)
    * [schema](src/test_case_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/test_case_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
