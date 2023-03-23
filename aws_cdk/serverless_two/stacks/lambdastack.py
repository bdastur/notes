from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
import aws_cdk.aws_iam as awsiam

import helpers.compute as compute
import helpers.iam as iam

from constructs import Construct

class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, options, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # Role creation: 
        # Scenario 1: Most basic. The client provides the policy document.
        accountPrincipal = kwargs["env"].account
        ddbPolicy = {"policy_document": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": [
                        "dynamodb:GetItem",
                        "dynamodb:GetRecords"
                    ],
                    "Resource": "arn:aws:dynamodb:*:%s:table/*" % accountPrincipal
                },
                {
                    "Sid": "VisualEditor1",
                    "Effect": "Allow",
                    "Action": "dynamodb:ListTables",
                    "Resource": "*"
                }
            ]
        },
            "policy_name": "ddpPolicy"
        }

        options = {
            "trusted_entity": "aws_service",
            "service_principal": "lambda",
            "account_principal": accountPrincipal,
            "policies": [ddbPolicy]
        }
        myRole = iam.IAM(self, "Mynewrole", **options)

        # Role creation.
        # Using delay create (no role should be created).
        options["delay_create"] = True
        myRole2 = iam.IAM(self, "Mysecondrole", **options)


        # Managed Policy creation.
        policy = iam.createManagedPolicy(self, "MyManagedPolicy", **options)



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


