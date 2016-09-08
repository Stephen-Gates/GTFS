#GoodTables Tests
Use the links below to perform the tests using GoodTables. 

The test links call GoodTables using links to the raw data and schema files as input to GoodTables e.g.
  - valid data: https://raw.githubusercontent.com/Stephen-Gates/GTFS/master/data/agency.txt
  - schema: https://raw.githubusercontent.com/Stephen-Gates/GTFS/master/schemas/agency-schema.json
  - invalid data: https://github.com/Stephen-Gates/GTFS/blob/master/tests/agency.txt
    
The URL passed to GoodTables needs escaped versions of the links above e.g. 
  - http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fagency.txt&format=csv&encoding=&schema_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Fagency-schema.json

## GoodTables issues
- GoodTables supposedly has a 100,000 row limit (see [goodtables-web #54](https://github.com/frictionlessdata/goodtables-web/issues/54)) but it appears to be [limited to 30,000*](https://github.com/frictionlessdata/goodtables-web#api)
- only returns a [limited number of errors](https://github.com/frictionlessdata/goodtables-web/issues/66) so the test data will need to be split into smaller sets.
- GoodTables doesn't use the primary key to check for duplicates ([see goodtables-web #64](https://github.com/frictionlessdata/goodtables-web/issues/64))
- GoodTables doesn't handle optional uri fields (see [goodtables #109](https://github.com/frictionlessdata/goodtables/issues/109))
- view other [goodtables-web](https://github.com/frictionlessdata/goodtables-web/issues) and [goodtables](https://github.com/frictionlessdata/goodtables/issues) issues

## Test using valid data and no schema:
- [Test agency.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fagency.txt&format=csv&encoding=&schema_url=)
- [Test calendar.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fcalendar.txt&format=csv&encoding=&schema_url=)
- [Test calendar_dates.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fcalendar_dates.txt&format=csv&encoding=&schema_url=)
- [Test feed_info.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Ffeed_info.txt&format=csv&encoding=&schema_url=)
- [Test routes.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Froutes.txt&format=csv&encoding=&schema_url=)
- [Test shapes.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fshapes.txt&format=csv&encoding=&schema_url=) *30,000 rows processed - seemed overly neat.
- [Test stops.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fstops.txt&format=csv&encoding=&schema_url=)
- [Test trips.txt without a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Ftrips.txt&format=csv&encoding=&schema_url=)

## Test using valid data with its schema:
- [Test agency.txt with a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fagency.txt&format=csv&encoding=&schema_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Fagency-schema.json)
- Test calendar.txt with a schema
- Test calendar_dates.txt with a schema
- Test feed_info.txt with a schema
- [Test routes.txt with a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Froutes.txt&format=csv&encoding=&schema_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Froutes-schema.json)
- [Test shapes.txt with a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fshapes.txt&format=csv&encoding=&schema_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Fshapes-schema.json)  
- [Test stops.txt with a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fstops.txt&format=csv&encoding=&schema_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Fstops-schema.json)  
- Test trips.txt with a schema

## Test using invalid data and its schema:
- [Test invalid agency.txt with a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Ftests%2Fagency.txt&format=csv&encoding=&schema_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Fagency-schema.json)
- Test calendar.txt with a schema
- Test calendar_dates.txt with a schema
- Test feed_info.txt with a schema
- Test routes.txt with a schema
- [Test invalid shapes.txt with a schema](http://goodtables.okfnlabs.org/reports?data_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Ftests%2Fshapes.txt&format=csv&encoding=&schema_url=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Fshapes-schema.json)
- Test stops.txt with a schema
- Test trips.txt with a schema



