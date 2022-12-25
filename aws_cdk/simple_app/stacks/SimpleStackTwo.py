#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aws_cdk as cdk
import constructs
from aws_cdk import (
    aws_s3 as s3,
    aws_iam as iam
)
from reusable_constructs.AppRole import AppRole

class SimpleAppStack2(cdk.Stack):
    def __init__(self, scope: constructs.Construct,
                 constructor_id: str,
                 myBucket=None,
                 **kwargs) -> None:
        super().__init__(scope, constructor_id, **kwargs)

        # Create another S3 bucket.
        bucket = s3.Bucket(self, "My2CDKBucket", versioned=False,
                           removal_policy=cdk.RemovalPolicy.DESTROY,
                           auto_delete_objects=True)

        # Create Role.
        role = iam.Role(self, "AppRole2",
                        assumed_by=iam.AccountPrincipal("727820809195"),
                        description="This is a sample role",
                        role_name="SampleAppRole")

        bucket.grant_read_write(role)

        # Stack1 Bucket.
        stackOneBucket = myBucket
        stackOneBucket.grant_read_write(role)

        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::727820809195:root"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }

        ddbPolicyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "VisualEditor0",
                    "Effect": "Allow",
                    "Action": [
                        "dynamodb:GetItem",
                        "dynamodb:GetRecords"
                    ],
                    "Resource": "arn:aws:dynamodb:*:462972568455:table/*"
                },
                {
                    "Sid": "VisualEditor1",
                    "Effect": "Allow",
                    "Action": "dynamodb:ListTables",
                    "Resource": "*"
                }
            ]
        }
        managedPolicyArns = [
            "arn:aws:iam::aws:policy/AmazonDynamoDBReadOnlyAccess",
            "arn:aws:iam::aws:policy/AWSCertificateManagerReadOnly"
            ]

        

        ddbPolicy = iam.CfnRole.PolicyProperty(
            policy_document=ddbPolicyDocument,
            policy_name="ddbTestPolicy")
        # Create Role (Cfn Construct)
        roleCfn = iam.CfnRole(self,
                              "AppRole22",
                              role_name="SampleAppRole22",
                              assume_role_policy_document=policyDocument,
                              policies=[ddbPolicy],
                              managed_policy_arns=managedPolicyArns)

        print("Role cfn path: %s" % roleCfn.path)
        print("Is cfn element: %s" % iam.CfnRole.is_cfn_element(roleCfn))
        print("Is cfn resource: ", iam.CfnRole.is_cfn_resource(roleCfn))

        print(bucket.bucket_name)

        # New role from Construct.
        newRole1 = AppRole(self, "AppRoleCustom")