#--------------------------------------------------------------------------------
# Networking
#--------------------------------------------------------------------------------

# Service: VPC
* Core networking component, serves as a private, layer 2 isolated networking layer.

------------------------------------------------------------
*Features*
The following features help you configure a VPC to provide connectivty to your apps:

*VPC*
A virtual network that closely resembles a traditional network. A VPC is at a region
level.

*Subnets*
A subet is a range of IP addresses in your VPC. A subnet must reside in a single AZ.
You deploy resources in your subnet.

*IP addressing*
You can assign IPV4 and IPV6 address to your VPCs and subnets. You can also bring your
public IPV4 addresses and IPV6 GUA addresses to AWS and allocate them to resources
in your VPC, such as EC2 instances, NAT gateways and network LBs.

*Routing*
Use route tables to determine where n/w traffic from your subnet or gateway is directed.

*Gateway and endpoints*
A gateway connects your VPC to another network. Eg internet gateway to connect your
VPC to the internet. Use VPC endpoints to connect to AWS services privately, without
using IGW or NAT device.

*Peering connections*
Allows you to route traffic between resources in two VPCs.

*Traffic Mirroring*
Copy n/w traffic from nw interfaces and send it to security and monitoring appliances
for deep packet inspecting.

*Transit gw*
Use Transit gateway, which acts as a central hub to route traffic between your VPCs,
VPN connections and AWS direct connect connections.

*VPC Flow logs*
A flow log captures information about the IP traffic going to and from network
interfaces in your VPC.

*VPN connections*
Connect your VPCs to on-prem nws using AWS VPN.

------------------------------------------------------------

## Types of IPV4 addresses:

*Elastic IP addresses EIPs*
Static, public IPV4 addresses provided by Amazon that you can associate with an
EC2 instance, elastic nw interface or AWS resource.

*Elastic public IPV4 address*
Public IPV4 addresses assigned to EC2 instances by Amazon (if instance is launched
in default subnet or a subnet that has been configured to automatically assign a
public IPV4 address)

*BYOIPv4 addresses*
Public IPV4 addresses in the IPv4 address range that you have brought to AWS.

*Service-managed IPV4 addresses*
Public IPV4 addresses automatically provisioned on aws resources and managed by
the AWS service. For eg: public ipv4 address on Amazon ECS, RDS, Workspaces.



------------------------------------------------------------
## Access the Internet.
* A default VPC includes an IGW, and each default subnet is public subnet. Any instance
  launched in a default subnet has a private and public IPV4 address and can
  communicate with the internet through the IGW.
* A non-default subnet, by default is not connected to an IGW. instances launched in
  a nondefault subnet have a private IPv4 address, but not a public IP address,
  unless you assign at launch or modify the subnet's public ip address attribute. Instances
  can communicate with each other by default, but cannot access the internet.
* you can enable internet access for non-default subnet by attaching an IGW to it's
  VPC and associating an Elastic IP address with the instance.
* You can also allow instances in your VPC to initiate outbound connections to the
  internet, but prevent inbound connections. For this use a NAT device. NAT maps multiple
  private IPv4 addresses to a single public IP address. COnfigure NAT device wieth an
  Elastic IP address and connect it to the internet through an IGW. Instances in private
  subnet can then connect to the internet through the NAT, routing traffic from the
  instance to the internet gateway and any responses to the instance.
  EC2 ---> NAT device --> IGW ---> Internet.
* For IPv6, instances can connect to the internet through IGW. Alternately, instances
  can initiate outbound connections to the internet over IPv6 using an egress-only
  internet gateway. *NOTE: Your route tables must include separate routes for bIPv6
  traffic*

------------------------------------------------------------

## Access a corporate or home network.
* Connect your VPC to a corp network data center using an IPSec AWS site-to-site VPN connection.
* a VPN connection consist of two VPN tunnels between a virtual private gateway or transit
  gateway on AWS side, and a customer gateway device on-prem.
* VPN supports Internet Protocol security (IPsec) VPN connections.
Limitations:
-----------
* IPv6 traffic is not supported for VPN connections on virtual private gateway.
* AWS VPN connection does not support Path MTU Discovery.
* Ensure to use non overlapping CIDR blocks between your VPC and on-prem network.

