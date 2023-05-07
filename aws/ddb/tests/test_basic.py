#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        "AttributeName": "EmployeeName",
        "AttributeType": "S"
    }

    sortKey = {
        "AttributeName": "Tenure",
        "AttributeType": "N"
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
    #ret = ddbsimple.createDDBTable(client, tableName, checkExists=True)
    assert ret == 0

    # item.
    item = {"EmployeeId": {"S": "EI9002"}, "Tenure": {"N": "20"}}
    ret = ddbsimple.createDDBItem(client, tableName, **item)








