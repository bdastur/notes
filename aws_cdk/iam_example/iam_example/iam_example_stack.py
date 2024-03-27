import os
from aws_cdk import (
    # Duration,
    Stack,
    aws_iam as iam
)
from constructs import Construct
import helpers.iam as iamhelper


class IamExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # IAM Role.
        accountPrincipal = os.getenv("ACCOUNTID")

        # Assumed account/service principal takes only one principal.
        assumedbyPrincipal = iam.ServicePrincipal("lambda.amazonaws.com")
        role = iam.Role(self, "BRDTestRoleTwo",
                        assumed_by=assumedbyPrincipal,
                        description="This is a sample Role",
                        role_name="BRD-TestRole")

        # Policy
        allowS3Statement = iam.PolicyStatement(actions=["s3:GetObject*"], resources=["*"])
        allowEc2Statement = iam.PolicyStatement(actions=["ec2:describe*"], resources=["*"])
        iamPolicy = iam.Policy(self, "test-policy", statements=[allowS3Statement, allowEc2Statement])
        role.attach_inline_policy(iamPolicy)

        secondPolicyDoc = iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    actions=["elasticfilesystem:ClientWrite", "elasticfilesystem:ClientMount"],
                    resources=["*"]
                ),
                iam.PolicyStatement(
                    actions=["s3:PutObject*", "s3:List*"],
                    resources=["*"])
            ]
        )
        secondPolicy = iam.Policy(self, "test-second-policy", document=secondPolicyDoc)
        role.attach_inline_policy(secondPolicy)

        # IAM Role using the library.

        # Trust policy
        trustPolicyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::214732530209:root" 
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        cfnRole = iam.CfnRole(self,
                              "test-role",
                              assume_role_policy_document=trustPolicyDocument,
                              max_session_duration=4200,
                              path="/testrole/",
                              role_name="BRDTESTROLECFN")
    
        # Policy doc.
        s3AccessPolicyDoc = {
            "Version": "2012-10-17",
            "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:Get*",
                    "s3:List*",
                    "s3:Describe*",
                    "s3-object-lambda:Get*",
                    "s3-object-lambda:List*"
                ],
                "Resource": "*"
            }
        ]}
        s3CfnPolicy = iam.CfnRolePolicy(self, "s3-policy-doc", 
                                       policy_name="S3Policy", 
                                       policy_document=s3AccessPolicyDoc,
                                       role_name="BRDTESTROLECFN")



