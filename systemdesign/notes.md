# System Design & Architecture notes.


## Useful links
* [System design primer](https://github.com/donnemartin/system-design-primer)



## CAP Theorem.

Also known as Brewer's theorem. It states that any distributed data store can only
provide two of the following three gurantees:
* Consistency
Every read receives the most recent write or an error.

* Availability
Every request receives a (non-error) respose, without the gurantee that it contains
the most recent write.

* Partition tolerance
The system continues to operate despite an arbitar number of messages being dropped
(or delayed) by the network between nodes.


