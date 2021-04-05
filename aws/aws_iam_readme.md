# AWS Identity and Access Management

## Useful Links:

* [AWS Reinvent: Become an IAM Policy Master](https://www.youtube.com/watch?v=YQsK4MtsELU)
* [AWS Reinvent: Getting started with AWS identity](https://www.youtube.com/watch?v=Zvz-qYYhvMk)
* [IAM JSON policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
* [Actions, Resources & Condition keys for AWS Services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html)
* [Access policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types)
* [IAM JSON policy elements: conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)
* [Example policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)
* [Example of policy summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-summary-examples.html)
* [S3 condition key examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html)

## Policy Types:

*Identity-based policies*
* Managed and inline policies that can be attached to IAM entities
  (users, groups, roles)

*Resource-based policies*
* Inline policies attached to resources, like S3, KMS, etc.
* Requires a Principal. Principal can be in the same or different account.

*Permission boundaries*
* A managed policy used as a permissions boundary for an IAM entity (user or role).
* This policy defines the maximum permissions that the identity-based policies can
  grant to an entity, but does not grant permissions.
* Resource-based policies that specify the user or role as the principal
  are not limited by the permissions boundary.
* An explicit deny in any of these policies overrides the allow.

*Organizations SCPs*
* AWS Organizations service control policy (SCP) define the maximum permissions
  for the account members of an organization or organizational unit.
* SCPs limit permissions  that identity-based policies or resource-based
  policies grant to entities within the account, but do not grant permissions.

*Access control lists*
* ACLS control which principals in other accounts can access the resource to
  which the ACL is attched.
* ACLs are similar to resource-based policies.
* ACLS are cross-account permission policies that grant permissions to specified
  principal.
* ACLs cannot grant permissions to entities within the same account.

*Session policies*
* Pass advanced session policies when you use the AWS CLI or API to assume a
  role or a federated user.
* Session policies limit the permissions that the role or user's identity-basedd
  policies grant to the session.
* Session policies limit permissions for a created session, but do  not grant
  permissions.


## Policy reference
[IAM Policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)

### JSON element reference

#### Version (Required)

```
"Version": "2012-10-17"
```

* If you do not include Version elemennt, some features will not work.

#### Id  (optional)
#### Statement (Required)
#### Sid (statement id)
* Multiple policy statement blocks, cannot have same sid in the same policy.

#### Effect (Required)
* Allow or Deny

#### Principal
You can specify any of the following principals in a policy
* AWS Account and root user
* IAM User, IAM roles.
* Federated users (using web identity or SAML federation)
* Assumed-role sessions
* AWS Services
* Anonymous users (not recommended)

#### NotPrincipal.
* Used to specify an IAM user, role, federated user, account, service or
  other principal that is *not* allowed, or denied access to the resource.
* Enables you to specify an exception to the list of principals.

#### Action
#### NotAction
* It explicitly matches everything except the specified list of actions. 
* Using NotAction can result in a shorter policy, listing only a few actions 
  that should not match, rather than a long list of actions that will match.
* Keep in mind that actions specified in this element are the only actions 
  that are limited. Means that all of the applicable actions or services that 
  are not listed are allowed if you use the Allow effect.
* When you use NotAction with the Resource element, you provide scope for the policy. 

**NOTE**: 
Be careful when using NotAction with Allow. You could grant more
permissions than you intended.

*NotAction with Allow*

Example 1:
* This allows  access to all S3 actions except Delete bucket.
* This does not allow ListAllMyBuckets, as it reqiures "\*" resource.
* This does not allow actions in other services, as resource is specified as S3.

```
"Effect": "Allow",
"NotAction": "s3:DeleteBucket",
"Resource": "arn:aws:s3:::*",
```

Example 2:

* This allows access to all actions on all AWS services except IAM.

```
"Effect": "Allow",
"NotAction": "iam:*",
"Resource": "*"
```

*NotAction with Deny*

* This example denies access to non-IAM actions if the user is not signed 
  in using MFA. If the user is signed in with MFA, then the "Condition" test 
  fails and the "Deny" statement has no effect. Note, however, that this 
  would not grant the user access to any actions; it would only explicitly 
  deny all other actions except IAM actions.

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "DenyAllUsersNotUsingMFA",
        "Effect": "Deny",
        "NotAction": "iam:*",
        "Resource": "*",
        "Condition": {"BoolIfExists": {"aws:MultiFactorAuthPresent": "false"}}
    }]
}
```

Another example: 
[Deny Access based on region](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.html)


#### Resource
#### NotResource
* Explicitly match every resource except the ones specified.


### Condition
* Let's you specify conditions for when a policy is in effect.

```
"Condition" : { 
    "{condition-operator}" : { "{condition-key}" : "{condition-value}" }
}
```

#### condition-key:

##### Global condition key:
[Global condition context](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)


##### condition-operator:
* Used to match the condition-key and the condition values in the request
  context.
* [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
 

*condition operator categories:*

* *String*
* *Numeric*
* *Date & time*
* *Boolean*
* *Binary*
* *IP address*
* *ARN* (available for only some services)
* *...IfExists* (checks if the key value exists as part of another check)
* *Null check* (checks if the kkey value exists)



---

### How to generate IAM credentials report.
```
#!/bin/bash
aws iam generate-credential-report  --profile core-services-prod
aws iam get-credential-report \
    --query Content --output text \
    --profile dev | base64 -D

