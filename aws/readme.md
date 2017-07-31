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
* Remember to update your route table to point to the NAT gateway for traffic
  from private subnet to flow out the NAT gateway.


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
* Can be categorized into two broad groups:
  - RDBMS (Relational Database Management Systems)
  - NoSQL (Non relational databases)

### Relational Databases:
* Most common relational database software packages include MySQL, MariaDB,
  PostgreSQL, Microsoft SQL server and Oracle.
* RDBMS provide a common interface that lets users read and write from the
  database using SQL.
* Database --> Tables --> Rows (with columns/fields)
* Structure of the table must be defined prior to data being added to the table.

* A relational database can be categorized as either:
  -  *Online Transaction processing* (OLTP) or
  - *Online Analytical Processing* (OLAP)
  database system.
* **OLTP**: Transaction oriented applications that are frequently writing
  and changing data.
* **OLAP**: Typically for data warehouses and refer to reporting or analyzing
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
* Amazon DynamoDB is an example of NoSQL Db service.
* A common use case for NoSQL is managing user session state, user profiles,
  shopping cart data or time series data.

### Amazon RDS:
* Amazon RDS is often used for OLTP workloads, but it can also be used for
  OLAP.
* Amazon Redshift is a high performance data warehouse designed specifically for
  OLAP use cases.
* Amazon manages the maintenance of DB instances.
* There is no shell access to DB instances.
* A DB instance is an isolated database environment deployed in your private
  network segment.

#### Database Instances:
* CreateDBInstance API to create new DB Instance.
* ModifyDBInstance API to modify existing DB instance.
* Can contain multiple different databases, all of which you can create and
  manage within the DB instance using SQL commands.
* DB parameter group: To manage common configuration settings, that can be
  applied to one or more DB instances.
* DB option group: acts as a container for engine features, which is empty by
  default.
 * You can modify your DB instance while it is running to scale up/down the
   instance type, size of Db etc.

#### Database Engines:
**MySQL**:
**PostgreSQL**:
**MariaDB**:
**Oracle**:
**Microsoft SQL Server**:

#### Licensing:
* Amazon RDS Oracle and Microsoft SQL Server are commercial software products
  that require appropriate licenses to operate in the cloud.
* Two licensing models:
  - License Included
  - Bring your own license (BYOL)

* License Included:
  * The license is held by AWS and is included in the RDS instance price.
  * For Oracle license included provides license for Standard Edition one.
  * For SQL Server, license provides licensing for SQL Server Express Edition,
    Web Edition and Standard Edition.

* Bring Your Own License (BYOL):
  * You must provide the appropriate Oracle DB license
  * You are responsible for tracking and managing licenses.

#### Amazon Aurora:
* Offers enterprise grade commercial database technology while offering
  the simplicity and cost effectiveness of an open source database.
* Re-designed internal components of MySQL to take more service oriented approach.
* MySQL compatible, and provides increased reliability and performance over
  standard MySQL deployments.
* Can deliver up to 5 times the performance of MySQL.
* When you first create an Amazon Aurora instance, you create a DB cluster.
* A DB cluster has one ore more instances and includes a cluster volume that
  manages the data for those instances.
* A cluster volume is a virtual database storage volume that spans multiple
  AZs, with each AZ having a copy of the cluster data.
* Aurora DB cluster consist of two types of instances:
  - **Primary Instance**:
    * This is the main instance which supports read and write workloads.
    * Each Amazon Aurora has one primary instance.

  - **Amazon Aurora Replica**:
    * This is a secondary instance that supports only read operations.
    * Each DB cluster can have up to 15 Amazon Aurora Replicas in addition to
      a primary instance.
    * Helps increase performance by distributing the read workloads among various
      instances.
    * You can locate your Aurora replicas in multiple AZs to increate DB availability.

#### Storage Options:
* Can scale up to 4 to 6 TB in provisioned storage and upto 30,000 IOPS.
* Three types:
  - Magnetic
    * Also called standard storage
    * cost effective storage for light IO requirements.

  - General purpose SSD
    * Also called gp2.
    * Can provide faster access than magnetic storage.
    * Can provide burst performance and ideal for small to medium sized DBs.

  - Provisioned IOPS (SSD)
    * High I/O intensive workloads, sensitive to storage performance and
      consistency in random access I/O throughput.

