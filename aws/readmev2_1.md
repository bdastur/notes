# AWS Notes (Version 2.0).

NOTE:
* Some practices to manage notes.
 * Only two levels.
 * Use **Bold** text for subsections.



**Useful links:**
* [AWS Well-architected framework](https://wa.aws.amazon.com/wat.concepts.wa-concepts.en.html)
* [S3 FAQ](https://aws.amazon.com/s3/faqs/)
* [S3 - Deleting versioned objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)
* [S3 - multipart upload](http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html)
* [S3 - best practices design patterns](https://docs.aws.amazon.com/whitepapers/latest/s3-optimizing-performance-best-practices/introduction.html)
* [S3 - blocking S3 traffic by VPC/IP](https://aws.amazon.com/premiumsupport/knowledge-center/block-s3-traffic-vpc-ip/)
* [S3 VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html)
* []()
* []()
* []()
* []()
* []()
* []()


## Concepts:

**Availability, Reliability, Resiliency, Durability**

* Availability:
  A measurement of a system's ability to provide it's designed functionality.

* Durability:
  The ability of a system to remain functional when faced with the challenges of
  normal operation over its lifetime.

* Reliability:
  A measure of your workloads ability to provide functionality when desired by the
  user

* Resiliency:
  The ability for a system to recover from a failure induced by load, attacks, and
  failures.

--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
## AWS Identify and Access Management
#--------------------------------------------------------------------------------

**Useful Links:**
* [AWS Reinvent: Become an IAM Policy Master](https://www.youtube.com/watch?v=YQsK4MtsELU)
* [AWS Reinvent: Getting started with AWS identity](https://www.youtube.com/watch?v=Zvz-qYYhvMk)
* [IAM JSON policy reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html)
* [IAM Access Analyzer now generates policies](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)
* [Actions, Resources & Condition keys for AWS Services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html)
* [Access policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types)
* [IAM JSON policy elements: conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html)
* [Example policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html)
* [Example of policy summaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-summary-examples.html)
* [S3 condition key examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html)

--------------------------------------------------------------------------------
**AWS Arn:**
ARNs all begin with:

```
  arn:partition:service:region:account_id:
```

Partition  == aws|aws-cn
Service    == s3|ec2|rds...
region     == us-east-1|us-west-2...
account_id == 20393829222 (eg.)

Ends with:
resiource
resource_type/resource
resource_type/resource/qualifier
resource_type:resource
resource_type:resource:qualifier.

--------------------------------------------------------------------------------

## Policy Types:

**Identity-based policies**
* Managed and inline policies that can be attached to IAM entities (users, groups,
  roles)

**Resource-based policies**
* Inline policies attached to resources, like S3, KMS, etc.
* Requires a principal. Principal can be in the same or different account.

**Permission boundaries**
* A managed policy used as a permissions boundary for an IAM entity (user or role).
* This policy defines the maximum permissions that the identity-based policies can
  grant to an entity, but does not grant permissions.
* Resource-based policies that specify the user or role as the principal are not
  limited by the permissions boundary.
* An explicit deny in any of these policies overrides the allow.

**Access control lists**
* ACLs control which principals in other accounts can access the resource to which
  the ACL is attached.
* ACLs are similar to resource-based policies.
* ACLs are cross-account permission policies that grant permissions to specified
  principal.
* ACLs cannot grant permissions to entities within the same account.

**Session policies**
* Pass advanced session policies when you use the AWS CLI or API to assume a role
  or a federated user.
* Session policies limit the permissions that the role or user's identity-based
  policies grant to the session.
* Session policies limit permissions for a created session, but do not grant
  permissions.

--------------------------------------------------------------------------------

## Policy Reference:

**version:**
```
"Version": "2012-10-17"
```
* If you do not include version element, some features will not work.

**Id**        (optional)
**Statement** (Required)
**Sid (statement id)**
* Multiple policy statement blocks must not have the same sid in the same policy.

**Principal**
You can specify any of the following principals in a policy
* AWS Account and root user
* IAM user, IAM roles
* Federated user (using web identity or SAML federation)
* Assumed-role sessions
* AWS services
* Anonymous users (not recomended)

**Action**
**NotAction**
* It explicitly matches everything except the specified list of actions.
* Using NotAction can result in a shorter policy, listing only a few actions
  that should not match, rather than a long list of actions that will match.
* Keep in mind that actions specified in this element are the only actions that
  are limited. Means all the applicable actions or services that are not listed
  are allowed if you use the Allow effect.
* When you use NotAction with the Resource element, you provide scope for the policy.

**NOTE**
Be careful when using NotAction with Allow. you could grant more permissions than
you intended to.

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

Example 3:
* This example denies access to non-IAM actions if the user is not signed in using
  MFA. If the user is signed in with MFA, then the "Condition" test fails and the
  "Deny" statement has no effect. Note, however, that this would not grant the user
  access to any actions; it would only explicitly deny all other actions except
  IAM actions.

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

**More Examples:**
[Deny Access based on region](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.html)

**Resource**
**NotResource**
* Explicitly match every resource except the ones specified.

-----------------------------------------
**Condition**
* Let's you specify conditions for when a policy is in effect.

```
"Condition" : {
    "{condition-operator}" : { "{condition-key}" : "{condition-value}" }
}
```

**Global condition Key**
[Global condition context](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)

**Condition-operator**
* Used to match the condition-key and the condition values in the request context
* [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)

**Condition operator categories**
* *string*
* *Numeric*
* *Date & time*
* *Boolean*
* *Binary*
* *IP address*
* *ARN* (available for only some services)
* *...IfExists* (checks if the key value exists as part of another check)
* *Null check* (checks if the kkey value exists)


-----------------------------------------

## How to generate IAM credentials report
```
#!/bin/bash
aws iam generate-credential-report  --profile core-services-prod
aws iam get-credential-report \
    --query Content --output text \
    --profile dev | base64 -D

```

## Creating a role with path.
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
Role created with ARN: `arn:aws:iam::838423692566:role/operations/testrole`


## Policy Examples

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

--------------------------------------------------------------------------------

## AWS Directory Service:
* Family of managed services
* Provides directories that contain information about your org, including users
  groups, computers and other resources.
* Designed to reduce identity management tasks.
* Each directory is deployed across multiple AZs and monitoring automatically
  detects and replaces domain controllers that fail.
* Data replication and automated daily snapshots are configured.

**Three directory types**
* Microsoft AD
* Simple AD
* AD connector

**Microsoft AD**
* Provides similar functionality offered by Microsoft AD, plus integration with
  other AWS services.
* Easily setup trust relationships with existing AD domains to extend those
  directories.

*Shared Responsibilities*

          AWS                                      Customers
- Multi-az deployment                        - Users, groups & group policies
- Patch, monitor, recover domain controller  - Standard AD tools
- Instance rotation, version upgrades        - Scale out Domain controllers
- snapshot and restore                       - Employ AD Trusts (resource forests)
                                             - Mgmt of certificate authorities & Federation

**Simple AD**
* Microsoft AD compatible directory service from AWS powered by Samba 4.
* Supports: user accounts, group memberships, domain-joining EC2 instances
  running Linux and Windows, Kerberose-based SSO, and group policies.
* User accounts in Simple AD can also access AWS applications, like AWS
  Workspaces, WorkDocs and WorkMail.
* They can also use IAM roles to access console and manage AWS resources.
* Provides daily automated snapshots.
* You can setup trust relationships between simple AD and other AD domains.
* Features not supported: DNS dynamic update, schema extensions, MFA,
  communication over LDAP, AD cmdlets and transfer of flexible Single-Master
  operations roles.
* Two sizes to deploy small (up to 500 users); Large (up to 5000 users)

**AD Connector**
* Proxy service for connecting your on-premise Microsoft AD to AWS without
  requiring complex directory synchronization or the cost and complexity
  of hosting a federation infrastructure.
* AD connector forwards sign-in requests to your AD domain controllers for
  authentication.
* After setup your users can use their existing corp credentials to login
  to AWS applications.

**Cloud directory:**
* Directory-based store for developers.
* Multiple hieraarchies with hundereds of million of objects.
* Use cases: Org charts, course catalogs, device registries.
* Fully managed service

**Cognito user pools:**
* Managed user directory for SAAS applications.
* Sign-up and sign-in services.

**AD Compatible services**
you can use:
* Managed Microsoft AD
* AD Connector
* Simple AD

**Not AD compatible services**
* Cloud directory
* Cognito user pools

--------------------------------------------------------------------------------

## AWS Resource Access Manager (RAM)
* Easily and securely share AWS resources with any AWS account or within your
  AWS organization.
*Allowed Resources:*
- AppMesh
- Aurora
- CodeBuild
- EC2
- EC2 Image builder
- License manager
- Resource groups
- Route53

## AWS single sign-on (SSO):
* Allows centrally manage access to multiple AWS accounts and applications.
* Provide users with SSO access to all their assigned accounts and apps from one
  place.

--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
## Simple Storage Service (S3):
#--------------------------------------------------------------------------------

* Secure, durable, highly scalable object storage.
* Files can be from 0 bytes to 5 TB.
* Largest object that can be uploaded in a single PUT is 5 GB.
* For objects > 100 MB, customers should use multipart upload capability.
* Unlimited storage.
* S3 is a universal namespace. That is, bucket names must be unique globally across
  AWS accounts.
* Reason for this uniqueness of name is S3 is is actually create a web address.
  - If you create a bucket in us-east-1, it will create a web address:
     https://acloudguru.s3.amazonaws.com/
  - Alternatively creating a S3 bucket in Ireland, it will create this address:
     https://acloudguru.eu-west-1.amazonaws.com/

* When you upload an object to S3, upon success you will get a HTTP 200 code.

--------------------------------------------------------------------------------
**Data consistency**
- Readr-after-write consistency for PUTS of new objects (new Key) - Means if you
  upload a file to S3, you will be able to read it immediately.
- Eventual consistency for overwrites/updates PUTS and DELETES (can take some
  time to propogate) - let's say you have version 1 of a file, and you upload
  version two, and you immediately try and read the object, you might get version 1.
- In all cases updates to a single key are atomic - for eventually-consistent reads,
  you will get old data or new data, but never an inconsistent mix of data.

--------------------------------------------------------------------------------
**S3 Storage Classes:**

**S3 Standard**
* 99.99% availability
* 99.99999999999% durability (11 9s durability)
* Stored redundancly across multiple devices in multiple facilities, and
  designed to sustain the loss of 2 facilities concurrently.

**S3 IA**
* For data that is accessed infrequently. But requires rapid access when needed.
* Lower fee than S3, but you are charged a retrieval fee.

**S3 One Zone - IA**
* Lower cost option for infrequently accessed data, but do not require multi-az
  resiliency.

**S3 intelligent tiering**
* Designed to optimize costs by automatically moving data to most cost-effective
  access tier, without performance impact or operational overhead.

**S3 Glacier**
- Secure, durable, and low-cost storage class for data archiving.
- Can store any amount of data at costs that are competitive with or cheaper than
  on-prem solutions.
- Retrieval times configurable from mins to hours.

**S3 Glacier Deep Archive**
- Lowest cost storage class.
- Retrieval time of 12 hours.


**S3 charges**
You are charged for:
* Storage
* Requests
* Storage management pricing
* Data transfer pricing
* Transfer acceleration
* Cross region replication pricing.

--------------------------------------------------------------------------------
**S3 Transfer Acceleration**
* Enables fast, easy and secure transfer of files over long distance between your
  end users and an S3 bucket.
* Transfer acceleration takes advantage of Amazon CloudFront's globally distributed
  edge locations.
* As the data arrives at an edge location, data is routed to Amazon S3 over an
  optimized network path.

**S3 Security & Encryption**
* By default all newly created buckets are PRIVATE.

--------------------------------------------------------------------------------
## Access control:
* By default when you create a bucket or object in S3, only you have access.
* To allow access to others, S3 ACLs, Bucket policies, IAM polices can be configured.
* ACL allows you to grant coarse-grained permissions: Read, Write & Full control
  on an object or bucket.
* ACLs are legacy access control, created before IAM existed.
* S3 bucket policies are the recommended access control mechanism for S3 and provide
  a finer grained control.
* S3 buckets can be configured to create access logs which log all requests made to
  the S3 bucket. This can be sent to another bucket in another account.
**Interesting note on ACLs:**
 * You can make a specific object publicly accessible using ACls, however you can
   still control access to this object with bucket policy. Like restricting access
   to the object from certain specific IP addresses:
```
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowFromMyNetworkOnly",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::mybucket/path/to/object/*"
            ],
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": [
                        "192.168.2.0/24",
                        "172.22.10.0/28"
                    ]
                }
            }
        }]
     }
```

**Additional docs**
* [AWS Doc on blocking S3 traffic by VPC or IP](https://aws.amazon.com/premiumsupport/knowledge-center/block-s3-traffic-vpc-ip/)
* [S3 VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html)


* Encryption in transit is achieved by SSL/TLS.

* Encryption at rest (Server side) is achieved by
 * S3 managed keys SSE-S3
 * AWS Key management service, Managed Keys SSE-KMS
 * Service side encryption with customer provided keys SSE-C
 * Client side encryption

--------------------------------------------------------------------------------
**S3 Versioning:**
* Versioning is enabled at the bucket level.
* Once versioning is enabled it cannot be removed. It can be suspended.
* Integrates with lifecycle rules.
* Versioning's MFA Delete capability, which uses multi-factor authentication, can
  be used to provide an additional layer of security.
* When you make an object public, does not necessarily make all the versions public.
**Deleting versioned objects:**
* A simple delete cannot permantly delete an object when versioning is enabled.
* Instead S3 inserts a 'delete marker' in the bucket and that marker becomes the
  current version of the object with a new ID.
* GET on the object whose current version is 'delete marker', will behave as though
  object has been deleted.
* You can restore the object by deleting the 'delete marker' version.
* To delete versioned objects permanently you must DELETE Object versionId.

--------------------------------------------------------------------------------
**S3 Object Lock**
* Allows you to store objects using a write-once-ready-many (WORM) model.
* Prevent objects from being deleted or overwritten for a fixed amount of time or
  idefinitely.
* Meet regulatory requirememnts or simply add another layer of protection against
  object changes.
* It works only on versioned buckets, and retention periods and legal holds apply
  to individual object versions.
* You can only enable 'object lock' during bucket creation. If you want to turn on
  object lock for an existing bucket, contact AWS support.
* If you create bucket with object lock enabled, you cannot suspend versioning or
  disable object lock for the bucket.
* Governance Mode:
  - In this mode, users can't overwrite or delete an object or later it's lock
    settings unless they have special permissions.
  - You protect objects against being deleted by most users, but you can still grant
    some users permissions to later retention settings or delete the object.
* Compliance Mode:
  - In this mode protected object version can be overwritten or delete by any user,
    including the root user.
  - Objects can be overwritten, deleted for the duration of the retention period.

**Glacier Vault lock**
* Easily deploy and enforce compliance controls for individual S3 Glacier vaults with
  vault lock policy.
* You can specify WORM controls, in a vault lock policy and lock the policy from
  future edits. Once locked the policy can no longer be changed.

--------------------------------------------------------------------------------
## S3 Performance
* S3 has extremely low latency. You can get the first byte out of S3 within
  100-200 milliseconds.
* You can achive a high number of requests: 3500 PUT/COPY/POST/DELETE and
  5500 GET/HEAD requests *per second per prefix*.
* You can get better performance by spreading your reads across different prefixes.
  - You can achieve 11,000 requests per second with two prefixes
  **Organizing objects using prefixes**
  * Prefix is similar to a directory name, that enables you to group objects together
    in a bucket.
  * Eg: mybucket/folder1/subfolder1/myfile.jpg -- '/folder1/subfolder1'

**S3 limitations when using KMS**
* If you are using SSE-KMS to encrypt your objects in S3, you must keep in mind the
  KMS limits. Uploading and downloading will count towards region specific quota.
* When you upload a file, you will call GenerateDataKey in the KMS API.
* When you download a file, you will call Decrypt in the KMS API.
* Region specific: 5,500, 10000, 30000 requests per second depending on the region.

--------------------------------------------------------------------------------
## Multipart uploads:
* Recommended for files > 100 MB. Required for files > 5GB.
* Parallelize uplods (increases efficiency.
* Each chunk should be a minimum of 5 MB size.
* Always complete or abord a multipart upload - else the individual chunks uploaded
  will not be cleaned up and will cost.
* You can define lifecycle policy to delete stale multipart upload chunks to reduce
  cost.

**S3 Byte-Range Fetches**
* Can speed up downloads
* Can be used to download partial amounts of file.

--------------------------------------------------------------------------------
## S3 Select:
* Enables applications to retrieve only a subset of data from an object using
  simple SQL expressions.
* Get data by rows and colums using SQL expressions.
* You can achive drastic performance increases.
* Save money on data transer and increase speed.

## Glacier Select:
* Some usecases require writing data directly to Amazon Glacier. Eg satisfy compliance.
* Glacier select allows you to run SQL queries against Glacier directly.
--------------------------------------------------------------------------------
## Pre-signed URLs:
* All S3 objects are by default private.
* Owners can shared objects with others without granting explicit permissions
  with IAM policies, by creating pre-signed URL using their own security credentials
  to grant time-limited permissions to download objects.
* To create a pre-signed URL for an object, you must provide your security
  credentials, specify the bucket, object key, the HTTP method and expiration
  date and time.
* The pre-signed URLs are valid only for specific time.

Example:
```
>>> session = boto3.Session(profile_name="default", region_name="us-east-1")
>>>
>>> s3client = session.client('s3')
>>>
>>> s3client.generate_presigned_url('get_object',
Params={'Bucket': 'my-test-bucket', 'Key': 'scripts/volume_helper.py'}, ExpiresIn=3600)

u'https://my-test-bucket.s3.amazonaws.com/scripts/volume_helper.py?AWSAccessKeyId=AXXX3REGL5A&Expires=1491340796&Signature=2pfqmdtyOcRbXWQ8'
>>>
>>>
```

--------------------------------------------------------------------------------
## Static Website hosting
* Create a bucket, upload static files, make them public (world readable)
* Enable static website hosting for the bucket. This includes specifying an
  index document and an error document.
* This website will now be available at:
   <bucketname>.s3-website-<aws region>.amazonaws.com
* Create a friendly DNS name in your own domain for the website using a CNAME
  and you have your website available.























