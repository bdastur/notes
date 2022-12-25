#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aws_cdk as cdk
import constructs
from aws_cdk import (
    aws_s3 as s3
)

class SimpleAppStack(cdk.Stack):
    def __init__(self, scope: constructs.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(self, "MyCDKBucket", versioned=False,
                           removal_policy=cdk.RemovalPolicy.DESTROY,
                           auto_delete_objects=True)
        self.myBucket = bucket

        print(bucket.bucket_name)