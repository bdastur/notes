# Cloudwatch:



## Cloudwatch Log Insight:


### Cloudtrail Queries

---
Find the 20 most recently added log events.

```
  fields @timestamp, @message 
  | sort @timestamp desc 
  | limit 20
```

----

Find the 20 most recently added log events. Skippingg kms events.

```
fields @timestamp, @message
| filter eventSource != "kms.amazonaws.com"
| sort @timestamp desc
| limit 20
```

---
Find the number of log entries for each service, event type, and AWS Region.

```
stats count(*) by eventSource, eventName, awsRegion
```

---
Find the number of log entries for each service and event type.

```
stats count(*) by eventSource, eventName
```

---
Find the number of log entries , group by 1 hour

```
stats count(*) by bin(1hr)
```

---
Find all API calls which failed due to 'AccessDenied' error.

```
 stats count(*) by bin(1hr)                                          
| filter ispresent(errorCode) and errorCode =~ "AccessDenied"
```

---
Find failed API calls that failed for reasons other than 'AccessDenied'

```
fields @timestamp, @message                                          
| filter ispresent(errorCode) and errorCode != "AccessDenied"
```


---
Number of ec2 events per hour

```
stats count(*) by bin(1h), eventSource                                         
| filter eventSource =~ "ec2.amazonaws.com"
```

### VPC Flowlogs insight

---
${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}


```
stats sum(packets) as packetsTransferred by srcAddr, dstAddr, dstPort
    | sort packetsTransferred  desc
    | filter dstPort =~ "2379"
    | limit 15
```

```
stats sum(packets) as packetsTransferred by bin(1h) as Timestamp, srcAddr, dstAddr, dstPort
| sort @timestamp desc
| limit 10
```



```
stats sum(packets) as packetsTransferred by bin(1h), srcAddr, dstAddr, dstPort
| filter dstAddr =~ "10.208.22.134" or dstAddr =~ "10.208.151.200"
| limit 50
```

```
fields @timestamp, srcAddr, srcPort, dstAddr, dstPort,  protocol
| filter dstAddr =~ "10.208.22.134" or dstAddr =~ "10.208.151.200"
| sort @timestamp desc
| limit 50
```