------------------------------------------------------------

## Connecting VPCs and networks.
* Create VPC peering connection between two VPCs. It will enable you to route traffic
  between them privately. Instances in either VPC can communicate with each other
* You can also create transit gateway and use it to interconnect your VPCs and
  on-prem networks. TGW acts as a regional virtual router for traffic flowing between
  its attachments, which includes VPCs, VPN connections, AWS direct connect gateways,
  transit gw peering connections

------------------------------------------------------------

## AWS private global network.
* AWS provides a high performance low latency private global network that delivers
  secure cloud computing environment.
* AWS regions are connected to multiple ISPs as well as to private global network
  backbone, which provides improved network performance for cross-region traffic.
* Traffic within the AZ in all regions routes over AWS private global network.
* Traffic between regions always routes over the AWS private global network, except
  china regions.


------------------------------------------------------------

## Instance IP addressing.

### Private IPv4 addresses
* It is not reachable over the internet, and can only be used for communication
  between instances in the same VPC.
* When you launch an instance into an ipv4-only or dual stack (ipv4 & ipv6) subnet,
  the instance receives a primary private ip address from the address range of the
  subnet.
* Each isntance has a default network interface (eth0) that is assigned the primary
  private IPv4 address.
* Unlike primary, a secondary private ip addresses can be reassigned from one
  instance to another.
* Number of network interfaces and private ipv4/6 addresses you can specify depends
  on the instance type.
* use cases for multipe ip addresses associated to an instance:
   * Host multiple websistes on a signel server.
   * Operate network appliances like firewalls or load balancers that have
     multiple ip addresses for each network interface.
   * Redirect internal traffic to a standby instance in case of instance failure,
     by reassigning secondary ip address to the standby.

### Public IPv4 addresses
* An address that is reachable from the internet.
* When an instance is launched in a default VPC, a public ip address is associated
  by default. For nondefault only private ip address is associated.
* A public ip address is assigned to the instance from Amazon's pool of public
  IPv4 addresses and is not associated with AWS account. When it is disassociated
  from the instance, it is released back to the address pool, and you cannot reuse it.
* A publc ip address is released from the instance when: it is stopped, hibernated
  or terminated. Stopped or hibernated instances receive a new public ip address when
  it is started again.
* a public ip address is released when an Elastic IP address is associated with it.
  When you disassociate the EIP from the instance, it gets a new public ip address.
* If the public IP address of your instance in a VPC has been released, it will not
  receive a new one if there is more than one network interface attached to your instance.
* If your instance's public IP address is released while it has a secondary private IP
  address that is associated with an Elastic IP address, the instance does not receive
  a new public IP address.

### Elastic IP addresses
* A static IPv4 address that is allocated to your AWS account, and its yours till you
  release it.
* By using an elastic ip address, you can mask the failure of an instance by
  remapping the address to another instance in your account. Alternately you can
  specify an elastic ip address in your DNS record for your domain, so that your
  domain points to your instance.
* An Elastic IP address is a public IPv4 address, which is reachable from the
  internet. If your instance does not have a public IPV4 address you can associate
  and elastic ip address to enable communication with the internet.
* Elastic ip address is static and does not change over time.
* It is for use in a specific region only, and cannot be moved to a different region.
* To use and EIP, you first allocate one to your account, and then associate it with
  your instance or nw interface.
* When you associate an EIP with an instance or its primary network interface, the
  instances public ipv4 address (if it had one) is released back into Amazon's pool
  of public IPv4 addresses. You cannot reuse a public IPV4 address, and cannot convert
  a public IPV4 address to an EIP address.


------------------------------------------------------------

## Elastic network interfaces
* A logical networking component in a VPC that represents a virtual network card.
  It can include the following attributes
  - A primary private ipv4 address from the address range of your vpc.
  - A primary ipv6 address from the address range of your vpc.
  - One or more secondary private ipv4 addresses from the address range of your vpc.
  - One EIP address per private IPV4 address
  - One public ipv4 address
  - One or more IPv5 addresses
  - One or more security groups
  - A MAC address
  - A source/destination check flag.
  - A description

