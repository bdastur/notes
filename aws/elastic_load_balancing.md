# Elastic Load Balancing.

## Links
* [Loadbalancer FAQ](https://aws.amazon.com/elasticloadbalancing/faqs/?nc=sn&loc=5)
* [AWS NLBs and mixed up TCP connections](https://www.niels-ole.com/cloud/aws/linux/2020/10/18/nlb-resets.html)


* ELB service allows you to distribute traffic across a group of EC2 instances in one
  or more AZs within a region.
* It monitors health of it's registered targets and routes traffic only to healthy
  targets.

* ELB supports the following load balancers:
  - Application Load balancers
  - Network load balancers
  - Gateway load balancers
  - Classic load balancers

## Application Load Balancers

**Components:**

**Listener**:
* Listener checks for connection requests from clients using protocol and port you
  configure.
* Rules determine how the load balancer routes requests to it's registered targets.
* Each rule consists of a priority, one or more actions and one or more conditions.
  When the conditions for a rule are met, it's actions are performed.
* Must define a default rule for each listener, and additional rules may be defined.
* A listener can route traffic to one or more target groups.

**Target group**
* Routes requests to one ore more registered targets, such as EC2 instances,
  using protocol and port number.
* You can register a target with multiple target groups.
* Health checks are configured per target group.
* Health checks are performed on all targets registered to the TG.


* Internet facing ELB: A load balancer that takes requests from clients over
  the internet and distributes them to EC2 instances that register with the ELB.
* It receives a public DNS name that clients can use to send requests to your
  application.

* ELB in VPCs support IPV4 addresses only. In EC2 classic it supports IPV4 and
  IPV6.
* Internal ELB: as name suggest is not exposed to the web.


**Overview**
* Functions at layer 7.
* Once a request is received it evaluates listener rules in priority order.
* Routing is performed independently for each target group, even when a target
  is registered with multiple target groups.
* Default routing algorithm is round robin
* ELB scales your load balancer as traffic to your application changes over time.


## Network Load Balancers:
* Functions at layer 4 of the OSI model.
* Can handle millions of requests per second.
* When you enable AZ for the load balancer, ELB creates a load balancer node in
  that AZ.
* By default each load balancer node distributes traffic across registered targets
  in it's AZ only.
* If you enable cross-zone load balancing, each load balancer node distributes
  traffic across targets in all enabled AZs.
* Each individual TCP connection is routed to a single target for the life of
  the connection.
* A UDP flow has the same source and destination, so it's consistently routed to a
  single target throughout its lifetime.
* Different UDP flows are routed to different targets.


## Gateway Load Balancers:
* Enable you to deploy, scale and manager virtual appliances like firewalls,
  intrusion detection and prevention systems, deep packet inspection systems.
* Operates at Layer 3 of the OSI model, the network layer.
* It listens for IP packets across all ports and forwards traffic to the TG
  that's specified in the listener rule.
* It maintains stickiness of flows to specific target appliance using 5-tuple for
  TCP/UDP flows, or 3-tuple for non TCP/UDP flows.
* The GW load balancer and it's registered virtual appliance instances exchange
  traffic using GENEVE protocol on port 6081.
* Supports maximum transmission unit (MTU) size of 8500 bytes.
* GW load balancers use GW load balancer endpoints to securely exchange traffic
  across VPC boundaries.
* A Gateway Load Balancer endpoint is a VPC endpoint that provides private connectivity 
  between virtual appliances in the service provider VPC and application servers in the 
  service consumer VPC. 



## Idle connection timeout:
* For each request a client makes, the ELB maintains 2 connections.
* For each connection the ELB manages the idle timeout that is triggered when no data
  is sent over the connection for the specified time period.
* After the timeout period, the ELB closes the connection.
* Default idle timeout is 60 seconds for both connections.
* If using HTTP or HTTPS, recommendation is to use the keep-alive option for
  EC2 instances.
* You can enable keepalive in the web server settings or kernel settings of
  EC2 instance.
* To ensure that ELB is responsible for closing the connections to the instances,
  make sure that the keep alive time is greater than the idle timeout setting on the ELB.

* Cross zone load balancing: ensures that request traffic is routed evenly
  across all back end instances regardless of AZ.


## X-Forwarded-For Header.
* This request header is automatically added and helps you identify the IP address
  of a client when using an HTTP or HTTPS load balancer.













