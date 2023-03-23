#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import aws_cdk.aws_iam as iam

PERMISSIONS = {}

PERMISSIONS["s3"] =  {
        "list": {"actions": [
        "s3:ListAccessPoints",
        "s3:ListAccessPointsForObjectLambda",
        "s3:ListAllMyBuckets",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:ListBucketVersions",
        "s3:ListJobs",
        "s3:ListMultiRegionAccessPoints",
        "s3:ListMultipartUploadParts",
        "s3:ListStorageLensConfigurations"
    ]},
        "read": {"actions":[
        "s3:DescribeJob",
        "s3:DescribeMultiRegionAccessPointOperation",
        "s3:GetAccelerateConfiguration",
        "s3:GetAccessPoint",
        "s3:GetAccessPointPolicy",
        "s3:GetAccessPointPolicyForObjectLambda",
        "s3:GetAccessPointPolicyStatus",
        "s3:GetAccessPointPolicyStatusForObjectLambda",
        "s3:GetAccountPublicAccessBlock",
        "s3:GetAnalyticsConfiguration",
        "s3:GetBucketAcl",
        "s3:GetBucketCORS",
        "s3:GetBucketLocation",
        "s3:GetBucketLogging",
        "s3:GetBucketNotification",
        "s3:GetBucketObjectLockConfiguration",
        "s3:GetBucketOwnershipControls",
        "s3:GetBucketPolicy",
        "s3:GetBucketPolicyStatus",
        "s3:GetBucketPublicAccessBlock",
        "s3:GetBucketRequestPayment",
        "s3:GetBucketTagging",
        "s3:GetBucketVersioning",
        "s3:GetBucketWebsite",
        "s3:GetEncryptionConfiguration",
        "s3:GetIntelligentTieringConfiguration",
        "s3:GetInventoryConfiguration",
        "s3:GetJobTagging",
        "s3:GetLifecycleConfiguration",
        "s3:GetMetricsConfiguration",
        "s3:GetMultiRegionAccessPoint",
        "s3:GetMultiRegionAccessPointPolicy",
        "s3:GetMultiRegionAccessPointPolicyStatus",
        "s3:GetMultiRegionAccessPointRoutes",
        "s3:GetObject",
        "s3:GetObjectAcl",
        "s3:GetObjectAttributes",
        "s3:GetObjectLegalHold",
        "s3:GetObjectRetention",
        "s3:GetObjectTagging",
        "s3:GetObjectTorrent",
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl",
        "s3:GetObjectVersionAttributes",
        "s3:GetObjectVersionForReplication",
        "s3:GetObjectVersionTagging",
        "s3:GetObjectVersionTorrent",
        "s3:GetReplicationConfiguration",
        "s3:GetStorageLensConfiguration",
        "s3:GetStorageLensConfigurationTagging",
        "s3:GetStorageLensDashboard"
    ]},
    "write": {"actions": [
        "s3:PutAccelerateConfiguration",
        "s3:PutAccessPointConfigurationForObjectLambda",
        "s3:PutAccessPointPolicy",
        "s3:PutAccessPointPolicyForObjectLambda",
        "s3:PutAccessPointPublicAccessBlock",
        "s3:PutAccountPublicAccessBlock",
        "s3:PutAnalyticsConfiguration",
        "s3:PutBucketAcl",
        "s3:PutBucketCORS",
        "s3:PutBucketLogging",
        "s3:PutBucketNotification",
        "s3:PutBucketObjectLockConfiguration",
        "s3:PutBucketOwnershipControls",
        "s3:PutBucketPolicy",
        "s3:PutBucketPublicAccessBlock",
        "s3:PutBucketRequestPayment",
        "s3:PutBucketTagging",
        "s3:PutBucketVersioning",
        "s3:PutBucketWebsite",
        "s3:PutEncryptionConfiguration",
        "s3:PutIntelligentTieringConfiguration",
        "s3:PutInventoryConfiguration",
        "s3:PutJobTagging",
        "s3:PutLifecycleConfiguration",
        "s3:PutMetricsConfiguration",
        "s3:PutMultiRegionAccessPointPolicy",
        "s3:PutObject",
        "s3:PutObjectAcl",
        "s3:PutObjectLegalHold",
        "s3:PutObjectRetention",
        "s3:PutObjectTagging",
        "s3:PutObjectVersionAcl",
        "s3:PutObjectVersionTagging",
        "s3:PutReplicationConfiguration",
        "s3:PutStorageLensConfiguration",
        "s3:PutStorageLensConfigurationTagging",
        "s3:ReplicateDelete",
        "s3:ReplicateObject",
        "s3:ReplicateTags",
        "s3:RestoreObject",
        "s3:SubmitMultiRegionAccessPointRoutes",
        "s3:UpdateJobPriority",
        "s3:UpdateJobStatus"
    ]},
    "admin": {"actions": [
        "s3:AbortMultipartUpload",                                                   
        "s3:BypassGovernanceRetention",                                              
        "s3:CreateAccessPoint",                                                      
        "s3:CreateAccessPointForObjectLambda",                                       
        "s3:CreateBucket",                                                           
        "s3:CreateJob",                                                              
        "s3:CreateMultiRegionAccessPoint",         
        "s3:DeleteAccessPoint",
        "s3:DeleteAccessPointForObjectLambda",
        "s3:DeleteAccessPointPolicy",
        "s3:DeleteAccessPointPolicyForObjectLambda",
        "s3:DeleteBucket",
        "s3:DeleteBucketPolicy",
        "s3:DeleteBucketWebsite",
        "s3:DeleteJobTagging",
        "s3:DeleteMultiRegionAccessPoint",
        "s3:DeleteObject",
        "s3:DeleteObjectTagging",
        "s3:DeleteObjectVersion",
        "s3:DeleteObjectVersionTagging",
        "s3:DeleteStorageLensConfiguration",
        "s3:DeleteStorageLensConfigurationTagging",
    ]}
}


