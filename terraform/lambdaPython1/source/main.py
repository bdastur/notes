#!/usr/bin/env python
# -*- coding: utf-8 -*-


import boto3
import botocore
import json
import os


def handler(event, context):
    print("Event definition =======================")
    print(json.dumps(event))
    print("Event definition End ===================")

    # Get environment variables.
    region = os.environ.get("region", "us-east-1")

    bucketList = listBuckets(region, event)
    body = "List of buckets: %s" % (bucketList["Buckets"])

    returnValue = {
        'statusCode': 200,
        'headers': {
            'Content/Type': 'text/plain'
        },
        'body': body 
    }

    return returnValue


def listBuckets(region, event):

    if event.get("local", False):
        session = boto3.Session(profile_name="dev", region_name=region)
    else:
        session = boto3.Session(region_name=region)

    client = session.client("s3")
    ret = client.list_buckets()
    return ret


# Test Locally.
def main():
    testEvent = {'local': True}
    val = handler(testEvent, None)
    print(val)

if __name__ == '__main__':
    main()