* You can create a network interface, attach it to an instance, detach it and attach
  it to another instance. The attributes of the interface follow it as its attached
  to the instances.
* When you move a network interface from one instance to another, network traffic
  is redirected to the new interface.
* you can attach a network to an instance when it's running (hot attach), when it's
  stopped (warm attach), or when instance is being launched (cold attach).
* You can detach secondary network interfaces when the instance is running or stopped.
  You cannot detach the primary network interface.
* You can move secondary network interface from one instance to another if they are
  in the same AZ and VPC but in different subnets.
* you cannot attach another network interface to an instance (eg: NIC teaming)
  to increase or double the network bandwidth to or from dual-homed instance.

*Primary network interface*
* Each instance has a default network interface, called the primary network interface.
* You cannot detach a primary network interface from the instance.
* You can create and attach additional network interfaces.
* Max number of network interfaces that you can attach to an instance depends on
  the instane type.

*Public IPv4 addresses for network interfaces*
* In a VPC, all subnets have an attribute that determines whether network interfaces
  created in that subnet are assigned public IPv4 addresses. The public IPv4 address
  is assigned from Amazon's pool of public IPv4 addresses. When you launch an instance
  the IP address is assigned to the primary network interface that's created.
* When you create a network interface, it inherits the public IPv4 addressing attribute
  from the subnet. If you later modify the public IPv4 addressing attribute of the
  subnet, the n/w interface keeps the setting that was in effect when it was created.

*Elastic IP addresses for network interface*
* If you have an EIP address, you can associate it with one of the private IPv4
  address for the network interface.

*Termination behavior*
* You can specify whether the network interface should be automatically deleted when
  the instance is terminated.


------------------------------------------------------------

## Network bandwidth
* Instance b/w specifications apply to both inbound and outbound traffic for the
  instance.
* Available network bandwidth of an instance depends on the number of vCPUs it has.
  However instances might not achive this bandwidth; for eg: if they exceed nw
  allowances at instance level, such as packets per second or number of tracked
  connections.
* Instances receive the maximum number of network I/O crets at launch. If it exhausts
  it's network I/O credits, it returns to its baseline bandwidth.

------------------------------------------------------------

## Placemet groups.
* Depending on the type of workload you can create a placement group using one of
  the following placement strategies.
* You can create a max of 500 placement groups per account in each region.
* Name you specify for the placement group must be unique within the AWS account for
  the region.
* You cannot merge placement groups.
* An instance can be launched in one placement group at a time; it cannot span
  multiple placement groups.
* You can't launch dedicated hosts in placement groups.
* You can't launch a spot instance that is configured to stop or hibernate on
  interruption in a placement group.


*Cluster*:
* Packs instances close together inside an AZ. This strategy enables workloads to
  achieve low-latency network performance for tightly coupled node-to-node communication
  used in HPC applications.

*Partition*:
* Spreads your instances across logical parititions such that groups of instances
  in one partition do not share the underlying hardware with groups of instances
  in different partitions. Used for large distributed and replicated workloads like
  Hadoop, Cassandra and Kafka.

*Spread*:
* Strictly places group of instances across distinct underlying hardware to reduce
  correlated failures.


------------------------------------------------------------
## Network ACLs.
* A network ACL allows or denies specific inbound or outbound traffic at the subnet
  level.
* Each subnet must be associated with a network ACL. If you dont associate a subnet
  with a network ACL, the subnet is automatically associated with the default network ACL.
* You can associate a network ACL with multiple subnets. However a subnet can be
  associated with only one NACL at a time.
* A NACL has inbound and outbound rules. Each rule can either allow or deny traffic.
* Each rule has a number from 1 to 32766. Rules are evaluated in order, starting
  with the lowest numbered rule. If the traffic matches a rule, the rule is applied
  and we do not evaluate any additional rules.
* NACLs are stateless.
* NACLs cannot block DNS requests to or from route53 resolved.
* NACLs cannot block traffic to instanc metadata service.
* Default NACL is configured to allow all traffic to flow in and out of the subnets.
* Each NACL also includes a rule whose rule number is an asterick (\*). This rule
  ensures that if a packet does not match any other numbered rules, it is denied. You
  cannot modify this rule.

