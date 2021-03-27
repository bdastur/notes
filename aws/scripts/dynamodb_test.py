#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import unittest
import boto3
import botocore

def generate_sample_item_data():
    random.seed()
    id = random.randint(1, 90000)
    age = random.randint(18, 67)
    fnames = ['jake', 'john', 'kevin', 'kat', 'karl', 'bob']
    surnames = ['mystery', 'wong', 'doe', 'sutter', 'powers']
    fid = random.randint(0, 5)
    sid = random.randint(0, 4)
    name = '%s %s' % (fnames[fid], surnames[sid])
    test_item = {
        'employee_id': {'N': str(id)},
        'employee_name': {'S': name},
        'age': {'N': str(age)}
    }
    return test_item


def create_table(dbclient, table_name):
    task_success = True
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
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
    try:
        dbclient.create_table(TableName=table_name,
                              AttributeDefinitions=attribute_definitions,
                              KeySchema=key_schema,
                              ProvisionedThroughput=provisioned_throughput)
    except botocore.exceptions.ClientError as ce:
        print "Failure.  %s " % ce.response['Error']
        task_success = False

    return task_success


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
        self.table_name = "brd-testtable"

    def test_list_tables(self):
        print "test"
        if self.dbclient:
            print self.dbclient.list_tables()

    def test_create_table(self):
        print "Create Table"
        if not self.dbclient:
            print "DBCLient not set"
            return

        if create_table(self.dbclient, 'brd-testtable'):
            print self.dbclient.describe_table(TableName='brd-testtable')

    def test_delete_table(self):
        print "Delete table"
        table_name = "brd-testtable"
        self.dbclient.delete_table(TableName=table_name)

    def test_put_item(self):
        print "Put items"
        try:
            self.dbclient.describe_table(TableName=self.table_name)
        except botocore.exceptions.ClientError as ce:
            print "Resource %s not found" % self.table_name
            print " exception: %s" % ce.response['Error']
            return
        # If table exists. Put Item.

        for x in range(0, 40):
            item = generate_sample_item_data()
            print "Item: ", item
            self.dbclient.put_item(TableName=self.table_name, Item=item)

        print "Done!"

    def test_scan_table(self):
        print "Scan table"
        print self.dbclient.scan(TableName=self.table_name)





    def test_dummy(self):
        pass
