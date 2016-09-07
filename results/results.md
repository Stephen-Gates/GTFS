#GoodTables Test Results
Note GoodTables has a 100,000 row limit (see https://github.com/frictionlessdata/goodtables-web/issues/54)

Test results using valid data and no schema:
- [agency](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fagency.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000)
- [calendar](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fcalendar.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000)
- [calendar_dates](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fcalendar_dates.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000)
- [feed_info](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Ffeed_info.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000) 
- [routes](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Froutes.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000)
- [shapes](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fshapes.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000) presume 30,000 row limit reached.
- [stops](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fstops.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000)
- [trips](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Ftrips.txt&report_type=grouped&format=csv&row_limit=100000&report_limit=1000)

Test results using valid data and its schema:
- [agency](http://goodtables.okfnlabs.org/reports?data=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fdata%2Fagency.txt&schema=https%3A%2F%2Fraw.githubusercontent.com%2FStephen-Gates%2FGTFS%2Fmaster%2Fschemas%2Fagency-schema.json&format=csv&row_limit=100000&report_type=grouped&report_limit=1000)
- calendar
- calendar_dates
- feed_info
- routes
- shapes
- stops
- trips

GoodTables doesn't let you store test results for failed tests.
