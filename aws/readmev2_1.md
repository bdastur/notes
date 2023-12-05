# AWS Notes (Version 2.0).

NOTE:
* Some practices to manage notes.
 * Only two levels.
 * Use **Bold** text for subsections.



**Useful links:**
* [AWS Well-architected framework](https://wa.aws.amazon.com/wat.concepts.wa-concepts.en.html)
* [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
* [AWS Architecture Center](https://aws.amazon.com/architecture/)
* [AWS How pricing works](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/introduction.html)
* [S3 FAQ](https://aws.amazon.com/s3/faqs/)
* [S3 - Deleting versioned objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjectVersions.html)
* [S3 - multipart upload](http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html)
* [S3 - best practices design patterns](https://docs.aws.amazon.com/whitepapers/latest/s3-optimizing-performance-best-practices/introduction.html)
* [S3 - blocking S3 traffic by VPC/IP](https://aws.amazon.com/premiumsupport/knowledge-center/block-s3-traffic-vpc-ip/)
* [S3 VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html)
* [S3 - Managing cross account access](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html)
* [S3 cross account access](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/)
* [S3 thread model](https://controlcatalog.trustoncloud.com/dashboard/aws/s3)
* [EC2 Burstable performance concept](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-credits-baseline-concepts.html)
* [AMI - copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html#ami-copy-steps)
* [EC2 - using spot instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
* [EC2 - spot instance advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)
* [EC2 - spot instance pricing](https://aws.amazon.com/ec2/spot/pricing/#Spot_Instance_Prices)
* [EC2 - spot fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html)
* [EC2 - New spot pricing](https://aws.amazon.com/blogs/compute/new-amazon-ec2-spot-pricing/)
* [Using IMDS V2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)
* [EBS - volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)
* [Cloudwatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html)
* [SQS - How it works](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-how-it-works.html)
* [KMS - multiple master key encryption](https://aws.amazon.com/blogs/security/new-aws-encryption-sdk-for-python-simplifies-multiple-master-key-encryption/)
* [Lambda - Best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
* [DynamoDB - designing partition keys](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-uniform-load.html)
* [DynamoDB - choosing partition key](https://aws.amazon.com/blogs/database/choosing-the-right-dynamodb-partition-key/)
* [CI/CD AWS - Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/practicing-continuous-integration-continuous-delivery.pdf)
* [Cloudformation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_TemplateQuickRef.html)
* [Cognito Authentication](https://aws.amazon.com/blogs/mobile/understanding-amazon-cognito-authentication/)
* [Cognito Authentication-2](http://mobile.awsblog.com/post/Tx2FL1QAPDE0UAH/Understanding-Amazon-Cognito-Authentication-Part-2-Developer-Authenticated-Ident)
* [Cognito Authentication-3](http://mobile.awsblog.com/post/Tx1OSMBRHZVM9V0/Understanding-Amazon-Cognito-Authentication-Part-3-Roles-and-Policies)
* [Cognito Authentication-4](https://aws.amazon.com/blogs/mobile/understanding-amazon-cognito-authentication-part-4-enhanced-flow/)
* [AWS Extend Switch Roles](https://github.com/tilfinltd/aws-extend-switch-roles)
* [cli tool for AWS login](https://github.com/Versent/saml2aws)
* [Serverless snippets collection](https://serverlessland.com/snippets)
* [https://workshops.aws/](AWS Workshops)
* [awslabs - flexible snapshot proxy](https://github.com/awslabs/flexible-snapshot-proxy)
* [AWS Samples - github](https://github.com/aws-samples)
* [AWS Skillbuilder site](https://explore.skillbuilder.aws/learn/signin)
* [EC2 instance connect - a better way to ssh into EC2 instances](https://aws.amazon.com/blogs/compute/secure-connectivity-from-public-to-private-introducing-ec2-instance-connect-endpoint-june-13-2023/)
* [Cloud design patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/acl.html)


**Walkthroughs exercises**:
* [Serverless Lab](https://github.com/saha-rajdeep/serverless-lab)
* [Event driven architecture - Eventbridge](https://catalog.us-east-1.prod.workshops.aws/workshops/63320e83-6abc-493d-83d8-f822584fb3cb/en-US/eventbridge)
* [Run infra as code with Jenkins](https://www.youtube.com/watch?v=XnRqGMSCQyY)
* [GitOps](https://www.youtube.com/watch?v=o4QG_kqYvHk&t=0s)
* [Static website on S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html)
* [Static website with cloudfront and route53](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html)
* [Convert cloudformation templates to diagrams](https://github.com/mhlabs/cfn-diagram)
* [A collection of projects](https://github.com/acantril/learn-cantrill-io-labs/blob/master/get-paid-to-create-projects.md)
* [Python SDK Code examples (Dynamodb)](https://docs.aws.amazon.com/code-library/latest/ug/python_3_dynamodb_code_examples.html)


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
## AWS Route53
#--------------------------------------------------------------------------------

* Route53 is highly available and scalable DNS web service. You can use Route53 to
  perform 3 main functions.

**Register domain names**
* Route53 lets you register a name for your websiste (known as domain name)

**Route internet traffic to the resources for your domain**

**Check the health of your resources**
* Route53 sends automated requests over the internet to a resource to verify that
  it is reachable, available and functional.

## DNS Concepts:

**TLDs**  (Top Level Domains)
* Most general part of the domain
* eg: .com, .org, .edu
* Top of the hierarchy in terms of domain names.
* ICANN - Internet Corporation for Assigned Names and Numbers.

* Domain names: Human friendly name used to associate to an internet source.
* A proper FQDN ends with a '.', indicating the root of the DNS hierarchy.
* Sometimes software that calls for an FQDN does not require an ending ., but
  it is required to conform to ICAAN standards.

In the URL: api.aws.amazon.com.
api            == host
aws.amazon.com == subdomain
amazon         == sld
com            == tld
.              == root

* DNS uses port 53 to serve requests.
* DNS primarily uses UDP protocol to serve reuests.
* When the response data exceeds 512 bytes TCP protocol is used.

**Name servers:**
* A computer designated to translate domain names to IP addresses
* A nameserver can be authoritative, meaning that they give answers to queries
  about domains under their control. Or they may point to other servers to
  serve cached copies of other name servers data.

**Zone files:**
* A simple text file that contains mapping between domain names and IP
  addresses.
* This is how a DNS server finally identifies which IP maps to a certain
  domain name.
* Zone files reside in name servers and define the resources available under
  a specific domain, or the place where one can go to get that info.

**Top level Domain (TLD) Name Registrars**
* Domain names must be unique
* Domain registrar is an organization or commercial entity that manages
  reservation of internet domain names.
* A domain name registrar must be accredited by a generic TLD registry and/or
  a country code TDL (ccTLD registry)

**Steps involved in DNS resolution**
* When you type a domain name in your browser, the computer first checks it's
  host file to see if the domain name is stored locally.
* If not it will check it's DNS cache to see if the site was visited before.
* If it still does not have a record of that domain name, it will contact a
  DNS server to resolve the domain name.
* DNS is a hierarchical system. At the top of the system are root servers.
* There are approximately 13 root servers in operation.
* When a request comes in for a domain that a lower level name server cannot
  resolve, a query is made to the root server for domain.
* The root servers are mirrored and replicated. When requests are made to a
  certain root server, the request will be routed to the nearest mirror
  of that root server.
* The root servers won't actually know where the domain is hosted. They will
  however be able to direct the requester to the name server that handles
  the specifically-requested TLD.
* For eg: if request for www.wikipedia.org is made to the root server, it will
  check it's zone files for a listing that matches the domain name but will
  not find it.
* It will instead find a record for .org TLD and give the requester address
  of the name server responsible for .org addresses.

**Top level domain servers:**
* After the root server returns the address of the appropriate server
  responsible for the TLD, the requester sends a new request to that address.
* Once again when the name server searches it's zone files it will not find
  one in it's records. However it will find a listing for the IP address of
  the name server responsible for wikipedia.org.

**Domain-level name servers:**
* At this point the requester has the IP address of the name server that is
  responsible for knowing the actual IP address of the resource.
* It sends a request to the name server to resolve www.wikipedia.org
* The name server checks it's zone files and finds a zone file associated
  with wikipedia.org. Inside the file is a record that contains the IP address
  of the .www host.
* The name server returns the final address to the requester.

**Resolving name servers:**
* A resolving name server is configured to ask other servers questions.
* It's primary function is to act as an intermediary for a user, caching
  previous query results for improving speed and providing the address of
  appropriate root servers to resolve new requests.
* A user will have a few name servers configured on their computer system.
* Name servers are typically provided by an ISP or other organization.
* There are public DNS servers that you can query.

**Zone files:**
* Zone files are the way the name servers store info about domains they know.
* The more zone files a name server has, the more requests it will be able to
  answer authoritatively.
* If the server is configured to handle recursive queries, like a Resolving
  name server, it will find the answer and return it. Otherwise it will tell
  the requesting entity where to look next.
* Zone files describe a DNS zone, which is a subset of the entire DNS.
* Generally used to configure a single domain.
* Zone file's $ORIGIN directive is a parameter equal to the zone's highest
  level of authority by default.
* If a zone file is used to configure the example.com domain, the $ORIGIN would
  be set to example.com
* TTL - Time to live value. Defines the length of time the previously queried
  results are available to the caching name server before they expire.


## Record Types:
A record is a single mapping between a resource and a name.

**Start of Authority Record (SOA)**
* Mandatory in all zone files.
* Identifies the base DNS information about the domain
* Each zone contains a single SOA record.
* Stores information about:
  * Name of the DNS server for that zone
  * The administrator of the zone.
  * The current version of the data file
  * Number of seconds a secondary name server should wait before checking for
    updates.
  * Number of seconds a secondary name server should wait before retrying
    failed zone transfer.
  * Max number of seconds a secondary name server can use data before it
    must be refreshed or expire.
  * Default TTL value for resource records in the zone.

**A and AAAA Record:**
* Both types of address records map a host to an IP address
* A: map a host to IPV4 address
* AAAA: map a host to IPV6 address
* A stands for Address

**Canonical Name (CNAME):**
* Defines an alias for the CNAME for your server (the domain name defined in
  A or AAAA record)
* Resolves one domain to another.

**Mail Exchange (MX):**
* Define the mail servers used for a domain and ensures emails are routed
  correctly.
* MX record should point to a host defined by A or AAAA record and not defined
  by CNAME.

**Name Server (NS)**
* Used by TLD servers to direct traffic to the DNS server that contains the
  authoritative DNS record.

**Pointer (PTR)**
* PTR record is essentially the reverse of an A record
* PTR records map an IP address to a DNS name.
* Mainly used to check if the server name is associated with an IP address
  from where the connection was initiated.
* A PTR record is used to resolve an IP address to a domain name commonly
  referred to as 'reverse DNS'


**Sender Policy Framework (SPF)**
* SPF records are used by mail servers to combat spam
* It tells a mail server what IP addresses are authorized to send emails
  from your domain name.
* Prevents people from spoofing emails from your domain name.


**Text (TXT)**
* Used to hold text information
* Provides the ability to associate some arbitrary and unformatted text with
  a host or other name, such as human readable information about a server,
  network, data center.

**Service (SRV)**
* It is a specification of data in the DNS defining the location of the
  servers for specified services.

## Route53 3 main functions:

### **Domain registration:**
* Amazon route53 lets you register domain names, such as example.com.
* You also have an option to transfer an already registered domain name with
  another registrar to route53.
* Supports domain registration for a wide variety of generic TLDs and
  geographic TLDs.
* There is a limit of 20 domain names for new customers as of March 2021.
* If you have an existing account and your default limit is 50 now, it will remain
  at 50. Reference: Amazon Route 53 Quotas.

### **DNS Service:**
* Route53 is an authoritative DNS service.
* When someone enters your domain name in a browser or sends you an email,
  a DNS request is forwarded to the nearest Route53 DNS server in a global
  network of authoritative DNS servers. Route53 responds with the IP address
  that you specified.
* If you registered your domain with another domain registrar, that registrar
  is probably providing DNS service for your domain. You can transfer DNS
  service to Route53 without having to transfer the registration for the domain.

### **Hosted Zones:**
* A hosted zone is a collection of resource record sets hosted by route53.
* A hosted zone represents resource record sets that are managed together
  under a single domain name.
* Each hosted zone has it's own metadata and configuration information.
* There are two types of hosted zones:
  * Private hosted zone: Holds information about how you want to route traffic
    for a domain and it's subdomains within one or more VPCs.

  * Public hosted zone: How you want to route traffic on the internet for
    a domain and it's subdomains.
* Resource record sets contained in a hosted zone must share the same suffix.

## **Supported Record Types**
Supported record types:
* A
* AAAA
* CNAME
* MX
* NS
* PTR
* SOA
* SPF
* SRV
* TXT
* **Alias Records** have special functions that are not present in other DNS servers.
* Their main function is to provide special functionality and integration into AWS
   services.
* Unlike CNAME records, they can also be used at the Zone Apex, where CNAME records
  cannot.
* Alias Records can also point to AWS Resources that are *hosted in other accounts*
  by manually entering the ARN


## Routing Policies:

**Simple**
* This is the default routing policy when you create a new resource.
* You can't create multiple records that have the same name and type.
* You can specify multiple vaules in the same record. Route53 returns all values
  to the user in random order. The user then chooses a vaule and resubmits the query.


**Weighted**
* You can associate multiple resources with a single DNS name.
* Useful for load balancing and testing new versions of software.

**Latency based**
* Based on users location and latency.


**Failover**
* Lets you route traffic to a resource when a resource is health or to a different
  resource when the first resource is unhealthy.
* Active/Passive

**Geolocation**
* Allows EU customers to be sent to EU backend and US customers to US backend.
* Lets you choose the resources that serve your traffic based on geographic
  location of your users, meaning the location that DNS queries originate from.
* With this you can localize your content & present some or all of your webiste in
  language of your users. You can also restrict distribution of content based on
  location.
* Another possible use is for balancing load across endpoints

**Geoproximity Routing**
* Geoproximity routing lets Route53 route traffic to your resources based on the
  geographic location of your users and your resoures.
* You can optionally choose to route more or less traffic to a resource by specifying
  a vaule, known as bias.
* To use this routing, you must use Route53 'traffic flow'

**Multivalue Answer Routing**
* R53 Multivalue lets you respond to DNS queries with up to eight IP addresses of
  'healthy' targets. Plus it will give a different set of 8 to different DNS resolvers.
* The R53 Simple policy will provide a list of multiple instances in random order,
  but Multivalue is the AWS preferred option for this type of service.

### **Health checking:**


--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
## AWS Autoscaling (ASG)
#--------------------------------------------------------------------------------
* Allows automatic scaling of EC2 instances based on criteria.
* Scaling in or scaling out.

## ASG scaling options
**Maintain current levels**
* Maintain a minimum or specified number of running instances at all times.
* When ASG finds an unhealthy instance it terminates it and launches a new one.

**Scale Manually**
* Most basic way to scale your resources.
* Specify the change in max, min & desired capacity of your ASG group.
* ASG maintains the process of creating or terminating instances to maintain the
  updated capacity.

**Scale based on schedule**
* Scaling actions are performed automatically as a functio of time and date.

**Dynamic scaling/Scale based on demain**
* Create a scaling policy based on criteria like n/w bandwidth or CPU measured
  by cloudwatch.
* Useful for scaling in response to changing conditions, when you don't know when
  those conditions will change.

**Predictive scaling**
* Predicting based on previous EC2 usage, with decision based on billions of data
  points drawn from observations.
* Well suited for situations where you have:
  * Cyclical traffic, such as high resource usage during business hours.
  * Recurring on-and-off workload patters - batch processing, testing, etc.
  * Apps that take a long time to initialize

## ASG Components:
**Launch configuration & Configuration templates**
* A template that ASG uses to create new instances.
* It is composed of config name, AMI, Instance type, SG, key pair.
* Only a launch config name, AMI and instance type are required to create a
  launch configuration. key pair, SG, block device mapping are optional elements.
* Default limit for launch configs is 100 per region.

* ASG can use on-demand or spot instances as EC2 instances it manages.
* on-demand is default, but spot instances can be used by referencing a max
  bid price in the launch config.
* A launch config can reference on-demand or spot instances but not both.
* Launch configuration templates are the new version of launch configuration.
* You can create new versions of launch templates unlike launch configuration.
* **Launch tempaltes** provide more advanced EC2 configuration options - like using
  **Dedicated hosts with an ASG**.


**Autoscaling group:**
* ASG is a collection of EC2 instances managed by ASG service.
* An Autoscaling group must have minimum size and launch configuration defined
  in order to be created.

**Scaling policy:**
* You can associate cloudwatch alarms and scaling policies to an ASG group
  to adjust dynamically.
* The policy is a set of instructions that tell ASG whether to scale out or in.
* You can associate more than one scaling policy to an ASG group.

* You are billed for a full hour of running time even for EC2 instances that
  are launched and terminated within the hour.

* A good ASG best practice is to scale out quickly when needed but to scale in
  more slowly to avoid having to relaunch new and separate EC2 instances for
  a spike in workload that fluctuates up and down within minutes.
* It is important to consider bootstrapping for EC2 instances launched by
  ASG.
* It takes time to configure each EC2 instance before the instance is
  healthy and capable of accepting traffic.
* Instances that are more stateless instead of stateful will more gracefully
  enter and exit an ASG group.

## ASG Limits
* Default launch configurations per region: 200
* Default ASG groups per region:            200
* Default scaling policies per ASG:         50
* Default scheduled actions per ASG:        125
* Default SNS topics per ASG:               10
* Default Classic LBs per ASG:              50
* Default Target groups per ASG:            50
* Step adjustments per scaling policy:      20

**Default Termination Policy**
* AWS applies a number of criteria in deciding instance termination during a scale-in
  event, but the most basic is **use the oldest launch template or configuration**

* [ASG instance termination](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html)

**Scale-in protection**
* You can enable instance scale-in protection at the ASG level or an individual
  ASG instance.
* An instance inherits the scale-in protection of the ASG when it is launched.
* You can change the scale-in protection setting from an ASG or an ASG instance
  at any time.
* If you detach an instance that is protected from scale-ins, it looses it's
  scale in protection setting.
* It does not prevent ASG instances from the following:
  * Manual termination of EC2 instances.
  * Health check replacement if the instance fails health checks.
  * Spot instance interruptions.



--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
## AWS Identify and Access Management (IAM)
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

Example 4:
* This example policy allows access to dynamodb:GetItem, but only between
  Jul 1, 2020 and Dec 31, 2020 and if initiated from a specific vpc.
```
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Action": "dynamodb:GetItem",
        "Resource": "*",
        "Condition": {
            "DateGreaterThan": {
                "aws:CurrentTime": "2020-07-01T00:00:00Z"
            },
            "DateLessThan": {
                "aws:CurrentTime": "2020-12-31T23:59:59Z"
            }
        },
        "StringEquals": {
            "aws:SourceVpc": "vpc-111bbb22"
        }
    }
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

#--------------------------------------------------------------------------------
## AWS Directory Service:
#--------------------------------------------------------------------------------
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
*  Multi-az deployment                         * Users, groups & group policies
*  Patch, monitor, recover domain controller   * Standard AD tools
*  Instance rotation, version upgrades         * Scale out Domain controllers
*  snapshot and restore                        * Employ AD Trusts (resource forests)
                                               * Mgmt of certificate authorities & Federation

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
- Read-after-write consistency for PUTS of new objects (new Key) - Means if you
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
* Stored redundantly across multiple devices in multiple facilities, and
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
* *Governance Mode*:
  - In this mode, users can't overwrite or delete an object or later change it's lock
    settings unless they have special permissions.
  - You protect objects against being deleted by most users, but you can still grant
    some users permissions to later change retention settings or delete the object.
* *Compliance Mode*:
  - In this mode protected object version can not be overwritten or deleted by any
    user, including the root user.
  - Objects can't be overwritten, deleted for the duration of the retention period.

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
* Max number of file shares per gateway is 10.
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
* The tape gateway is deployed in your on-prem environment as a VM running on
  VMWare ESXi, KVM or Microsoft Hyper-V.
* Minimum size of virtual tape: 100GB
* Maximum size of a virtual tape: 2.5 TB
* Maximum number of virtual tapes for a VTL (virtual tape library): 1500
* Total size of all tapes in a VTL: 1 PB.
* Maximum number of virtual tapes in archive: unlimited.

--------------------------------------------------------------------------------

## Database Migration Service (DMS) (On-prem services)
* DMS is a cloud service that makes it easy to migrate relational databases,
  data waehouses, NoSQL databases and other types of data stores to AWS.
* Can setup one-time migration or on-going replication. On-going replication keeps
  your source and target databases in sync.
* Supports homogenous migrations such as Oracle to Oracle, as well as hetrogenous
  migrations between different database platforms, such as Oracle or MS SQL to
  Amazon Aurora.
* Source DB remains fully operational during the migration, minimizing downtime.

--------------------------------------------------------------------------------

## Server Migration Service (SMS)  (On-prem services)
* Automates migration of on-prem virtual machines to AWS cloud.
* Supports incremental replication of your server VMs as cloud-hosted AMIs ready
  for deployment on EC2.

--------------------------------------------------------------------------------








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

* Macie is a security service which uses ML and NLP to discover, classify and
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

**NOTE**:
The older way of accessing the instance metadata is being replaced with a more secure
method, known as IMDSv2.

IMDSv2 uses session oriented requests. You can create a session token that defines
the session duration, which can be from 1 sec to 6 hours.

Example:

creating a token:
```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" \
       -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
```

Using the token to query metadata service
```
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/
```


**Termination Protection**
* Prevents from accidental Termination from console, CLI or API.
* It does not prevent termination triggered by an OS shutdown command,
  termination from an ASG, or termination of a spot instance due to spot price
  changes
* It is turned off by default, you must turn it on.


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
* Good for flexibility, short-term use or testing the waters.

## Reserved
* Provides you with capacity reservation.
* Offers a significant discount on the hourly charge.
* Contract terms are 1 Year or 3 Years.
* Good for: Predictable usage, specific capacity requirements

**Standard Reserved Instances**
* Offer up to 72% off on demand instances. The more you pay upfront and longer the
  contract, the greater the discount.
* Enables you to modify AZ, scope, networking type and instance size within the same
  instance type of your RI.

**Convertible Reserved Instances**
* Offer up to 54% off on demand.
* Capability to change the attributes of the RI as long as the exchange results in
  the creation of RIs of equal or greater value.
* Enables you to exchange one or more convertible RIs for another convertible RI
  with a different configuration, including instance family, OS and tenancy.
* There are no limits to how many times you can perform an exchange as long as the
  target RI is of an equal or higher value than the convertible RI that you are
  exchanging.

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
* Enables you to purchase unused capacity at a discount of up to 90%.
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
**Usecases**
- compliance: Regulatory requirements that may not support multi-tenancy.
- licensing: which does not support multi-tenancy


## Savings Plans
* Three types:
  * Compute savings Plan: apply to usage on EC2, Lambda and AWS Fargate.
  * EC2 savings plan: apply to EC2 usage
  * SageMaker savings plan: apply to SageMaker usage.

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



#--------------------------------------------------------------------------------
## EBS (Elastic Block Storage)
#--------------------------------------------------------------------------------
* Provide persistent block-level storage volumes for use with EC2 instances.
* EBS volume is automatically replicated within it's AZ to provide HA and durability.
* you can dynamically increase capacity and change volume type with no downtime or
  performance impact to live systems.

--------------------------------------------------------------------------------
**Types of EBS Volumes**

## Solid state drives
**General purpose SSD (gp3)**
* 99.8 - 99.9% durability
* Ranges from 1GB to 16TB volume size, and provides baseline performance of 3 IOPS
  per gigabyte provisioned.
* EG: For a 1 TB volume, you can expect a baseline performance of 3000 IOPS.
* Under 1TB it has ability to burst up to 3000 IOPS for extend periouds of time.
* When not using, IOPS are accumulated as I/O credits, which get used during
  heavy traffic.
* Use cases:
 * system boot volumes
 * small to medium sized DB
 * Dev and test environments.
* Max IOPS per volume: 16,000
* Max throughput: 1,000 MiB/s


**Provisioned IOPS SSD**
* Designed to meet needs of I/O intensive workloads.
* Ranges from 4 GB - 16 TB.
* When provisioning, specify the size and desired IOPs, up to the lower of
  maximum of 30 times the number of GB of volume or **64,000 IOPs.**
  NOTE IO2 Block express can go upto a Max of 256,000 IOPS.
* EBS delivers within 10% of the provisioned IOPS 99.9% of the time over a
  given year.
* Price is on the provisioned size. Additional monthly fee is based on provisioned
  IOPS (whether consumed or not).
**Use cases:**
 * Critical business apps requiring sustained IOPS.
 * Large DB workloads

**IO2**
* Lagest generation of provisioned IOPs
* Higher durability and performant.
* 500 IOPS per GIG
* 99.999% durability instead of 99.8 - 99.9 % durability
* I/O intensive apps, large DBs and latency sensitive workloads.


## HDD Hard disk drives
**Throughput optimized HDD (st1)**
* baseline throughput of 40 MB/s per TB.
* Burst up to 250 MB/s per TB with Max throughput of 500 MB/s per TB.
* Sequential writes
* Frequently accessed workloads.
* Usually used for data warehouse apps, throughput-intensive workloads, Big Data,
  ETL and log processing.
* Volume size 125GB - 16 TB.
* Cannot be a boot volume.

**Cold HDD (sc1)**
* Baseline throughput of 12 MB/s per TB.
* Ability to burst up to 80 MB/s per TB with Max throughput of 250 MB/s per TB.
* Less frequently accessed data.
* Usually used for file servers.
* Cannot be a boot volume.

* st1 and sc1 cannot be used as root volumes.
* HDD, magnetic - standard can be used for root volumes.
* Termination protection is turned off by default, you must turn it on.
* Default action for the root EBS volume is to be deleted when the instance is
  terminated.


## EBS Magnetic volumes (standard)
* Lowest performance characteristics and lowest cost per gigabypte.
* Great cost effective solution for appropriate workloads
* Can range from 1 GB - 1 TB and average 100 IOPS, with ability to burst to
  hunders of IOPs.
* Use cases:
 * Infrequently accessed data
 * Sequential reads.
 * Situation where low-cost storage is a requirement.
* Billed based on provisioned space, regardless of how much data is actually
  stored on the volume.

--------------------------------------------------------------------------------

## I/O credits and burst performance.
* Performance of gp2 volumes is tied to volume size, which determines the baseline
  performance level of the volume and how quickly it accumulates I/O credits.
* I/O credits represent the available bandwidth that your gp2 volume can use to
  burst large amounts of I/O when more than the baseline performance is needed.
* Each volume receives an intial I/O credit of 5.4 million I/O credits - enough to
  sustain a max burst performance of 3000 IOPS for atleast 30 minutes.
* If your gp2 volume uses all it's I/O credit, the max IOPS performance of the
  volume remains at the baseline IOPS performance level.

--------------------------------------------------------------------------------
## Protecting data

**snapshots:**
* Snapshots are incremental backups, meaning only the blocks on the device that have
  changed since your most recent snapshot are saved.
* Snapshots are saved in S3. They are point-in-time copies of the volume.
* The action for taking a snapshot is free. You pay for the storage cost.
* Snapshots are constrained to the region in which they are created. Meaning
  you can use them to create new volumes only in the same region.
* If you need to restore a snapshot in a different region, you can copy a
  snapshot to another region.
* To use a snapshot you create a new EBS volume from the snapshot. The volume
  is created immediately, but data is loaded lazily - Means the volume can be
  accessed upon creation, and if the data being requested is not yet restored, it
  will be upon first request.
* Snapshots can be used to increase the size of an EBS volume.
* Snapshots of encrypted volumes are encrypted automatically.
* Volumes restored from encrypted snapshots are encrypted automatically.
* You can share snapshots, but only if they are unencrypted.
* To create a snapshot for EBS volumes that serve as root devices, you should stop
  the instance before taking the snapshot.

--------------------------------------------------------------------------------

**Encryption:**
* EBS volumes can be encrypted. Uses AWS Key management service to handle key
  management.
* A new master key is created unless you select a master key.
* Data and keys are encrypted using AES-256 algorithm.
* Encryption happens on the servers that host the EC2 instance, so the data is
  actually encrypted in transit between the host and the storage media and also
  on the media.
* Encryption is transparent, and you can expect same IOPS performance with minimal
  effect on latency.
* Snapshots from encrypted volumes are automatically encrypted, as are the volumes
  created from encrypted snapshots.
* EBS Root volumes of your default AMIs cannot be encrypted.
* You can use 3rd party tools to encrypt the root volume, or it can be Done
  when creating AMIs in the AWS console or using API.
* You are not tied to the type of volume with snapshot. Meaning - you could have a
  snapshot of a volume of type magnetic disk, and you can created a new volume from
  this snapshot with a different volume type like SSD.

* To move an EC2 volume from one AZ to another, take a snapshot of it, create an
  AMI from the snapshot and then use the AMI to launch the EC2 instance in the
  new AZ.
--------------------------------------------------------------------------------

## Instance stores:
* Provides temporary block-level storage for your instance.
* Located on disks that are physically attached to the host computer.
* The size of an instance store as well as the number of devices available varies by
  instance type.
* Data in an instance store persists only during the lifetime of it's associated
  instance.
* If the instance reboots (intentionally or unintentionally), data in the instance
  store persists.
* Data in the instance store is lost when:
  * The underlying disk drive fails.
  * The instance is stopped.
  * The instance terminates.
* When you stop or terminate an instance, every block of storage in the instance
  store is reset. Therefore data cannot be accessed through the instance store of
  of another instance.
* If you create an AMI from the instance, the data on it's instance store volumes
  isn't preserved and isn't present on the instance store volumes of the instance
  that you launched from the AMI.
* You cannot create a snapshot of an instance store like you can for an EBS volume.

--------------------------------------------------------------------------------

## ENI vs ENA vs EFA

## Elastic Network Interface (ENI):
* An ENI is a virtual n/w interface that you can attach to an instance in a VPC.
* ENIs are only available within a VPC and are associated with a subnet upon
  creation.
* They can have 1 public ip address and multiple private ip addresses. One of
  them is primary.
* Allows you to create dual-homed instances with workloads on distinct subnets.
* Each instance has a default network interface, called the primary network
  interface. You cannot detach a primary network interface from an instance.
* You can enable/disable source destination checks. These checks are enabled by
  default.

* **Hot attach**: Attaching a network interface to an instance when it's running
* **warm attach**: Attaching a network interface to an instance when it's stopped
* **cold attach**: Attaching a network interface to an instance when it's launching

* You can detach secondary n/w interfaces when the instance is running or stopped.
* You cannot detach a primary netork interface.
* You can move an ENI from one instance to another if they are in the same AZ
  and VPC but in different subnets.
* When launching an Amazon Linux or Windows instance with multiple ENIs, automatically
  configures interfaces, private IPV4 addresses and route tables on the OS.
* A warm or hot attach of an ENI may require you to manually bring up the interface,
  configure the ipv4 address and modify the route table.
* Attaching a second ENI cannot be used as a method to increase network bandwidth
  to/from the dual-homed instance.



## Enhanced Networking (EN)
* Enhanced networking uses single root I/O virtualization (SR-IOV) to provide
  high performance networking capabilities on supported instance type.
* Provides higher I/O performance and lower CPU utilization when compared to
  traditional virtualized network interfaces.
* There is no additional charge for using enhanced networking.
* You can enable EN, using one of the following:
  **Elastic Network Adapter (ENA)**
  * ENA supports n/w speeds of up to 100 Gbps for suppored instance types.
  * Supported by all instances except C4, D2 & M4 (smaller than m4.16xlarge)

 **Intel 82599 Virtual Function (VF) Interface**
 * Supports n/w speeds of up to 10 Gbps for supported instance types.
 * Instance types that use VF: C3, D4, D2, I2, M4 (excluding M4.16xlarge), R3

## Elastic Fabric Adapter
* A network device that you can attach to your Amazon EC2 instance to accelerate
  high performance computing (HPC) and machine learning applications.
* Provides lower and more consistent latency and higher throughput than TCP
  transport traditionally used in cloud-based HPC systems.
* EFA can use OS-bypass. OS-bypass enables HPC and machine learning applications to
  bypass the operating system kernel and communicate directly with the EFA device.
  NOT supported with windows currently, only Linux.

--------------------------------------------------------------------------------

## Spot Instances
* It is an instance that uses spare EC2 capacity that is available for less than
  on-demand price.
* You can request a spot instance at a steep discount as compared to on-demand.
* The spot price for each instance type in each AZ is set by Amazon EC2 and is
  adjusted based on long-term supply of and demand for spot instances.

## Spot Instance Request
* To use spot instance you create a spot instance request.
* It should include:
  * Desired number of instances
  * AZ
  * Maximum price
  * Launch specification
  * Request type: one-time | persistent.
  * Valid from, valit until

## Spot fleets
* A collection of spot instances and optionally on-demand instances.
* Attempts to launch the number of spot instances and on-demand instances to meet
  the target capacity you specified in the spot fleet request.
* Request for spot instances is fulfilled if there is available capacity and the
  maximum price you specified in the request exceeds the current spot price.

* strategies for spot fleets:

**Capacity Optimized**
* The spot instances come from the pool with optimal capacity.
* It launches spot instances into the most available pools by looking at real-time
  capacity data.
* Possibility of fewer interruptions.

**Lowest price**
* This is the default strategy. Spot instances come from the pool with lowest cost.

**Diversified**
* Spot instances are distriuted across all pools.

**InstancePoolsToUseCount**
* Spot instances are distributed across the number of Spot pools that you specify.
  This parameter is valid only when used in combination with lowestPrice.

--------------------------------------------------------------------------------

## EC2 Hibernate
* EC2 hibernate preserves the in-memory RAM on persistent storage (EBS)
* Much faster boot up because you do not need to reload the OS.
* Instance RAM must be less than 150 GB.
* Instances families, include C3-5, M3-5, R3-5.
* Available for windows, Amazon Linux 2 AMI and ubuntu.
* Instances can't be hibernated for more than 60 days.
* Available for on-demand or reserved instances.
* You are not charged for an instance usage for a hibernated instance when it is
  in stopped state.

--------------------------------------------------------------------------------

## Security groups
* A virtual firewall that controls inbound and outbound traffic to AWS resources
  and EC2 instances.
* Security groups are stateful, unlike Network ACLs which are stateless.
* If a SG is not specified at launch, then the instance will be launched with a
  default SG.
* A default SG:
  * Allows all outbound traffic
  * Denies all inbound traffic
  * Allows communication within the SG.
* You can create up to 500 security groups per VPC.
* You can add 50 inbound and 50 outbound rules to each SG.
* You can specify allow rules but not deny rules in a SG.
* Have sparate rules for inbound and outbound traffic.
* By default all outbound traffic is allowed.
* SGs are stateful - this means the responses to allowed inbound traffic are
  allowed to flow outbound regardless of the outbound rules.
* You can change the SG which is associated to an instance, and changes will take
  effect immediately.
* Security groups and Network ACLs can span multiple AZs.
* Your VPC includes a default security group. You can't delete this group, but you
  can change the group rules.

--------------------------------------------------------------------------------

## Network ACLs
* Your VPC automatically comes with a default network ACL, and by default it allows
  all outbound and inbound traffic.
* You can create a custom network ACL and associate it with a subnet. By default
  it denies all inbound and outbound traffic, until you add rules.
* Operates at subnet level (second level of defense)
* Supports allow and deny rules.
* It is stateless. Return traffic must be explicitly allowed by rules.
* Processes rules in numbered order when deciding whether to allow traffic. Starting
  with the lowest numbered rule.
* Automatically applied to all EC2 instances in the associated subnet.
* Each subnet in your VPC must be associated with a network ACL. If you do not
  explicitly associate a subnet with a network ACL, the subnet is automatically
  associated with the default network ACL.
* You can associate network ACL with multiple subnets, but a subnet can be
  associated to only one network ACL at a time.

**Ephemeral ports**
* To cover the different types of clients that might initiate traffic to public
  facing instances in your VPC, you can open ephemeral ports 1025-65635. However
  you can also add rules to your ACL to deny traffic on any malicious ports within
  that range.
* Remember to place DENY rules earlier in table than ALLOW rules that open the wide
  range of ephemeral ports.

--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
## CloudWatch:
#--------------------------------------------------------------------------------

Monitoring service to monitor your AWS resources, as well as the applications
that you run on AWS.
* Two plans: basic/standard and detailed.
* Basic monitoring is default, sends data points to cloudwatch every 5 minutes for
  limited number of metrics.
* Detailed is to be explicitly enabled. Sends data points every minute and allows
  data aggregation.
* Limit of 500 alarms per AWS account.
* Metrics data is retained for 2 weeks.
* A cloudwatch log agent is available that provides an automated way to send log
  data to cloudwatch logs. Install it on EC2 instance. It stays running until disabled.
* Cloudwatch metrics provide hypervisor visible metrics.
* By default it monitors host level metrics:
  * CPU
  * Network
  * Disk
  * Status check.

## Cloudwatch concepts:
**Namespaces:**
* Is a container for cloudwatch metrics.
* Metrics in different namespaces are isolated from each other.
* There is no default namespace. You must specify a namespace for each
  data point you publish to cloudwatch.
* Names must contain valid XML characters and must be < 265 characters in length.
**Metrics:**
* Metrics are the fundamental concept in cloudwatch. It represents a time-ordered
  set of data points that are published to cloudwatch.
* Think of metrics as a variable to monitor, and data points as representing the
  values of that variable over time.
* Metrics exist in the region they were created.
* Metrics cannot be deleted, but they automatically expire after 15 months if no new
  data is published to them. Data points older than 15 months expirre on a rolling
  basis, as new data points come in.
**Timestamps:**
* Each metric data point must be associated with a timestamp.
* Timestamp can be 2 weeks in the past or upto two hours in the future.
* If you do not provide a timestamp, Cloudwatch creates it for you based on the time
  the data point was received.
**Metrics Retention:**
* Data points with a period of < 60 secods are available for 3 hours. These are high
  resolution custom metrics.
* Data points with a period of 60 seconds (1 min) are available for 15 days
* Data points with a period of 300 seconds (5 min) are available for 63 days
* Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months)
**Dimensions:**
* A dimension is a name/value pair that is part of the identity of a metric.
* You can assign upto 10 dimensions to a metric.
* Cloudwatch treats each unique combination of dimensions as a separate metric, even if
  the metric have the same metric name.
**Resolution**:
* Each metric is either:
  * Standard resolution, with data having a one-minute granularity.
  * High resolution, with data at a granularity of one second.
**Statistics:**
* Statistics are metrics data aggregations over specified periods of time.

--------------------------------------------------------------------------------

## EC2 Placement groups:

**Cluster placement group**
* Group of instances within a single AZ.
* Recommended for apps that need low network latency, high nw throughput
* Only certain instances can be launched in a clustered placement group.

**Spread placement group**
* A group of instances that are each placed on distinct underlying hardware.
* Are recomended for apps that have a small number of critical instances that
  should be kept separate from each other.
* Have a limitation of maximum of 7 running instances per AZ.

**Partitioned placement group**
* Amazon EC2 divides each group into logical segments called partitions.
* Each partition within a placement group has it's own set of racks.
* Each rack has its own n/w and power source.
* No two partitions within a placement group share the same rack.
* Allows you to isolate the impact of hardware failure within your application.

* Name you specify for a placement group must be unique within your AWS account.
* Only certain type of instances can be launched in a placement group (Compute
  optimized, GPU, Memory optimized, Storage optimized)
* AWS recommends homogenous instances within clustered placement groups.
* You can move an existing instance in to a PG. Before you move, the instance must
  be in stopped state.


--------------------------------------------------------------------------------

## HPC on AWS
HPC is used for industries such as genomics, finance and financial risk modeling,
machine learning, weather prediction and even autonomous driving.

What are the different services we can use to achive HPC on AWS?

**Data transfer**
* Snowball, Snowmobile (terabytes/petabytes worth of data)
* AWS Datasync to store on S3, EFS, FSx for windows etc
* Direct connect

**Compute and Network services**
* EC2 instances (GPU or CPU optimized)
* EC2 fleets (spot instances or spot fleets)
* Placement groups (cluster placement)
* Enhanced networking
* Elastic network adapters (ENA)
* Elastic fabric adapters

**Storage services**
* EBS: scales up to 64000 IOPS with provisioned IOPS
* Instance store: Scales up to millions of IOPS; low latency

Network storage:
* Amazon S3.
* Amazon EFS
* Amazon FSx for lustre.

**Orchestration & Automation**
*AWS Batch:*
* Easily and efficiently run hunderes and thousands of batch computing jobs on AWS.
* Supports multi-node parallel jobs, which allows you to run a single job that
  spans multiple EC2 instances.
* Easily schedule jobs and launch EC2 instances according to your needs.

*AWS ParallelCluster*
* Open-source cluster management tool - make sit easy to deploy and manage HPC
  clusters on AWS.
* Uses a simple text file to model and provision all the resources needed for HPC
  applications
* Automate creation of VPC, subnet, cluster type, and instance types.

--------------------------------------------------------------------------------

## AWS WAF (Web Application Firewall)
* It's a layer 7 aware firewall.
* AWS WAF lets you monitor the HTTP and HTTPs requests that are forwarded to API
  gateway, Cloudfront or ALB.
* It also lets you control access to your content.
* WAF allows 3 different behaviors:
 * Allow all requests except the ones you specify
 * Block all requests except the ones you specify
 * Count the requests that match the properties you specify (passive)
* Configure filter rules to allow/deny traffic:
 * IP address
 * Query string parameters
 * SQL query injection
 * Cross-site scripting attacks.
* Extra protection against web attacks using contitions you specify.
 * IP addresses that request originate from
 * Country that requests originate from.
 * Values in request headers.
 * Strings that appear in requests, either specific strings or string that match
   regular expressions.
 * Length of requests
 * Presence of SQL code that is likely to be malicious (SQL injection)
 * Presence of a script that is likely to be malicious (Known as cross-site scripting)


--------------------------------------------------------------------------------

## AWS Firewall Manager
* Centrally configure and manage firewall rules across an AWS organization.
* Using firewall manager you can adminster tasks across multiple accounts and
  resources for different protections including AWS WAF< AWS Shield Advanced,
  VPC Security groups, Network firewall and Route53 resolver DNS firewall.
* You setup protections once and service automatically applies them across your
  accounts and resources, even as you add new accounts and resources.








#--------------------------------------------------------------------------------
# SQS Simple Queue Service
#--------------------------------------------------------------------------------
* A fast, reliable, scalable and fully managed queuing service.
* Using SQS, you can decouple the components of an application so they run
  independently.
* Messages can contain up to 256KB of text in any format.
* To manage large messages you can use S3 and SQS Extended client library for Java.
  Useful for storing and consuming messages up to 2 GB. You can't do this with
  AWS CLI, console, HTTP API or any other AWS SDK.
* Makes it simple and cost effective to decouple components of your cloud application.
* Makes a best effort, but Does not guarantee message delivery order (no FIFO)
* If message order is required applications can handle that by passing a message
  sequence id.
* Ensures delivery of each message at least once and supports multiple readers and
  writers interacting with the same queue.
* NOTE: SQS is pull based, not push based.

## Message lifecycle
1. (Producer) sends message A to a queue. The message is redundantly distributed
   across the SQS servers.
2. (Consumer) retrieves the message from the queue and message A is returned
   .While message A is being processed, it remains in the queue and is not
   returned to subsequent receive requests for a duration of the visibility timeout.
3. (consumer) deletes message A from the queue to prevent the message from being
   received and processed again after the visibility timeout expires.

## Delay queues and visibility timeouts:

**Delay Queues**
* Delay queues allow you to postpone the delivery of a new message in a queue for
  specific number of seconds.
* Any message that you send in that queue will be invisible to the consumer for the
  duration of the delay period.
* Delay period can range from 0 to 900 seconds (0 to 15 mins)
* Default value of delay period is 0 seconds.
* You can turn an existing queue into a delay queue using SetQueueAttributes to set
  the queue's DelaySeconds attribute.

**Visibility timeout**
* Visibility timeout is the amount of time a message is invisible in the SQS queue
  after a reader picks up the message. Provided the job is processed before the
  visibility timeout expires, the message will then be deleted from the queue. If the
  job is not processed within that time, the message will become visible again and another
  reader will process it. This could result in same message being delivered twice.
* Immediately after a message is received, it remains in the queue. SQS sets
  visibility timeout, a perioud during which SQS prevents other consumers from
  receiving and processing the message.
* Default visibility timeout is 30 seconds. Min is 0 seconds, Max is 12 hours.
* SQS automatically deletes messages that have been in the queue for more than
  maximum message retention period.
* Message retention periods: Default: 4 days, Shortest: 60 secs, Longest: 14 days.
* Visibility timeout begins when SQS returns a message. During this time the
  consumer processes and deletes the message.
* If the consumer fails to delete the message within the visibility timeout, the
  message becomes visibile to other consumers and is received again.

**Message states**
An SQS message has three basic states:
1. Sent to a queue by a producer.
* This message is considered 'stored' after it is sent to a queue by a producer, but
  not yet received from the queue by a consumer.
* There is no quota on stored messages (unlimited stored messages)

2. Received from the queue by a consumer.
* A message is considered 'in flight' after it is received by a consumer, but not yet
  deleted from the queue.
* There is a quota on inflight messages. A max of 120,000 messages can be inflight.

3. Deleted from the queue.
* A message is deleted by the consumer after processed.

* SQS returns OverLimit error if the quotas are exceeded.

## Queue operations, unique ids and metadata.
* Some SQS Operations:
  CreateQueue, ListQueues, DeleteQueue, SendMessage, SendMessageBatch,
  ReceiveMessage, DeleteMessage,..
* Messages are identified via a globally unique ID that SQS returns when the
  message is delivered to the queue. The ID is useful for tracking whether a
  particular message in the queue has been received.
* When you receive a message from the queue, the response includes a receipt
  handle, which you must provide when deleting the message.

## Queue and message identifiers:
* Three identifiers for SQS: queue URLs, message IDs and receipt handles.
* When creating a new queue, you must provide a queue name that is unique within
  the scope of all your queues. SQS assigns each queue an identifier called
  the queue URL, which includes the queue name and other components that SQS
  determines.
* Provide the queue URL whenever you want to perform an action on the queue.

* SQS assigns each message a unique ID, that it returns to you in the
  SendMessage response.
* The identifier is useful for identifying messages but not deleting it.

* Each time you receive a message from a queue, you also get a receipt handle
  for that message.
* To delete the message you must provide the receipt handle.
* Max length of the receipt handle is 1024 characters.

## Message Attributes:
* Provide structured metadata items about the message.
* Each message can have up to 10 attributes.
* Are optional and separate from, but sent along with the message body.
* The receiver can use this information to help decide how to handle the message
  without having to process the message body first.


## Long polling:
* To receive message the consumer invokes ReceiveMessage API.
* ReceiveMessage will check for existence of a message in the queue and return
  immediately, either with or without a message.
* With long polling, you send WaitTimeSeconds argument to ReceiveMessage of up to
  20 seconds.
* If there is no message in the queue the call will wait up to WaitTimeSeconds
  for a message before returning.
* If a message appears before the time expires, the call will return with the
  message right away.

## Dead Letter Queues:
* A queue that other queues can target to send messages that for some reason could
  not be successfully processed.
* Ability to sideline and isolate unsuccessfully processed messages.

## FIFO queue
* FIFO queue complements the standard queue.
* Most important features are FIFO delivery and exactly-once processing. The order
  in which the messages are sent and received is strictly preserved and a message
  is delivered once and remains available until a consumer processes and deletes
  it. Duplicates are not introduced into the queue.
* FIFO queues also support message groups that allow multiple ordered message
  groups within a single queue.
* FIFO queues are limited to 300 transactions per second, but have all the
  capabilities of a standard queue.


--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
## Simple Workflow Service (SWF):
#--------------------------------------------------------------------------------
* SWF makes it easy to coordinate work across distributed application components.
* SWF enables applications for a range of use cases, including media processing,
  web application backends, business process workflows and analytics pipelines,
  designed to coordinate tasks.
* In SWF task represents a logical unit of work that is performed by a component
  of your application.
* You implement the workers to perform tasks.
* Workers can run either on EC2 or on-premises instances/servers.
* You can create long running tasks that might fail, timeout or require restart
  or tasks that can complete with varying throughput and latency.
* SWF stores tasks, and assigns them to workers when they are ready, monitor
  their process and maintain their state, including details on their completion.
* To coordinate tasks you write a program that gets the latest state of each
  task from SWF and uses it to initiate subsequent tasks.
* SWF workflow executions can last up to 1 year.

## Workflows:
* In SWF you can implement distributed, asynchronous applications as workflows.
* Workflows coordinate and manage execution of activities that can be run
  asynchronously across multiple computing devices and that can feature both
  sequential and parallel processing.

## Workflow Domains:
* Workflows in different domains cannot interact with one another.
* Domains are a way of scoping SWF resources within your AWS account.

## Workflow history:
* Is a detailed, complete and consistent record of every event that occurred
  since the workflow execution started.

## Actors:
* Programatic features are known as actors.
* They can be **workflow starters**, **deciders** or **activity workers**.
* Actors communicate with SWF through it's API.
* You can develop actors in any programming language.
* A workflow starter is an app that initiates workflow executions - like a
  website or a mobile application.
* A decider is the logic that coordinates the tasks in a workflow. The decider
  also processes events that arrive while the workflow is in progress.
* An activity worker is a single computer process (or thread) that performs
 the activity task in your workflow.


## Tasks:
* Three types of tasks:
  * Activity tasks:
    * tells and activity worker to perform it's function.
  * AWS Lambda tasks:
    * Similar to activity task, but executes an AWS Lambda function
  * Decision tasks:
    * Tells a decider that the state of the workflow execution has changed
      to determine the next activity that needs to be performed.

--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
## Simple Email Service (SES):
#--------------------------------------------------------------------------------
* Provides an easy, cost-effective way to send and receive email using your
  own email addresses and domains.
* Can trigger a lambda function or SNS notification.
* Can be used for both incoming and outgoing email.
* Email address is all that is required to start sending messages.

### Sample operations with SES.

**Send an email (Raw format)**

```
 %~> aws sesv2 send-email \
    --destination ToAddresses=bdastur@acme.com --content file://message.json \
    --from-email-address bdastur@acme.com \
    --cli-binary-format raw-in-base64-out  --profile dev --region us-east-1
```

The message.json file looks like this:
```
 %~> more message.json
{
    "Raw": {
        "Data": "This is a test message - raw email from CLI"
    }
}

```

NOTE: Here the the option '--cli-binary-format raw-in-base64-out' was to workaround
the following error when executing send-email cli:
```
Invalid base64: "THis is a test message - raw email from CLI"

Git issue: https://github.com/aws/aws-cli/issues/6657
```


--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
## Simple Notification Service (SNS):
#--------------------------------------------------------------------------------
* A web service for mobile and enterprise messaging that enables you to setup,
  operate and send notifications.
* It follows the publish-subscribe messaging paradigm, with notifications being
  delivered to clients using push mechanism that eliminates the need to check
  periodically for new updates.
* You can use SNS to send short message service (SMS) messages to mobile devices
  in the US or to email recipients worldwide.
* Two client types:
  * **Publishers** and **Subscribers**.

* Publishers communicate to Subscribers asynchronously by sending a message to
  a topic.
* A topic is simply a logical access point/communication channel that contains
  a list of subscribers and the methods used to communicate to them.
* When you send a message to a topic it is automatically forwarded to each
  subscriber of that topic using the communication method configured for that
  subscriber.
* Topic names should typically be available for reuse approx 30 - 60 seconds
  after the previous topic with same name is deleted. Topics with larger
  subscription lists may take longer.
* After a message has been successfully published to a topic, it cannot be
  recalled.
* Protocols included: HTTP, HTTPS, EMAIL, EMAIL-JSON, Amazon SQS, Application.

### Common SNS scenarios:
* Fanout:
  A SNS message is sent to a topic and then replicated and pushed to
  multiple SQS queues, HTTP endpoints or email addresses.
* Application and System Alerts:
  They are SMS and/or email notifications that are triggered by predefined
  thresholds.
* Push Email and Text messaging:
  Two ways to transmit messages to individuals or groups via email and/or SMS.
* Mobile push notifications:
  Enables you to send messages directly to mobile applications.

--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
## Elastic Transcoder
#--------------------------------------------------------------------------------
* Media transcoder in the cloud.
* Convert media files from original source into different formats that will play
  on smartphones, tables, PCs etc.


#--------------------------------------------------------------------------------
## API Gateway
#--------------------------------------------------------------------------------
* Fully managed service that makes it easy for developers to publish, maintan,
  monitor and secure APIs at any scale.
**what can it do?**
* Exposes HTTPs endpoints to define a restful api.
* Serverless-ly connect to services like lambda and dynamodb.
* Send each API endpoint to a different target.
* Run efficiently with low cost.
* Scale effortlessly
* Track and control usage by API key.
* Throttle requests to prevent attacks
* Connect to cloudwatch to log all requests for monitoring.
* Maintain multiple versions of API.
* You can throttle API GW to prevent attacks
* If you are using JS/AJAX that uses multiple domains with API GW, ensure that
  you have enabled CORS on API GW.

**API Gateway Caching**
* You can enable API caching to cache your endpoint's response.
* With caching you can reduce the number of calls made to your endpoint and also
  improve latency of the requests to your API.
* Default TTL for caching is 300 seconds (5 mins).
* When you enable caching for a stage, API GW caches responses from your endpoint
  for a specified time-to-live period, in seconds.
* Then API GW responds to the request by looking up the endpoint response from the
  cache instead of making a request to your endpoint.

**API Gateway Throttling**
* Prevents your API from being overwhelmed by too many requests.
* API GW limits the steady-state request rate to 10,000 requests per second, per
  region by default.
* Maximum concurrent requests is 5,000 requests across all APIs per region.
* If you exceed these limits, you will get a '429 Too Many Requests' error.

### Same origin policy & CORS
* In computing, the same-origin policy is an important concept in the web application
  security model.
* Under the policy, a web browser permits scripts contained in a first web page
  to access data in a second web page, but only if both web pages have the same
  origin (only if they have same domain name).
* This is done to prevent cross-site scripting (XSS) attacks.
* CORS is one way the server at the other end (not the client code in the browser),
  can relax the same-origin policy.
* Cross-Origin resource sharing (CORS) is a mechanism that allows restricted
  resources on a web page to be requested from another domain outside the domain
  from which the first resource was served.

--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
## Amazon Kinesis
#--------------------------------------------------------------------------------

* Platform for handling massive streaming data on AWS

## Kinesis Firehose
* Amazon's data-ingestion product.
* It is used to capture and load streaming data into other AWS services like S3 and
  Redshift.
* Clients write data to stream using API call and data is automatically sent to
  proper destination.
* When configured to save to S3, firehose sends data directly to S3. For Redshift
  data is first send to S3 and then Redshift copy command is executed to load
  data to Redshift.
* Firehose can also write data to Elasticsearch, with option to back it up in S3.
* There is **no data persistence** in Kinesis firehose.


## Kinesis Streams
* you can use Kinesis Data Streams for rapid and cntinuous data intake and
  aggregation.
* Type of data can be: IT infra log data,, appln logs, social media, market data
  feeds and web clickstream data.
* Capable of capturing large amounts of data from data producers and streaming
  it into custom applications for data processing and analysis.
* You can scale to support limitless data streams by distributing incoming data
  across number of shads.
* The processing is then executed on consumers which read data from shards and run
  the kinesis stream application.
* Allows you to **persistently store data for 24 hours up to 7 days.**
* Kinesis streams consist of shards
 - 5 transactions per second for reads, up to a max total data read rate of 2 MB/sec
   and up to 1000 records per second for writes, up to a max total data write rate
   of 1 MB/ sec (including partition keys)

Producers        Kinesis Streams         Consumers

EC2 -----------> Shard  ------------->  EC2               DynamoDB, S3
Mobile --------> Shard  ------------->  EC2      -------> EMR, Redshift
IOT    --------> Shard  ------------->  EC2


## Kinesis Analytics
* Enables you to analyze streaming data real time with standard SQL.
* Works with Firehose or Streams.

--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
## Web Identity Federation & Cognito
#--------------------------------------------------------------------------------
* Web identity federation lets you give your users access to AWS resources
  after they have successfully authenticated with a web-based identity provider
  like Amazon, Facebook or Google.
* Following successful authentication, the user receives and authentication code
  from the Web ID provider, which they can trade for temporary AWS security
  credentials.

**Cognito**
* Amazon Cognito provides web identity federation with following features:
 * Sign-up and sign-in to your apps
 * Access for guest users.
 * Acts as an identity broker between your application and Web ID providers, so
   you don't need to write any code.
 * Synchronizes user data for multiple devices.
 * Recomended for all mobile applications AWS services.
* Cognito brokers between the app and Facebook or Google to provide temporary
  credentials which map to an IAM role allowing access to the required resources.
* No need for applications to embed or store AWS credentials locally on the device
  and it gives users a seamless experience across all mobile devices.

**Cognito userpools**
* User pools are user directories used to manage sign-up and sign-in functionality
  for mobile and web applications.
* Users can sign-in directly to the user pool, or using facebook, amazon or Google.
* Cognito acts as an Identity broker between the identiy provider and AWS.
  Successful authentication generates a JSON Web token (JWTs).

**Cognito Identity pools**
* Identity pools enable provide temporary AWS credentials to access AWS services
  like S3 or DynamoDB.

**Cognito Synchornization**
* Cognito tracks the association between user identity and the various different
  devices they sign-in from. In order to provide a seamless user experience for
  your application.
* It uses push synchronization to push updates and synchronize user data across
  multiple devices.
* Cognito uses SNS to send a notification to all devices associated with a given
  user identity whenever data stored in the cloud changes.

--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
## Amazon EMR
#--------------------------------------------------------------------------------

* Fully managed on-demand Hadoop framework, to process and analyze vast amounts of
  data.
* Central component of EMR is the cluster. Each instance in the cluster is a node.
* node types:
  * **Master node**: A node that manages the cluster.
  * **Core node**:   A node with software components that run tasks and store data
                     in HDFS. (atleast one)
  * **Task node**:   A node with software components that only run tasks and do
                     not store data.

* When you launch an EMR cluster you specify:
  * Instance type
  * Number of nodes in the cluster
  * Version of Hadoop to run
  * Additional tools or applications like Hive, Pig, Spark or Presto.
* You can use EMR with a customized version of hive with connectivity to DynamoDB
  to perform operations on data stored in DynamoDB.

* Storage types when using EMR:
**Hadoop Distributed File System (HDFS)**
* Standard file system that comes with hadoop.
* All data is replicated across multiple instances for durability
* Can use instance storage or EBS.

**EMR File System (EMRFS)**
* Is an implementation of HDFS that allows clusters to store data on S3.
* You get durability and low cost while preserving your data even if the cluster
  shuts down.
* Key factor is whether cluster is persistent.

* For persistent clusters HDFS is appropriate.

* For some use cases like big data workloads, which are run infrequently, it can
  be cost effective to turn off the cluster when not in use.
* These are called **transient clusters**.
* EMRFS is well suited for such clusters as data persist independent of the
  lifecycle of the cluster.

**Use cases:**
  * Log processing: large number of unstructured logs to get useful insights.
  * Clickstream analysis: to segment users and understand user preferences.
  * Genomics and life sciences: Process vas amounts of genomic data and
    other large scientific datasets quickly and efficiently.

--------------------------------------------------------------------------------

## AWS Data pipeline:
* A web servie that helps you reliably process and move data between different
  compute and storage services and also on-premise data sources at specified
  intervals.
* It is best for regular batch processing instead of continuous data streams.

--------------------------------------------------------------------------------

## OpsWorks
* A configuration management service that helps you configure and operate apps
  in a cloud by using Puppet or Chef.
* Can work with any application, and is independent of any architectural patterns.
* You can define an application's architecture and specification of each component,
  including package installation, configuration and resources such as storage.
* Supports both linux and windows servers, including existing EC2 instances and
  servers running in private data center.
**OpsWorks for Puppet Enterprise**
* Lets you create AWS managed Puppet master servers.

**OpwsWorks for Chef Automate**
* Lets you create AWS-managed Chef servers that include Chef Automate premium
  features, and use the Chef DK and other Chef tooling to manage them.

**OpsWorks for Stacks**
* Provides a simple and flexible way to create and manage stacks and applications.
* A stack is a group of instances like EC2 instances and RDS instances.

--------------------------------------------------------------------------------

## AWS Cloudformation
* Provides an easy way to create and manage a collection of related AWS resources,
  provisioning and updating them in a orderly and predictable manner.
* CF Template formats: JSON or YAML.
* By default 'automatic rollback on error' feature is enabled. This will direct
  CF to only create/udpate all resources in your stack if all operations succeed.
  If they do not, CF reverts the stack to the last known stable configuration.

## concepts:
**Templates**
* A template is a blueprint for building your AWS resources. It is defined in
  a JSON or YAML formatted text file.
**Stacks**
* You manage related resources using a single unit called a stack.
* You create update and delete resources, by creating, updating & deleting stacks.
**change sets**
* To make changes to resources in a stack, you update the stack.
* Before making changes to your resources, you can generate a change set, which is
  a summary of your proposed changes.

## Template anatomy:

**Format Version** (optional)
* Identifies the capabilities of the template. Latest format version: '2010-09-09'

**Description** (optional)
* A text string, describing the template.

**Metadata** (optional)
* Objects that provide additional info about the template.

**Parameters** (optional)
* Values to pass to your template at runtime.

**Rules** (optional)
* Validates a parameter or a combination of parameters passed to a template during
  a stack creation or stack update.

**Mappings** (optional)
* A mapping of keys and associated values that you can use to specify conditional
  parameter values.

**Conditions** (optional)
* Conditions that control whether certain resources are created or whether certain
  properties are assigned a value during stack creation or update.

**Transform** (optional)
* For serverless applications, specifies version of the SAM to use.
* To re-use code located in S3.
* Transform: AWS::Serverless-2016-10-31 is required for AWS SAM template files.

**Resources** (required)
* Specifies the stack resources and their properties. This is the only component
  that is required.

**Outputs** (optional)
* Describes the values that are returned whenever you view your stack's properties.

## Cloudformation Nested Stacks

Uses Resource:
`AWS::CloudFormation::Stack`

* Allows you to re-use your CF code.
* Useful for frequently used configurations like load balancers, web or appln
  servers.
* Reference it using the 'Stack' resource type.

--------------------------------------------------------------------------------

## AWS Elastic Beanstalk:
* Fastest way to get application up and running
* Developers simply upload their application code and the service automatically
  handles details like resource provisioning, load balancing, auto scaling
  and monitoring.
* An Elastic Beanstalk application is a logical collection of these AWS beanstalk
  components.
* An application is conceptually similar to a folder.
* An application version refers to a specific labeled iteration of deployable
  code.
* An application version points to an S3 object that contains deployable code.
* An environment is an application version that is deployed on AWS resources.
* Each environment runs only a single application version at a time. However
  the same version or different version can run in many different environments
  at the same time.
* An environment configuration identifies a collection of parameters and
  settings that define how an environment and it's resources behave.
* When env configurations are updated, Elastic beanstalk applies those changes
  to existing resources or deletes and deploys new resources.
* The environment tier that is chosen determines whether AWS elastic beanstalk
  provisions resources to support a web application that handles http/s
  requests or an application that has background processing tasks. Web server
  tier, or worker tier as they are called.
* It does not support applications developed in C++.

**Elastic Beanstalk and Docker containers**
* Elastic Beanstalk supports deployment of Docker containers.
* It handles the capacity provisioning, load balancing, scaling and application
  health monitoring.
* You can run single Docker container on an ec2 instance provisioned by ElBs.
* You can run multiple Docker containers by using an ECS cluster and deploy
  multiple Docker containers on each instance.

--------------------------------------------------------------------------------

## AWS Config:
* Service that provides you with AWS resource inventory, configuration history,
  configuration change notification.
* Gives detailed view of configuration of AWS resources, including how resources
  are related and how they were configured in the past, and shows how relationships
  and configurations changed over time.
* When you turn on AWS config, it first discovers the supported AWS resources and
  generates a configuration item for each resource.
* The configuration item include metadata, attributes, relationships, current
  configuration and related events.
* By default AWS config creates config items for every supported resource in the
  region. You can override that by specifying the resource type you want to it
  to track.

**Usecases:**
* Discovery
* Change management
* Continous audit and compliance
* Troubleshooting
* Security and incident analysis

--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# ## Serverless (Lambda)
#--------------------------------------------------------------------------------

**Links**:
* http://docs.aws.amazon.com/lambda/latest/dg/welcome.html
* http://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
* http://docs.aws.amazon.com/lambda/latest/dg/limits.html


* Server-less way to run your application
* Allows you to run code without provisioning or managing servers.
* Executes your code only when needed and scales automatically from few requests
  per day to thousands per second.
* Supports synchronous and asynchronous invocation of a lambda function.
* You can control the invocation type only when you invoke a lambda function.
* When the lambda function is invoked from another aws service, the invocation
  type is pre-determined.
* languages supported: C#, Java, Node.js, Python.
* Lambda billing is based on both, the MB of RAM reserved and the execution duration
  in 100ms units.


## Creating a Lamda layer with python.

Lambda layers need to follow a specific [directory structure](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
The PATH variable includes specific folders in the /opt directory. If you define the
same folder structure in your layer .zip file, your function code can access the layer
content without the need to specify the path.

For python : python

## Creating a zip file for the layer
```
mkdir tempdir
cd tempdir
python3 -m venv python
source ./python/bin/activate
pip3 install requests
zip -r py38_layer.zip python
```

## Creating or updating a lambda layer.

The same CLI works for creating a new layer or updating an existing layer. If the
layer already exists, it's version will be bumped up by 1.

```
aws lambda publish-layer-version \
    --layer-name py38_layer \
    --compatible-runtimes python3.8 \
    --zip-file fileb://py38_layer.zip \
    --profile test \
    --region us-west-2

```

## Listing lamda layers:

```
aws lambda list-layers --profile dev1 --region us-west-2
```

#### Deleting lambda layers.
You will need to delete all versions of the lambda layer.
```
aws lambda delete-layer-version --layer-name py38_layer --version-number 3 --profile dev1 --region us-west-2
aws lambda delete-layer-version --layer-name py38_layer --version-number 2 --profile dev1 --region us-west-2
aws lambda delete-layer-version --layer-name py38_layer --version-number 1 --profile dev1 --region us-west-2
```

--------------------------------------------------------------------------------

## Serverless Application Model (SAM)
* Extension to cloudformation used to define serverless applications.
* Provides a simplified syntax for defining serverless resources; APIs, Lambda
  functions, DynamoDB tables etc.
* It has it's own CLI called the 'SAM CLI' to package your deployment code, upload
  to S3 and deploy your serverless application.

## Lambda versions.
* $LATEST is always the last version of code you uploaded to Lambda
* use Lambda versioning and aliases to point your apps to a specific version, if
  you don't want to use $LATEST.
  `arn:aws:lambda:us-west-2:4783832992883:function:mylambda:Prod`
  `arn:aws:lambda:us-west-2:4783832992883:function:mylambda:$LATEST`
* If you appln uses an alias, instead of $LATEST, remember that it will not
  automatically use new code when you upload it.

## Lambda concurrent executions.
* Safety feature to limit the number of concurrent executions across all functions
  in a given region per account.
* Default is 1000 concurrent executions per region. Once hit you will get a
  'TooManyRequestsException' and HTTP Status code: 429.
* You can get this limit increased.
* Reserved concurrency gurantees a set number of executions which will always be
  available for your critical function, however this also acts as a limit.

## Lambda and VPC access
* Lambda function needs to have access to 'CreateNetworkInterface' in order to
  begin communicating with resources in your VPC.
* To allow lambda access to VPC - provide VPC config to function - private subenet
  id, security group id.
* Lambda uses VPC information to setup ENIs using an IP from the private subnet
  CIDR range.

## Weighted alias
* A lambda alias allows you to direct traffic to one or more versions of a function.
  You can shift traffic between two versions based on weights (%), which you assign.

## Lambda best practices
* Seperate lambda handler from core logic - reusable code.
* Initialize SDK clients and DB connections outside of function handler, and cache
  static assets locally in /tmp directory.
* To avoid data leaks across invocations, don't use the execution environment to
  store user data, events or other info with security implications.

--------------------------------------------------------------------------------

## AWS X-Ray
* Helps developers analyze and debug distributed applications.
* Provides a visualization of your application's underlying components.

## X-Ray service map:
* Provides an end-to-end view of requests as they travel through your appln. Can
  be used to troubleshoot connectivity and performance issues.
* You will need three things:
  * X-Ray SDK.
  * X-Ray daemon installed on your EC2
  * Instrument your app using the SDK to send required data to X-Ray.

--------------------------------------------------------------------------------

## CLI Pagination.
* You can control the number of items included in the output when you run a
  CLI command.
* By default, the AWS CLI uses a page size of 1000. i.e: if you run the
  `aws s3api list-objects <bucket name>` command on a bucket which has 3000 objects,
  the CLI actually makes 3 API calls to S3, but displays the entire output in one
  go.
* 'max-items' is The  total number of items to return in the command's output
  If the total number of items available is more than the value specified, a NextToken
  is provided in the command's output. To resume pagination provide the NextToken
  value in the starting-token argument of a subsequent command.
  Do not use the NextToken response element directly outside of the AWS CLI.



#--------------------------------------------------------------------------------
## AWS Glue
#--------------------------------------------------------------------------------
* Fully managed ETL service (extract, transform and load) that makes it simple
  and cost effective to categorize, clean, enrich and move your data between
  various data stores and data streams.
* It consist of a central metadata repo known as AWS Glue catalog that automatically
  generates Python or Scala code and a scheduler to handle dependency resolution,
  job monitoring and retries.
* AWS Glue is serverless, so no need to manage infrastructure.
* Designed to work with semi-structured data.

--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
## AWS Single Sign-on (SSO)
#--------------------------------------------------------------------------------
* Cloud-based SSO service that makes it easy to centrally manage SSO access to all
  your AWS accounts and cloud applications.
* Helps manage SSO access and user permissions across all your AWS accounts in
  AWS organization.


#--------------------------------------------------------------------------------
## Systems Manager parameter store
#--------------------------------------------------------------------------------
* AWS Systems manager is a service that you can use to view and control your
  infrastructure on AWS.
* It supports EC2 instances, edge devices and on-prem servers and VMs.

**Parameter store**
* Provides secure, hierarchical storage for configuration data and secrets mgmt.
* Can store data such as passwords, database strings, AMI IDs, license codes as
  parameter values.
* Parameter store is also integrated with Secrets manager.
* Consist of standard and advanced parameters.
* Standard parameters - no additional cost
* Advanced parameters - changed based on number of parameters and per API interaction.
                        (0.05 per parameter/month prorated hourly)

|----------------------------------------------------------| -------- | -------- |
| Description                                              | standard | Advanced |
| -------------------------------------------------------  | -------- | -------- |
| Total no of parameters allowed per aws account and region| 10,000   | 100,000  |
| Max size of a parameter value                            | 4kb      |   8kb    |
| Parameter policies                                       |    No    |   yes    |
| Cost                                                     | No cost  |   Yes    |
| -------------------------------------------------------- | -------- | -------- |



#--------------------------------------------------------------------------------
## AWS Key Management Service (KMS)
#--------------------------------------------------------------------------------
* Makes it easy to create and control the cryptographic keys used to protect your
  data.
* Deals with generation, exchange, storage, use and replacement of keys.
* Two services are offered: KMS and CloudHSM.
* You can use KMS directly in your application or through cloud services that are
  integrated with KMS.
* Enables you to control, who can use your keys and gain access to encrypted data.

**Symmetric and Asymmetric keys**
* When you create an AWS KMS key, by default you get a symmetric key.
* A symmetric KMS key represents a 256 bit encryption key that never leaves KMS
  unencrypted.
* The same key is used for encryption and decryption.
* Most times, you will use this key type.
* AWS services integrated with KMS use symmetric keys.
* You can also create multi-region KMS symmetric keys.

* An asymmetric KMS key represents a mathematically related public key and
  private key.
* Private key does not leave KMS unencrypted. To use private key you must call KMS.
* You can use the public key by calling KMS or you can download the public key.

## Customer managed keys:
* KMS uses a type of key called customer master key to encrypt/decrypt data.
* CMKs are the fundamental resource that KMS manages.
* They can be used inside KMS to encrypt/decrypt up to 4KB of data directly.
* They can also be used to encrypt generated data keys that are then used to
  encrypt/decrypt large amount of data outside of the service.
* CMKs can never leave KMS unencrypted, but data keys can.

## Data keys:
* Data keys are used to encrypt large data objects in your application (outside of
  KMS)
* GenerateDataKey API call - kms returns a plaintext version of the key and
  ciphertext that contains the key encrypted under the specified CMK.
* AWS tracks which CMK was used to encrypt the data key.
* You use the plaintext data key in your application to encrypt data, and you
  typically store the encrypted key alongside the encrypted data.
* Remove the plaintext key from memory as soon as possible.
* To decrypt data pass the encrypted data key to the decrypt function. AWS uses
  the CMK to decrypt and retrieve your plaintext data key. Use this plaintext key
  to decrypt your data and then remove the key from memory.


## Envelope Encryption:
* KMS uses envelope encryption to protect data.
* You can retrieve a plaintext data key only if you have the encrypted data key
  and have permissions to use the corresponding master key.
* Used for encrypting anything over 4KB.

Encryption:
(Customer master
    key)              (Envelope key)            (unencrypted data)
   |CMK|---------------> |Data key| -------------> |your data| ---> |encrpted data|
        Generate data                  Encrypts
             key

Decryption:                                        (Decrypted
 (Envelope key)                                     plaintext)
{ |Data key| + |Encrypted data|} -> |CMK| -------> |Data key| --------> |decrypted data|
                                          Decrypts          Decrypts your
                                          envelope key       data

* KMS does not store the data key, instead the encrypted copy of the data key
  is stored with the data.
* Once data is decrypted, plain text key is deleted from memory.

**Why use envelope encryption?**
* Network and performance:
 * When you encrypt data directly with KMS, it needs to be transferred over the
   network.
 * With envelope encryption only the data key goes over the network, not your data,
   avoiding transfer of large amounts of data to KMS.


## Encryption context:
* All KMS cryptographic operations accept an optional key/value map of additional
  contextual information called encryption context.
* Context must be the same for both encrypt and decrypt operations or decryption
  will fail.
* The encryption context is logged and can be used for auditing, and is available
  as context in AWS policy language for fine-grained policy based authentication.

## KMS operations:

* Creating a new KMS customer key:

```
aws kms create-key \
    --profile dev1 --region us-west-2 \
    --description "Customer test key"
KEYMETADATA 111111111111    arn:aws:kms:us-west-2:1111111:key/839-f1114-1411-02222228   122409.9    Customer test key   True    83118   CUSTOMER    Enabled ENCRYPT_DECRYPT AWS_KMS

```

* List key policies:

```
$ aws kms list-key-policies \
    --key-id 81xx9-15-41-111011 \
    --profile dev1 --region us-west-2
POLICYNAMES default

```


* Get Key policy:

```
$ aws kms get-key-policy \
    --key-id 811-15111a1-1111 \
    --policy-name default \
    --profile dev1 --region us-west-2
{
  "Version" : "2012-10-17",
  "Id" : "key-default-1",
  "Statement" : [ {
    "Sid" : "Enable IAM User Permissions",
    "Effect" : "Allow",
    "Principal" : {
      "AWS" : "arn:aws:iam::111111111111:root"
    },
    "Action" : "kms:*",
    "Resource" : "*"
  } ]
}

```

An alias makes it easy to identify the key.
* Create an alias.

```
$ aws kms create-alias \
    --alias-name alias/brdtestkey \
    --target-key-id 1x11-15-1-1-11  \
    --profile dev1 --region us-west-2

```


Now let's use are new key to encrypt and decrypt data. We will use the alias
created instead of the long convoluted key-id:

* Encrypt user data.
You can encrypt up to 4 kilobytes (4096 bytes) of arbitrary data such
as an RSA key, a database password, or other sensitive information.

The ciphertext that is returned by a successful  encrypt  command  is
base64-encoded text. You must decode this text before you can use
the AWS CLI to decrypt it.

```
$ aws kms encrypt \
    --key-id alias/brdtestkey \
    --plaintext fileb://testfile \
    --query CiphertextBlob \
    --profile dev1 --region us-west-2 \
    --output text | base64 --decode > encrypted_data

```

* Decrypt data.

```
$ aws kms decrypt \
    --ciphertext-blob fileb://encrypted_data \
    --output text \
    --query Plaintext \
    --profile dev1 --region us-west-2 | base64 --decode > decodedfile

$ cat decodedfile
THis is a test document
THis is a second line in the document.
{
 "Somesecret": "Blah"
}

```

## AWS CLoudHSM:
* Service providing secure cryptographic key storage by making hardware security
  modules (HSM) in the cloud.
* A HSM is a hardware appliance that provides secure key storage and cryptographic
  operations within a temper-resistant hardware module.

--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
## AWS Developer tools
#--------------------------------------------------------------------------------
AWS tools for CI/CD:

* **CodeCommit**   (Continous Integration)
  * Source control service enabling teams to collaborate on code.

* **CodeBuild**    (Continous Delivery)
 * Automated build service - compiles source code, run tests and proces packages
   that are ready to deploy

* **CodeDeploy**   (Continous Delivery)
  * Automates code deployments to any instance, include EC2, Lambda and on-prem.

* **CodePipeline** (Continous Deployment)
  * End-to-end solution to build, test and deploy your appln every time there is a
    code change

--------------------------------------------------------------------------------

## CodeCommit (Continous Integration)
* Source control service enabling teams to collaborate on code.
* Source code, binaries, images, libraries.
* Based on Git.
* You can configure notifications using SNS and CloudWatch, to send notifications to
  subscribers.

--------------------------------------------------------------------------------

## CodeBuild  (Continous delivery)
* Automated build service - compiles source code, runs tests and produces packages
  that are ready to deploy

--------------------------------------------------------------------------------

## CodeDeploy (Continous delivery)
* Automates code deployments to any instance, include EC2, lambda and on-premises.
* There are two deployment approaches: In-place deployment, Blue/Green deployment.

**In-place**
* The appln is stopped on each instance and the new release is installed.
* Also known as rolling update.
* Capacity is reduced during the deployment.
* Lambda is not supported
* There is no easy way to rollback to previous revision if there is an issue with
  the new version of software. Requires a re-deploy.
* Great when deploying first time.

**Blue-Green**
* New release is installed on new instances.
* Blue represents the active deployment, green is the new release.
* No capacity reduction.
* Green instances can be created ahead of time.
* Easy to switch between old and new.
* You pay for 2 environments until you terminate the old instances.

**AppSpec File**
* Configuration file that defines the parameters to be used during a CodeDeploy
  deployment.
* For EC2 and on-prem systems, YAML only.
* For Lambda based deployment - supports JSON and YAML.
* Should be saved to the root of your revision directory.

**File structure**
* Version: Currently the allowed value is 0.0
* OS: Operating system version
* Files: Location of appln files that need to be copied and where to copy.
* Hooks: Scripts which need to run at set points in deployment lifecycle.
         They have a very specific run order.
         order: BeforeInstall, AfterInstall, ApplicationStart, ValidateService

* Run order for In-Place Deployment:
 De-register phase (from the LB):
 * BeforeBlockTraffic
 * BlockTraffic
 * AfterBlockTraffic
 * ApplicationStop
 Application Install:
 * DownloadBundle
 * BeforeInstall
 * Install
 * AfterInstall
 * ApplicationStart
 * ValidateService
 Re-register with LB:
 * BeforeAllowTraffic
 * AllowTraffic
 * AfterAllowTraffic

--------------------------------------------------------------------------------

## CodePipeline (Continous deployment)
* End-to-end solution, build, test, and deploy your application every time there is
  a code change.
* Fully managed CI/CD service.
* The pipeline is triggered every time there is a code change.
* Integrates with: CodeCommit, CodeBuild, CodeDeploy, Github,Jenkins, EBS, CF,
  Lambda, ECS.


--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
## Elastic Container Service (ECS)
#--------------------------------------------------------------------------------
* Fully managed container orchestration service, which supports Docker and Windows
  containers.
* Two ways to run:
 * Cluster of Virtual machines:
   ECS will run your containers on clusters of virtual machines.
 * Fargate for Serverless:
   Use Fargate for Serverless containers and you don't need to worry about the
   underlying EC2 instances.

**ECR Elastic Container Registry**
* Registry of container services
* Services that use ECS: Sagemaker, Amazon Lex, Amazon.com

--------------------------------------------------------------------------------
### Cloud design patterns.
* [AWS Architecture Center](https://aws.amazon.com/architecture/compute-hpc/?docec2_rl1/index.html&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)
* [Cloud design patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/acl.html)

1. Anti-corruption layer pattern.
2. API routing patterns
    2.1 Hostname routing
    2.2 Path routing
    2.3 Header-based routing.
3. Circuit breaker pattern
4. Event sourcing pattern
5. Publish-subscribe pattern
6. Retry with backoff pattern
7. Saga pattern
8. Strangler fig pattern
9. Transactional outbox pattern



#--------------------------------------------------------------------------------
## Follow ups
#--------------------------------------------------------------------------------

* AWS Support plans: Basic, Developer, Business & Enterprise

* S3 URLS
* path style url: https://s3.Region.amazonaws.com/bucket-name/key
* virtual-host style url: https://bucket-name.s3.Region.amazonaws.com/key
* Path-Style URLs will be eventually deprecated in favor of virtual hosted-style URLs for S3 bucket access

* You can change the instance tenancy attribute of a VPC from dedicated to default.
  Modifying the instance tenancy of the VPC does not affect the tenancy of any
  existing instances in the VPC. The next time you launch an instance in the VPC,
  it has a tenancy of default, unless you specify otherwise during launch.

* Since Amazon ElastiCache for Memcached is multithreaded, it can make use of
  multiple processing cores. This means that you can handle more operations by
  scaling up compute capacity. Amazon ElastiCache for Redis doesn't support this feature.
* Amazon ElastiCache offers a fully managed Memcached and Redis service. Although
  the name only suggests caching functionality, the Redis service in particular can
  offer a number of operations such as Pub/Sub, Sorted Sets and an In-Memory Data
  Store. However, Amazon ElastiCache for Redis doesn't support multithreaded architectures.


* Which AWS service can meet this need by exporting data from DynamoDB and importing data into DynamoDB?
* Can you delete or change rules of default security group

* What you are currently testing is removing the ENI from the legacy instance and attaching it to the EC2 instance. You want to attempt a warm attach. What does this mean?

You are working as a Solutions Architect in a large healthcare organization. You have many Auto Scaling Groups that you need to create. One requirement is that you need to reuse some software licenses and therefore need to use dedicated hosts on EC2 instances in your Auto Scaling Groups. What step must you take to meet this requirement?

Use a launch template with your Auto Scaling Group.

Make sure your launch configurations are using Dedicated Hosts.

. You want to attempt a cold attach. What does this mean?
Attach ENI to an instance when it's running.
Attach ENI before the public IP address is assigned.
Attach ENI when it’s stopped.
Attach ENI when the instance is being launched.


. You have determined and will recommend that the best DR configuration to meet the cost and RT/RP Objectives will be to have a minimal version of the application always running in another Region. Which AWS disaster recovery plan will best meet these requirements?

Backup and restore
Pilot light
Multi-site
Warm standby

----
Additional services:
AWS Glue
AWS SSO
ECS, Fargate

--------------------------------------------------------------------------------
Your organization is developing a CI/CD environment to improve software delivery of
your applications. It has already adopted a plan to execute the various phases of
the CI/CD pipeline from continuous integration to continuous deployment. There are
now discussions around restructuring the team make-up to implement a CI/CD environment.
How would you recommend creating developer teams as a best practice to support this
change in the long run?

Ans: Set up an application team to develop applications. Set up an infrastructure
team to create and configure the infrastructure to run the applications. Set up a
tools team to build and manage the CI/CD pipeline.

https://d0.awsstatic.com/whitepapers/DevOps/practicing-continuous-integration-continuous-delivery-on-AWS.pdf

--------------------------------------------------------------------------------
You are developing an online auction application which uses SQS to exchange messages
between application components. Some of the messages are between 1GB and 2GB in size.
What is the AWS recommended way of managing large messages in SQS?

Ans: Use the Amazon SQS Extended Client Library for Java to manage SQS messages
     Store message in S3.

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.html

--------------------------------------------------------------------------------
You are developing a online-banking website which will be accessed by a global
customer base. You are planning to use CloudFront to ensure users experience good
performance regardless of their location. The Security Architect working on the
project asks you to ensure that all requests to CloudFront are encrypted using
HTTPS. How can you configure this?

ANS: Set the Viewer Protocol Policy to redirect HTTP to HTTPS
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

--------------------------------------------------------------------------------
Which of the following approaches can improve the performance of your Lambda function?

ANS: Only include the libraries you need to minimize the size of your deployment package
     Establish your database connections from within the Lambda execution environment to enable connection reuse

--------------------------------------------------------------------------------
You want users to receive an email notification whenever they push code to their
AWS CodeCommit repositories. How can you configure this?

ANS: Configure Notifications in the console, this will create a CloudWatch Events
rule to send a notification to an SNS topic which will trigger an email to be sent
to the user

SES is not  valid target for CloudWatch events.

--------------------------------------------------------------------------------
A developer is configuring CodeDeploy to deploy an application to an EC2 instance.
The application's source code is stored within AWS CodeCommit.

How do you need to set up and configure your IAM Policy to allow CodeDeploy to
perform the deployment to EC2?

ANS:
Create an IAM policy with an action to allow codecommit:GitPull on the required
repository. Attach the policy to the EC2 instance profile role.

CodeDeploy interacts with EC2 via the CodeDeploy Agent, which must be installed and
running on the EC2 instance. During a deployment, the CodeDeploy Agent running on
EC2 pulls the source code from CodeCommit. The EC2 instance accesses CodeCommit
using the permissions defined in its instance profile role; therefore, it is the
EC2 instance itself that needs CodeCommit access.

--------------------------------------------------------------------------------
Upon creating your code repository, you remember that you want to receive
recommendations on improving the quality of the Java code for all pull requests in
the repository. Which of the following services provide this ability?

ANS:
CodeGuru Reviewer for Java

--------------------------------------------------------------------------------
You need to find a source code repository that everyone can use, and that will allow
developers to continue to work on their code even when they are not connected to the
internet. Which of the following would you suggest to the team?

ANS:
Use CodeCommit to manage your source code.

--------------------------------------------------------------------------------
A content publishing organization runs its own platform, which uses DynamoDB as its
data store. A bug report has come in from the content team. They say that when two
editors are working on the same content they frequently overwrite each other's changes.

What DynamoDB feature would prevent the most number of overwrite bug reports?

ANS:
Include a condition-expression in the UpdateItem command.

--------------------------------------------------------------------------------

KMS
Step functions, Lambda
API GW, LAMBDA
Cognito.

























