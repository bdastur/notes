
 AWS Notes:

## Links:
* [AWS Learning Library](https://www.aws.training/LearningLibrary)
* [E2connect - a way of authenticating SSh sessions using IAM](https://github.com/glassechidna/ec2connect)
* [S3 Benchmark](https://github.com/dvassallo/s3-benchmark)
* [Open Guides AWS](https://github.com/open-guides/og-aws)
* [AWS Builder's library](https://aws.amazon.com/builders-library/?cards-body.sort-by=item.additionalFields.customSort&cards-body.sort-order=asc)
* [Tagging best practices](https://www.flexera.com/blog/cloud/2018/01/tagging-best-practices-for-cloud-governance-and-cost-management/)
* [AWS Cost Optimization Playbook](https://d1.awsstatic.com/pricing/AWS_CO_Playbook_Final.pdf)
* [Simple Storage calculator](https://www.duckbillgroup.com/aws-super-simple-storage-calculator/?storage=100&units=10&region=uswest2&submitButton=Compare+Storage+Costs)
* [Cost estimates for terraform](https://github.com/infracost/infracost)
* [Infracost - cost estimates for terraform](https://www.infracost.io/docs/)
* [AWS Fault injection](https://aws.amazon.com/fis/)
* [Cloudquery - Monitoring, governance & security](https://github.com/cloudquery/cloudquery)
* [EC2 Serial console - troubleshoot boot & n/w issues](https://aws.amazon.com/blogs/aws/troubleshoot-boot-and-networking-issues-with-new-ec2-serial-console/)
* [AWS Cost Explorer tips-1](https://aws.amazon.com/blogs/aws-cost-management/getting-started-with-aws-cost-explorer-part-1/)
* [AWS Cost Explorer tips-2](https://aws.amazon.com/blogs/aws-cost-management/tips-and-tricks-for-exploring-your-data-in-aws-cost-explorer-part-2/)
* [Amortize vs Blended vs Unblended costs](https://aws.amazon.com/blogs/aws-cost-management/understanding-your-aws-cost-datasets-a-cheat-sheet/)
* [Cost of cloud, a trillion dollar paradox](https://a16z.com/2021/05/27/cost-of-cloud-paradox-market-cap-cloud-lifecycle-scale-growth-repatriation-optimization/)
* [Open platform for building developer portals](https://backstage.io/)
* [S3 FAQs](https://aws.amazon.com/s3/faqs/)
* [Best practices for configuring n/w interfaces](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/best-practices-for-configuring-network-interfaces.html)
* [Collection of useful tools and scripts](https://github.com/dannysteenman/aws-toolbox)
* [Blog by Corey - Multicloud practice pitfalls](https://www.lastweekinaws.com/blog/multi-cloud-is-the-worst-practice/)
* [AWS Well architected labs](https://wellarchitectedlabs.com/operational-excellence/100_labs/100_inventory_patch_management/)
* [AWS Cost - trends dashboard with Athena](https://aws.amazon.com/blogs/aws-cost-management/trends-dashboard-with-aws-cost-and-usage-reports-amazon-athena-and-amazon-quicksight/)
* [Cost explore API example](https://medium.com/@devops_83824/report-your-aws-costs-programmatically-using-the-cost-explorer-api-aa8dc0f9d8f1)
* [SAAS Cost tools problems - comentary by Corey Quinn](https://www.lastweekinaws.com/blog/saas-cost-tools-suck/)

**Benchmarking**:
* [Tool for benchmarking EC2/S3 throughput](https://github.com/dvassallo/s3-benchmark)
* [EC2 instance connect](https://github.com/glassechidna/ec2connect)
* [EC2 instance connect - AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html)


## Identity and Authorization (IAM):

* [AWS Reinvent: Become an IAM Policy Master](https://www.youtube.com/watch?v=YQsK4MtsELU)
* [AWS Reinvent: Getting started with AWS identity](https://www.youtube.com/watch?v=Zvz-qYYhvMk)
* [Okta AWS CLI Tool](https://github.com/jmhale/okta-awscli)

### How to generate IAM credentials report.
```
#!/bin/bash
aws iam generate-credential-report  --profile core-services-prod
aws iam get-credential-report \
    --query Content --output text \
    --profile core-services-dev | base64 -D

```

### Links:

* https://aws.amazon.com/blogs/security/new-attach-an-aws-iam-role-to-an-existing-amazon-ec2-instance-by-using-the-aws-cli/?sc_channel=sm&sc_campaign=rolesforrunninginstances&sc_publisher=tw&sc_medium=social&sc_content=read-post&sc_country=global&sc_geo=global&sc_category=ec2&sc_outcome=launch

* https://github.com/duo-labs/cloudtracker

* [Manage AWS IAM Roles with Tags](https://aws.amazon.com/blogs/security/add-tags-to-manage-your-aws-iam-users-and-roles/)

* [Block S3 Public Access](https://aws.amazon.com/blogs/aws/amazon-s3-block-public-access-another-layer-of-protection-for-your-accounts-and-buckets/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+AmazonWebServicesBlog+%28Amazon+Web+Services+Blog%29)



## EC2:
* Default maximum EC2 instance limit per region is 20.
* Within each family of instance type, there are several choices that scale
  up linearly in size. The hourly price for each size scales linearly as well.

### Useful links

[Automated Draining of spot instance nodes](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-supports-automated-draining-for-spot-instance-nodes-on-kubernetes/)

### Instance types

**General Purpose:**
T2:
* Burstable performance instances.
* Provide a baseline level of CPU performance with ability to burst above
  the baseline.
* The baseline performance and ability to burst are governed by CPU credits.
* Lowest cost general purpose instance types.
Uses:
* Webservers, developer environments and databases.

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/t2-instances.html#t2-instances-cpu-credits

M4:
* Latest generation of general purpose instances
* Support for enhanced networking
* EBS optimized by default at no additional cost.
* Balance of compute, memory and network resources.

M3:
* SSD based instance storage for fast I/O performance.
* Balance of compute, memory and network resources

Uses:
* Small and midsize databases, data processing

**Compute Optimized:**
C4:
* Features highest performing processors and lowest price/compute performance
  in EC2.
* EBS optimized by default
C3:
* Support for enhanced networking
* Support for clustering
* SSD backed

**Memory Optimized:**
X1:
* Memory optimized and have lowest price per GiB of RAM in EC2 types.
* Upto 1953 GiB of DDR based instance memory.
* SSD Storage
* EBS optimized
* Ability to control processor C-state and P-state configuration.

R4:
* Enhanced networking
* DDR4 memory

R3:
* SSD Storage
* High frequency intel Xeon Ivy bridge processors
* Enhanced networking

**Accelerated Computing:**
P2:
* General purpose GPU compute

G2:
F1:


**Storage Optimized:**
I3:
* High I/o instances
* NVMe SSD Storage

D2:
* HDD Storage
* High disk throughput.

**Enhanced Networking:**
* Many instances support enhanced networking. Enhanced networking reduces
  impact of virtualization on network performance by enabling a capability called
  SR-IOV (Single Root I/O Virtualization). The result is more PPS, lower
  latency and less jitter.
* Enhanced networking is available only for instances launched in Amazon VPC.


* When the host on which an EC2 instance restarts, the instance will stay
  with the same EC2 host. But if the instance is stopped and then restarted
  or if AWS stops the instance for maintenance etc on their end, then the
  instance will be reassigned to another host in the same AZ.

### AMIs
* AMIs define the initial software that will be on an instance when launched.
* OS, Initial state of any patches, application or system software.

There are 4 sources:
* Published by AWS
* AWS Marketplace
* Generated from existing instances
* Uploaded virtual servers

* When launching windows instance, EC2 generates a random password for the
  local admin account and encrypts the password using a public key. initial
  access is obtained by decrypting the password with the private key, either
  in the console or using API.
  The decrypted password can be used to login into the instance with local
  admin account via RDP.

### Security Groups:
* Virtual firewall
* Security groups have different capabilities depending on whether they are
  associated with a VPC or EC2 classic.
EC2 classic SG -- Control outgoing instance traffic
VPC SG         -- Control outgoing and incoming instance traffic.

* SG is stateful firewall; that is an outgoing message is remembered so that
  the response is allowed through the SG without an explicit inbound rule
  being required.
* Changes to SG are immediate.
* Everything is denied by default. You can add a SG Rule to allow traffic,
  you cannot add a rule to deny traffic.

* You can only export previously imported EC2 instances. Instances launched
  within AWS from AMIs cannot be exported.

* Instance metadata: http://169.254.169.254/latest/meta-data/

**Termination Protection**
* Prevents from accidental Termination from console, CLI or API.
* It does not prevent termination triggered by an OS shutdown command,
  termination from an ASG, or termination of a spot instance due to spot price
  changes.

### Pricing Options:
**On-Demand Instances:**
* The price per hour for each instance type published on AWS website represents
  the price for on-demand instances.
* This is the most flexible pricing option. No upfront commitment required,
  and customer has control over when instance is launched and terminated.
* It is the least cost effective of the three pricing options per compute hour.

**Reserved Instances:**
* Enables to make capacity reservations for predictable workloads.
* Can save upto 75% on the on-demand hourly rate.
* When reserving customers specify the instance type and availability zone for
  the instance.
* Capacity in AWS DC is reserved for the customer.
* Payment Options
  * All upfront
  * Partial upfront
  * No upfront

**Modifying your reserved instances:**
* Modification does not change the remaining term of your reserved instances.
  Their end dates remain the same. There is no fee and you do not receive
  a new bill or invoice.
* Modification is different from purchase.
* What can you modify?
  * Switch AZz within the same region.
  * Change between EC2 VPC and EC2 classic.
  * Change instance type within the same instance family (Linux only)

* ASG can take advantage of reserved instance pricing. Reserved instances,
  are billing construct. RI gets applied to any running instance that fits
  the parameters of the RI. In other words it really isn't associated to just
  one instance.
* If you have an ASG which launches instances in an AZ where you purchased RI,
  it will take advantage of that.

**Spot Instances:**
* Can be used for workloads that are not time critical and tolerant to
  interruption.
* Offers greatest discount.
* Specify the price you are willing to pay for a certain instance type. When
  the bid price is above the current spot price, the customer will receive the
  requested instances.
* These instances operate like all other instances, and customers pay the spot
  price for the hours that the instances run.
* The instances run until:
  * The customer terminates them
  * The spot price goes above the customers bid price.
  * There is not enough unused capacity to meet the demand of the spot instances.
* If AWS needs to terminate the spot instance, the instance will receive a
  termination notice providing 2 minute warning prior to terminating the
  instance.
* If AWS terminates the instance, you get the hour it was terminated in for
  free.
* If you terminate your spot instance, you pay for the hour.

[spot instance advisor](https://aws.amazon.com/ec2/spot/instance-advisor/)
[spot instance pricing](https://aws.amazon.com/ec2/spot/pricing/#Spot_Instance_Prices)
[spot fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html)
[New spot pricing](https://aws.amazon.com/blogs/compute/new-amazon-ec2-spot-pricing/)


### Tenancy Options:

**Shared Tenancy:**
* Default tenancy model for all EC2 instances regardless of instance type or
  pricing.
* Single host machine may host instances for different customers.
* AWS does not use over provisioning. Fully isolates instances from other
  instances on the same host.

**Dedicated Instances:**
* Run on hardware that is dedicated to a single customer.
* Other instances in the account will run on shared tenancy and will be
  isolated at hardware level from dedicated instances in the account.


**Dedicated host:**
* A physical server with EC2 instance capacity fully dedicated to a customer.
* Customer has control over which specific host runs an instance at launch.

**Placement groups:**
* A logical grouping of instances within a single AZ.
* Recommended for applications that benefit from low network latency, high
  network throughput or both.

### Instance Stores:
* Provides temporary block-level storage for your instance.
* Located on disks that are physically attached to the host computer.
* The size of an instance store as well as the number of devices available
  varies by instance type.
* Data in an instance store persists only during the lifetime of it's
  associated instance.
* If the instance reboots (intentionally or unintentionally), data in the
  instance store persists.
* Data in the instance store is lost when:
  * The underlying disk drive fails.
  * The instance is stopped.
  * The instance terminates.
* When you stop or terminate an instance, every block of storage in the
  instance store is reset. Therefore data cannot be accessed through the
  instance store of another instance.
* If you create an AMI from the instance, the data on it's instance store
  volumes isn't preserved and isn't present on the instance store volumes of
  the instances that you launched from the AMI.
* You cannot create a snapshot of an instance store like you can for an EBS
  volume.

### EBS:
* Provide persistent block-level storage volumes for use with EC2 instances.
* EBS volume is automatically replicated within it's AZ to provide HA and
  durability.

**Types of EBS Volumes:**

**General purpose SSD (gp2):**
* Strong performance at a moderate price.
* Ranges from 1GB to 16TB and provides baseline performance of 3 IOPS per
  gigabyte provisioned.
* Caping at 16,000 IOPS.
  EG: for a 1 TB volume, you can expect a baseline performance of 3000 IOPS
* Under 1TB, it has ability to burst upto 3000 IOPS for extended periods of
  time.
* When not using IOPS are accumulated as I/O credits, which get used during
  heavy traffic.
* Use cases:
  * System boot volumes
  * Small to medium sized DB.
  * Development and test environments.

**Provisioned IOPS SSD (io1):**
* Designed to meet needs of I/O intensive workloads.
* Range from 4GB to 16TB.
* When provisioning specify the size and desired IOPS, up to the lower of
  maximum of 30 times the number of GB of volume or 64,000 IOPS.
* EBS delivers within 10% of the provisioned IOPS 99.9 % of the time over a
  given year.
* Price is on provisioned size. Additional monthly fee is based on provisioned
  IOPS (whether consumed or not).
* Use cases:
  * Critical business apps requiring sustained IOPS performance.
  * Large DB workloads.

**EBS Magnetic volumes (standard):**
* Lowest performance characteristics and lowest cost per gigabyte.
* Great cost effective solution for appropriate workloads.
* Can range from 1 GB to 1 TB and avg 100 IOPS, with ability to burst to
  hundreds of IOPS.
Use cases:
  * infrequently accessed data
  * Sequential reads.
  * Situation where low-cost storage is requirement.
* Billed based on provisioned space, regardless of how much data is actually
  stored on the volume.


**Throughput optimized HDD (ST1):**
* Sequential writes.
* frequently accessed workloads.
* Usually used for data warehouse apps.


**Cold HDD (SC1):**
* Less frequently accessed data
* Usually used for file servers.

* Note that ST1 and SC1 cannot be used as Root volumes.
* HDD, magnetic - standard can be used as Root volume.
* Termination protection is turned off by default, you must turn it on.
* Default action for the root EBS volume is to be deleted when the instance
  is terminated.

**Protecting data:**
**Snapshots:**
* Snapshots are incremental backups, meaning only the blocks on the device that
  have changed since your most recent snapshot are saved.
* Snapshots are saved in S3.
* The action for taking a snapshot is free. You pay for the storage cost.
* Snapshots are constrained to the region in which they are created. meaning
  you can use them to create new volumes only in the same region.
* If you need to restore a snapshot in a different region, you can copy a
  snapshot to another region.
* To use a snapshot you create a new EBS volume from the snapshot. The volume
  is created immediately, but data is loaded lazily.
* Means the volume can be accessed upon creation, and if data being requested
 is not yet restored, it will be upon first request.
* Snapshots can be used to increase the size of an EBS volume.
* Snapshots of encrypted volumes are encrypted automatically.
* Volumes restored from encrypted snapshots are encrypted automatically.
* You can share snapshots, but only if they are unencrypted.
* To create a snapshot for EBS volumes that serve as root devices, you should
  stop the instance before taking the snapshot.

**Encryption:**
* EBS volumes can be encrypted. Uses AWS Key management service to handle
  key management.
* A new master key is created unless you select a master key.
* Data and keys are encrypted using AES-256 algorithm.
* Encryption happens on the servers that host the EC2 instance, so the data
  is actually encrypted in transit between the host and the storage media
  and also on the media.
* Encryption is transparent, and you can expect same IOPS performance with
  minimal effect on latency.
* Snapshots from encrypted volumes are automatically encrypted, as are the
  volumes created from encrypted snapshots.
* EBS Root volumes of your default AMIs cannot be encrypted.
* You can use 3rd party tools to encrypt the root volume, or it can be Done
  when creating AMIs in the AWS console or using API.
* You are not tied to the type of volume with snapshot. Meaning - you could
  have a snapshot of a volume of type magnetic disk, and you can created
  a new volume from this snapshot with a different volume type like SSD.


### Extending an EBS Volume:

**Links:**
http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-volume.html#recognize-expanded-volume-linux

How to modify the size, IOPS or Type of an AWS EBS Volume?

* From the Console, select EC2 -> volumes.
* Select the volume by VolumeId, and choose Actions -> modify volume
* Modifying a volume size has no effect until you also extend the volume's
  file system to make use of the new storage capacity.

After increasing the volume size, log into the Instance:
```
# df -h
Filesystem         Size  Used Avail Use% Mounted on
/dev/xvda1          40G  8.6G   30G  23% /
devtmpfs            32G     0   32G   0% /dev
tmpfs               32G     0   32G   0% /dev/shm
tmpfs               32G  121M   32G   1% /run
tmpfs               32G     0   32G   0% /sys/fs/cgroup
none                64K  4.0K   60K   7% /.subd/tmp
/dev/mapper/vol5   2.0T  935G  945G  50% /data/vol5
/dev/mapper/vol6   985G  788G  147G  85% /data/vol6
:
/dev/mapper/vol7   985G   77M  935G   1% /data/vol7
/dev/mapper/vol2   985G  695G  241G  75% /data/vol2
tmpfs              6.3G     0  6.3G   0% /run/user/0
tmpfs              6.3G     0  6.3G   0% /run/user/10038
tmpfs              6.3G     0  6.3G   0% /run/user/10807

(Volume size of /dev/mapper/vol5 is increased to 2.0 TB)


rahul_reddy]# lsblk
NAME    MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
xvda    202:0    0   40G  0 disk
└─xvda1 202:1    0   40G  0 part  /
xvdb    202:16   0 1000G  0 disk
└─vol1  253:3    0 1000G  0 crypt /data/vol1
xvdc    202:32   0 1000G  0 disk
└─vol2  253:9    0 1000G  0 crypt /data/vol2
xvdd    202:48   0 1000G  0 disk
└─vol3  253:2    0 1000G  0 crypt /data/vol3
xvde    202:64   0 1000G  0 disk
└─vol4  253:5    0 1000G  0 crypt /data/vol4
xvdf    202:80   0    2T  0 disk
└─vol5  253:4    0    2T  0 crypt /data/vol5
:
xvdk    202:160  0 1000G  0 disk
└─vol10 253:0    0 1000G  0 crypt /data/vol10

(this operation worked as the volume is encrypted)
# cryptsetup resize vol5 -v  resize2fs /dev/mapper/vol5

```


### Lifecycle of instances



## Elastic File System (EFS:)
* Supports NFS V4 protocol.
* You only pay for the storage you use.
* You can scale up to petabytes.
* Can support thousand of concurrent NFS connections.
* Data is stored across multiple AZs within a region.
* Read after write consistency
* Great use case for a file server.

## Amazon FSx for Luster:
* Designed for fast processing of workloads like ML, HPC, video processing,
  financial modeling and electronic design automation (EDA).
* Lets you launch and run a file system that provides sub-milliseconnd access
  to your data.
* Allows read/write speeds of up to hunderes of gigabytes/second and millions
  of IOPS.



## Elastic Load balancer (ELB:)
* ELB service allows you to distribute traffic across a group of EC2 instances
  in one or more availability zones within a region.

* Internet facing ELB: A load balancer that takes requests from clients over
  the internet and distributes them to EC2 instances that register with the ELB.
* It receives a public DNS name that clients can use to send requests to your
  application.

* ELB in VPCs support IPV4 addresses only. In EC2 classic it supports IPV4 and
  IPV6.
* Internal ELB: as name suggest is not exposed to the web.

**HTTPS load balancers:**
* Uses SSL/TLS protocol for encrypted connections. Enables encryption between
  client and the ELB.
* Must install a SSL cert on the ELB.
* ELB does not support Server Name Indication (SNI). This means if you want to
  host multiple websites on a fleet of EC2 instances behind ELB with a single
  SSL, you will need to add Subject Alternative Name for each website to the
  cert to avoid site users seeing a warning message when the site is accessed.

* Listener is a process that checks for connection requests.
* Listener is configured with a protocol and a port for the front end and
  back end connection.
* Protocols: HTTP, HTTPS, SSL, TCP.
* Protocols operate at L4 and L7.

### Idle connection timeout:
* For each request a client makes, the ELB maintains 2 connections.
* For each connection the ELB manages the idle timeout that is triggered
  when no data is sent over the connection for the specified time period.
* After the timeout period, the ELB closes the connection.
* Default idle timeout is 60 seconds for both connections.
* If using HTTP or HTTPS, recommendation is to use the keep-alive option for
  EC2 instances.
* You can enable keepalive in the web server settings or kernel settings of
  EC2 instance.
* To ensure that ELB is responsible for closing the connections to the
  instances, make sure that the keep alive time is greater than the idle
  timeout setting on the ELB.

* Cross zone load balancing: ensures that request traffic is routed evenly
  across all back end instances regardless of AZ.

* [AWS NLBs and mixed up TCP connections](https://www.niels-ole.com/cloud/aws/linux/2020/10/18/nlb-resets.html)


### Connection Draining for classic ELB:
* To ensure that the ELB stops sending requests to instances that are
  de-registering or unhealthy, while keeping existing connections open, use connection draining. This enables the ELB to complete in-flight requests
  made to instances that are de-registering or unhealthy.
* Max timeout value between 1 and 3600 seconds. Default is 300 seconds. after
  that ELB forcibly closes the connections to de-register instances.
* When connection draining is disabled any in-flight requests made to instances
  that are de-registering or unhealthy are not completed.

### Proxy Protocol:
* It is an internet protocol used to carry connection information from the
  source requesting the connection to the destination for which the connection
  was requested.
* ELB uses proxy protocol V1 which is human readable.
* Ensure that the ELB is not sitting behind a proxy server with proxy protocol
  enabled, otherwise there will be a duplicate header.

### Sticky sessions:
* Enables ELB to bind a user's session to a specific instance. This Ensures
  that requests from the user during the session are sent to the same instance.
* Key to managing sticky sessions is to determine how long your ELB should
  consistently route the users request to the same instance.
* If your app has a session cookie configure ELB so that the session cookie
  follows the duration specified by the application's session cookie.
* You can configure ELB to create a session cookie by specifying your own
  stickiness duration. ELB creates a cookie named AWSELB that is used to map
  the session to the instance.

* Health checks: to test the status of the EC2 Instances
* An ELB health check may be a ping, a connection attempt or a page that is
  checked.

* Either InService or OutOfService.


## Autoscaling (ASG:)
* Allows automatic scaling of EC2 instances based on criteria. Scaling in or
  scaling out.
**Links:**
Controlling which ASG Instances terminate during scale in:
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html


### Autoscaling plans:
**Maintain current levels:**
* Maintain a minimum or specified number of running instances at all times.
* When ASG finds an unhealthy instance it terminates it and launches a new one.

**Manual scaling:**
* Most basic way to scale your resources.
* Specify the change in max, min or desired capacity of your ASG group.
* ASG maintains the process of creating or terminating instances to maintain
  the updated capacity.

**Scheduled scaling:**
* Scaling actions are performed automatically as a function of time and date.

**Dynamic scaling or scaling on demand:**
* Create a scaling policy based on criteria like n/w bandwidth or CPU
  measured by cloudwatch and measure a threshold.

**Use predictive scaling**
* Predcting based on previous EC2 usage, with decision based on billions of
  data points drawn from observations.


### ASG Components:

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


### ASG Limits:
* Default Launch configurations per region: 100
* Default ASG groups per region: 20
* Default scaling policies per ASG: 50
* Default scheduled actions per autoscaling group: 125
* Default lifecycle hooks per ASG group: 10
* Default SNS topics per ASG group: 10
* Default Classic ELB per ASG: 50




## Virtual Private Cloud (VPC:):

**Links**
* [VPC Introduction](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html)
* [VPC Documentation](https://docs.aws.amazon.com/vpc/index.html)
* [VPC Invalid peering configs](https://docs.aws.amazon.com/vpc/latest/peering/invalid-peering-configurations.html#transitive-peering)
* [CIDR Range visualizer](https://cidr.xyz/)

* VPCs do not span regions, they can span availability zones.
* VPC lets you provision a logically isolated section of AWS cloud where you
  can launch AWS resources in a virtual network that you define.

* RFC 1918 defines 3 private address ranges
10.0.0.0 - 10.255.255.255 (10/8 prefix)
172.16.0.0  - 172.31.255.255 (172.16/12 prefix)
192.168.0.0 - 192.168.255.255 (192.168./16 prefix)

* VPC CIDR block may be as large as /16 (65536 ip addresses) or as
  small as /28 (16 ip addresses)
* Default limit for Amazon VPCs in a region is 5.
* Each subnet is mapped to a specific availability zone.
* Security groups and Network ACLs can span multiple availability zones.
* Can only have one internet gateway in a VPC.
* Network ACLs are stateless.
* When you create a VPC all subnets can communicate with each other by default.
* The first 4 ip addresses and the last ip address in each subnet CIDR block are not available
  for you to use.
  10.0.0.0 - network address
  10.0.0.1 - reserved by AWS for the VPC router.
  10.0.0.2 - Reserved by AWS for DNS
  10.0.0.3 - reserved by AWS for future use.
  10.0.0.255 - Network broadcast address. We do not support broadcast in VPC, therefore we reserve this address.


* VPC has the following components:
  * subnets
  * Route tables
  * DHCP option sets
  * Security groups
  * Network ACLs
  And the following optional components:
  * IGW
  * EIP addresses
  * ENI (Elastic network interfaces)
  * Endpoints
  * Peering
  * NAT instances and NAT gateways
  * VPG, customer gateways and VPNs.

* IPsec is the security protocol supported by VPC.

### Subnets:
* 1 Subnet == 1 AZ. 1 AZ however can have multiple subnets.
* Subnets can be private, public or VPN only
* A public subnet is one in which the associated route table directs the
  subnets's traffic to VPC's IGW.
* A private subnet is one in which the route table does not direct the
  subnet's traffic to VPC's IGW.
* A VPN-only subnet is one in which the route table directs the subnet traffic
  to Amazon VPC's VPG and does not have a route to IGW.
* Regardless of the type of subnet, the internal IP address range of the
  subnet is always private.
* The minimum size subnet you can have in a VPC is /28
* The maximum size subnet you can have in a VPC is /16
* AWS reserves 5 IP addresses within a subnet for it's own purposes.
  (First 4 and last 1 ip address)

### Route Tables:
* A logical construct that contains a set of rules/routes that are applied
  to the subnet to determine where n/w traffic is directed.
* You can use route tables to specify which subnets are public and which
  are private.
* Each route table contains a default route, called the local route which
  enables communication within the VPC. This route cannot be modified or removed.
* VPC has an implicit router.
* VPC comes with a main route table that you can modify.
* You can create additional custom route tables for your VPC.
* Each subnet must be associated with a route table.
* If you do not associate a route table, the subnet uses the main route table.
* You can replace main route table with a custom table, so that each new
  subnet is automatically associated with it.
* Each route in the route table specifies a destination CIDR and a target;
  eg: traffic destined for 172.16.0.0/12 is targeted for the VPG.
* AWS uses the most specific route that matches the traffic to determine
  how to route the traffic.

### Internet Gateways (IGW:)
* A component that allows communication between instances in the VPC and
  the internet. IGW translates the reply address to the instances public ip
  address and maintains a 1-to-1 map of the instance private ip addr and public
  ip addr.
* When IGW receives traffic from internet it translates dest addr (public ip)
  to instances private ip addr.
* You must do the following to create a public subnet with internet access:
  * Attach an IGW to amazon VPC.
  * Create a subnet route table rule to send all non-local traffic (0.0.0.0/0)
    to the IGW
  * Configure your network ACLs and security groups to allow relevant traffic
    to flow to and from your instance.

### DHCP option sets:
* AWS automatically creates and associates a DHCP option set for your VPC
  and sets two options: domain name servers and domain name.
* DHCP option sets allow you to direct EC2 host name assignments to your own
  resources.
* To assign your own domain name to your instances, create a custom DHCP
  option set and assign it to your VPC.
* Can configure the following values:
  - domain name servers - IP addr of up to 4 domain name servers.
  - domain name - desired domain name
  - ntp-servers - The ip address of up to 4 ntp servers.
  - netbios-name-servers - ip addr of up to 4 NetBIOS name servers.
  - netbios-node-type - set this value to 2.


### Elastic IP Addresses (EIP:)
* AWS maintains a pool of public ip addresses in each region.
* EIP allow you to maintain a set of IP addresses that remain fixed while the
  underlying infrastructure may change over time.
* You must first allocate an EIP for use within the VPC and then assign it to
  an instance.
* EIPs are specific to a region.
* There is a one-to-one relationship between network interfaces and EIPs.
* You can move EIPs from one instance to another, either in same or different
  VPC, but within the same region.
* EIPs remain associated with your AWS account until you release them.
* There is a charge for an EIP that is allocated to your account and if it
  is not associated with a resource.
* In Classic VPC if you stop and instance, its EIP is disassociated. But in a
 VPC if you stop and instance, it's EIP remains associated.

### Elastic Network interfaces (ENI:)
* An ENI is a virtual n/w interface that you can attach to an instance in a VPC.
* ENIs are only available within a VPC and are associated with a subnet
  upon creation.
* They can have 1 public ip address and multiple private ip address. One of
  them is primary.
* Allow you to create dual-homed instances with workloads on distinct subnets.

### VPC Endpoints:
* Enables you to create a private connection between your VPC and another AWS service
  without requiring access over the internet, or a NAT interface, VPN connection or AWS direct connect.
* VPC endpoint currently supports S3 and dynamodb.
* Does not require an IGW, Nat device, VPN connection or AWS direct connect connections.
* Instances in your VPC do not require public IP addresses to communicate with resources in
  the service.

* You can use the describe-prefix-lists to list the CIDRs for your
  endpoints in the vpc. This can be useful when opening specific CIDRs for
  outbound access from your EC2 instances.

```
$ aws ec2 describe-prefix-lists --profile devaccount
PREFIXLISTS	pl-6333400a	com.amazonaws.us-east-1.s3
CIDRS	53.251.0.0/17
CIDRS	51.116.0.0/15
PREFIXLISTS	pl-04442c6b	com.amazonaws.us-east-1.dynamodb
CIDRS	51.44.0.0/22
CIDRS	54.159.224.0/21
```

### Global Accelerator:
* It is a service in which you create accelerators to improve availability and
  performance of your applications for local and global users.
* You are assigned two static IP addresses (or you can bring your own)
* You can control traffic using traffic dials. This is done within the endpoint group.



### Default VPC:
* AWS provides a default VPC in each region.
* All subnets in default VPC have a route out to the internet
* Each EC2 instance that is deployed in the default VPC has a private and public
  ip address.
* If you delete the default VPC, only way to restore it is to contact AWS support.

### VPC Peering:
* Peering connection is a n/w connection between two VPCs that Enables
  communication between instances in those VPCs.
* Instances behave as if they were on the same private network.
* You can create a peering connection between VPCs in same account or a VPC
  in another AWS account, within a single region.
* A peering connection is neither a gateway nor a VPN connection and does not
  introduce a SPF for communication.

* Peering connections are created through request/accept protocol.
  * The owner of the requesting VPC sends a request to peer, to the owner of
    the peer VPC.
  * If the peer is in the same account it is identified by VPC id. If peer is
    in a different account it is identified by Account id and VPC id.
  * The owner of the peer VPC has 1 week to accept or reject the request
    else the request expires.
* You cannot create a peering connection between VPCs that have matching or
  overlapping CIDR blcoks.
* You cannot create peering connections between VPCs in different regions.
* Does not support transitive peering.
* You cannot have more than one peering connection between same two VPCs at
  the same time.

### AWS PrivateLink:

* AWS Privatelink enables cutomers to access services hosted on AWS securely
  by keeping all the n/w traffic within the AWS network.
* You can use this capability to privately access services supported by AWS
  privatelink from your VPC, without using public IPs, on Amazon n/w.
* When you create endpoints for services that are available on AWS privatelink,
  these service endpoints will appear as ENIs with private IPs in your vpc.
* PrivateLink also offers AWS partners, ability to offer services that look and
  feel like services that are hosted directly on a customer's private network.







### Security groups:
* A virtual firewall that controls inbound and outbound traffic to AWS
  resources and EC2 instances.
* All EC2 instances must be launched into a SG.
* If a SG is not specified at launch, then the instance will be launched in
  the default SG.
* A default SG :
  * allows all outbound traffic,
  * allows communication within the SG
  * Denies all inbound traffic.
* You can create up to 500 security groups for each VPC.
* You can add 50 inbound and 50 outbound rules to each SG.
* You can specify allow rules but not deny rules in a SG.
* Have separate rules for inbound and outbound traffic.
* By default all outbound traffic is allowed.
* SGs are stateful. This means the responses to allowed inbound traffic are
  allowed to flow outbound regardless of the outbound rules.
* You can change the SG which is associated to an instance, and changes will
  take effect immediately.


### Network ACLs:
* Your VPC automatically comes with a default network ACL and by default it allows
  all outbound and inbound traffic.
* Operates at subnet level (second level of defense)
* Supports allow and deny rules.
* Stateless: Return traffic must be explicitly allowed by rules.
* Processes rules in numbered order when deciding whether to allow traffic,
  starting with the lowest numbered rule.
* Automatically applied to all instances in the associated subnets.
* When you create a custom network ACL, it's initial configuration will deny
  all inbound and outbound traffic, until you create rules to allow otherwise.
* Each subnet in your VPC must be associated with a network ACL. If you do not
  explicitly associate a subnet with a network ACL, the subnet is automatically
  associated with the default network ACL.
* You can associate a network ACL with multiple subnets, however a subnet can
  be associated to only one network ACL at a time.


**Ephemeral Ports**
* To cover the different types of clients that might initiate traffic to
public facing instances in your VPC, you can open ephemeral ports
1025-65535. However you can also add rules to your ACL to deny traffic on
any malicious ports within that range.
* Remember to place DENY rules earlier in table than ALLOW rules that open
the wide range of ephemeral ports.


### NAT Instance and NAT Gateway:
* NAT instances and gateways allow instances deployed in private subnets to
  gain internet access.

**NAT Instances**
* When creating a NAT instance, disable source/destination check on the instance
* Always deploy NAT Gateway in the public subnet.
* Deploy NAT instance in the public subnet.
* Must have an Elastic IP address associated to work.
* NAT gateways must be behind a security group.
* There must be a route from the private subnet to the NAT instance in order
  for this to work.
* The amount of traffic that a NAT instance supports depends on the instance size.

**NAT Gateways**
* Scales automatically upto 10 Gbps.
* AWS manages the NAT gateways.
* Not associated with security groups
* Automatically assigned a public ip address.
* Remember to update your route table to point to the NAT gateway for traffic
  from private subnet to flow out the NAT gateway.

### Virtual private gateways (VPG:), Customer gateways and VPNs:
* Allows you to connect existing datacenter to amazon VPC using either h/w
  or s/w VPN connections.
* A VGP: is a virtual private network connector on the AWS side of the VPN
  connection.
* A customer GW (CGW) represents the physical device or software application
  on the customers side of the VPN connection.
* After these two are created the last step is to create a VPN tunnel.
* A VPN tunnel is established after traffic is generated from the customers
  side of the VPN connection.
* You must specify the type of routing for the tunnel - dynamic (BGP) or static.
* VPG is the AWS end of the VPN tunnel.


### VPC Flowlogs:
* VPC FLow logs enables you to capture information about the IP traffic going to
  and from network interfaces in your VPC.
* Flow log data is stored in Amazon cloudwatch logs.
* You cannot enable flow logs for VPCs that are peered with your VPC unless the peer
  VPC is in your account.
* You can tag flow llogs.
* After you have created a flow log you cannot change it's configuration.


## ENI vs ENA vs EFA


## Route53:
* Route53 is an authoritative DNS system. An authoritative DNS system provides
  and update mechanism that developers use to manage their public DNS names.
  It then answers DNS queries, translating domain names into IP addresses so
  that computers can communicate to each other.

### DNS Concepts:

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

### Record Types:
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

### Route53 three main functions:

#### **Domain registration:**
* Amazon route53 lets you register domain names, such as example.com.
* You also have an option to transfer an already registered domain name with
  another registrar to route53.
* Supports domain registration for a wide variety of generic TLDs and
  geographic TLDs.
* There is a limit of 20 domain names for new customers as of March 2021.
* If you have an existing account and your default limit is 50 now, it will remain at 50. Reference: Amazon Route 53 Quotas.

#### **DNS Service:**
* Route53 is an authoritative DNS service.
* When someone enters your domain name in a browser or sends you an email,
  a DNS request is forwarded to the nearest Route53 DNS server in a global
  network of authoritative DNS servers. Route53 responds with the IP address
  that you specified.
* If you registered your domain with another domain registrar, that registrar
  is probably providing DNS service for your domain. You can transfer DNS
  service to Route53 without having to transfer the registration for the domain.

##### **Hosted Zones:**
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


##### **Supported Record Types**
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

* Alias Records have special functions that are not present in other DNS servers.
* Their main function is to provide special functionality and integration into AWS services.
* Unlike CNAME records, they can also be used at the Zone Apex, where CNAME records cannot.
* Alias Records can also point to AWS Resources that are *hosted in other accounts* by manually entering the ARN



##### **Routing Policies:**
**Simple**
* This is the default routing policy when you create a new resource.
* If you choose a simple routing policy you can only have one record with multiple
  IP addresses. If you specify multiple values in a record, Route53 returns all values
  to the user in a random order.

**Weighted**
* You can associate multiple resources with a single DNS name.
*

**Latency based**
* Based on users location and latency.

**Failover**
* Active/Passive

**Geolocation**
* Allows EU customers to be sent to EU backend and US customers to US backend.
* Lets you choose the resources that serve your traffic based on geographic
  location of your users, meaning the location that DNS queries originate from.

**Geoproximity Routing**
* Geoproximity routing lets Route53 route traffic to your resources based on the
  geographic location of your users and your resoures.

**Multivalue Routing**
* R53 Multivalue lets you respond to DNS queries with up to eight IP addresses of
  'healthy' targets. Plus it will give a different set of 8 to different DNS resolvers.
  The R53 Simple policy will provide a list of multiple instances in random order,
  but Multivalue is the AWS preferred option for this type of service.

#### **Health checking:**



## Databases:
* Can be categorized into two broad groups:
  - RDBMS (Relational Database Management Systems)
  - NoSQL (Non relational databases)

### Relational Databases:

#### Scaling Up and Out:
**Vertical Scaling**:
* By changing your DB instance type to a higher compute, memory or storage type.
* RDS automates the migration process to a new class with only a short disruption.
* Each DB instance can scale from 5GB up to 6 TB in provisioned storage depending
  on the storage type and engine.
* Storage expansion is supported for all Db engines except **SQL Server**.

**Horizontal Scaling**:
**Partitioning**:
* Partitioning a large relational database into multiple instances or shards is a
  common technique for handling more requests beyond the capabilities of a single
  instance.
* Requires additional logic in the application layer. Application needs to
  decide how to route DB request to the correct shard.
* NoSQL Databases like DynamoDB and Cassandra are designed to scale horizontally.

**Read Replicas**:
* Offload read transactions from the primary database to increase the overall
  number of transactions.
* Supported in RDS for MySQL, PostgreSQL, MariaDB and Aurora.
* RDS uses the MySQL, MariaDB and PostgreSQL DB engines built-in replication
  functionality to create a special type of DB instance, called a read replica
  from a source DB instance.
* Updates to the primary DB instance are asynchronously copied to the read
  replica.
* They are used for scaling, not for DR.
* Must have automatic backups turned on in order to deploy a read replica.
* You can have up to 5 read replica copies of any database.
* You can have read replicas of read replicas.

#### Security:
* Deploy RDS instance in private subnet within a VPC.
* Network ACLs and Security groups to restrict access from certain networks only.
* DB level access control with users with strong passwords that are rotated
  frequently.
* Encryption.


## Amazon Aurora:
* 5 times better performance that MysQL and 3 times better performance than
  postgres db.
* 2 copies of your data are contained in each AZ, with minimum of 3 AZs. 6 copies of
  your data.
* You can share Aurora snapshots with other AWS accounts.
* Automated backups turned on by default.
* Use Aurora serverless if you want a simple, cost-effective option for infrequent,
  intermittend or unpredicable workloads.

## Elasticache:
* SUpports two opensource caching engines
  - Memcached
  - Redis


## Amazon Redshift:
* Fast powerful, fully managed petabyte scale data warehouse service
* Relational database designed for OLAP scenarios.
* Optimized for high performance analysis and reporting very large datasets.
* Uses standard SQL commands to query large datasets.
* Currently only available in 1 AZ.
* Backups - enabled by default with a 1 day retention period, maximum retention
  period is 35 days.
* Always attempts to maintain atleast 3 copies of your data (the original and
  replica on the compute nodes and a backup in S3).
* It can asynchronously replicate snapshots to S3 in anothere region for DR.

### Clusters and Nodes:
* Key component of Redshift is cluster.
* A cluster is composed of a leader node and one ore more compute nodes.
* A client interacts with leader node. Compute nodes are transparent to applications.
* Supports six different node types with different mix of CPU, memory and storage.
* Nodes are grouped into two categories:
  * Dense compute: supports up to 326TB using fast SSDs.
  * Dense Storage: supports 2 Petabyte using large magnetic disks.

* Each cluster contains one ore more databases.
* User data for each table is distributed across compute nodes.
* Disk storage is divided into slices. Number of slices per node depends
  on node size of the cluster and varies between 2 to 16.
* Nodes participate in parallel query execution, working on data that is
  evenly distributed across slices.
* Query performance can be increased by adding multiple nodes to a cluster.
* You can resize a cluster to add storage and compute over time.
* During a resize database will become read only.

**Table design:**
* Like SQL databases, you can create a table using CREATE TABLE command.
* Takes name of the table, columns and their data types.
* In addition Redshift CREATE TABLE command also supports specifying compression
  encodings, distribution strategy and sort keys.

**Data Types**
* numeric data like INTEGER, DECIMAL and DOUBLE, text data like CHAR and VARCHAR,
  date types like DATE and TIMESTAMP.

**Compression Encoding**
* performance optimization used by Redshift
* Redshift will automatically sample your data and select the best Compression
  scheme for each column.
* You can also specify compression scheme on a per-column basis.

**Distribution Strategy**
* Define how to distribute the records across the nodes and slices in your
  cluster.
* Goal in selecting table distribution style is to minimize the impact
  of redistribution step by putting the data where it needs to be before
  the query is performed.

    Even distribution:
    * Default option.
    * Distributes across the slices in a uniform fashion regardless of data.

    Key distribution:
    * Rows are distributed according to the values in one column.
    * Leader node will store matching values close together and increase query
      performance.

    All distribution:
    * Full copy of the entire table is distributed to every node.
    * This is useful for lookup tables and other large tables that are not
      updated frequently.

**Sort Keys:**
* Sorting enables efficient handling of range restricted predicates.
* If a query uses a range-restricted predicate, the query processor can
  rapidly skip over large number of blocks during table scans.
* Sort keys can be compound or interleaved.
* Compound sort key is more efficient when query predicates use a prefix
  which is a subset of the sort key columns in order.
* An interleaved sort key gives equal weight to each column in the sort key,
  so query predicates can use any subset of the columns that make up the sort
  key in any order.

**Loading Data:**
* Supports SQL commands like INSERT and UPDATE to create and modify records in
  a table.
* For bulk operations provides COPY command. More efficient than INSERT of
  large number of records.
* When loading data from S3, COPY command can read from multiple files at the
  same time.
* After each bulk data load, you need to perform a VACUUM command to reorganize
  your data and reclaim space after deletes.
* Also recommended to run ANALYZE command to update table statistics.
* UNLOAD command to export data out of Redshift.

**Querying Data:**
* Standard SQL commands to query your tables.
* For large clusters supporting many users, you can configure Workload
  Management (WLM) to queue and prioritize queries.
* With WLM define multiple queues and set concurrency level for each queue.

**Snapshots:**
* Can create point-in-time snapshots of Redshift cluster.
* Supports automated and manual snapshots.
* You can perform manual snapshots and share them across regions or even other
  AWS accounts.
* Manual snapshots are retained until you delete them.

**Security:**
* IAM policies
* Network level security with VPC
* Also create a Master user account and password.
* You can create users and groups and grant permissions to tables and database
  objects. This is different than IAM policies.
* Data in transit encryption. SSL.
* Data at rest with KMS.


## DynamoDB:

**Links:**
http://docs.aws.amazon.com/amazondynamodb/latest/gettingstartedguide/quick-intro.html

http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GuidelinesForTables.html

* A fully managed NoSQL database service that provides fast and low latency
  performance that scales with ease.
* Amazon DynamoDB can provide consistent performance levels by automatically
  distributing data and traffic for a table over multiple partitions.
* DynamoDB will automatically add enough infrastructure capacity to support
  the requested throughput levels.
* You can adjust the read/write capacity after the table is created as well.
  DynamoDB will adjust the internal Partitioning accordingly.
* DynamoDB provides HA and durability by replicating data across multiple AZs
  within an AWS Region.
* Usecases for Dynamodb include storing metadata for S3 objects, json objects,
  managing web session data.

### Data Model:
* **Main components of DynamoDB are**:
* Tables:
  DynamoDB stores data in tables.

* Items:
  * Each table contains multiple items. An item is a group of attributes that
    is uniquely identifiable. For E.g in a people table each item represents
    one person.
  * There is no limit on the number of items you can store in a table.

* Attributes:
  * An attribute in DynamoDB is similar to fields or columns in other databases.
  * Each item is composed of one ore more attributes. An attribute is a
    fundamental data element that does not need to be broken down further.

* Primary Key:
  * When you create a table, in addition to the table name, you must specifically
    the primary key of the table.
  * A primary key in DynamoDB uniquely identifies each item in the table,
    so that no two items can have the same key.
  * When you add update or delete an item from a table you must specify
    the primary key attribute values for that item.

DynamoDB supports two types of primary keys:

**Partition Key**:
* A simple primary key, composed of one attribute known as the partition key.
* DynamoDB uses the partition key's value as input to an internal hash
  function. The output from the hash function determines the partition where the item is stored.
* No two items in a table can have the same partition key value.

    **Partition key and sort key**:
    * A composite primary key, composed of two attributes. First attribute is
      the partition key and the second one is the sort key.
    * All the items with the same partition key are stored together, in sorted
      order by sort key value.
    * With a composite key it is possible for two items to have the same
      partition key value, but those two items must have different sort keys.

  * Secondary Indexes:
    * You can read data in a table by providing it's primary key attribute value.
    * However you can read data using non-key attributes using a secondary
      index as well.
    * After you create a secondary index on a table, you can read data from
      the index in the same way as you do from the table.
    * Using secondary indexes, allows you to use many different query patterns,
      to access data from DynamoDB tables.


### Data types
* Scalar data types:
    * String: upto 400KB. Supports UTF8 encoding
    * number: Positive or negative number with up to 38 digits of precision.
    * Binary: Binary data images, compressed objects up to 400KB in size.
    * Boolean: Binary flag representing true or false value.
    * Null: Represents a blank, empty or unknown state.

* Set data types:
* Represent a unique list of one or more scalar values.
* Sets do not guarantee order.

    * String set: Unique list of string attributes
    * Number set: Unique list of number attributes
    * Binary set: Unique list of binary attributes

* Document data type:
* Document type is useful to represent multiple nested attributes,
  similar to a JSON file.

    * List: Each list can be used to store an ordered list of attributes of
      different data types.

    * Map: Each Map can be used to store an unordered list of key/value pairs.
      It can be used to represent any JSON object.

### Provisioned Capacity:
* When creating a DynamoDB table, you are required to provision certain
  read and write capacity to handle expected workloads.
* DynamoDB will provision the right amount of infrastructure capacity to meet
  the provisioned capacity configured.
* Provisioned capacity can be scaled up or down later as well depending on
  changing needs.
* The specific amount of capacity units consumed depends largely on the size
  of the item, but other factors apply as well.
* For read operations, the amount of capacity consumed also depends on the read
  consistency selected in the request.
* For eg, given a table without a local secondary index, you will consume
  1 capacity unit if you read an item that is 4KB or smaller.
* Similarly for write operations you will consume 1 capacity unit if you write
  an item 1KB or smaller.
* For read operations that are strongly consistent, they will consume twice
  the number of capacity units.
* You can use Amazon Cloudwatch to monitor your DynamoDB capacity and make
  scaling decisions.

### Secondary Indexes:
* You can optionally define one or more secondary indexes on a table, along with
  the partition key and sort key.
* A secondary index lets you query the data in the table using alternate key,
  in addition to queries against the primary key.

#### Global Secondary Index:
* It is an index with a partition and sort key that can be different from
  those on the table.
* You can create/delete a global secondary index on a table at any time.
* You can have multiple global secondary indexes on a table.

#### Local Secondary Index:
* It has the same partition key attribute as the primary key of the table,
  but a different sort key.
* Can only create a local secondary index during table creation.
* Allow you to search a large table efficiently and avoid and expensive
  scan operation to find items with specific attributes.
* You can only have one local secondary index.
* DynamoDB updates each secondary index when an item is modified. These Updates
  consume write capacity units from the main table, while global secondary
  indexes maintain their own provisioned throughput settings separate from
  the table.

### Reading and Writing Data:

#### Writing Items:
* PutItem, UpdateItem and DeleteItem are the 3 operations that you can do to
  write/modify/delete items into a DynamoDB table.
* PutItem will update an existing item, if it already exists (item with the
  same primary key value exists).
* UpdateItem action also provides support for atomic counters.
* These actions also support conditional expressions that allow you to
  perform validations before an action is applied.

#### Reading Items:
* GetItem action can be used to retrieve an item. Primary key is required
  for this action.
* All the items attributes are returned by default, and you have the option
  to select individual attributes to filter down the results.
* By default the GetItem action performs an eventually consistent read.
* You can optionally request a strongly consistent read, but will consume
  additional read capacity units - but will return the most up-to-date version
  of the item.

### Eventual Consistency:
* When reading items from DynamoDB, the operation can be either eventually
  consistent or strongly consistent.
* DynamoDB is a distributed system that stores multiple copies of an item
  across an AWS Region to provide HA and durability.
* When an item is updated in DynamoDB, it starts replicating across multiple
  servers. This replication might take some time to complete.
* A read request immediately following a write operation might not show the
  latest data.

### Strongly Consistent Reads:
* Applications might need to guarantee that the data is latest, in which case
  it can use strongly consistent reads. DynamoDB returns a response with the
  most up-to-date data that reflects updates by all prior related write
  operations to which DynamoDB returned a successful response.

* DynamoDb also provides batch write and read operations.
* BatchGetItem and BatchWriteItem. Using BatchWriteItem you can perform up to
  25 item creates or updates with a single operation.

### Searching Items:

#### Scan:
* Scan operation will read every item in a table or a secondary index.
* By default scan operation returns all of the data attributes of every item
  in the table or index.
* Each request can return up to 1MB of data.
* This can be resource intensive.

#### Query:
* Query is the primary search operation to find item in a table or a
  secondary index using only primary key attribute values.
* Results are automatically sorted by the primary key and are limited to 1MB.

### Scaling and Partitioning:
* A DynamoDb table can scale horizontally using partitions to meet the storage
  and performance needs of the applications.
* Each individual partition represents a unit of compute and storage capacity.
* A single DynamoDb partition can support a maximum of 3000 read capacity
  units or 1000 write capacity units. It can hold approximately 10GB of data.
* To achieve the full amount of request throughput provisioned for a table,
  keep your workload spread evenly across the partition key values.
* Distributing requests across partition key values distributes the requests
  across partitions.
* For example if a table has 10,000 provisioned read capacity units configured,
  but all the traffic is hitting one partition key, you will not be able to
  get more than 3,000 maximum read capacity units that a single partition can
  support.

* When you create a new table, the initial number of partitions can be expressed
  as below:
  ```
  (ReadCapacityUnits / 3000) +
     (WriteCapacityUnits/1000) = initial partitions (rounded up)
  ```
  For example: say you create a table with 1000 read capacity units and 500
  write capacity units, the initial partitions would be
  ```
   (1000/3000) + (500/1000) = 0.8333 --> 1
  ```

### Security
* DynamoDb gives you granular control over access rights and permissions for
  users and administrators.
* IAM policies to restrict access to specific tables.
* Restrict access to specific item and attributes with conditionals.

### DynamoDb Streams:
* Time ordered sequence of item-level changes in a table.
* To keep track of changes to DynamoDb.
* Can get a list of item modifications for the last 24 hour period.
* Each stream record represents a single data modification in the DynamoDb
  table to which the stream belongs.
* Each stream record is assigned a sequence number, reflecting the order in
  which the record was published to the stream.

### DynamoDB Accelerator (DAX):
* 10x performance improvement over DynamoDB
* Fully managed, highly available, in-memory cache
* Reduces request time from milliseconds to microseconds - even under load.
* No need to manage caching logic.
* Compatible with DynamoDB API calls.


### Transactions
* "All-or-nothing" operations - like financial transactions.
* Can operate of up to 25 items or 4 MB of data.


## Simple Queue Service (SQS)
* A fast, reliable, scalable and fully managed queuing service.
* Makes it simple and cost effective to decouple components of your cloud application.
* Does not guarantee message delivery order (no FIFO)
* If message order is required applications can handle that by passing a message
  sequence id.
* Ensures delivery of each message at least once and supports multiple readers and
  writers interacting with the same queue.

### Message lifecycle:
1. Component 1 sends message A to a queue. The message is redundantly distributed
    across the SQS servers.
2. Component 2 retrieves the message from the queue and message A is returned.
   While message A is being processed, it remains in the queue and is not
   returned to subsequent receive requests for a duration of the visibility
   timeout.
3. Component 2 deletes message A from the queue to prevent the message from
   being received and processed again after the visibility timeout expires.

### Delay Queues and Visibility Timeouts:
* Delay queues allow you to postpone the delivery of new messages in a queue
  for specific number of seconds.
* Any message that you send in that queue will be invisible to the consumer for
  the duration of the delay period.
* Delay period can range from 0 to 900 seconds (0 to 15 minutes)
* Default value of delay period is 0 seconds.
* You can turn an existing queue into a delay queue using SetQueueAttributes
  to set the queue's DelaySeconds attribute.
* Visibility timeout hides a message only after the message is retrieved
  from the queue.
* When a message is in the queue but is neither delayed nor in a Visibility
  timeout, it is considered to be "in flight"
* You can have up to 120,000 messages in flight at any given time.
* Default visibility timeout is 30 seconds.
* SQS supports up to **12 hours max visibility timeout**.
* SQS automatically deletes messages that have been in the queue for more than
  maximum message retention period.
* Shortest message retention period is 60 seconds.
* Default message retention period is 4 days.
* Longest message retention period is 14 days.
* Visibility timeout is the amout of time a message is invisible in the SQS queue
  after a reader picks up the message. Provided the job is processed before the
  visibility timeout expires, the message will then be deleted from the queue. If the
  job is not processed within that time, the message will become visible again and another
  reader will process it. This could result in same message being delivered twice.


### Queue Operations, Unique IDs and Metadata:
* Some SQS Operations:
  CreateQueue, ListQueues, DeleteQueue, SendMessage, SendMessageBatch,
  ReceiveMessage, DeleteMessage,..
* Messages are identified via a globally unique ID that SQS returns when the
  message is delivered to the queue. The ID is useful for tracking whether
  a particular message in the queue has been received.
* When you receive a message from the queue, the response includes a
  receipt handle, which you must provide when deleting the message.

### Queue and message identifiers:
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

### Message Attributes:
* Provide structured metadata items about the message.
* Each message can have up to 10 attributes.
* Are optional and separate from, but sent along with the message body.
* The receiver can use this information to help decide how to handle the
  message without having to process the message body first.


### Long polling:
* To receive message the consumer invokes ReceiveMessage API.
* ReceiveMessage will check for existence of a message in the queue and
  return immediately, either with or without a message.
* With long polling, you send WaitTimeSeconds argument to ReceiveMessage
  of up to 20 seconds.
* If there is no message in the queue the call will wait up to WaitTimeSeconds
  for a message before returning.
* If a message appears before the time expires, the call will return with
  the message right away.


### Dead Letter Queues:
* A queue that other queues can target to send messages that for some reason
  could not be successfully processed.
* Ability to sideline and isolate unsuccessfully processed messages.

### Access Control:
* IAM policies to grant specific instructions.



## Simple Workflow Service (SWF):
* SWF makes it easy to build applications that coordinate work across distributed
  components.
* In SWF task represents a logical unit of work that is performed by a component
  of your application.
* You implement the workers to perform tasks.
* Workers can run either on EC2 or on on-premises instances/servers.
* You can create long running tasks that might fail, timeout or require
  restart or tasks that can complete with varying throughput and latency.
* SWF stores tasks, and assigns them to workers when they are ready, monitor
  their progress and maintain their state, including details on their completion.
* To coordinate tasks you write a program that gets the latest state of each task
  from SWF and uses it to initiate subsequent tasks.
* SWF workflow executions can last up to 1 year.

### Workflows:
* In SWF you can implement distributed, asynchronous applications as workflows.
* Workflows coordinate and manage execution of activities that can be run
  asynchronously across multiple computing devices and that can feature
  both sequential and parallel processing.

### Workflow Domains:
* Workflows in different domains cannot interact with one another.
* Domains are a way of scoping SWF resources within your AWS account.

### Workflow history:
* Is a detailed, complete and consistent record of every event that occurred
  since the workflow execution started.

### Actors:
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


### Tasks:
* Three types of tasks:
  * Activity tasks:
    * tells and activity worker to perform it's function.
  * AWS Lambda tasks:
    * Similar to activity task, but executes an AWS Lambda function
  * Decision tasks:
    * Tells a decider that the state of the workflow execution has changed
      to determine the next activity that needs to be performed.



## Simple Notification Service (SNS):
* A web service for mobile and enterprise messaging that enables you to
  setup, operate and send notifications.
* It follows the publish-subscribe messaging paradigm, with notifications
  being delivered to clients using push mechanism that eliminates the need to
  check periodically for new updates.
* You can use SNS to send short message service (SMS) messages to mobile devices
  in the US or to email recipients worldwide.
* Two client types:
  * **Publishers** and **Subscribers**.

* Publishers communicate to Subscribers asynchronously by sending a message to
  a topic.
* A topic is simply a logical access point/communication channel that contains
  a list of subscribers and the methods used to communicate to them.
* When you send a message to a topic it is automatically forwarded to each
  subscriber of that topic using the communication method configured for
  that subscriber.
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

## Elastic Transcoder:
* Media transcoder in the cloud.
* Convert media files from original source in to different formats.


## AWS CloudFront:
* It is a global Content Delivery Network (CDN) service.
* A CDN is a globally distributed network of caching servers that speed up
  the downloading of web pages and other content.
* CDNs use DNS geo-location to determine the geographic location of each
  request for a web page, then serve that content from edge caching servers
  closest to that location.
* CloudFront can be used to deliver your web content using Amazon's global
  network of edge locations.
* A request is first routed to the edge location that provides the lowest latency.
  If the content is already in the edge location, CloudFront delivers it. If the
  content is not present, then CloudFront retrieves it from the origin server.
* CloudFront works with S3 buckets, S3 static websites, EC2, ELB and also
  non AWS origin server such as on-premises web server.
* CloudFront also integrates with Route53.
* It supports all content that can be served over HTTP or HTTPS, including static
  files, HTML files, images, JS, CSS, audio, video and media files or software
  downloads, also supports media streaming using both HTTP and RTMP.

### CloudFront Basics:
Three core concepts to understand CloudFront.

#### Distributions
* This is the name given to the CDN which consists of a collection of Edge
  locations.
* You start by creating a distribution, which is identified by a DNS domain
  name like 'd11223233.cloudfront.net'.
* To serve files from CloudFront, you simply use the distribution domain name
  in place of your website's domain name. Rest of the file path stays the same.
* You can also create a CNAME record in Route53 for DNS.


#### Origins
* You must specify the DNS domain name of the origin - S3 bucket or HTTP server.

#### Cache control
* Once requested and served from the edge location, objects stay in the Cache
  until they expire or are evicted to make room for more frequently requested
  content.
* By default objects expire from the cache after 24 hours.
* You can control how long objects stay in CloudFront cache before expiring.
* You can use cache-control headers set by your origin server or you can
  set the min, max and default TTL for objects in your CloudFront distribution.
* You can also remove copies of an object from all CloudFront edge locations
  at any time by calling the invalidation API. This feature removes the object
  from every CloudFront edge location regardless of the expiration period set
  on the object on your origin server.
* Instead of invalidating objects, it is best practice to use a version
  identifier as part of the object path name.
* When using versioning, users will always see the latest content through
  CloudFront, when you update your site. Old versions will expire from the
  cache automatically.

#### Advance CloudFront Features:
* Can be setup to use more than one origins. You can control which requests
  are served by which origin and how the requests are cached - using a feature
  called "cache behaviors".
* Cache Behaviors:
  * Path patterns
  * Which origin to forward requests to
  * Whether to forward query strings to your origin
  * Whether you need signed URL for specific files.
  * Require HTTPS access
* Cache behaviors are applied in order. If a request does not match the
  first path pattern, it drops down to the next.
* Signed URLs - URLs that are valid only between certain times and
  optionally from certain IP addresses.
* Signed cookies - Require authentication via public and private keys.
* Origin Access Identities: Restrict access to an S3 bucket only to a
  special CloudFront user associated with your distribution.


## Simple Storage Service (S3):
* S3 has the following features:
 * Tiered Storage
 * Lifecycle managemennt
 * Versioning
 * Encryption
 * MFA Delete
 * Secure your data using Access Control Lists and Bucket Policies

### S3 Storage classes:
 * *S3 Standard:*
 - 99.99% availability
 - 99.99999999999% durability (11x9 durability)
 - Stored redundantly across multiple devices in multiple facilities, and
   is designed to sustain the loss of 2 facilities concurrently.


 * *S3 IA:*
  - For data that is accessed less frequently, but requires rapid access
    when needed.
  - Lower fee than S3, butt are charged a retrieval fee.

 * *S3 One Zone - IA:*
  - Lower cost option for infrequently accessed data, but does not require
    multiple AZ data resiliency.

 * *S3 Intelligent tiering:*
  - Designed to optimize costs by automatically moving data to most cost-effective
    access tier, without performance impact or operational overhead.

 * *S3 Glacier:*
  - Secure,  durable, and low cost storage class for data archivin.
  - Retrieval times configurable from mins to hours

 * *S3 Glacier Deep Archive:*
  - Lowest cost storage class.
  - Retrieval time of 12 hours.


### S3 Security & Encryption

Access control::
* Bucket policies
* Access control lists
* S3 buckets can be configured to create access logs which log all requests
  made to the S3 bucket. This can be sent to another bucket in another account.

* Encryption iin transit is achieved by
 * SSL/TLS

* Encryption at rest (Server side) is achieved by
  * S3 Managed Keys SSE-S3
  * AWS Key Management Service, Managed Keys-SSE-KMS
  * Server Side Encryption with customer provided keys SSE-C
  * Client side encryption

### S3 object lock

* You can use S3 object lock to store objects using a write-once-read-many
  (WORM) model. It can help prevent objects from being deleted or modified
  for a fixed amount of time or indefinitely.

* You can use S3 object lock to meet regulatory requirements that require
  WORM storage, or add extra layer of protection against object changes and
  deletion.

* You can only enable Object lock for new buckets. If you want to turn on
  Object lock for an existing bucket, contact AWS support.
* When you create a bucket with object lock, Amazon S3 will automatically enable
  versioning for the bucket.
* If you create a bucket with Object lock enabled, you can't disable Object lock
  or suspend versioning for the bucket.

* With *governance mode*, users can't overwrite or delete an object version or
  alter it's lock settings unless they have special permissions.
* With *compliance mode*, a protected object version can't be overwritten or
  deleted by any user, including the root user in your AWS account.


### S3 Performance
* S3 has extremely low lattency. You can get the first byte out of S3
  within 100-200 milliseconds.

* You can achieve a high number of requests: 3500 PUT/COPY/POST/DELETE
  and 5,500 GET/HEAD requests per second *per prefix*.

* You can get better performance by spreading your reads across different
  prefixes. Eg: If you are using two prefixes, you can achieve 11,000 requests
  per second.

*S3 limitations when using KMS*
* If you are using SSE-KMS to encrrypt your ojects in S33, you must keep in
  mind the KMS limits. Uploading/downloading will count toward KMS quota.

* When you upload a file, you will call GenerateDataKey in the KMS API.

* When you download a file, you will call Decrypt in the KMS API.

* Region-specific, however it's either 5,5000, 10,000 or 30,000 requests per
  second.

### S3 Select:
* Retrieve only a subset of data from an object by  using simple SQL expressions.
* Get data by rows or columns using simple SQL expressions.
* Save money on data transfer and increase speed.

###  Granting S3 bucket access cross accounts:

* Using Bucket policy and IAM (Applies across entire bucket) Programmatic Access Only
* Using Bucket ACLs and IAM (individual objects) Programmatic Access only
* Cross account IAM Roles. Programmatic and Console access.

### S3 Transfer Acceleration:


* Once versioning is enabled, it cannot be disabled. Only suspended.

* read-after-write consistency for PUTs to new objects (new key),
* But eventual consistency for GETs and DELETEs of existing objects (existing key).
  Eventual consistency means if you PUT new data to an existing key, a subsequent
  GET might return old data. Similarly if you DELETE an object, a subsequent GET
  for that object might still read the deleted object.
  In all cases updates to a single key are atomic - for eventually-consistent
  reads you will get new data or old data, but never an inconsistent mix of data.

* Durability in S3 is achieved by replicating data geographically to different
  AZs regardless of the versioning configuration. AWS does not use tables.

* Bucket names must be unique across all AWS accounts, much like DNS names.
* Bucket names can contain up to 63 lowercase letters, numbers, hyphens and
  periods.
* Can have upto 100 buckets per account by default.
* Even though the namespace of S3 is global, each S3 bucket is created in a
  specific region that you choose. This lets you control where your data is
  stored. Default if you don't specify is us-east-1.
* Each object consist of data and metadata. Data is opaque to S3. Data is
  treated simply as a stream of bytes.
* metadata can be system metadata - created and used by S3 or user metadata
  which is optional, and can be specified during object creation time.
* Keys define the objects in S3 buckets. It can be upto 1024 bytes of unicode
  UTF-8 unicode characters including embedded slashes, backslashes, dots and
  dashes.
* Normal bucket URL: https://s3/amazonaws.com/(bucketname)/(keypath)
* S3 website URL: https://<bucketname>.s3.amazonaws.com/<path>/<to>/<my>/<file>
* Object url: http://<bucketname>.s3.amazonaws.com/<path>/<to>/<my>/<file>
* Durability : 99. 11 9s and Availability: 99.99%
* Largest file size you can use to PUT an object: 5GB. After that you have
  to use multipart upload.
* For objects larger than 100 MB you should use multipart upload.
* Minimum file size: 0 bytes
* Maximum file/object size: 5TB.
* RRS: Reduced Redundancy Storage - offers 99.99% durability.

### Access Control:
* By default when you create a bucket or object in S3, only you have access.
* To allow access to others, S3 ACLS or IAM policies can be configured.
* ACL allow you to grant coarse-grained permissions: READ, WRITE and
  FULL control on the object or bucket level.
* ACLs are legacy access control, created before IAM existed.
* S3 bucket policies are the recommended access control mechanism for S3
  and provide much finer grained control.
* **An interesting note on ACLs:**
  * You can make a specific object publicly accessible using ACLs.
  * However you can still control access to this object with bucket policy.
    Like restricting access to the object from specific IP addresses.

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

* [AWS Doc on blocking S3 traffic by VPC or IP](https://aws.amazon.com/premiumsupport/knowledge-center/block-s3-traffic-vpc-ip/)
* [S3 VPC Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html)

### Static Website hosting:
* Create a bucket, upload static files, make them public (world readable)
* Enable static website hosting for the bucket. This includes specifying an
  index document and an error document.
* This website will now be available at:
   <bucketname>.s3-website-<aws region>.amazonaws.com
* Create a friendly DNS name in your own domain for the website using a CNAME
  and you have your website available.


### Storage classes:

#### S3 Standard:
* High durability, high availability, low latency and high performance
  object storage for general purpose use.
* Offers low first byte latency and high throughput.

#### S3 Standard - Infrequent Access:
* High throughput as S3 standard, but is designed for long lived, licenses
  frequently accessed data.
* It has lower per GB-month storage cost than standard.
* Minimum object size of 128KB.
* Objects can be moved here 30 days after creation.

#### S3 Reduced Redundancy Storage (RRS):
* Offers slightly less durability (4 nines) than standard or standard AI at
  reduced cost

#### Amazon Glacier:
* Secure, durable and extremely low cost storage for data.
* Optimized for infrequently accessed data.
* Data is stored in archives. An archive can contain up to 40TB of data.
* You can have unlimited number of archives.
* After an archive is created it cannot be modified.
* Vaults are containers for archives.
* Each AWS account can have up to 1000 vaults.
* Vault access can be controlled with IAM policies.
* To retrieve object from Glacier you issue a restore command using S3 APIs.
  Three to five hours later object is copied to S3 RRS.
* Glacier allows you to retrieve up to 5% of the S3 data store in glacier
  for free each month.
* Objects archived to glacier incur cost for at least 90 days even if they
  are deleted or overwritten earlier.

### Versioning:
* Versioning is enabled at the bucket level.
* Once turned on versioning cannot be removed, it can be suspended

### MFA Delete:
* Requires additional authentication to delete an object version or change
  the versioning state of a bucket. MFA delete requires an additional
  authentication code generated by a hardware or MFA device.
* MFA delete can only be enabled by the root account.


### Pre-Signed URLs:
* All S3 objects are by default private.
* Owners can shared objects with others without granting explicit permissions
  with IAM policies, by creating pre-signed URL using their own security
  credentials to grant time-limited permissions to download objects.
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
Params={'Bucket': 'my-test-bucket', 'Key': 'scripts/aws_volume_helper.py'}, ExpiresIn=3600)
u'https://my-test-bucket.s3.amazonaws.com/scripts/aws_volume_helper.py?AWSAccessKeyId=AXXXXXXXXXXX3REGL5A&Expires=1491340796&Signature=2pfqmdtyOcRbXWQ8'
>>>
>>>
```

### Multipart Upload:

**Links**
  http://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadComplete.html

* For larger objects use multipart Upload
* Each chunk should be minimum 5MB size.
* Always complete or abort a multipart upload - else the individual chunks
  upload will not be cleaned up and will cost.


### Cross-Region Replication:
* To enable CRR you need versioning enabled on source and destination buckets.
* Existing objects will not be replicated, only new objects will be replicated.
* Permissions also get replicated.
* When you delete specific versions of an object or delete a delete marker,
  it does not get replicated to the dest bucket, it's only when you delete
  an object that it gets deleted from the replicated bucket.

* S3 will scale automatically to support very high request rates, automatically
  re-partitioning your buckets as needed. If you need request rates higher than
  100 requests/second, you may want to review the S3 best practices guidelines
  in DEV guide.
* To support higher request rates, it is best to ensure some level of random
  distribution of keys. For eg, by including a hash as a prefix to key names.

* S3 charges:
  You are charged for:
  * Storage
  * requests
  * Storage management pricing (charged for each tag)
  * Data transfer pricing
  * Transfer acceleration

### S3 cross-account access:
[Managing cross account access](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.html)
[cross account access](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/)

## Cloudwatch:
* Two plans: basic/standard and detailed
* Basic is default, sends data points to Cloudwatch every 5 minutes for a
  limited number of metrics.
* Detailed is to be explicitly enabled. Sends data points every minute and
  allows data aggregation
* Limit of 500 alarms per AWS account.
* Metrics data is retained for 2 weeks.
* A cloudwatch logs agent is available that provides an automated way to
  send log data to cloudwatch logs. Install it on an EC2 instance. It stays
  running until you disable it.
* Cloudwatch metrics provide hypervisor visible metrics.
* Services it can monitor:
  * Compute
    . Autoscaling groups, EC2, ELBs, Route53 health checks.
  * Storage and Content Delivery
    . EBS volumes, Storage gateways, CLoudfrront
  * Databases and Analytics
   . DynamoDB, Elasticache nodes, RDS instances, Elastic Mapreduce job flows, Redshift
  * SNS, SQS, OpsWorks, Cloudwatch logs, Estimated AWS billing
* By default it monitors Host level metrics.
  - CPU
  - Network
  - Disk
  - Status check.
* Other things are custom metrics - like RAM utilization.
### Cloudwatch Concepts:
*Namespaces:*
* Is a container for cloudwatch metrics.
* Metrics in different namespaces are isolated from each other.
* There is no default namespace. You must specify a namespace for each
  data point you publish to cloudwatch.
* Names must contain valid XML characters and must be < 265 characters in length.
*Metrics:*
* Metrics are the fundamental concept in cloudwatch. It represents a time-ordered
  set of data points that are published to cloudwatch.
* Think of metrics as a variable to monitor, and data points as representing the values
  of that variable over time.
* Metrics exist in the region they were created.
* Metrics cannot be deleted, but they automatically expire after 15 months if no new data
  is published to them. Data points older than 15 months expirre on a rolling basis, as
  new data points come in.
*Timestamps:*
* Each metric data point must be associated with a timestamp.
* Timestamp can be 2 weeks in the past or upto two hours in the future.
* If you do not provide a timestamp, Cloudwatch creates it for you based on the time
  the data point was received.
*Metrics Retention:*
* Data points with a period of < 60 secods are available for 3 hours. These are high
  resolution custom metrics.
* Data points with a period of 60 seconds (1 min) are available for 15 days
* Data points with a period of 300 seconds (5 min) are available for 63 days
* Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months)
*Dimensions:*
* A dimension is a name/value pair that is part of the identity of a metric.
* You can assign upto 10 dimensions to a metric.
* Cloudwatch treats each unique combination of dimensions as a separate metric, even if
  the metric have the same metric name.
*Statistics:*



## Storage Gateway:

[Storage gateway FAQ](https://aws.amazon.com/storagegateway/faqs/)
* Connects on-premise software appliance with cloud based storage.
* Provides seamless integration with data security between your data center
  and AWS storage infrastructure.
* AWS storage gateway offers
  - file-based file gateways (Amazon S3 File & Amazon FSx File)
  - Volume based (cached and stored)
  - tape-based storage solutions


### S3 File Gateway:
* Adds to the users current block-based volume and VTL storage.
* Provides access to objects in S3 as files on NFS mount point.
*  It combines a service and virtual software appliance.
* The appliance/gateway is deployed on the premise on a VMWare ESXi, Microsoft
  hyper-V or KVM.
* The gateway provides access to S3 objects as NFS mounted files.
* With File gateway you can:
  * Store and retrieve files directly using NFS 3 or 4.1 protocol.
  * Access your data directly in S3 from any cloud application or service.
  * Manage your data in S3 using lifecycle policies, cross origin replication
    and versioning.
* It also provides low latency access to data through transparent local caching.
* Maximum number of file shares/S3 bucket is 1. There isa 1-to-1 mapping
  between a file share and S3 bucket.
* maximum number of file shares per gateway is 10.
* Maximum file size is 5 TB (same as the limit for S3.)

### Amazon FSx File Gateway
* Enables you to sotre and retrieve files in Amazon FSx for windows file server
  using SMB protocol.


### Volume gateway:
* Provides cloud backed storage volumes that you can mount as iSCSI devices
  from on-premise application servers.

#### Cached Volumes
* You store your data in S3 and retain a copy of frequently accessed data
  locally.
* They offer substantial cost savings on primary storage and minimize need
  to scale on premise storage.
* You also retain low-latency access to your frequently accessed data.
* Maximum size of a cached volume is 32 TB
* Maximum number of volumes / gateway : 32
* Total size of all volumes: 1024 TB.


#### Stored Volumes:
* This configuration provides durable and inexpensive off-site backups that you
  can recover to your local data center or EC2.
* You configure your on-premises gateway to store all data locally and then
  asynchronously backup point-in-time snapshots to S3.
* Maximum size of a stored volume is 16 TB.
* Maximum number of volumes/gateway : 32
* Total size of all stored volumes: 512 TB


### Virtual Tape gateway:
* cost-effectively and durably archive backup data in Amazon Glacier.
* Provides a virtual tape infrastructure that scales seamlessly with your
  business needs.
* Minimum size of virtual tape : 100 GiB
* Maximum size of a virtual tape: 2.5 TiB
* Max number of virtual tapes for a VTL (Virtual tape library): 1500
* Total size of all tapes in a VTL: 1 PiB
* Max number of virtual tapes in archive: unlimited.


## AWS Directory Service:
* Provides directories that contain information about your org, including users
  groups, computers and other resources.
* Designed to reduce identity management tasks.
* Each directory is deployed across multiple AZs and monitoring automatically
  detects and replaces domain controllers that fail.
* Data replication and automated daily snapshots are configured.

* Three directory types:
  * Microsoft AD
  * Simple AD
  * AD connector



### Microsoft AD:
* Provides similar functionality offered by Microsoft AD, plus integration
  with other AWS services.
* Easily setup trust relationships with existing AD domains to extend
  those directories.

### Simple AD:
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

### AD connector:
* Proxy service for connecting your on-premise Microsoft AD to AWS without
  requiring complex directory synchronization or the cost and complexity
  of hosting a federation infrastructure.
* AD connector forwards sign-in requests to your AD domain controllers for
  authentication.
* After setup your users can use their existing corp credentials to login
  to AWS applications.

## AWS Key Management Service (KMS) and CLoudHSM:
* Key management is a management of cryptographic keys within a cryptosystem.
* Deals with generation, exchange, storage, use and replacement of keys.
* Two services are offered: KMS and CloudHSM.

### AWS Key Management Service (KMS):
* Service to generate, store, enable/disable and delete symmetric keys
* Lets you create keys that can never be exported from the service and that
  can be used to encrypt and decrypt data based on policies you define.
* You can use KMS directly in your appln or through cloud services that are
  integrated with KMS.
* Enables you to have control over who can use your keys and gain access to
  encrypted data.

#### Useful links:
* https://aws.amazon.com/blogs/security/new-aws-encryption-sdk-for-python-simplifies-multiple-master-key-encryption/

#### Customer managed keys:
* KMS uses a type of key called Customer Master Key to encrypt/decrypt data.
* CMKs are the fundamental resource that KMS manages.
* They can be used inside KMS to encrypt/decrypt upto 4KB of data directly.
* They can also be used to encrypt generated data keys that are then used
  to encrypt/decrypt large amount of data outside of the service.
* CMKs can never leave KMS unencrypted, but data keys can.

#### Data keys:
* Data keys are used to encrypt large data objects in your appln (outside
  of KMS)
* GenerateDataKey API Call - KMS returns a plaintext version of the key and
  ciphertext that contains the key encrypted under the specified CMK.
* AWS tracks which CMK was used to encrypt the data key
* You use the plaintext data key in your appln to encrypt data, and you
  typically store the encrypted key alongside the encrypted data.
* Remove the plaintext key from memory as soon as possible.
* To decrypt data pass the encrypted data key to the decrypt function.
  AWS uses the CMK to decrypt and retrieve your plaintext data key. Use
  this plaintext key to decrypt your data and then remove the key from memory.


#### Envelope Encryption:
* KMS uses envelope encryption to protect data.
* You can retrieve a plaintext data key only if you have the encrypted data
  key and have permission to use the corresponding master key.

#### Encryption Context:
* All KMS cryptographic operations accept an optional key/value map of
  additional contextual information called encryption context.
* Context must be the same for both encrypt and decrypt operations or decryption
  will fail.
* The encryption context is logged and can be used for auditing, and is
  available as context in AWS policy language for fine-grained policy based
  authentication.

#### KMS Operations:

- Creating a new KMS customer key:

```
aws kms create-key \
    --profile dev1 --region us-west-2 \
    --description "Customer test key"
KEYMETADATA	111111111111	arn:aws:kms:us-west-2:1111111:key/839-f1114-1411-02222228	122409.9	Customer test key	True	83118	CUSTOMER	Enabled	ENCRYPT_DECRYPT	AWS_KMS

```

- List key policies:

```
$ aws kms list-key-policies \
    --key-id 81xx9-15-41-111011 \
    --profile dev1 --region us-west-2
POLICYNAMES	default

```


- Get Key policy:

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
- Create an alias.

```
$ aws kms create-alias \
    --alias-name alias/brdtestkey \
    --target-key-id 1x11-15-1-1-11  \
    --profile dev1 --region us-west-2

```


Now let's use are new key to encrypt and decrypt data. We will use the alias created instead of the long convoluted key-id:

- Encrypt user data.
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

- Decrypt data.

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

## AWS Secrets Manager:


## AWS Systems Manager /Parameter Store:


## Athena vs Macie

## Athena
* Interactiive query service which enables you to analyze and query data
  located in S3 using standard SQL.

* Serverless, nothing to provision, pay per query / per TB scanned
* No need to setup complex Extract/Transform/Load (ETL) processes
* Works directly with data stored in S3
* Data formats supported: JSON, Apache Parquet, Apaache ORC

### What can Athena be used for?
* Query log files stored in S3, eg ELB logs, S3 access logs, cloudtrail logs.
* Generate business reports on data stored in S33
* Analyze AWS cost and usage reports
* Run queries on click-stream data

### What is PII (Personally Identifiaable Information)?

* Personnal data used to establish an individual's identity.
* This data can be exploited by criminals, used in identity theft and
  financial fraud
* Home address,  email, SSN, Passport number, driver's license number
* DOB, phone, bank account, credit card number.

### Macie?

* It is a security service which uses ML and NLP to discover, classify and
  protect sensitive data stored in S3

* Uses AI to recognise if your S3 objects contain sensitive data such as PII
* Dashboards, reporting and alerts
* Works directly with data stored in S3.
* Can only analyze CloudTrail logs
* Great for PCI-DSS and preventing ID theft.




### AWS CloudHSM:
* Service providing secure cryptographic key storage by making hardware
  security modules (HSM) in the cloud.
* A HSM is a hardware appliance that provides secure key storage and
  cryptographic operations within a temper-resistant hardware module.

## Cloudtrail:

* Records important info about each API call, including API name, user, time of
  api, request parameters and response elements returned by AWS service.
* Two types of trails:
  **Trail that applies to all regions:**
  * Cloudtrail creates the same trail in each region, records the log files in
    each region and delivers the log files to a S3 bucket and to cloudwatch
    log groups if specified.
  * This is the default option.
  * If you choose, you can receive SNS notification for log file deliveries. One
    SNS topic will suffice for all regions.

  **Trail that applies to one region:**

* By default, your log files are encrypted using S3 SSE.
* Typically delivers logfiles within 15 minutes of API call.
* Service publishes new log files multiple times an hour, usually every
  5 minutes.

## Amazon Kinesis:
* Platform for handling massive streaming data on AWS.

### Kinesis Firehose:
* It is Amazon's data-ingestion product.
* It is used to capture and load streaming data into other AWS services like S3 and
  Redshift.
* Clients write data to stream using API call and data is automatically sent
  to proper destination.
* When configured to save to S3, firehose sends data directly to S3. for
  Redshift data is first sent to S3 and then a Redshift copy command is
  executed to load data to Redshift.
* Firehose can also write data to Elasticsearch, with option to back it up
  in S3.
* There is not data persistence in Kinesis firehose.

### Kinesis Streams:
* Capable of capturing large amounts of data from data producers and streaming
  it into custom applications for data processing and analysis.
* You can scale to support limitless data streams by distributing incoming
  data across number of shards.
* The processing is then executed on consumers which read data from shards
  and run the kinesis stream application.
* Allows you to persistently store your data for 24 hrs up to 7 days.
* Kineshis streams consists of shards:
  - 5 transactions per second for reads, up to a max total data read rate of
    2 MB per second and up to, 1000 records per second for writes, up to a max
    total data write rate of 1 MB per second (including partition keys)

Producers        Kinesis Streams         Consumers

EC2 -----------> Shard  ------------->  EC2               DynamoDB, S3
Mobile --------> Shard  ------------->  EC2      -------> EMR, Redshift
IOT    --------> Shard  ------------->  EC2



### Kinesis Analytics:
* Enables you to analyze streaming data real time with Standard SQL.
* Works with Firehose or streams.

## Amazon EMR:
>> Moved to readmeV2

## AWS Data pipeline:
>> Moved to readmeV2

## Web Identity Federation & Cognito
>> Moved to readmeV2

## OpsWorks:
>> Moved to readmeV2

## AWS Cloudformation:
>> Moved to readmeV2

## AWS Elastic Beanstalk:
>> Moved to readmeV2

## Trusted Advisor:
* Trusted Advisor provides 4 checks at no cost:
**Cost optimization**
[AWS Cost Optimization Playbook](https://d1.awsstatic.com/pricing/AWS_CO_Playbook_Final.pdf)

**Security**

**Fault tolerance**

**Performance improvement**


## AWS Config:
>> Moved to readmeV2


## API Gateway:
>> Moved to readmeV2

## AWS WAF (web application firewall)
>> Moved to readmeV2

## AWS Firewall manager
>> Moved to readmeV2


## Serverless (Lambda):
>> Moved to readmeV2


## Elastic Container Service (ECS):


## AWS EKS:


### Creating a kubeconfig
```
aws eks update-kubeconfig \
    --name test-eks-cluster \
    --role-arn arn:aws:iam::461168169469:role/SSOAdmin1Role \
    --kubeconfig ./kubeconfig
```


###
``
kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   172.20.0.1   <none>        443/TCP   13h

```


### Creating a node group
```
aws eks create-nodegroup \
    --cluster-name test-eks-cluster \
    --nodegroup-name eks-general \
    --subnets subnet-0301c41ac3e4d860f \
    --node-role arn:aws:iam::4xxxxxxxxx:role/eks-worker-role-NodeInstanceRole-1BA \
    --scaling-config minSize=1,maxSize=4,desiredSize=2 \
    --instance-types m4.large
```


## AWS Import/Export:
* Service that accelerates transferring large amounts of data in and out of
  AWS using physical storage appliances, bypassing the internet.
* A good choice if you have 16TB or less of data to import into S3 or EBS.
* You can also export from S3 with AWS import/export.
* Exporting as a VM is useful when you want to deploy a copy of an EC2 instance in
  your on-site virtualization environment. You can export most EC2 instances to
  Citrix Xen, Microsoft Hyper-V or VMware vSphere.

## Snowball:
* Uses Amazon provided shippable storage appliances, shipped through UPS.
* Each Snowball is protected by KMS and made physically rugged to secure
  and protect your data while in transit.
* Comes in two sizes: 50 TB and 80 TB and varies by region.
* Features:
  * Import/export data between on-premise data storage and S3.
  * Encryption is enforced.
  * You don't buy and maintain your own hardware devices.
  * Manage your jobs through AWS snowball console.

## Snowball Edge:
* 100TB data transfer device with on-board storage and compute capabilities.
* Snowball edge connects to your existing applications and infra using standard
  storage interfaces.
* It can cluster together to form a local storage tier and process your
  data on-premise, ensuring applications continue to run even when they are
  not able to access the cloud.

## Snowmobile:
* Petabyte and Exabyte amount of data.

## Database Migration Service (DMS)  (On-prem services)
* Helps migrate databases to AWS quickly and securely.
* Source DB remains fully operational during the migration, minimizing downtime.
* Supports homogenous migrations such as Oracle to Oracle, as well as hetrogenous
  migrations between different database platforms, such as Oracle or MS SQL to
  Amazon Aurora.
* Can setup a one-time migration or on-going replication. on-going replication keeps
  your source and target databases in sync.

## Server Migration Service (SMS) (On-prem services)
* Supports incremental replication of your on-premises servers in to AWS.
* Can be used as a backup tool, multi-site strategy and a DR tool.

## Application Discovery Service (On-prem services)
* Helps migration to AWS by gathering information about on-premises data centers.
* Collected data is retained in encrypted format in AWS application discovery service
  data store.
* The data is also available in AWS migration hub.
* You install the AWS App Discovery Agentless Connector as a virtual appliance on
  VMWare vCenter.
* It will build a server utilization map and dependency map of your on-prem environment.

## VM Import/Export (On-prem services)
* Easily import virtual machine images from on-prem environment to EC2 instances,
  and export them back.
* Service that accelerates transferring large amounts of data in and out of
  AWS using physical storage appliances, bypassing the internet.
* A good choice if you have 16TB or less of data to import into S3 or EBS.
* You can also export from S3 with AWS import/export.
* Exporting as a VM is useful when you want to deploy a copy of an EC2 instance in
  your on-site virtualization environment. You can export most EC2 instances to
  Citrix Xen, Microsoft Hyper-V or VMware vSphere.



## HA Architecture:



## Security on AWS:
* AWS is responsible for security of the cloud, and customers are responsible
  for security in the cloud.

**Links**:
https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf

```
+-----------------------------------------------------
Customer data
+-----------------------------------------------------
Platform, Applications, Identity and Access Management
+-----------------------------------------------------   Customer Responsible
Operating System, Network and Firewall configuration
+------------------------------------------------------
Client side Encryption,
Server side Encryption, Network Traffic Protection
+-------------------------------------------------x------x-----x-----x-----
Compute, Storage, Database, Networking
+-----------------------------------------------------      AWS Responsible
AWS GLobal Infrastruture (Regions, AZs) Edge Locations
+------------------------------------------------------
```

## Difference between Region, AZ and Edge location.

* A Region is a physical location in the world which consists off two or
  more AZs.
* An AZ is one or more discrete data centers, each with redunndant power,
  networking and connectivity, housed in separate facilities.
* Edge locations are endpoints for AWS whhich are used for cachin content.
  Typically consists of Cloudfront, Amazon's content



### Physical and Environmental Security
#### Fire detection and supression
#### power
#### Climate and Temperature
#### Management
#### Storage device decommissioning

### Business Continuity Management:
#### Availability:
* Data centers are build in clusters in various global regions.
* Each AZ within a region is designed as an independent failure zone.
* AZs are are all redundantly connected to multiple tier-1 transit providers.

#### Incident response:
#### Communication:

### Network Security
#### Secure network architecture

#### Secure Access points
* Strategically placed limited number of access points to the cloud.
* More comprehensive monitoring of inbound and outbound communications and
  network traffic.
* Permit secure HTTP (HTTPS) traffic.
* Supports FIPS compliance.

#### Transmission protection

### Network monitoring and protection:
#### DDoS Attachs.
#### Man in the middle attacks.
#### IP Spoofing.
* Amazon EC2 instances cannot send spoofed network traffic.
* AWS controlled host based firewall will not permit an instance to send
  traffic with a source IP or MAC address other than it's own.
#### Port scanning
* Unauthorized port scans by EC2 customers are a violation of AWS acceptable
  use policy.
* You may request permission from Amazon to conduct vulnerability scans to
  meet your specific compliance requirements.
* These scans must be limited to your own instances.

#### Packet sniffing by other tenants
* While you can place your instances in promiscuous mode, the hypervisor
  will not deliver any traffic to them that is not addressed to them.
* Even two virtual instances that are owned by the same customer located on
  the same physical host cannot listen to each other's traffic.


### AWS Account Security Features
#### AWS credentials
  * passwords
  * MFA
  * Access keys
  * Key pairs (ssh access)
  * X.509 certificates
* If you loose credentials you cannot recover them, you can however create
  new credentials and then disable or delete the old set of credentials.

### AWS Cloudtrail

### AWS Cloud Service specific Security


## AWS CLI:

* You can use your AWS Roles and access CLI.

**Links**:
http://docs.aws.amazon.com/cli/latest/userguide/cli-roles.html

Here is an example:
1. Create a Role in AWS Account. EG TESTROLE.
2. Create an IAM user that can assume the TESTROLE (it can be in a different account)
3. Now you aws config and credentials file will look like below:

```
~/.aws/config:
[profile myuser]
output = text

[profile role-testrole]
role_arn = arn:aws:iam::644444444456:role/TESTROLE
source_profile =  myuser

~/.aws/credentials
[myuser]
aws_access_key_id = AFDFFSFSFSFS
aws_secret_access_key = xxxxkduedo.....B+oelQ


```

This way you do not maintain multiple api keys. The user can assume multiple roles,
and you can use the same api credentials to access all roles.


## AWS Limits:
[Service limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)

### Cloudwatch
[limits](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_limits.html)

### Cloudtrail
[limits](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html)

## AWS Pricing
[pricing](https://aws.amazon.com/pricing/)


## AWS Offer file

### AWS offer index file
[AWS Price list api](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html)
[offer index](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json)
[EC2 offer file](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json)



## Boto3:

### Catching Exceptions:
You can either explicitly catch some exceptions like ProfileNotFound etc,
or you can catch any Client Error, as ClientError exception.
```
try:
    self.dbclient.describe_table(TableName=table_name)
except botocore.exceptions.ClientError as ce:
    print "Resource %s not found" % table_name
    print " exception: %s" % ce.response['Error']

```

## Credstash:

https://github.com/fugue/credstash

It is a simple yet useful way to manage secrets. It requires access to AWS.
It uses AWS KMS key for encrypting/decrypting and DynamoDB for storage.

Basic usage:

*Create a new DynamoDB table to use for credstash*
-
You can create a credential-store table, which is the default name credstash uses, or something
else, but will have to pass that in command line when saving/retrieving secrets.

```
$ credstash -p dev1 -t brdtesttable setup
Creating table...
Waiting for table to be created...
Table has been created. Go read the README about how to create your KMS key

```

*Create a new KMS key*
You can create a new KMS key with alias 'alias/credstash', or any other alias.

*Put a new secret*

```
$ credstash -p dev1 -t brdtesttable put -k alias/brdtestkey my-secret "this is my value"
my-secret has been stored

```

*List all secrets*

```
$ credstash -p dev1 -t brdtesttable list
my-secret -- version 0000000000000000001

```

*Retrieve a secret*

```
$ credstash -p dev1 -t brdtesttable get  my-secret
this is my value

```

## AWS Well-Architected Framework

### Five pillars
- Operational excellence:
  Ability to run and monitor systems to continually improve business value and
  support processes and procedures.

 - Security
   Ability to protect your information, systems and assets through risk
   assessment and mitigation.

 - Reliability
   Ability to recover from infrastructure or service disruptions, acquiring
   resources to meet demand and mitigating disruptions.

 - Performance Efficiency
   Ability to use compute resources efficiently to meet systems requiremenets
   while demands change and technologies evolve.

 - Cost Optimization
   Ability to run systems to deliver business value at the lowest price

 - AWS Well-Architected Framework Tool
   Review workloads and compare the state of workload to architectural best
   practices.

### Desin Principals:
- Stop guessin capacity
- Test systems at production scale
- Automate your architecture
- Improve throuh game days
- Allow for evolutionary changes





## Cost optimization:
[Foundations for Cost optimization](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/introduction.html)

### Cost optimization pillars:
* Right size
  Pickingg the correct instances for our current resources as well as resources
  we plan to use.

* Increase elasticity
  Using ASG to only use resources when those resources are needed, and not
  using resources when they are not. pay-for-what-we-use model.

* Leverage the right pricing model
  AWS offers different pricing models - reserved instances, on-demand and spot.

* Optimize storage
  Matching storage to our  uses.

* Measurre, monitor and improve
  Monitor and track our usage and cost


###  Services that help with cost
- AWS Budgets
- AWS Cost & Usage report
- Cost Explorer
- Reserved Instance reporting

### Cost effective resources and services
- Spot instances
- S3
- S3 glacier
- AWS Lambda
- AWS Autoscaling
- AWS Trusted Advisor
- AWS Cost & Usage report
- AWS Cost explorer

### Cost optimization design principles:
- Adopt a consumption model
  Pay for what you consume

- Measure overall efficiency
  Define and track your metrics and goals

- Stop spending money on data centers.

- Analyze and attributed expendetures
  Track your costs and usage - tagging, budgets, cost explorer, etc.

- Use AWS managed services
  Reduce your overall cost of ownership

- Recommends a CCOE (Cloud center of excellence).
  This is a team who stays updated on AWS bestt practices, new release etc
  so we can make sure we are using  AWS in most efficient and cost effective
  ways.


### Cost Optimization best practices

Tagging strategy:
See what resources are costing more

Ownership of costs:
Hold engineers responsible

Define your account structures:
Know your goals, and define metrics to track progress


### Fedramp:

* [AWS Fedramp integrated inventory workbook](https://aws.amazon.com/blogs/publicsector/automating-creation-fedramp-integrated-inventory-workbook/)
* [Fedramp.gov](https://www.fedramp.gov/new-integrated-inventory-template/)


---
Followups:
Basic (included for all AWS customers), Developer, Business, and Enterprise are the available AWS Support Plans. Reference: Compare AWS Support Plans.
https://aws.amazon.com/premiumsupport/plans/


The business support plan has a maximum response time of < 1 hour for "production system down" cases.

VPC peering only routes traffic between source and destination VPCs. VPC peering does not support edge to edge routing. Reference: Unsupported VPC peering configurations.
https://docs.aws.amazon.com/vpc/latest/peering/invalid-peering-configurations.html


Dynamodb: When you request a strongly consistent read, DynamoDB returns a response with the most up-to-date data, reflecting the updates from all prior write operations that were successful. However, this consistency comes with some disadvantages such as read might not be available if there is a network delay or outage, higher latency than eventually consistent reads, global secondary indexes not supported, and use of more throughput capacity than eventually consistent reads.

DynamoDB allows for the storage of large text and binary objects, but there is a limit of 400 KB.

spot instances:
Capacity Rebalancing helps you maintain workload availability by proactively augmenting your fleet with a new Spot Instance before a running Spot Instance receives the two-minute Spot Instance interruption notice. When Capacity Rebalancing is enabled, Auto Scaling or Spot Fleet attempts to proactively replace Spot Instances that have received a rebalance recommendation, providing the opportunity to rebalance your workload to new Spot Instances that are not at elevated risk of interruption. Capacity Rebalancing complements the capacity optimized allocation strategy (which is designed to help find the most optimal spare capacity) and the mixed instances policy (which is designed to enhance availability by deploying instances across multiple instance types running in multiple Availability Zones). Reference: Best practices for EC2 Spot.

Allocation strategies in Auto Scaling groups help you to provision your target capacity without the need to manually look for the Spot Instance pools with spare capacity. AWS recommends using the capacity optimized strategy because this strategy automatically provisions instances from the most-available Spot Instance pools. You can also take advantage of the capacity optimized allocation strategy in Spot Fleet. Because your Spot Instance capacity is sourced from pools with optimal capacity, this decreases the possibility that your Spot Instances are reclaimed. Reference: Best practices for EC2 Spot.


Placement groups:
Spread placement groups have a specific limitation that you can only have a maximum of 7 running instances per Availability Zone and therefore this is the only correct option. Deploying instances in a single Availability Zone is unique to Cluster Placement Groups only and therefore is not correct. The last two remaining options are common to all placement group types and so are not specific to Spread Placement Groups.

S3 URLs for accessing a bucket:
Both Virtual-host-Style and Path-Style URLs are supported, but path-style URLs will be eventually deprecated in favor of virtual hosted-style URLs for S3 bucket access. DNS compliant names are also recommended.

Reference: Virtual hosting of buckets.

Both virtual-host-style and Path-Style URLs are supported, but path-style URLs will be eventually deprecated in favor of virtual hosted-style URLs for S3 bucket access. DNS compliant names are also recommended.

Reference: Virtual hosting of buckets.

Path-Style URLs will be eventually deprecated. Virtual-host-style URLs are strongly recommended.

Reference: Amazon S3 Path Deprecation Plan – The Rest of the Story.
https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/
https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html


Storage gateways and file gateways:

File gateway provides access to objects in S3 as files or file share mount points. A file gateway simplifies file storage in Amazon S3, integrates to existing applications through industry-standard file system protocols, and provides a cost-effective alternative to on-premises storage. Reference: What is AWS Storage Gateway?.

With cached volumes, you store your data in Amazon Simple Storage Service (Amazon S3) and retain a copy of frequently accessed data subsets locally. Cached volumes offer a substantial cost savings on primary storage and minimize the need to scale your storage on-premises. You also retain low-latency access to your frequently accessed data. Reference: What is AWS Storage Gateway?.


SQS:
* When a consumer receives and processes a message from a queue, the message remains
 in the queue. Amazon SQS doesn't automatically delete the message. To prevent other
 consumers from processing the message again, Amazon SQS sets a visibility timeout,
 a period of time during which Amazon SQS prevents other consumers from receiving and
 processing the message. The visibility timeout begins when Amazon SQS returns a message.
 During this time, the consumer processes and deletes the message. However, if the
 consumer fails before deleting the message and your system doesn't call the
 DeleteMessage action for that message before the visibility timeout expires,
 the message becomes visible to other consumers and the message is received again.
 If a message must be received only once, your consumer should delete it within the
 duration of the visibility timeout.

Standard queues support at-least-once message delivery. However, occasionally (because of the highly distributed architecture that allows nearly unlimited throughput), more than one copy of a message might be delivered out of order.

---
You have been engaged by a company to design and lead the migration to an AWS environment. An argument has broken out about how to meet future Backup & Archive requirements and how to transition. The Security Manager and CTO are concerned about backup continuity and the ability to continue to access old tape archives. The Senior engineer is adamant that there is no way to retain the old backup solution in the AWS environment, and that they will lose access to all the current archives. What information can you share that will satisfy both parties in a cost-effective manner?

Sorry!
AWS Import/Export is a service you can use to transfer large amounts of data from physical storage devices into AWS. You mail your portable storage devices to AWS and AWS Import/Export transfers data directly off of your storage devices using Amazon's high-speed internal network. It wouldn't help to manage legacy data and data formats.

Correct Answer
Any migration project needs to consider how to manage legacy data and data formats. This includes backup and archives. A 3rd party archive service is viable, but would be an ongoing expense. Storage Gateway can be used to efficiently move data into AWS. Old tapes could either be restored to the Storage Gateway volume, or migrated to Virtual tapes inside AWS using Tape Gateway.


---
Following advice from your consultant, you have configured your VPC to use dedicated hosting tenancy. Your VPC has an Amazon EC2 Auto Scaling designed to launch or terminate Amazon EC2 instances on a regular basis, in order to meet workload demands. A subsequent change to your application has rendered the performance gains from dedicated tenancy superfluous, and you would now like to recoup some of these greater costs. How do you revert to default hosting tenancy?​

You can change the instance tenancy attribute of a VPC from dedicated to default. Modifying the instance tenancy of the VPC does not affect the tenancy of any existing instances in the VPC. The next time you launch an instance in the VPC, it has a tenancy of default, unless you specify otherwise during launch. You can modify the instance tenancy attribute of a VPC using the AWS CLI, an AWS SDK, or the Amazon EC2 API only. Reference: Change the tenancy of a VPC.


what is cold attach

NACL Rule processing

Your company is storing highly sensitive data in S3 Buckets. The data includes personal and financial information. An audit has determined that this data must be stored in a secured manner and any data stored in the buckets already or data coming into the buckets must be analyzed and alerts sent out flagging improperly stored data. Which AWS service can be used to meet this requirement?


AWS GuardDuty


AWS Trusted Advisor


AWS Inspector


Amazon Macie





Your company is slowly migrating to the cloud and is currently in a hybrid environment. The server team has been using Puppet for deployment automations. The decision has been made to continue using Puppet in the AWS environment if possible. If possible, which AWS service provides integration with Puppet?


Elastic Beanstalk


AWS OpsWorks


This is not possible. The AWS Developer Tools suite can handle automations.


CloudFormation





Your team has provisioned multiple Auto Scaling Groups in a single Availability Zone. The Auto Scaling Groups at max capacity would total 40 EC2 instances between them. However, you notice that the Auto Scaling Groups will only scale out to a total of 20 instances at any one time. What could be the problem?


There is a vCPU-based on-demand instance limit per region.


You can only have 20 instances per Availability Zone.


The associated load balancer can only serve 20 instances at one time.


You can only have 20 instances per region. This is a hard limit.





A small startup company has begun using AWS for all of its IT infrastructure. The company has two AWS Solutions Architects, and they are very proficient with AWS deployments. They want to choose a deployment service that best meets the given requirements. Those requirements include version control of their infrastructure documentation and granular control of all of the services to be deployed. Which AWS service would best meet these requirements?


CloudFormation


Terraform


OpsWorks


Elastic Beanstalk



Your company is using a hybrid configuration because there are some legacy applications which are not easily converted and migrated to AWS. And with this configuration comes a typical scenario where the legacy apps must maintain the same private ip address and MAC address. You are attempting to convert the application to the Cloud and have configured an EC2 instance to house the application. What you are currently testing is removing the ENI from the legacy instance and attaching it to the EC2 instance. You want to attempt a warm attach. What does this mean?


Attach the ENI to an instance when it's running.


Attach the ENI before the public IP address is assigned.


Attach the ENI to an instance when it is stopped.


Attach the ENI when the instance is being launched.



## Uncategorized.

* You can attach network interface to an instance when:
  - its running (hot attach)
  - it's stopped (warm attach)
  - when it is being launched (cold attach)

* You cannot detach primary n/w interface.
* You can detach secondary n/w interface when instance is running or stopped.
* You can move a n/w interface from one instance to another, if the instances are
  in the same AZ and VPC but in different subnets.


* A setup where you have an DR region up and running along side an active one, is
  following a *Multi-site* deployment patter.

* Each subnet in your VPC must be associated with a network ACL. If you don't
  explicitly associate a subnet with a network ACL, the subnet is automatically
  associated with the default network ACL.

* Cannot create an lias with a CNAME record set at the zone apex.

DIff bettween kinesis firehost kinesis streams, analytics
....

