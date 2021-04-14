# AWS Databases.

## Useful links
* [Introducing Aurora engine](https://aws.amazon.com/blogs/database/introducing-the-aurora-storage-engine/)
* [Amazon Aurora-Under the hood](https://aws.amazon.com/blogs/database/amazon-aurora-under-the-hood-quorum-and-correlated-failure/)

* Can be categorized into two broad groups:
  - RDBMS (Relational Database Management Systems)
  - NoSQL (Non relational databases)


## Relational databases:
* Most common relational database software packages include MySQL, MariaDB,
  PostgreSQL, Microsoft SQL server and Oracle.
* RDBMS provide a common interface that lets users read and write from the
  database using SQL.
* Database --> Tables --> Rows (with columns/fields)
* Structure of the table must be defined prior to data being added to the table.

* A relational database can be categorized as either:
  - *Online Transaction processing* (OLTP) or
  - *Online Analytical Processing* (OLAP)
  database system.
* *OLTP*: Transaction oriented applications that are frequently writing
  and changing data.

* *OLAP*: Typically for data warehouses and refer to reporting or analyzing
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


## Amazon RDS (OLTP)
* Amazon RDS is often used for OLTP workloads, but it can also be used for
  OLAP.
* Amazon Redshift is a high performance data warehouse designed specifically for
  OLAP use cases.
* Amazon manages the maintenance of DB instances.
* There is no shell access to DB instances.
* A DB instance is an isolated database environment deployed in your private
  network segment.

### Database Instances:
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

### Licensing:
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


* Amazon RDS supports Microsoft SQL Server Enterprise edition and the license is
  available *only* under the BYOL model.

### Amazon Aurora:
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


### Storage options:

*General Purpose SSSD*:
* Deliver single digit millisecond latencies and burst to 3,000 IOPS for
  extended periods.
* Baseline perfformance is determined by volume's size.
* MariaDB, Mysql and postgress DB instances: 20 GiB - 64 TiB
* SQL server   20 GiB - 16 TiB
* Baseline I/O performance is 3 IOPS/1 GiB , minimum of 1000 IOPS.
* Larger volume size gives better performance.

Burst duration = (credit balance) / (burst IOPS) - 3 x (storage size in GiB)


*Provisioned IOPS*
* Designed to meet needs of I/O intensive workloads, requiring low latency and
  consistent I/O throughput.

*Magnetic*
* Supports this storage class for backward compatability


### Backup and Restore
* *Recovery point Objective (RPO)*:
  * Defined as the maximum period of data loss that is acceptable in the
    event of a failure or incident.

* *Recovery Time Objective (RTO)*:
  * Defined as the maximum amount of downtime that is permitted to Recovery
    from backup and to resume processing.

* For large databases, it can take hours to restore from a full backup.
* In the event of failure, you can reduce your RTO to minutes by failing over
  to secondary node.

#### Automated Backups
* Automated backups allow you to recover your databases to any point in time
  within a "retention period".
* Retention period can be between 1 and 35 days.
* backup data is stored in S3 and you get free storage space equal to the
  size of your DB.
* If you don't set the backup retention period, default retention period is
  *1 day* (if you create the DB instance using  API or CLI).
* Default backup retention period is *7 days* if using AWS console.
* Setting backup retention period to 0 disables automaated backups.

* When you delete a DB instance, all automated backup snapshots are deleted
  and cannot be recovered.
* You can choose to retain automated backps during DB instance deletion.
* Retained backups contain system snapshots, transaction logs from DB instance.
* Also include DB instance properties like allocated storage, DB instance class,
  required to restore it to an active state.

* Manual snapshots are not deleted when a Db instance is deleted.

#### Manual DB snapshots
* Manual DB snapshots are not deleted when you delete the Db instance.

#### Recovery:
* RDS allows you to recover your DB quickly from automated or manual DB
  snapshots.
* You cannot restore from a Db snapshot to an existing DB instance. A new
  DB instance is created when you restore.
* When you restore a DB instance, only the default DB parameter and SG are
  associated with the restored instance.
* When using automated backups, RDS combines the daily backups performed
  during your maintenance window in conjunction with transaction logs, to
  enable you to restore your DB instance to any point during your retention
  period, typically up to last 5 minutes.

### Encryption at rest:
* Supported for MySQL, Oracle, SQL Server, Postgres, MariaDB & Aurora.
* Done using AWS KMS service.
* Once your RDS instance is encrypted, the data stored at rest is encrypted,
  as are it's automated backups, read replicas and snapshots.

### High availability (Multi-AZ)
* Provides HA and failover suppport for DB instances usin Multi-AZ deployments.
* RDS automatically provisions and maintains a synchronous standby replica in
  a different AZ.
* The primary DB instance is synchronously replicated across AZs to a standby
  replica to provide data redundancy, eliminate I/O freezes, and minimize
  latency spikes during system backups.
* RDS can handle planned or unplanned outages to the DB instance. RDS
  automatically switches to a standby replica in another AZ.


### Read Replicas:
* Reduces load on primary DB instance by routing read queries to special
  DB instances called read replicas.
* Servers read traffic when source DB instance is unavailable.
* Must have automatic backups turned on in order to deploy a read replica.
* Can have up to 5 RR copies of any database.
* You can have read replicas of read replicas (watch out for latency)
* When you create a read replica, RDS takes a snnapshot of the source instance
  and creates a RO instance from the snapshot.
* You can only create a read replica from an existing DB instance.
* RDS uses asynchronous replication method for the DB engine to update the
  read replica whenever there is a change to primary DB instance.

* Available for:
  - Mysql, postgres, mariadb, oracle, Aurora


















