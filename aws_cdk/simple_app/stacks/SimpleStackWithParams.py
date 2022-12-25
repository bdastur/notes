#!/usr/bin/env python
# -*- coding: utf-8 -*-


import aws_cdk as cdk
import constructs
from aws_cdk import (
    aws_s3 as s3,
    aws_iam as iam
)

class SimpleStackWithParameter(cdk.Stack):
    def __init__(self, scope: constructs.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a new S3 bucket.
        bucketName = cdk.CfnParameter(self, "uploadBucketName", type="String", default="TestBucket1001-BRD")

        bucket = s3.Bucket(self, "NewParamBucket", bucket_name=bucketName.value_as_string)