------------------------------------------------------------
## Network Firewall.
* You can filter network traffic at the perimiter of your VPC using network firewall.
* It is a stateful, managed network firewall and intrusion detection and prevention
  service.


------------------------------------------------------------
## AWS Privatelink.
* AWS privatelink establishes private connectivity between VPC and supported
  AWS services, hosted by other AWS accounts.
* To use AWS PrivateLink, create a VPC endpoint in your VPC, specifying the name
  of the service and a subnet. This creates an elastic network interface in that
  subnet that serves as an entry point for traffic destined to the service.
* You can create your own VPC endpoint service, and enable other AWS customers to
  access your service.

------------------------------------------------------------
## Route Tables.



#--------------------------------------------------------------------------------
# Service: CloudFront.
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
* You can configure CF to create log files that contain detailed info about every
  user request that CF receives. These are called standard logs or access logs.
* You can use an origin request policy to configure CF to include cookies and HTTP
  request headers in origin requests.
* An OAI (Origin Access Identity) is a special CF user that can access files in an
  S3 bucket and serve them to users. It allows us to restrict access to the contents
  of a bucket, so that all users must use the CF URL instead of a direct S3 URL.

## How you configure CloudFront to deliver content.
1. You specify origin servers (like S3 bucket or an HTTP server) from where CF gets
   your files which will be distributed from CF edge locations.
2. You upload your files to the origin servers.
3. You create a CF distribution, which tells CF which origin servers to use. You
   specify details like whether you want CF to log all requests and whether you want
   the distribution to be enabled as soon as it's created.
4. CF assigns a domain name to your new distribution that you can see in CF console or
   returns it as a response to API.
5. CF sends your distribution's configuration to all edge locations or points of
   presence - collections of servers in geographically dispersed data centers.

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


#--------------------------------------------------------------------------------
# Service: Elasticache
#--------------------------------------------------------------------------------
* Improves application performance by storing the most frequently accessed
  data in memory.
* Simplifies the setup and management of distributed in-memory caching environments.
* You can choose from Memcached or Redis protocol-compliant cache engine and quickly
  launch a cluster within minutes.

## Deployment options
*Serverless caching*
* With Elasticache Serverless, you can create highly-available and scalable cache
  in less than a minute, eliminating the need to provision, plan for and manage
  cluster capacity.
* Automatically stores data across 3 AZs and provides 99.99% availability.
* Automatic data replication across AZs.

*Self-designed clusters*

## Memcached vs Redis

|          Requirement        | Memcached | Redis |
| --------------------------- |:---------:|:-----:|
|Simple cache to offload DB   | yes       | yes   |
|Data types                   | Simple    |Complex|
|Data tiering                 | no        | yes   |
|Ability to scale horizontally| yes       | yes   |
|Multi-threaded performance   | yes       | No    |
|Advanced data types          | no        | yes   |
|Ranking/Sorting data sets    | no        | yes   |
|Pub/Sub capabilities         | no        | yes   |
|Persistence                  | no        | yes   |
|Multi-AZ                     | no        | yes   |

## Memcached
* Provides a simple interface that allows you to write and read objects into
  in-memory key/value data stores.
* You can elastically grow and shrink a cluster of memcached nodes to meet your
  demands.
* You can partition your cluster into shards and parallelize operations for very
  high performance throughput.
* Increasing the vaule of memcached_connections_overhead parameter will reduce the
  amount of memory available for storing items and prove a large buffer for
  connection overhea.

## Redis
* Beyond the object support provided in Memcached, Redis supports a rich set of
  data types like strings, lists and sets.
* Unlike Memcached, Redis supports the ability to persist the in-memory data
  on to disks. This allows creating snapshots that backup data and then
  recover or replicate from the backups.
* It can support up to 5 read replicas to offload read requests. In the event
  of a primary node failure, a read replica can be promoted to become the new
  master using multi AZ replication groups.
* Redis also has advanced features that make it easy to sort and rank data.

