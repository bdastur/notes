import os
from aws_cdk import (
    # Duration,
    Stack,
    aws_iam as iam
)
from constructs import Construct
import helpers.iam as iamhelper


class IAMOneStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # IAM Role.
        accountPrincipal = os.getenv("ACCOUNTID")

        # Trust policy
        roleName = "BRDTestRoleTwo"
        rolePath = "/testrole/"
        sessionDuration = 4200

        trustPolicyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::2xxxxxx:root"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        cfnRole = iam.CfnRole(self,
                              "test-role",
                              assume_role_policy_document=trustPolicyDocument,
                              max_session_duration=sessionDuration,
                              path=rolePath,
                              role_name=roleName)


        ec2TrustPolicyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ec2.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        newCfnRole = iam.CfnRole(self,
                                 "mytestrole",
                                 assume_role_policy_document=ec2TrustPolicyDocument,
                                 max_session_duration=sessionDuration,
                                 path="/",
                                 role_name="BRDTestRoleEc2")

        # IAM Helper.
        options = {
                "session_duration": 3600,
                "managed_policy_arns": ["arn:aws:iam::aws:policy/AmazonChimeReadOnly",
                             "arn:aws:iam::aws:policy/AlexaForBusinessLifesizeDelegatedAccessPolicy"]
        }
        cfnRoleTwo = iamhelper.IAMRole(self, id="newtestrole",
                                       name="BRDTestRoleEC2helper", **options)

        statements = [
            ["Allow",
             ["s3:ListBucket", "s3:GetBucket*"],
             ["arn:aws:s3:::config-bucket-45",
              "arn:aws:s3:::config-bucket-45/*"]
             ],
            [
                "Allow",
                ["s3:ListBucket", "s3:GetBucket*"],
                ["arn:aws:s3:::cf-te-1",
                "arn:aws:s3:::cf-te-1/*"]
            ]
        ]
        cfnRoleTwo.addInlinePolicy("MyNewInlinePolicy", statements)
        cfnRoleTwo.addTrustEntity(["ec2.amazonaws.com"])

        cfnRoleTwo.render()


