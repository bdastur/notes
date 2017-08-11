# AWS Notes:


## IAM

### Links:

https://aws.amazon.com/blogs/security/new-attach-an-aws-iam-role-to-an-existing-amazon-ec2-instance-by-using-the-aws-cli/?sc_channel=sm&sc_campaign=rolesforrunninginstances&sc_publisher=tw&sc_medium=social&sc_content=read-post&sc_country=global&sc_geo=global&sc_category=ec2&sc_outcome=launch




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

**Links:**
http://docs.aws.amazon.com/amazondynamodb/latest/gettingstartedguide/quick-intro.html

http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GuidelinesForTables.html

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
    * An attribute in DynamoDB is similar to fields or colums in other
      databases.
    * Each item is composed of one ore more attributes. An attribute is a
      fundamental data element that does not need to be broken down further.

  * Primary Key:
    * When you create a table, in addition to the table name, you must specifically
      the primary key of the table.
    * A primary key in DynamoDB uniquely identifies each item in the table,
      so that no two items can have the same key.
    * When you add update or delete an item from a table you must specifically
      the primary key attribute values for that item.

    DynamoDB supports two types of primary keys:

    **Partition Key**:
    * A simple primary key, composed of one attribute known as the partiton key.
    * DynamoDB uses the partiton key's value as input to an internal hash function.
      The output from the hash function determines the partition where the item is
      stored.
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
* Sets do not gurantee order.

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
* You can use Amazon cloudwatch to monitor your DynamoDB capacity and make
  scaling decisions.

### Secondary Indexes:
* You can optionally define one or more secondary indexes on a table, along with
  the partiton key and sort key.
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
* GetItem action can be used retrive an item. Primary key is required for this
  action.
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
* A read request immediately a write operation might not show the latest

### Strongly Consistent Reads:
* Applications might need to guarantee that the data latest, in which case it
  can use strongly consistent reads. DynamoDB returns a response with the
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
* Each request can return upto 1MB of data.
* This can be resource intensive.
*
#### Query:
* Query is the primary search operation to find item in a table or a
  secondary index using only primary key attribute values.
* Results are automatically sorted by the primary key and are limited to 1MB.

### Scaling and Partitioning:
* A DynamoDb table can scale horizontally using partitions to meed the storage
  and performance needs of the applications.
* Each individual partition represents a unit of compute and storage capacity.
* A single DynamoDb partition can support a maximum of 3000 read capacity
  units or 1000 write capacity units. It can hold approximately 10GB of data.
* To achive the full amount of request throughput provisioned for a table,
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
* To keep track of changes to DynamDb.
* Can get a list of item modifications for the last 24 hour period.
* Each stream record represents a single data modification in the DynamDb table
  to which the stream belongs.
* Each stream record is assigned a sequence number, reflecting the order in
  which the record was published to the stream.

## Simple Queue Service (SQS)
* A fast, reliable, scalable and fully managed queuing service.
* Makes it simple and cost effective to decouple components of your cloud
  application.
* Does not guarantee message delivery order (no FIFO)
* If message order is required applications can handle that by passing a
  message sequence id.
* Ensures delivery of each message at least once and supports multiple
  readers and writers interacting with the same queue.

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
* SQS supports up to 12 hours max visibility timeout.
* SQS automatically deletes messages that have been in the queue for more than
  maximum message retention period.
* Shortest message retention period is 60 seconds.
* Default message retention period is 4 days.
* Longest message retention period is 14 days.


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
* A queue that other queus can target to send messages that for some reason
  could not be successfully processed.
* Ability to sideline and isolate unsuccessfully processed messages.

### Access Control:
* IAM policies to grant specific instructions.



## Simple Workflow Service (SWF):


## Simple Notification Service (SNS):



## ElastiCache:
* Improves application performance by storing the most frequently accessed
  data in memory.
* Simplifies the setup and management of distributed in-memory Catching
  environments.
* You can choose from Memcached or Redis protocol-compliant cache engine and
  quickly launch a cluster within minutes.

### Cache Engines:

#### Memcached
* Provides a simple interface that allows you to write and read objects into
  in-memory key/value data stores.
* You can elastically grow and shrink a cluster of memcached nodes to meet
  your demands.
* You can partition your cluster into shards and parallelize oprations for
  very high performance throughput.


#### Redis
* Beyond the object support provided in Memcached, Redis supports a rich
  set of data types like strings, lists and sets.
* Unlike Memcached, Redis supports the ability to persist the in-memory data
  on to disks. This allows you to create snapshots that backup data and then
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
* Redis allows you to persist your data from in-memory to disk and create a
  snapshot.
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


## CloudFront:
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
* You start by creating a distribution, which is identified by a DNS domain
  name like 'd11223233.cloudfront.net'.
* To serve files from CloudFront, you simply use the distribution domain name
  in place of your website's domain name. Rest of the file path stays the same.
* You can also create a CNAME record in Route53 for DNS.

#### Origins
* You must specify the DNS domain name of the origin - S3 bucket or HTTP server.

#### Cache control
* Once requested and served from the edge location, objects stay in the Cache
  until they expire or are evicted to make room for more frequently reqeusted
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











....