def createPolicyDocument(statements):
    policyDocument = {
        "Version": "2012-10-17",
        "Statement": statements
    }
    return policyDocument

"""
    Operation: list, read, write, admin
"""
def addAllowPermission(service, operation, resources):

    validOperations = ["list", "read", "write", "admin"]
    supportedServices = ["s3"]

    # Validations.
    operation = operation.lower()
    if operation not in validOperations:
        print("Operation should be one of %s" % validOperations)
        return

    service = service.lower()
    if service not in supportedServices:
        print("Supported services should be one of %s" % supportedServices)
        return


    randomNumber = random.randrange(1000, 1000000)
    statement = {
        "Sid": "Allowed%son%s%s" % (operation, service, str(randomNumber)),
        "Effect": "Allow",
        "Action": PERMISSIONS[service][operation]["actions"],
        "Resource": resources 
    }
    return statement

def createManagedPolicy(scope, cId, **options):
    accountPrincipal = "462972568455"

    statements = []
    myStatement = addAllowPermission("s3", "list", ["*"])
    statements.append(myStatement)
    policyDocument = createPolicyDocument(statements)

    import pprint
    pp = pprint.PrettyPrinter()
    pp.pprint(policyDocument)

    """
    statements = [
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
            "Action": [
                "dynamodb:ListTables",
                "dynamodb:GetItem"
            ],
            "Resource": "*"
        }]
    policyDocument = createPolicyDocument(statements)
    """

    managedPolicy = iam.CfnManagedPolicy(
            scope, cId, policy_document=policyDocument,
            managed_policy_name="Mytestpolicy")

    return managedPolicy


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


class IAMRole(object):
    def __init__(self, scope, id, **options):
        self.scope = scope
        self.id = id
        self.options = options
        self.trustedPolicyDocument = None

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



class IAM(object):
    def __init__(self, scope, id, **options):
        self.scope = scope
        self.id = id
        self.options = options
        self.policyDocument = None

        delayCreate = self.options.get("delay_create", False)

        if not delayCreate:
            self.createRole()

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

    def createManagedPolicy(self, scope, id, **options):
        accountPrincipal = "462972568455"
        policyDocument = {
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
                    "Action": [
                        "dynamodb:ListTables",
                        "dynamodb:GetItem"
                    ],
                    "Resource": "*"
                }
            ]
        }
        managedPolicy = iam.CfnManagedPolicy(
                scope, id, policy_document=policyDocument,
                managed_policy_name="Mytestpolicy")


    def createRole(self):
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




