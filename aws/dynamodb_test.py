#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest
import boto3
import botocore


class DynamoDBTest(unittest.TestCase):

    def setUp(self):
        env = os.environ.get('PROFILE_NAME', 'default')
        if env == "default":
            print "Using Default profile"
        else:
            print "Using %s profile" % env

        try:
            session = boto3.Session(profile_name=env,
                                    region_name="us-east-1")
        except botocore.exceptions.ProfileNotFound:
            print "Profile %s not found!" % env
            self.dbclient = None
            return

        self.dbclient = session.client('dynamodb')

    def test_list_tables(self):
        print "test"
        if self.dbclient:
            print self.dbclient.list_tables()

    def test_create_table(self):
        print "Create Table"
        if not self.dbclient:
            print "DBCLient not set"
            return

        table_name = "brd-testtable"
        attribute_definitions = [
            {
                'AttributeName': 'employee_id',
                'AttributeType': 'N'
            }
        ]
        key_schema = [
            {
                'AttributeName': 'employee_id',
                'KeyType': 'HASH'
            }
        ]
        provisioned_throughput =  {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }

        self.dbclient.create_table(TableName=table_name,
                                   AttributeDefinitions=attribute_definitions,
                                   KeySchema=key_schema,
                                   ProvisionedThroughput=provisioned_throughput)

        print self.dbclient.describe_table(TableName=table_name)

    def test_put_item(self):
        print "Put items"
        table_name = "brd-testtable"
        try:
            self.dbclient.describe_table(TableName=table_name)
        except botocore.exceptions.ClientError as ce:
            print "Resource %s not found" % table_name
            print " exception: %s" % ce.response['Error']
            return

        print "Done!"


    def test_delete_table(self):
        print "Delete table"
        table_name = "brd-testtable"
        self.dbclient.delete_table(TableName=table_name)







    def test_dummy(self):
        pass
