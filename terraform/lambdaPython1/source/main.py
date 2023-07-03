#!/usr/bin/env python
# -*- coding: utf-8 -*-


import boto3
import botocore
import json
import os
import awslibs.s3_helper as s3_helper


def handler(event, context):
    print("Event definition =======================")
    print(json.dumps(event))
    print("Event definition End ===================")

    # Get environment variables.
    region = os.environ.get("region", "us-east-1")

    bucketList = s3_helper.listBuckets(region, event)

    body = "List of buckets: %s" % (bucketList["Buckets"])

    returnValue = {
        'statusCode': 200,
        'headers': {
            'Content/Type': 'text/plain'
        },
        'body': body 
    }

    return returnValue


# Test Locally.
def main():
    testEvent = {'local': True}
    val = handler(testEvent, None)
    print(val)

if __name__ == '__main__':
    main()
