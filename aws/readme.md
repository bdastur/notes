# AWS Notes:


## Dynamo DB:

## Virtual Private Cloud (VPC):

**Links**
http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html

* VPCs do not span regions, they can span availability zones.
* VPC lets you provision a logically isolated section of AWS cloud where you
  can launch AWS resources in a virtual network that you define.

* RFC 1918 defines 3 private address ranges
10.0.0.0 - 10.255.255.255 (10/8 prefix)
172.16.0.0  - 172.31.255.255 (172.16/12 prefix)
192.168.0.0 - 192.168.255.255 (192.168./16 prefix)

* Maximum addressable size of a network size is /16.
* Each subnet is mapped to a specific availability zone.
* Security groups and Network ACLs can span multiple availability zones.
* Can only have one internet gateway in a VPC.
* Network ACLs are stateless.

### Default VPC:
* AWS provides a default VPC in each region.
* All subnets in default VPC have a route out to the internet
* Each EC2 instance that is deployed in the default VPC has a private and public
  ip address.
* If you delete the default VPC, only way to restore it is to contact AWS support.

### VPC Peering:
* Allows you to connect one VPC with another via a direct network route using
  private IP addresses.
* Instances behave as if they were on the same private network.
* You can peer VPCs with other AWS accounts as well as with other VPCs in
  the same account.
* Peering is a star configuration. **No transitive peering**.

## NAT Instance and NAT Gateway:

**NAT Instances**
* When creating a NAT instance, disable source/destination check on the instance
* Always deploy NAT Gateway in the public subnet.
* Must have an Elastic IP address associated to work.
* NAT gateways must be behind a security group.
* There must be a route of the private subnet to the NAT instance in order
  for this to work.
* The amount of traffic that a NAT instance supports depends on the instance size.

**NAT Gateways**
* Scales automatically upto 10 Gbps.
* AWS manages the NAT gateways.
* Not associated with security groups
* Automatically assigned a public ip address.
* Remember to update your route table to point to the NAT gateway for traffic from private subnet to flow out the NAT gateway.


### VPC Security (Network ACL and Security Groups)
* Your VPC automatically comes with a default network ACL and by default it
  allows all outbound and inbound traffic.
* You can create a custom network ACL. By default the custom network ACL denies
  all inbound and outbound traffic until you add rules.
* Each subnet in your VPC must be associated with a network ACL. If you do not
  explicitly associate a subnet with a network ACL, the subnet is automatically
  associated with the default network ACL.
* You can associate a network ACL with multiple subnets, however a subnet can
  be associated to only one network ACL at a time.
* A network ACL contains a numbered list of rules, that is evaulated in order
  with the lowest numbered rule.
* A network ACL is stateless. It has separate inbound and outbound rules. And
  each rule can allow or deny traffic.
* When you want to explicitly deny certain traffic you have to add a rule to
  a network ACL. You cannot use a SG.

**Ephemeral Ports**
* To cover the different types of clients that might initiate traffic to   
  public facing instances in your VPC, you can open ephemeral ports
  1025-65535. However you can also add rules to your ACL to deny traffic on
  any malicious ports within that range.
* Remember to place DENY rules earlier in table than ALLOW rules that open
  the wide range of ephemeral ports.


### VPC Flowlogs:




## Databases:


* Can be categorized into two broad groups: RDBMS and NoSQL
### Relational Databases:
* Most common relational database software packages include MySQL, MariaDB,
  PostgreSQL, Microsoft SQL server and Oracle.
* RDBMS provide a common interface that lets users read and write from the
  database using SQL.
* Database --> Tables --> Rows (with columns/fields)
* Structure of the table must be defined prior to data being added to the table.
* A relational database can be categorized as either an *Online Transaction
  processing* (OLTP) or *Online Analytical Processing* (OLAP) database system.
* **OLTP**: Transaction oriented applications that are frequently writing
  and chaning data.
* **OLAP**: Typically for data warehouses and refer to reporting or analysing
  large data sets.
* Traditional RDBMS are difficult to scale beyond a single server without
  significant engineering cost.

### NoSQL Databases:
* NoSQL allows horizontal scalability on commodity hardware.
* Are non relational and do not have the same table and column semantics of
  a relational database.
* Common NoSQL databases: Hbase, MongoDB, Amazon DynamoDB, Cassandra, CouchDB,
  Riak.
* They can store large volumes of data with high transaction rate.
* Can scale horizontally across many machines for performance and fault tolerance.
*

### Amazon RDS:
* Amazon manages the maintenance of DB instances.
* There is no shell access to DB instances.
* A DB instance is an isolated database environment deployed in your private
  network segment.

## DynamoDB:















....
