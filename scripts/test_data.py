from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import json
import unittest

from goodtables import pipeline as _pipeline
from goodtables import processors
import datapackage

# TODO: consistent API for dp validate
# errors = dp.validate()
# if errors: ...

report_limit = 1000
row_limit = 100000
dp = datapackage.DataPackage('./datapackage.json')

class TestData(unittest.TestCase):

    def check_datapackage_json(self):
        try:
            dp.validate()
        except datapackage.exceptions.ValidationError as e:
            # Handle the ValidationError
            pass

    def test_structure(self):
        # TODO: infer from data package format field (and default to csv)
        data_format = 'csv'
        processor = processors.StructureProcessor(format=data_format, fail_fast=False,
            row_limit=row_limit,
            report_limit=report_limit)

        data = dp.metadata['resources'][0]['path']
        valid, report, data = processor.run(data)

        output_format = 'txt'
        exclude = ['result_context', 'processor', 'row_name', 'result_category',
                                   'column_index', 'column_name', 'result_level']
        out = report.generate(output_format, exclude=exclude)

        self.assertTrue(valid, out)

    # check the data against the schema
    def test_schema(self):
        data_format = 'csv'
        data = dp.metadata['resources'][0]['path']
        schema = dp.metadata['resources'][0]['schema']

        # TODO: check JTS is valid JTS before we go on

        processor = processors.SchemaProcessor(schema=schema,
                                               format=data_format,
                                               row_limit=row_limit,
                                               report_limit=report_limit)
        valid, report, data = processor.run(data)

        output_format = 'txt'
        exclude = ['result_context', 'processor', 'row_name', 'result_category',
                                   'column_name', 'result_id', 'result_level']
        out = report.generate(output_format, exclude=exclude)

        self.assertTrue(valid, out)


if __name__ == '__main__':
    unittest.main()

