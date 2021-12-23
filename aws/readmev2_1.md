# AWS Notes (Version 2.0).

NOTE:
* Some practices to manage notes.
 * Only two levels.
 * Use **Bold** text for subsections.



**Useful links:**
* [AWS Well-architected framework](https://wa.aws.amazon.com/wat.concepts.wa-concepts.en.html)
* [AWS How pricing works](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/introduction.html)
* [S3 FAQ](https://aws.amazon.com/s3/faqs/)
* [S3 - Deleting versioned objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)
* [S3 - multipart upload](http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html)
* [S3 - best practices design patterns](https://docs.aws.amazon.com/whitepapers/latest/s3-optimizing-performance-best-practices/introduction.html)
* [S3 - blocking S3 traffic by VPC/IP](https://aws.amazon.com/premiumsupport/knowledge-center/block-s3-traffic-vpc-ip/)
* [S3 VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html)
* [S3 - Managing cross account access](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html)
* [S3 cross account access](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/)
* [EC2 Burstable performance concept](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html)
* [AMI - copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html#ami-copy-steps)
* [EC2 - spot instance advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)           
* [EC2 - spot instance pricing](https://aws.amazon.com/ec2/spot/pricing/#Spot_Instance_Prices)
* [EC2 - spot fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html)    
* [EC2 - New spot pricing](https://aws.amazon.com/blogs/compute/new-amazon-ec2-spot-pricing/)
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
##S3 Transfer Acceleration
* Enables fast, easy and secure transfer of files over long distance between your
  end users and an S3 bucket.
* Transfer acceleration takes advantage of Amazon CloudFront's globally distributed
  edge locations.
* As the data arrives at an edge location, data is routed to Amazon S3 over an
  optimized network path.

--------------------------------------------------------------------------------
#S3 Security & Encryption
* By default all newly created buckets are PRIVATE.

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

--------------------------------------------------------------------------------
## S3 Cross-account Access
* [Managing cross account access](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html)
* [cross account access](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/)


## Cross-Region Replication:
* To enable CRR you need versioning enabled on source and destination buckets.
* Existing objects will not be replicated, only new objects will be replicated.
* Permissions also get replicated.
* When you delete specific versions of an object or delete a delete marker,
  it does not get replicated to the dest bucket, it's only when you delete
  an object that it gets deleted from the replicated bucket.



--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
## AWS Organizations
#--------------------------------------------------------------------------------

**Best Practices**
* Always enable multi-factor authentication on root account.
* Always use a strong complex password on root account.
* Paying account should be used for billing purposes only. Do not deploy resources
  into the paying account.
* Enable/Disable AWS services using service control policies (SCP) either on OU or
  on individual accounts.




#--------------------------------------------------------------------------------
## AWS DataSync  (On-prem services)
#--------------------------------------------------------------------------------
* Used to move large amounts of data from on-premises to AWS
* Used with NFS and SMB compatible file sytems.
* Replication can be done hourly, daily or weekly
* Install Datasync agent to start replication.
* Can be used to replicate EFS to EFS.



#--------------------------------------------------------------------------------
## AWS CloudFront
#--------------------------------------------------------------------------------
* It is a global content delivery network (CDN) service.
* A CDN is a globally distributed network of caching servers that speed up the
  downloading of web pages and other content.
* CDNs use DNS geo-location to determine the geographic location of each request for
  a web page, then serve that content from the edge caching servers closest to that
  location.
* CloudFront can be used to deliver your web content using Amazon's global network
  of edge locations.
* A request is first routed to the edge location that provides the lowest latency.
  If the content is already in the edge location, CloudFront delivers it. If the
  content is not present, then CloudFront retrieves it from the origin server.
* CloudFront works with S3 buckets, S3 static websites, EC2, ELB and also
  non AWS origin server such as on-premises web server.
* CloudFront also integrates with Route53.
* It supports all content that can be served over HTTP or HTTPS, including static
  files, HTML files, images, JS, CSS, audio, video and media files or software
  downloads, also supports media streaming using both HTTP and RTMP.

## CloudFront Basics:
Core concepts:

**Distributions**
* This is the name given to the CDN which consists of a collection of Edge locations.
* You start by creating a distribution, which is identified by a DNS domain name
  like 'd484222.cloudfront.net'
* To serve files from CloudFront, you simply use the distribution domain name in
  place of your website's domain name. Rest of the file path stays the same.
* You can also create CNAME record in Route53 for DNS.

**Origins**
* This is the origin of all the files that the CDN will distribute.
* You must specify the DNS domain name of the origin - S3 bucket, EC2 instance,
  ELB, Route53  or HTTP server.

**Edge Location**
* This is the location where content will be cached. This is separate to an AWS
  Region/AZ.
* Edge locations are not just READ only - you can write to them too. (ie put an
  object on to them.)

**Cache Control**
* Once requested and served from the edge location, objects stay in the Cache until
  they expire or are evicted to make room for more frequently requested content.
* By default objects expire from the cache after 24 hours.
* You can control how long objects stay in CloudFront cache before expiring.
* You can use cache-control headers set by your origin server or you can
  set the min, max and default TTL for objects in your CloudFront distribution.
* You can also remove copies of an object from all CloudFront edge locations
  at any time by calling the invalidation API. This feature removes the object from
  every CloudFront edge location regardless of the expiration period set on the
  object on your origin server.
* Instead of invalidating objects, it is best practice to use a version
  identifier as part of the object path name.
* When using versioning, users will always see the latest content through CloudFront
  when you update your site. Old versions will expire from the cache automatically.

## Advanced CloudFront Features
* Can be setup to use more than one origins. You can control which requests are
  served by which origin and how the requests are cached - using a feature
  called "cache behaviors".
* Cache Behaviors:
  * Path patterns
  * Which origin to forward requests to
  * Whether to forward query strings to your origin
  * Whether you need signed URL for specific files.
  * Require HTTPS access
* Cache behaviors are applied in order. If a request does not match the first path
  pattern, it drops down to the next.
**Signed URL and Signed Cookies**
* Signed URLs
  - Signed URL is for individual files.
  - URLs that are valid only between certain times and optionally from certain IP
    addresses.
* Signed cookies
  - A signed cookie is for multiple files.
  - Require authentication via public and private keys.
* Origin Access Identities: Restrict access to an S3 bucket only to a special
  CloudFront user associated with your distribution.

--------------------------------------------------------------------------------




#--------------------------------------------------------------------------------
## Snowball / Snowball Edge / Snowmobile
#--------------------------------------------------------------------------------

## Snowball
* Petabyte scale data transport solution that uses secure appliances to transfer
  large amounts of data into and out of AWS.
* Addresses challenges with large scale data transfers including high n/w costs,
  long transfer times and security concerns.
* Uses Amazon provided shippable storage appliances, shipped through UPS.
* Each snowball is protected by KMS and made physically rugged to secure and
  protect your data while in transit.
* Comes in two sizes: 50 TB and 80TB and varies by region.
* Features:
  - Import/export data between on-premise data storage and S3.
  - Encryption is enforced.
  - You don't buy and maintain your own hardware devices.
  - Manage your jobs through AWS snowball console.


## Snowball Edge:
* 100TB data transfer device with onboard storage and compute capablities.
* Snowball edge connects to your existing applications and infra using standard
  storage interfaces.
* It can cluster together to form a local storage tier and process your data
  on-premize, ensuring applications continue to run even when they are not able
  to access the cloud.


## Snowmobile:
* Petabyte and Exabyte amount of data.

--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
## Storage Gateway (On-prem services)
#--------------------------------------------------------------------------------
* [Storage gateway FAQ](https://aws.amazon.com/storagegateway/faqs/)
* Connects on-prem software appliance with cloud based storage.
* Provides seamless integration with data security between your data center and AWS
  storage infrastructure.
* AWS storage gateway offers
  - file-based file gateways (Amazon S3 File and Amazon FSx File)
  - Volume based (cached and stored)
  - Tape based storage solutions.

--------------------------------------------------------------------------------
## S3 File Gateway:
* Provides access to objects in S3 as files on NFS mount point.
* It combines a service and virtual software appliance.
* The appliance/gateway is deployed on the premise on a VMware ESXi, Microsoft
  hyper-V or KVM.
* The gatway provides access to S3 objects as NFS mounted files.
* With file gateway you can:
  * Store and retrieve files directly using NFS 3 or 4.1 protocol.
  * Access your data directly in S3 from any cloud application or service.
  * Manage your data in S3 using lifecycle policies, cross origin replication and
    versioning.
* It also provides low latency access to data through transparent local caching.
* Max number of file shares/S3 bucket is 1. 1-1 mapping between a file share and S3
  bucket.
* Max number of fil shares per gateway is 10.
* Max file size is 5 TB (Same as the limit for S3)

## Amazon FSx File Gateway
* Enables you to store and retrieve files in Amazon FSx for windows file server
  using SMB protocol.
--------------------------------------------------------------------------------

## Volume gateway:
* The volume interface presents your applications with disk volumes using the
  iSCSI block protocol.
* Data written to these volumes asynchronously backed up as point-in-time snapshots
  of your volumes, and stored in the cloud as EBS snapshots.
* Snapshots are incremental backups that capture only changed blocks. All snapshot
  storage is also compressed to minimize your storage charges.

**Cached Volumes:**
* you store your data in S3 and retain a copy of frequently accessed data locally.
* They offer substantial cost savings on primary storage and minimize need to
  scale on-prem storage.
* You also retain low-latency access to your frequently accessed data.
* Max size of a cached volume is 32TB.
* Max number of volumes/gateway is 32.
* Total size of all volumes is 1024TB.

**Stored Volumes:**
* Provides durable and inexpensive offsite backups that you can recover to your
  local data center or EC2.
* You configure your on-prem gateway to store all data locally and then asynchronously
  backup point-in-time EBS snapshots to S3.
* Max size of a stored volume is 16TB.
* Max number of volumes/gateway is 32.
* Total size of all stored volumes is 512 TB.
--------------------------------------------------------------------------------

##Virtual Tape Gateway:
* Cost-effectively and durably backup data in Amazon Glacier.
* Provides a virtual tape infrastructure that scales seamlessly with your business
  needs.
* Minimum size of virtual tape: 100GB
* Maximum size of a virtual tape: 2.5 TB
* Maximum number of virtual tapes for a VTL (virtual tape library): 1500
* Total size of all tapes in a VTL: 1 PB.
* Maximum number of virtual tapes in archive: unlimited.




#--------------------------------------------------------------------------------
## Athena vs Macie
#--------------------------------------------------------------------------------

## Athena
* Interactive query service which enabies you to analyze and query data located in
  S3 using standard SQL.
* Serverless, nothing to provision, pay per query / TB scanned.
* No need to setup complex Extract/Transform/Load (ETL) processes.
* Works directly with data stored in S3.
* Data formats supported: JSON, Apache Parquet, Apache ORC.

**What can Athena be used for**
* Query log files stored in S3, eg ELB logs, S3 access logs, cloudtrail logs.
* Generate business reports on data stored in S3
* Analyze AWS cost and usage reports
* Run queries on click-stream data

--------------------------------------------------------------------------------

## Macie

**What is PII**
* Personal data used to establish an individual's identity.

* Machie is a security service which uses ML and NLP to discover, classify and
  protect sensitive data stored in S3.
* Uses AI to recognise if your S3 objects contain sensitive data such as PII
* Dashboards, reporting and alerts
* Works directly with data stored in S3.
* Can only analyze CloudTrail logs
* Great for PCI-DSS and preventing ID theft.

--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
## AWS EC2
#--------------------------------------------------------------------------------

* Default maximum EC2 instance limit per region is 20.
* Within each family of instance type, there are several choices that scale up
  linearly in size. The hourly price for each size scales linearly as well.
* When the host on which an EC2 instance restarts, the instance will stay with the
  same EC2 host. But if the instance is stopped and then restarted or if AWS stops
  the instance for maintenance etc on their end, then the instance will be
  reassigned to another host in the same AZ.
* AWS originally modified Xen Hypervisor to host EC2. Later it rolled out it's own
  hypervisor called Nitro.
* To attach an IAM role to an instance that has no role, the instance can be in the
  stopped or running state.
* To replace the IAM role on an instance that already has an attached IAM role,
  the instance must be in the running state.

* Instance metadata: http://169.254.169.254/latest/meta-data/
* Instance user data: http://169.254.169.254/latest/user-data/

**Termination Protection**
* Prevents from accidental Termination from console, CLI or API.
* It does not prevent termination triggered by an OS shutdown command,
  termination from an ASG, or termination of a spot instance due to spot price
  changes


--------------------------------------------------------------------------------
## Instance Types:
**General purpose**
* Provide a balance of compute, memory and networking resources and can be used
  for a wide range of workloads.

**T3**
* Low cost general purpose
* Burstable performance instances
* Provide a baseline level of CPU performance with ability to burst above the
  baseline.
* The baseline performance and ability to burst are governed by CPU credits.
* Uses: webservers, developer environments and databases.

**T4**:
* ARM based Gavitron2 processors. Deliver up to 40% better price performance over
  T3 instances.

**M5,M5a**:
* Latest generation of general purpose instances.
* Powered by Intel Xenon 8175M processors.
* 25 Gbps network bandwidth using enhanced networking.
* Instance storage offered via EBS or NVMe SSD that are physically attached to
  the host server - provide block storage that is coupled to the lifetime of the
  M5 instances.

**M5zn**:
* Bare metal instance.
* Ideal for extremely high single threaded performance, high throughput & low latency
  networking.
* For Gaming, HPC, Simulation modeling.

**MAC**:
* Powered by Apple MAC mini computers and build on AWS Nitro system.

--------------------------------------------
**Compute Optimized**
* Ideal for compute bound applications that benefit from high performance processors.

**C5,C5n**:
* Delivers cost-effective high performance at low price per compute ratio.
* Requires HVM AMIs that include drivers for ENA and NVMe
* Up to 25 Gbps of n/w bandwidtth and 19 Gbps of dedicated bw to Amazon EBS.

**C6,C6gd, C6gn**:
* AWS Graviton2 processors.

--------------------------------------------
**Memory Optimized**
* Designed to deliver fast performance for workloads that process large data sets
  in memory.

**R5**
* High Frequency Intel Xeon E5-2686 v4 (Broadwell) processors
* DDR4 Memory
* Support for Enhanced Networking
* R5 delivers 5% additionnal memory per vCPU than R4.

--------------------------------------------
**Storage optimized**
* Designed for workloads that require high, sequential read and write access to
  very large data sets on local storage.

**D2,D3**:
* Optimized for applications that require high sequential I/O performance
  and disk throughput.
* Up to 48 TB of HDD instance storage.
* D3 offers Up to 45% higher read and write disk throughput than D2 instances.

**I3**:
* Provides NVMe  SSD-backed instance storage, optimized for low latency,
  very high random I/O performance, high sequential read throughput and high
  IOPS at low cost.
* I3 also provides bare metal instances (I3.metal)
* Up to 25 Gbps of n/w bandwidth using ENA based enhanced networking.

--------------------------------------------
**Accelerated computing**:
* Uses hardware accelarators, or co-processors to perform functions such as
  floating point number calculations, graphics processing or data pattern match.

**P2,P3, P4**
* GPU based instances, provide highest performance for ML training and
  HP computing in the cloud.
* 400 Gbps instance networking support for Elastic Fiber Adapter and NVIDIA
  GPUDirect RDMA (remote direct memory access)
* 600 GB/s peer to peer GPU communication with NVIDIA NVswitch

**F1**:
* Offers customizable hardware  acceleration with field programmable gate
  arrays (FPGA).


--------------------------------------------------------------------------------
## EC2 Pricing Models

## On Demand
* Allows you to pay a fixed rate by the hour (or by the second) with no commitments.

## Reserved
* Provides you with capacity reservation.
* Offers a significant discount on the hourly charge.
* Contract terms are 1 Year or 3 Years.
**Standard Reserved Instances**
* Offer up to 75% off on demand instances. The more you pay upfront and longer the
  contract, the greater the discount.

**Convertible Reserved Instances**
* Offer up to 54% off on demand.
* Capability to change the attributes of the RI as long as the exchange results in
  the creation of RIs of equal or greater value.

**Scheduled Reserved Instances**
* Available to launch within the time windows you reserve. Allows you to match
  your capacity reservation to a predictable recurring schedule that only requires
  a fraction of a day, week or month.

* Payment options:
  * All upfront
  * Partial upfront.
  * No upfront.

**Modifying your reserved instances:**
* Modification does not change the remaining term of your reserved instances.
  Their end dates remain the same. There is no fee and you do not receive a new
  bill.
**What can you modify?**
* Change AZs within the same region.
* Change the network from EC2 Classic to Amazon VPC and vice versa.
* Change the scope from AZ to Region and vice versa
* Change instance size within the same instance family (Linux only)

## Spot
* Enables you to bid whatever price you want for instance capacity.
* If a spot instance is terminated by Amazon EC2, you will not be charged for
  a partial hour of usage. However, if you terminate the instance yourself, you will
  be charged for any hour in which the instance ran.

* [spot instance advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)           
* [spot instance pricing](https://aws.amazon.com/ec2/spot/pricing/#Spot_Instance_Prices)
* [spot fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html)    
* [New spot pricing](https://aws.amazon.com/blogs/compute/new-amazon-ec2-spot-pricing/)
                       

## Dedicated Hosts
* Physical EC2 server dedicated for your use.
* Can help reduce costs by allowing you to use your existing server bound
  software licenses.


--------------------------------------------------------------------------------
## Burstable performance
* Burstable performance instances provide a baseline level of CPU utilization with
  the ability to burst CPU utilization above the baseline level.
* Use credits for CPU usage.
* Each burstable performance instance continuously earns credit when it stays below
  the CPU baseline, and spends it when it burst above the baseline.
* If there are no accrued creds remaining, then the instance gradually comes down
  to baseline CPU utilization and cannot burst above baseline till it accrues more
  credits.


--------------------------------------------------------------------------------
## AMIs:
* AMIs define the initial software that will be on an instance when launched.
* OS, initial state of any patches, applications or system software.

**Four sources:**
* Published by AWS
* AWS Marketplace
* Generated from existing instances
* Uploaded virtual servers

* When launching windows instance, EC2 generates a random password for the local
  admin account and encrypts the password using a public key. initial access is
  obtained by decrypting the password with the private key, either in the console
  or using API.
  The decrypted password can be used to login into the instance with local
  admin account via RDP.

**Creating an AMI**:
You can create
* An  EBS backed linux AMI
* An Instance store backed Linux AMI

**EBS Backed Linux AMI**
*From EC2 instance.*
--------------------
Steps overview:
* Launch an instance from an AMI (similar to one you like to create)
* Customize the instance (install s/w, apps etc)
* Stop the instance
* Create the image
* When you create an EBS backed AMI, Amazon will automatically register it for you.

* During AMI creation, EC2 creates shanpshots of your instance's root volumes and
  any other EBS volumes attached to your instance.
* You are charged for the snapshots until you deregister the AMI and delete the
  snapshots.
* If any volumes attached to the instances are encrypted, the new AMI only launches
  on instances that support Amazon EBS encryption.

*From an EBS snapshot*
---------------------
* Select the snapshot from which to create the AMI.
* Choose image name, architecture, root device name, virtualization type.
* Customize block device mappings
* create image.

**Copying an AMI**
* You can copy an Amazon AMI within or across AWS regions.
* You can copy EBS backed and instance-store-backed AMIs.
* You can copy AMIs with encrypted snapshots and also change encryption status
  during the copy process.
* You can copy AMIs that are shared with you.



--------------------------------------------------------------------------------
## EBS
* Provide persistent block-level storage volumes for use with EC2 instances.
* EBS volume is automatically replicated within it's AZ to provide HA and durability.

**Types of EBS Volumes**
















