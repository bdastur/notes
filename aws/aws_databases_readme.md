# AWS Databases.

## Useful links
* [Introducing Aurora engine](https://aws.amazon.com/blogs/database/introducing-the-aurora-storage-engine/)
* [Amazon Aurora-Under the hood](https://aws.amazon.com/blogs/database/amazon-aurora-under-the-hood-quorum-and-correlated-failure/)
* [Dynamodb Getting started](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html)
* [DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)



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

* *OLTP*: Transaction oriented applications that are frequently writing and
          changing data.

* *OLAP*: Typically for data warehouses and refer to reporting or analyzing
          large data sets.

* Traditional RDBMS are difficult to scale beyond a single server without
  significant engineering cost.

### Relational databases on AWS:
 * SQL Server
 * Oracle
 * MySQL
 * Aurora
 * PostgresSQL
 * MariaDB.

### Key Features:
 * Multi-AZ for Disaster recovery
 * Read Replicas - for performance

### Backup and Recovery
*Two different types of backups for RDS:*
 * Automated Backups
 * Database Snapshots

*Automated Backups*
* Allow you to recover your DB to any point in time within a "retention period".
* The retention period can be between 1 and 35 days.
* Automated backups will take a full daily snapshot and will store transaction logs
  throught the day.
* For recovery, AWS will first choose the most recent daily backup and then apply
  the transaction logs relevant to that day. This allows 'a point in time' recovery
  down to a second, within the retention period.
* Automated Backups are enabled by default. Backup data is stored in S3. You get
  free storage space equal to the size of your database.
* Storage I/O may be suspended during backup window, may experience elevated latency.

*Database Snapshots*
- DB snapshots are done manually (user initiated).
- They are stored even after the RDS instance is deleted (unlike automated backups).

* Whenever you restore either an Automated backup or a manual snapshot, the restored
  version of the DB will be a new RDS instance with a new DNS endpoint.

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
* Amazon RDS is often used for OLTP workloads, but it can also be used for OLAP.
* *Amazon Redshift* is a high performance data warehouse designed specifically for
  *OLAP* use cases.
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
* Offers enterprise grade commercial database technology while offering the
  simplicity and cost effectiveness of an open source database.
* Re-designed internal components of MySQL to take more service oriented approach.
* MySQL compatible, and provides increased reliability and performance over
  standard MySQL deployments.
* Can deliver up to 5 times the performance of MySQL.
* When you first create an Amazon Aurora instance, you create a DB cluster.
* A DB cluster has one ore more instances and includes a cluster volume that manages
  the data for those instances.
* A cluster volume is a virtual database storage volume that spans multiple AZ.
* Aurora automatically maintains 6 copies of your data across 3 AZs, with each
  AZ having a copy of the cluster data.
* Aurora DB cluster consist of two types of instances:
  - **Primary Instance**:
    * This is the main instance which supports read and write workloads.
    * Each Amazon Aurora has one primary instance.

  - **Amazon Aurora Replica**:
    * This is a secondary instance that supports only read operations.
    * Each DB cluster can have up to *15* Amazon Aurora Replicas in addition to
      a primary instance.
    * Helps increase performance by distributing the read workloads among various
      instances.
    * You can locate your Aurora replicas in multiple AZs to increate DB availability.

* *Aurora Serverless* - provides a simple cost effective option for infrequent,
  intermittent or unpredictable workloads.

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
  * Defined as the maximum period of data loss that is acceptable in the event of
    a failure or incident.

* *Recovery Time Objective (RTO)*:
  * Defined as the maximum amount of downtime that is permitted to Recovery from
    backup and to resume processing.

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
* RDS allows you to recover your DB quickly from automated or manual DB snapshots.
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
* Provides HA and failover suppport for DB instances using Multi-AZ deployments.
* RDS automatically provisions and maintains a synchronous standby replica in
  a different AZ.
* The primary DB instance is synchronously replicated across AZs to a standby
  replica to provide data redundancy, eliminate I/O freezes, and minimize
  latency spikes during system backups.
* RDS can handle planned or unplanned outages to the DB instance. RDS
  automatically switches to a standby replica in another AZ.
* Available for SQL Server, Oracle, MySQL Server, PostgresSQL, MariaDB.
* You can force a failover from on AZ to another, by rebooting the RDS instance.
* There is no charge associated to replicating data between AZs for your multi-az
  deployment.
* DB instances using multi-az DB deployments can have increased write and commit
  latency compared to single AZ deployments.
* Failover tiems from active to standby are typically 60 - 120 seconds.


### Read Replicas:
* Can be Multi-az.
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
* Can be promoted to master. This will break the read replica.

* Available for:
  - Mysql, postgres, mariadb, oracle, Aurora


#--------------------------------------------------------------------
## DynamoDB
#--------------------------------------------------------------------
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
* Data is stored on SSD.
* Spread across 3 geographically distinct datacenters.

*Two types of read models:*
 - Eventual consistent reads (default)
 - Strongly consistent reads

### Data Model:
* Main components of DynamoDB are:
  * Tables:
    DynamoDB stores data in tables.

  * Items:
    * Each table contains multiple items. An item is a group of attributes that
      is uniquely identifiable. For E.g in a people table each item represents
      one person.
    * There is no limit on the number of items you can store in a table.

  * Attributes:
    * An attribute in DynamoDB is similar to fields or columns in other
      databases.
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
      function. The output from the hash function determines the partition
      where the item is stored.
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
* Allow you to search a large table efficiently and avoid an expensive
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


## DynamoDB Advanced Features:

### DynamoDB Accelerator (DAX)
* Fully managed, highly available in-memory cache
* 10x performance improvement
* Reduces request time from milliseconds to microseconds - even under load
* No need for developers to manage caching loic
* Compatible with DynamoDB API calls.

### Transactions
* DynamoDB transactions provide atomicity, consistency, isolation, and
  durability (ACID) across one or more tables within a single AWS account
  and region.
* You can use transactions when building apps that require coordinated inserts,
  deletes, or updates to multiple items as part of a single logical business operation.
* Examples of these type of operations are financial transactions,
  fulfilling orders.
* Two underlyin reads or writes - prepare/commit
* Transactions can operate on up to 25 items or 4 MB of  data.

### On-Demand Capacity
* Provides Pay-per-request pricing.
* No charge for read/write - only storage and backups.
* Pay more per request than with provisioned capacity

### Backup and Restore.
* Full backups at any time
* Zero impact on table performance or availability
* Consistent within seconds and retained until deleted.
* Operates within the same region as the source table.

### Point-in-Time Recovery (PITR)
* Protects against accidental writes or deletes.
* Restores to any point in the last 35 days
* Incremental backups
* Not enabled by default.

### Streams
* Time-ordered sequence of item-level changes in a table.
* Stored for 24 hours.
* Provides a stream of inserts, updates and deletes to the table items.
* Stream contains stream record - A stream records represents a single data
  modification in the table.
* Each stream record is assigned a seq number reflecting the order
* Stream records are organized in to groups or shards.

### Global tables
* Managed multi-maaster, multi-region replication.
* Based on DynamoDB streams
* Multi-region redundancy for DR or HA
* No appliacation rewrites
* Replication latency under one second.




#---------------------------------------------------------------------
## Amazon Redshift:
#---------------------------------------------------------------------
* Fast powerful, fully managed petabyte scale data warehouse service
* Relational database designed for *OLAP* scenarios.
* Optimized for high performance analysis and reporting very large datasets.
* Uses standard SQL commands to query large datasets.
* Start at just 0.25$ per hour with no commitments or upfront cost.
* Scale to a petabyte or more for $1000 per terrabyte per year.
* Backup enaabled by default wiith a 1 day retention period - Max of 35 days.
* Redshift always attempts to maintain at least three copies of your data (
  the original and replica on compute nodes and a backup in S3)

#---------------------------------------------------------------------
## ElastiCache:
#---------------------------------------------------------------------
* Improves application performance by storing the most frequently accessed
  data in memory.
* Simplifies the setup and management of distributed in-memory caching
  environments.
* You can choose from Memcached or Redis protocol-compliant cache engine and
  quickly launch a cluster within minutes.

### Memcached vs Redis

||          Requirement      || Memcached || Redis ||
|Simple cache to offload DB   | yes | yes |
|Ability to scale horizontally| yes | yes |
|Multi-threaded performance   | yes | No  |
|Advanced data types          | no  | yes |
|Ranking/Sorting data sets    | no  | yes |
|Pub/Sub capabilities         | no  | yes |
|Persistence                  | no  | yes |
|Multi-AZ                     | no  | yes |

#### Memcached
* Provides a simple interface that allows you to write and read objects into
  in-memory key/value data stores.
* You can elastically grow and shrink a cluster of memcached nodes to meet
  your demands.
* You can partition your cluster into shards and parallelize operations for
  very high performance throughput.


#### Redis
* Beyond the object support provided in Memcached, Redis supports a rich
  set of data types like strings, lists and sets.
* Unlike Memcached, Redis supports the ability to persist the in-memory data
  on to disks. This allows creating snapshots that backup data and then
  recover or replicate from the backups.
* It can support up to 5 read replicas to offload read requests. In the event
  of a primary node failure, a read replica can be promoted to become the new
  master using multi AZ replication groups.
* Redis also has advanced features that make it easy to sort and rank data.

### Nodes and Clusters
* Each deployment of ElastiCache consists of one or more nodes in a cluster.
* A single Memcached cluster can contain upto 20 nodes.
* Redis clusters are always made up of a single node; however multiple
  clusters can be grouped into a Redis replication group.
* For Memcached clusters ElastiCache supports Auto Discovery with the provided
  client library.

### Backup and Recovery
* Redis allows you to persist your data from in-memory to disk and create a snapshot.
* Each snapshot is a full clone of the data that can be used to recover to a
  specific point in time.
* Snapshots CANNOT be created for Memcached engine because it is purely
  in-memory key/value store and always starts empty.
* Taking snapshot can have performance impact, and best practice is to create
  a replication group and perform a snapshot against a read replica instead of
  a primary node.

### Access Control:
* Access to ElastiCache cluster is controlled primarily by restricting inbound
  network access to your cluster, using security groups.
* Access to manage the configuration of the cluster is controlled by IAM policies.


## AWS Database Migration Service (DMS):
* Makes it easy to migrate relational databses, data warehouses, NoSQL
  databases and other types of data stores.
* Can migrate data into AWS between on-prem instances or between combination
  of cloud and on-prem.
* Supports homogenous and hetrogenous migration. Eg orcale DB on prem to
  Oracle DB RDS, or SQL Server on prem to Amazon Aurora


## Caching strategies on AWS
* Cloudfront.
* API Gateway
* ElastiCache
* Dynamodb Accelerator (DAX)


## Amazon Elastic Map Reduce (EMR):
* Fully managed on-demand Hadoop framework.
* When you launch an EMR cluster you specify:
  * Instance type
  * Number of nodes in the cluster
  * Version of Hadoop to run
  * Additional tools or applications like Hive, Pig, Spark or Presto.

* EMR node types:
 * *Master node*:
   - A node that maanages the cluster. It tracks the status of tasks and
     monitors the health of the cluster.
   - Every cluster has a master node.

 * *Core node*:
   - Runs tasks and stores data in HDFS on the cluster.
   - Multi-node clusters have atleast 1 core node.

 * *Task node*:
   - Runs tasks and does not store data in HDFS.
   - Task nodes are optional.

* You can configure replication to S3 on 5 min intervals for all log data
  from master node. (Only configured when creating the cluster)

* Storage types when using EMR:
**Hadoop Distributed File System (HDFS)**
* Standard file system that comes with hadoop.
* All data is replicated across multiple instances for durability
* Can use instance storage or EBS.

**EMR File System (EMRFS)**
* Is an implementation of HDFS that allows clusters to store data on S3.
* You get durability and low cost while preserving your data even if the
  cluster shuts down.
* Key factor is whether cluster is persistent.

* For persistent clusters HDFS is appropriate.

* For some use cases like big data workloads, which are run infrequently it
  can be cost effective to turn off the cluster when not in use.
* These are called **transient clusters**.
* EMRFS is well suited for such clusters as data persist independent of the
  lifecycle of the cluster.

* Use cases:
  * Log processing: large number of unstructured logs to get useful insights.
  * Clickstream analysis: to segment users and understand user preferences.
  * Genomics and life sciences: Process vas amounts of genomic data and
    other large scientific datasets quickly and efficiently.







