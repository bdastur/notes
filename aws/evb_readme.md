# Amazon EventBridge.

EventBridge is a serverless service that uses events to connect application components
together, making it easier to build scalable event-driven applications.

EventBridge was formerly called Amazon CloudWatch Events. The default event bus and
rules you created in CW Events also display in the EVB console. EVB uses the same
CW events API, so your code that uses CW events API stays the same.


## Useful Links
* [AWS Docs - eventbridge userguide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)


Eventbridge includes two ways to process events: event buses and pipes.


**Event buses:**
* Event buses are routers that receive events and deliver them to 0 or more targets.
* Well suited for routing events from many sources to many targets
* provides optional transformation of events prior to delivery to a target.


**Pipes:**
* Pipes are intended for point-to-point integrations. Each pipe receives events
  from a single source for processing and delivery to a single target.
* Supports advanced transformations and enrichment of events prior to deliver
  to a target.



