#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import botocore

import time
import pytest
import ddbsimple

@pytest.fixture
def test_basic_one():
    assert 10 == 11

def test_basic_two():
    assert 12 == 12


def testBasicThree():
    assert 13 == 13


def createTestTable(client, tableName, checkExists=False):
    primaryKey = {
        "AttributeName": "Artist",
        "AttributeType": "S"
    }

    sortKey = {
        "AttributeName": "Song",
        "AttributeType": "S"
    }

    ret = ddbsimple.createDDBTable(client, tableName,
                                   primaryKey, sortKey=sortKey,
                                   checkExists=checkExists)
    return ret


def test_getDDBClient():
    # Invalid profile.
    invalidProfile = "foobar"
    ret, client = ddbsimple.getDDBClient(invalidProfile, regionName="us-east-1")
    assert ret == -1

    # Invalid region (does not throw an error)
    validProfile = "dev"
    ret, client = ddbsimple.getDDBClient(validProfile, regionName="foobar")
    assert ret == 0

    # Try creating a table with invalid client.
    ret = createTestTable(client, "brd_table", checkExists=False)
    assert ret == -1


def test_create_ddbTable():
    _, client = ddbsimple.getDDBClient("dev", regionName="us-east-1")

    tableName = "brd_table"
    #ret = ddbsimple.createDDBTable(client, tableName)
    ret = createTestTable(client, tableName, checkExists=False)
    assert ret == 0

    # get table.
    ret, tableInfo = ddbsimple.getDDBTable(client, tableName)
    assert ret == 0

    # get table invalid.
    ret, tableInfo = ddbsimple.getDDBTable(client, "foobar")
    assert ret == -1

    time.sleep(10)
    ret = ddbsimple.deleteDDBTable(client, tableName)
    assert ret == 0


def test_createDDBItem():
    _, client = ddbsimple.getDDBClient("dev", regionName="us-east-1")

    tableName = "brd_table"
    # Create a new table.
    ret = createTestTable(client, tableName, checkExists=True)
    assert ret == 0

    # item.
    item = {"Artist": {"S": "Lady Gaga"}, "Song": {"S": "Shallow"}, "Album": {"S": "Who cares"}, "MillionsSold": {"N": "10"}}
    ret = ddbsimple.createDDBItem(client, tableName, **item)

    item = {"Artist": {"S": "Lady Gaga"}, "Song": {"S": "Paparazzi"}, "Album": {"S": "Who cares"}, "MillionsSold": {"N": "11"}}
    ret = ddbsimple.createDDBItem(client, tableName, **item)

    item = {"Artist": {"S": "Lady Gaga"}, "Song": {"S": "Bad Romance"}, "Album": {"S": "Who cares"}, "MillionsSold": {"N": "8"}}
    ret = ddbsimple.createDDBItem(client, tableName, **item)

    item = {"Artist": {"S": "Metallica"}, "Song": {"S": "Nothing Else Matters"}, "Album": {"S": "One"}, "MillionsSold": {"N": "33"}}
    ret = ddbsimple.createDDBItem(client, tableName, **item)

    item = {"Artist": {"S": "Taylor Swift"}, "Song": {"S": "Ready"}, "Album": {"S": "Dont know"}, "MillionsSold": {"N": "50"}}
    ret = ddbsimple.createDDBItem(client, tableName, **item)



def test_queryDDBTable():
    tableName = "brd_table"
    _, client = ddbsimple.getDDBClient("dev", regionName="us-east-1")

    # get table.
    ret, tableInfo = ddbsimple.getDDBTable(client, tableName)
    assert ret == 0

    # Query table (By Artist lady gaga and specific song)
    expressionAttributeValues = {
        ":artist": {"S": "Lady Gaga"},
        ":song": {"S": "Shallow"}
    }

    data = client.query(TableName=tableName, KeyConditionExpression="Artist = :artist and Song = :song", ExpressionAttributeValues=expressionAttributeValues)
    print("Find artist lady gaga and song shallow")
    print(data["Items"])
    print("")

    # Query table (By Artist and all songs starting with anything after A1)
    expressionAttributeValues = {
        ":artist": {"S": "Lady Gaga"},
        ":song": {"S": "A"}
    }

    data = client.query(TableName=tableName, KeyConditionExpression="Artist = :artist and Song > :song", ExpressionAttributeValues=expressionAttributeValues)
    print("Find artist lady gaga and any songs starting with letter A and above")
    print(data["Items"])
    print("")


    # Query table (By Artist and all songs between A and P)
    expressionAttributeValues = {
        ":artist": {"S": "Lady Gaga"},
        ":songStart": {"S": "A"},
        ":songEnd": {"S": "Q"}
    }

    data = client.query(TableName=tableName, KeyConditionExpression="Artist = :artist and Song BETWEEN  :songStart AND :songEnd", ExpressionAttributeValues=expressionAttributeValues)
    print("Find artist lady gaga and songs with starting letters between A and Q (Q is not included)")
    print(data["Items"])
    print("")

   # Query table (By Artist and all songs between A and P, Filter albums sold)
    expressionAttributeValues = {
        ":artist": {"S": "Lady Gaga"},
        ":songStart": {"S": "A"},
        ":songEnd": {"S": "Q"}
    }

    # This is not valid:
    # botocore.exceptions.ClientError: An error occurred (ValidationException) when calling the Query operation:
    # Can not use both expression and non-expression parameters in the same request: Non-expression parameters:
    # {QueryFilter} Expression parameters: {KeyConditionExpression}
    #data = client.query(TableName=tableName,
    #                    KeyConditionExpression="Artist = :artist and Song BETWEEN  :songStart AND :songEnd",
    #                    ExpressionAttributeValues=expressionAttributeValues,
    #                    QueryFilter={"MillionsSold": {"ComparisonOperator": "GT", "AttributeValueList": [{"N": "10"}]}})
    #print("Find artist lady gaga and songs with starting letters between A and Q (Q is not included). Filter by Albums sold more than 10 Million")
    #print(data["Items"])
    #print("")


    # Query table (By Artist and all songs starting with anything after A1, and
    # albums sold >= 10mil)
    expressionAttributeValues = {
        ":artist": {"S": "Lady Gaga"},
        ":song": {"S": "A"},
        ":num": {"N": "10"}
    }

    data = client.query(TableName=tableName,
                        KeyConditionExpression="Artist = :artist and Song > :song",
                        FilterExpression="MillionsSold >= :num",
                        ExpressionAttributeValues=expressionAttributeValues)
    print("Find artist lady gaga and any songs starting with letter A and above, and albums sold >= 10mil")
    print(data["Items"])
    print("")



