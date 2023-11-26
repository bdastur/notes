# Simple Queue Service.

## Useful Links
* [SQS CW Metrics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html)


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

## Message Lifecycle.
1. (Producer) sends message (A) to the qeue. The message is redundandly distributed
  across the SQS servers.
2. (Consumer) retrieves the message from the queue and message (A) is retured. While
   message (A) is being processed, it remains in the queue and is not retured to
   subsequent receive requests for the duration of the visibility timeout.
3. (Consumer) deletes message (A) from the queue to prevent the message from being
   received and processed again after the visibility timeout expires.

## Delay queues and visibility timeouts.

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

**Message States**
An SQS message has three basic states:
1. Sent to a queue by a producer.
* This message is considered '*stored*' after it is sent to a queue by a producer, but
  not yet received from the queue by a consumer.
* There is no quota on stored messages (unlimited stored messages)

2. Received from the queue by a consumer.
* A message is considered 'in *flight*' after it is received by a consumer, but not yet
  deleted from the queue.
* There is a quota on inflight messages. A max of 120,000 messages can be inflight.

3. Deleted from the queue.
* A message is deleted by the consumer after processed.

* SQS returns OverLimit error if the quotas are exceeded.

## Queue operations, unique ids and metadata
* Some SQS operations:  CreateQueue, ListQueues, DeleteQueue, SendMessage,
  SendMessageBatch, ReceiveMessage, DeleteMessage.
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

## Short & Long polling:
* SQS provides short and long polling to receive messages from a queue. (Default is
  using short polling)
**Short Polling**
* ReceiveMessage request queries only a subset of servers to find messages that
  are available to include in the response. SQS sends the response right away, even
  if the qeury found no messages.
* Subsequent request might return your messages.

**Long Polling**
* With Longpolling to set a WaitTimeSeconds when invoking the ReceiveMessages.
* RecieveMessage request queries all the servers for messages. SQS sends a response
  after it collects atleast one available message, up to a maximum number of messages
  specified in the request. It only returns empty if the wait time expires.
* WaitTimeSeconds can be between 0 - 20 seconds.
* If there is no message in the queue the call will wait up to WaitTimeSeconds
  for a message before returning.
* If a message appears before the time expires, the call will return with the
  message right away.

## Dead Letter Queues:
* A queue that other queues can target to send messages that for some reason could
  not be successfully processed (consumed).
* Ability to sideline and isolate unsuccessfully processed messages.
* You can use deadletter queue redirve capability to move messages back to the
  source queue.

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











