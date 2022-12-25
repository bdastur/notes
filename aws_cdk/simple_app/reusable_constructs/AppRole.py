#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An example of a reusable construct.
"""

import random
import string
import constructs
from aws_cdk import (
    aws_iam as iam
)

class AppRole(constructs.Construct):
    def __init__(self, scope: constructs.Construct, id: str,
                 roleName=None, policies=[],
                 **kwargs):
        super().__init__(scope, id, **kwargs)

        statement = {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::727820809195:root"
            },
            "Action": "sts:AssumeRole"
        }

        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [statement]
        }

        if roleName is None:
            roleName = "%s_%s" % ("AppRole", ''.join(random.choices(string.ascii_uppercase, k=6)))

        # Create Role (Cfn Construct)
        self.appRole = iam.CfnRole(self,
                                   "AppRole",
                                   role_name=roleName,
                                   assume_role_policy_document=policyDocument,
                                   policies=policies)