#### Backup and Recovery:
* Recovery point Objective (RPO):
  * Defined as the maximum period of data loss that is acceptable in the
    event of a failure or incident.

* Recovery Time Objective (RTO):
  * Defined as the maximum amount of downtime that is permitted to Recovery
    from backup and to resume processing.

* For large databases, it can take hours to restore from a full backup.
* In the even of failure, you can reduce your RTO to minutes by failing over
  to secondary node.

#### Automated Backups:
* RDS feature that continuously tracks changes and backs up your database.
* Amazon RDS creates a storage volume snapshot of your DB instance, backing
  up entire DB instance and not just individual databases.
* You can set a backup retention period when you create a Db instance.
* One day of backup is retained by default, but you can modify to a max of
  35 days.
* When you delete a DB instance, all automated backup snapshots are deleted
  and cannot be recovered.
* Manual snapshots are not deleted when a Db instance is deleted.

#### Manual DB snapshots
* Manual DB snapshots are not deleted when you delete the Db instance.

#### Recovery:
* RDS allows you to recover your DB quickly from automated or manual DB
  snapshots.
* You cannot restore from a Db snapshot to an existing DB instance. A network
  DB instance is created when you restore.
* When you restore a DB instance, only the default DB parameter and SG are
  associated with the restored instance.
* When using automated backups, RDS combines the daily backups performed
  during your maintenance window in conjunction with transaction logs, to
  enable you to restore your DB instance to any point during your retention
  period, typically upto last 5 mintues.


#### HA with Multi AZ Deployment:
* You can select Multip AZ Deployment as an option when creating a DB instance.
* Primary instance is created in one AZ, while a secondary instance is created
  in another AZ.
* RDS automatically replicates data from master Db to slave Db using
  synchronous replication.
* RDS detects and automatically recovers from the most common failure scenarios.
* RDS performs an automatic failover in following cases:
  * Loss of availabilityin primary AZ.
  * Loss of network connectivity to primary db.
  * Compute unit failure on primary DB.
  * Storage failure on primary db.

#### Scaling Up and Out:
**Vertical Scaling**:
* By changing your DB instance type to a higher compute, memory or storage type.
* RDS automates the migration process to a new class with only a short
  disruption.
* Each Db instance can scale from 5GB up to 6 TB in provisioned storage depending
  on the storage type and engine.
* Storage expansion is supported for all Db engines except **SQL Server**.

**Horizontal Scaling**:
  **Partitioning**:
    * Partitioning a large relational database into mu,tiple instances or shards
      is a common technique for handling more requests beyond the capabilities
      of a single instance.
    * Requires additional logic in the application layer. Application needs to
      decide how to route DB request to the correct shard.
    * NoSQL Databases like DynamoDB and Cassandra are designed to scale horizontally.

  **Read Replicas**:
  * Offload read transactions from the primary database to increase the
    overall number of transactions.
  * Supported in RDS for MySQL, PostgreSQL, MariaDB and Aurora.
  * RDS uses the MySQL, MariaDB and PostgreSQL DB engines built-in replication
    functionality to create a special type of DB instance, called a read replica
    from a source DB instance.
  * Updates to the primary DB instance are asynchronously copied to the read
    replica.

#### Security:
* Deploy RDS instance in private subnet within a VPC.
* Network ACLs and Security groups to restrict access from certain networks only.
* DB level access control with users with strong passwords that are rotated
  frequently.
* Encryption.

## Amazon Redshift:
* Fast powerful, fully managed petabyte scale data warehouse service
* Relational database designed for OLAP scenarios.
* Optimized for high performance analysis and reporting very large datasets.
* Uses standard SQL commands to query large datasets.


### Clusters and Nodes:





## DynamoDB:
* A fully managed NoSQL database service that provides fast and low latency
  performance that scales with ease.
* Amazon DynamoDB can provide consistent performance levels by automatically
  distributing data and traffic for a table over multiple partitions.
* DynamoDB will automatically add enough infrastructure capacity to supported
  the requested throughput levels.
* You can adjust the read/write capacity after the table is created as well.
  DynamoDB will adjust the internal Partitioning accordingly.
* DynamoDB provides HA and durability by replicating data across multiple AZs
  within an AWS Region.
  














....