## Nodes and Clusters
* Each deployment of ElastiCache consists of one or more nodes in a cluster.
* A single Memcached cluster can contain 1 to 40 nodes.
* Redis clusters are always made up of a single node; however multiple
  clusters can be grouped into a Redis replication group.
* For Memcached clusters ElastiCache supports Auto Discovery with the provided
  client library.

## Backup and Recovery
* Redis allows you to persist your data from in-memory to disk and create a snapshot.
* Each snapshot is a full clone of the data that can be used to recover to a
  specific point in time.
* Snapshots CANNOT be created for Memcached engine because it is purely in-memory
  key/value store and always starts empty.
* Taking snapshot can have performance impact, and best practice is to create
  a replication group and perform a snapshot against a read replica instead of
  a primary node.

## Access Control:
* Access to ElastiCache cluster is controlled primarily by restricting inbound
  network access to your cluster, using security groups.
* Access to manage the configuration of the cluster is controlled by IAM policies.


#--------------------------------------------------------------------------------
# Cloudwatch:
#--------------------------------------------------------------------------------
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

## Cloudwatch Concepts:
*Namespaces*
* A container for cloudwatch metrics. Metrics in different namespaces are isolated
  from each other.
* There is no default namespace. You must specify a namespace for each data point you
  publish to Cloudwatch.
* Names must contain valid ASCII characters and must be < 265 characters in length.

*Metrics*
* A metric represents a time-ordered set of data points that are published to
  CloudWatch. Think of metrics as a variable to monitor, and data points as
  representing the vaules of that variable over time.
* Metrics exists only in the region they are created. They cannot be deleted, but
  they automatically expire after 15 months if no new data is published to them.
* Data points older than 15 months expire on a rolling basis; as new data points
  come in.
* Metrics are uniquely defined by a name, a namespace and zero or more dimensions.
  Each data point in a metric has a timestamp and (optionally) a unit of measure.

*Timestamps*
* Each metric data point must be associated with a timestamp. The timestamp can be
  two weeks in the past and up to 2 hours in the future.
* If you do not provide a timestamp, CloudWatch creates a timestamp based on the
  time the data point was received.
* Timestamps are datetime objects with complete data plus hours, minutes, seconds.
* CW alarms check metrics based on the current time in UTC.

*Metrics retention*
* Data points with a period:
 * (less than 60 seconds)  are available for 3 hours (These are high resolution custom metrics).
 * period of 60 seconds   are available for 15 days
 * period of 300 seconds (5 min)   - 63 days
 * period of 3600 seconds(1 hour)  - 455 days (15 months)
* Data points that are initially published with a shorter period are aggregated
  together for long-term storage.

*Dimensionsi & Dimension combinations*
* A name/value pair that is part of the identity of a metric.
* You can assign upto 30 dimensions to a metric.
* CW treats each unique combinatio of dimensions as a separate metric, even if the
  metric have the same metric name

*Resolution*
* Each metric is on of the following:
  * Standard resolution - with data having a one-minute granularity
  * High resolution - with data at a one second granularity
* Metrics producded by aws services are standard resolution.
* When you define custom metrics you can define it as standard or high resolution.
* Note that every PutMetricData call for custom metric is charged.

*Statistics*
* They are metric data aggregations over specified periods of time.
* Aggregations are made using namespaces, metric name, dimensions and the data point
  unit of measure within the time period specified.

*Units*
* You can specify unit when you create a custom metric. If you do not specify unit,
  CW uses None as the unit.

*Percentiles*
* A percentile indicates the relative standing of a value in a dataset.







#--------------------------------------------------------------------------------
# Cost and Performance Optimization.
#--------------------------------------------------------------------------------
* Cost allocation tags are tags which are used to help track AWS costs on a detailed
  level.
* user-defined tags created, defined and applied to your resources.
* AWS generated CATs are tags created, defined and applied to resources by AWS for
  supported resources.

# Cost Explorer.
* Allows you to visualize, view and analyze AWS usage costs.


# AWS BUdgets.
* cost budget.
* usage budget
* savings plan budget.
* reservation budget.



























