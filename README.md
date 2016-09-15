# GTFS

Public transportation schedules and associated geographic information for South-East Queensland.

The data is a snapshot and not planned to be kept up-to-date. The main purpose of this repository is to develop a data package and schemas for this dataset.

## Data
This data is the [General transit feed specification (GTFS) — South East Queensland](https://data.qld.gov.au/dataset/general-transit-feed-specification-gtfs-seq) data published by [Transport and Main Roads, Queensland Government](http://www.tmr.qld.gov.au/), licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/3.0/au/) sourced on 07 September 2016.

The data follows the [GTFS specification](https://developers.google.com/transit/gtfs/reference/) and some of its [extensions](https://developers.google.com/transit/gtfs/reference/gtfs-extensions) that define a common format for public transportation schedules and associated geographic information. The specification allows some files to be optional. It also allows some columns in the files to be optional. This means that the datapackage.json file and schemas may not work for [other GTFS files](https://code.google.com/archive/p/googletransitdatafeed/wikis/PublicFeeds.wiki).

The [data](https://github.com/Stephen-Gates/GTFS/tree/master/data) is made up of a number of files.

Each data file is defined by a [schema](https://github.com/Stephen-Gates/GTFS/tree/master/schemas). The schemas follow the [json table schema specification](http://specs.frictionlessdata.io/json-table-schema/).

These schemas will be combined into a [datapackage.json](https://github.com/Stephen-Gates/GTFS/blob/master/datapackage.json) file to fully describe the data collection. The datapackage.json file will follow the [data package specification](http://specs.frictionlessdata.io/data-packages/).

## Preparation
The data was downloaded, unzipped, and then uploaded to GitHub.

Two data files (shapes.txt and trips.txt) were too large to load into GitHub. They were truncated and uploaded. They will be adequate to use for testing valid data.

## Tests
The focus of the tests is to ensure the schemas are correct. There are already [GTFS data validation tools](https://developers.google.com/transit/gtfs/guides/tools) to test the data in more powerful ways than json table schemas allow.

The [tests](https://github.com/Stephen-Gates/GTFS/tree/master/tests) are invalid data that is used to ensure the schema detects all errors (e.g. incorrect [types](http://specs.frictionlessdata.io/json-table-schema/#field-types-and-formats) and violated [constraints](http://specs.frictionlessdata.io/json-table-schema/#field-constraints)).

## Results
The [results](https://github.com/Stephen-Gates/GTFS/blob/master/results/results.md) can be verified using links to  [Good Tables](http://goodtables.okfnlabs.org). Tests include:
- testing the valid data without a schema
- testing the valid data with a schema
- testing the invalid data with a schema

Good Tables doesn't check all types of errors (yet). Somethings not checked include:
- Foreign keys. (See Good Tables [#17](https://github.com/frictionlessdata/goodtables/issues/17),  [#8](https://github.com/frictionlessdata/goodtables/issues/8))
- Some constraints (See Good Tables[#55](https://github.com/frictionlessdata/goodtables/issues/55))

## Automatic Testing
The scripts and .travis.yml file are used to automatically test the data that is defined in datapackage.json. Whenever there is a change to this repository, it triggers [Travis](https://travis-ci.org/) to validate the data.  

The last automatic test returned [![datapackage validation](https://travis-ci.org/Stephen-Gates/GTFS.svg?branch=master)](https://travis-ci.org/Stephen-Gates/GTFS)

## Schemas
The [schemas](https://github.com/Stephen-Gates/GTFS/tree/master/schemas) were created using [Data Packagist](http://datapackagist.okfnlabs.org). Using Data Packagist:

- add some basic information about the data file (name, description, license, etc.)
- upload the data file

Data Packagist will create a datapackage.json file for you. Download this file.

Good Tables can only use a json table schema for validation ([see goodtables-web #65](https://github.com/frictionlessdata/goodtables-web/issues/65)). You can extract the json table schema from the datapackage.json file. It's this bit `{fields: [...]}`. Save this a separate file.

Edit the schema file with a text editor (e.g. [ATOM](https://atom.io), [jsoneditoronline.org](http://www.jsoneditoronline.org)) and add constraints, refine types and formats, etc. You may like to use the [json table schema schema](https://raw.githubusercontent.com/frictionlessdata/schemas/master/json-table-schema.json) to improve your editing experience.

Some constraints use regular expressions to define a pattern. Use a online tool to help create and test a regular expresion e.g. [regexr.com](http://regexr.com/) or [regex101](https://regex101.com/).

## View the Data Package
Data packages are about providing machine-readable metadata for your data. You can [view a human-readable version of the data package](http://data.okfn.org/tools/view?url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdatapackage.json) data, and readme files using the [Data Package Viewer](http://data.okfn.org/tools/view). There are a couple of [issues](https://github.com/okfn/data.okfn.org-new/issues) with the viewer including providing an incorrect link to the metadata [data.okfn.org-new #9](https://github.com/okfn/data.okfn.org-new/issues).

## License
All items in this repository, apart from the data, are licensed under [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/).
