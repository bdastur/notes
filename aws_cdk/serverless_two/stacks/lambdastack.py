from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
import aws_cdk.aws_iam as iam

import helpers.compute as compute

from constructs import Construct

class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, options, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # A new IAM.
        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                     "Principal": {
                         "Service": "lambda.amazonaws.com"
                     },
                     "Action": "sts:AssumeRole"
                }
            ]
        }
        newRole = iam.CfnRole(self, "myRole", assume_role_policy_document=policyDocument)


        # A new lambda.
        options = {
            "function_name": "Mytestfunction",
            "role": "arn:aws:iam::462972568455:role/service-role/helloLambda-role-c1tirmu9",
            "runtime": "python3.9",
            "handler": "index.handler",
            "code_property": {
                "zip_file": "lambdas/hello.py"
            }
        }
        newLambda = compute.AWSLambda(self, "MyNewFunction", **options)


