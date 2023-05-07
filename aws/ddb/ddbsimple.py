#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import botocore


def getDDBClient(profileName, regionName="us-east-1"):
    print("getDDBClient: [%s], [%s]" %(profileName, regionName))

    try:
        session = boto3.Session(profile_name=profileName)
        client = session.client("dynamodb", region_name=regionName)
    except botocore.exceptions.ProfileNotFound as err:
        print("Profile [%s] not found [%s]" % (profileName, err))
        return -1, None


    return 0, client

"""
    tableName:    [Required] Table anme.
    partitionKey: [Required] Unique key used by DDB as an input to an internal
                  hash function.
    format:
    {
        "AttributeName": "<value>,
        "AttributeType": "S"|"N"|"B"
    }
    sortKey:     [Optional]
    format:
    {
        "AttributeName": "<value>,
        "AttributeType": "S"|"N"|"B"
    }
"""
def createDDBTable(client, tableName,
                   primaryKey, sortKey=None,
                   billingMode="PROVISIONED", RCU=1, WCU=1,
                   checkExists=False):


    if checkExists:
        ret, _ = getDDBTable(client, tableName)
        if ret == 0:
            print("Table %s exists" % tableName)
            return 0

    attributeDefinition = [primaryKey]
    if sortKey is not None:
        attributeDefinition.append(sortKey)

    keySchema = [
            {
                "AttributeName": primaryKey["AttributeName"],
                "KeyType": "HASH"
            }
    ]
    if sortKey is not None:
        keySchema.append({
            "AttributeName": sortKey["AttributeName"],
            "KeyType": "RANGE"
            })

    provisionedThroughput = {
        "ReadCapacityUnits": RCU,
        "WriteCapacityUnits": WCU
    }

    try:
        client.create_table(TableName=tableName,
                            AttributeDefinitions=attributeDefinition,
                            KeySchema=keySchema,
                            BillingMode=billingMode,
                            ProvisionedThroughput=provisionedThroughput)
    except botocore.errorfactory.ClientError as err:
        print("Table [%s] alread exists. [%s]" % (tableName, err))
        return -1
    except botocore.exceptions.EndpointConnectionError as err:
        print("Failed to create table [%s] [%s]" % (tableName, err))
        return -1

    return 0


def getDDBTable(client, tableName):
    try:
        ret = client.describe_table(TableName=tableName)
    except botocore.errorfactory.ClientError as err:
        print("Table [%s] not found. [%s]" % (tableName, err))
        return -1, None

    return 0, ret["Table"]


def deleteDDBTable(client, tableName):
    try:
        client.delete_table(TableName=tableName)
    except botocore.errorfactory.ClientError as err:
        import pdb;pdb.set_trace()
        print("Table [%s] deletion failed. [%s]" % (tableName, err))
        return -1

    return 0

def createDDBItem(client, tableName, **item):

    try:
        ret = client.put_item(TableName=tableName, Item=item)
    except botocore.exceptions.ClientError as err:
        print("Item put failed [%s]" % err)
        return -1

    return 0


class DDBHelper():
    def __init__(self):
        pass

    def createTable(self):
        pass

    def addItem(self):
        pass


