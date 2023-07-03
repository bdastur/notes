#!/usr/bin/env python
# -*- coding: utf-8 -*-


import boto3
import botocore


def listBuckets(region, event):

    if event.get("local", False):
        session = boto3.Session(profile_name="dev", region_name=region)
    else:
        session = boto3.Session(region_name=region)

    client = session.client("s3")
    ret = client.list_buckets()
    return ret