```

### Creating a role with Path.
*NOTE*: AWS Console does not have a way to create a Role with Path. Only
        CLI and AWS SDK allow.

Create a role testrole,  in path /operations/

```
$ aws iam create-role \
  --role-name testrole --path /operations/ \
  --assume-role-policy-document file:///tmp/assume_role_policy_doc.json \
  --profile acguru
{
    "Role": {
        "Path": "/operations/",
        "RoleName": "testrole2",
        "RoleId": "AROA4GNPSIULAJQ3TRSOZ",
        "Arn": "arn:aws:iam::838423692566:role/operations/testrole2",
        "CreateDate": "2021-04-01T00:41:39+00:00",
        "AssumeRolePolicyDocument": {
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
    }
}

```

Role created with ARN: ```arn:aws:iam::838423692566:role/operations/testrole```


## Policy Examples.

*Allow a user to change his own user password*

```
{
    "Effect": "Allow",
     "Action": [
         "iam:ChangePassword"
     ],
     "Resource": [
         "arn:aws:iam::*:user/${aws:username}"
     ]
}
```

*Allow a specific user IAM permissions*

```
{
      "Sid": "Stmt1464991474200",
      "Effect": "Allow",
      "Action": [
        "iam:*",
        "config:*"
      ],
      "Condition": {
        "StringLike": {
          "aws:userid": "*john_doe"
        }
      },
      "Resource": [
        "*"
      ]
}
```

*Allow creating roles with specific path prefix*

When this policy is attached to an IAM entity it allows it to create roles
and instance profiles with --path /operations/. The IAM entity cannot create a
role in / 'default' path or any other --path prefix.

```
{
    "Sid": "Stmt1617235151794",
    "Action": [
        "iam:CreateRole",
        "iam:CreateInstanceProfile"
    ],
    "Effect": "Allow",
    "Resource": [
        "arn:aws:iam::*:role/operations/*",
        "arn:aws:iam::*:instance-profile/operations/*"
    ]
}
```


*S3 policy: Deny any requests that do not originate from specific vpc*

```
{
    "Sid": "DenyNonVPCRequests",
    "Effect": "Deny",
    "Principal": {
        "AWS": "*"
    },
    "Action": "s3:*",
    "Resource": [
        "arn:aws:s3:::mytestbucket123",
        "arn:aws:s3:::mytestbucket123/*"
    ],
    "Condition": {
        "Bool": {
            "aws:SecureTransport": "false"
        },
        "StringNotEquals": {
            "aws:SourceVpc": "vpc-b4ec6aa1"
        }
    }
}
```

*S3 policy: Deny put objects with incorrect encryption.*

```
{
    "Sid": "DenyIncorrectEncryptionHeader",
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:PutObject",
    "Resource": [
        "arn:aws:s3:::mytestbucket123",
        "arn:aws:s3:::mytestbucket123/*"
    ],
    "Condition": {
        "StringNotEquals": {
            "s3:x-amz-server-side-encryption": "aws:kms"
        }
    }
}
```

*S3 policy: Deny unencrypted object uploads*

```
{
    "Sid": "DenyUnEncryptedObjectUploads",
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:PutObject",
    "Resource": [
        "arn:aws:s3:::mytestbucket123",
        "arn:aws:s3:::mytestbucket123/*"
    ],
    "Condition": {
        "Null": {
            "s3:x-amz-server-side-encryption": "true"
        }
    }
}
```





















