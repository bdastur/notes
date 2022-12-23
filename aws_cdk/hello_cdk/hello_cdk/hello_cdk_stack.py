import aws_cdk as cdk
import aws_cdk.aws_s3 as s3

from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class HelloCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "MyFirstBucket",
                           removal_policy=cdk.RemovalPolicy.DESTROY,
                           versioned=True,
                           auto_delete_objects=True)



