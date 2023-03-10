#!/usr/bin/env python
# -*- coding: utf-8 -*-

import aws_cdk.aws_iam as iam

"""
Create IAM Entities.
Input JSON Definition:
{
    "trusted_entity": "aws_service|aws_account|web_identity|saml|custom_trust_policy
    "service_principal": Specific service principal for the trusted entity.
    "account_principal": Account id

    "delay_create": |True|False # Explicitly call .create to create resource.
}
"""

class IAM(object):
    def __init__(self, scope, id, **options):
        self.scope = scope
        self.id = id
        self.options = options
        self.policyDocument = None

        delayCreate = self.options.get("delay_create", False)

        if not delayCreate:
            self.create()

    def createTrustedPolicyDocument(self):
        trustedEntity = self.options.get("trusted_entity", "aws_service")
        if trustedEntity == "aws_service":
            servicePrincipal = "%s.amazonaws.com" % self.options["service_principal"]

        policyDocument = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                     "Principal": {
                         "Service": "%s" % servicePrincipal
                     },
                     "Action": "sts:AssumeRole"
                }
            ]
        }
        return policyDocument

    def create(self):
        self.policyDocument = self.createTrustedPolicyDocument()
        accountPrincipal = self.options["account_principal"]

        policies = self.options["policies"]

        cfnPolicies = []
        for policy in policies:
            cfnPolicies.append(iam.CfnRole.PolicyProperty(
                    policy_document=policy["policy_document"],
                                    policy_name=policy["policy_name"]))

        iamRole = iam.CfnRole(
                self.scope, self.id,
                assume_role_policy_document=self.policyDocument,
                policies=cfnPolicies)

