#!/usr/bin/env python3
import os
import aws_cdk as cdk
import constructs

#from simple_app.simple_app_stack import SimpleAppStack


class SimpleAppStack(cdk.Stack):

    def __init__(self, scope: constructs.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket
        bucket = cdk.aws_s3.Bucket(self, "MyCDKBucket", versioned=False, 
                                   removal_policy=cdk.RemovalPolicy.DESTROY,
                                   auto_delete_objects=True)
                                   
        print(bucket.bucket_name)


app = cdk.App()
SimpleAppStack(app, "SimpleAppStack")

app.synth()

