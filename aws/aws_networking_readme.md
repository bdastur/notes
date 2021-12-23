# AWS Advanced Networking:

## Links
* [Amazon VPC Limits](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html)
* [Interactive IP add & CIDR Range visualizer](https://cidr.xyz/)
* [VPC Introduction](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html)
* [VPC Documentation](https://docs.aws.amazon.com/vpc/index.html)                    
* [VPC Invalid peering configs](https://docs.aws.amazon.com/vpc/latest/peering/invalid-peering-configurations.html#transitive-peering)


## IP Addressing and Subnets:

* [Cisco IP Addressing/Subnetting Tutorial](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
* [Decimal to Binary converter](https://www.rapidtables.com/convert/number/decimal-to-binary.html)


## Networking with VPC:

* In AWS VPC is the core networking component.
* It serves as private layer 2 isolated network layer
* VPC is the main environment that provides logical network isolation and
  grouping of resources such as EC2, ECS and other AWS services.

* VPC CIDR range (/28 (16 ip addresses) - /16 (65536 ip addresses))
* Addressing in VPC defaults to IPV4, but IPV6 and dual stacks can run in the VPC
  if required.

* Provisioning in VPC is irreversible - once provisioned it cannot be changed.
* Considerations - some services running in the VPC are reserved by AWS - eg:
  IP address will be consumed by internet gateway, DHCP service, NAT gateway,
  and reserved addresses AWS keeps unused for future services.
* Default limit for Amazon VPCs in a region is 5.
* Each subnet is mapped to a specific AZ. 
* Security groups and Network ACLs can span multiple AZs.
* When you create a VPC, all subnets within the VPC can communicate with each other
  by default.
* The first 4 ip addresses and last ip address **in each subnet CIDR block** is reserved,
  not available to use:
  - 10.0.0.0   == Network address
  - 10.0.0.1   == Reserved by AWS for the VPC router
  - 10.0.0.2   == Reserved by AWS for DNS
  - 10.0.0.3   == Reserved by AWS for future use.
  - 10.0.0.255 == Network broadcast address. We do not support broadcast VPC, hence
                  we reserve this address. 

## VPC Components:
* Subnets
* Route tables
* DHCP option set
* Security groups
* Network ACLs
And following optional components:
* IGW
* EIP address
* ENI (Elastic network interface)
* Endpoints
* Peering
* NAT instances and NAT gateway
* VPC, customer gateways and VPNs.

* IPsec is the security protocol supported by VPC.

### Private and public subnets:
* 1 subnet == 1 AZ. 1 AZ however can have multiple subnets.
* Subnets can be private, public or VPN only.
* A public subjet is one in which the associated route table directs the subnet
  traffic to the VPC's IGW.
* A VPN-only subnet is one in which the route table directs the subnet traffic to
  Amazon VPC's VPG and does not have a route to the IGW.
* Regardless of the type of subnet, the internal IP address range of the subnet is
  always private.
* Minimum size subnet you can have in a VPC is /28
* Maximum size subnet you can have in a VPC is /16
* Two types of subnets within a VPC - public and private.
* The only difference that makes a subnet public rather than private -
  instances running in a public network are  able to access the internet
  by default and  also be made public by attaching a public or Elastic IPs to them.
* The public subnet - has an IGW attached to it and a route for all addresses
  pointing to the IGW.
* public subnet is sort of a DMZ in classical n/w terms. The subnet is hidden,
  from public view via a router (IGW) with 1:1 DNAT rules attached that map
  public or Elastic IPs of instances running in the subnet.

* Private networks are completely cut off from any access to the internet by
  default, but can communicate with any instances running in all subnets
  within the VPC.
* We can also control traffic between all subnets through the VPC's NACLs and
  define rules that will prevent certain subnets from communicating with
  each other.
* private subnets - can connect to other networks via NAT gateway that allows
  outbound traffic, or through a VPN gateway or direct connect - to connect
  to on-premise systems.
* IPV6 addresses are global unicast addresses. -  only way to allow an IPV6
  subnet to communicate with the internet is to attach an IGW to the subnet.
* All IPV6 addresses in a subnet with an IGW attached are inherently able to
  access the internet and instantly become accessible from the internet. But
  what if we want to keep our instances private and still communicate with
  the internet? For this AWS has introduced a so-called egress only gateway
  that can allow instances with IPV6 addresses to communicate with internet,
  but does not allow any traffic into the subnet since ingress traffic is
  automatically blocked.


### public, elastic and private IPs
* Public IPs are sourced from one or more AWS controlled public IP address
  pools and are attached to the instance randomly whenever an instance is
  started.
* When an instance using a public IP address fails and is recreated or
  shut down and restarted, it will not maintain the same public IP address.

* An Elastic IP address is associated with your account and is persistent.
* A public or EIP attachment means that a virtual 1:1 DNAT connection between
  the public or Elastic IP is established with the instances private IP.
* You will not see the public ip address from the os (eg ifconfig).
* However you can check the public ip address by accessing the metadata.

  ```
  http://169.254.169.254/latest/meta-data/public-ipv4
  ```

* Each VPC network can be divided into 200 subnets at most.
* We can asign upto 5 IPV4 CIDR blocks to each VPC. These are soft limits
  that can be increased.
* However we are limited to only one IPv6 CIDR block per vpc - This is a hard
  limit.
  * A VPC can only have one DHCP options set attached at any time



## VPC networking components

### ENI
* The ENI is a virtual network adapter that allows us to connect operating
  systems, containers and other components to a VPC.

* When an EC2 instance is created a special kind of ENI is created and
  **permanently** attached to it. This ENI is also called the primary network
  interface.
* A primary network interface has all the characteristics of an ENI, except
  it cannot be detached from the instance.

* An ENI can be created independently of an EC2 instance and arbitarily
  assign it's characteristics.
* When created separately, the ENI is created with a persistent MAC address.
* Once attached to an instance, this adapter will show up as a secondary
  network interface and the MAC address will be visible in the operating
  system.
* This ENI is completely idependent of the EC2 instance it is connected to
  and it's characteristics will persist through stops and starts, and will
  remain unchanged even when the instance is terminated.

* ENI can be detached and attached to another instance. This is useful when
  we use licensing that is tied to a MAC address. Instead of tying the
  licensse to the primary network interface and hoping that the instance
  never fails, we can assign the licensse to a separately created secondary
  ENI.

* By default you can assign up to 5 security groups to each ENI. But this is
  a soft limit. Absolute max is 16 security groups per ENI.
* However the absolute max number of rules per ENI is 300.

* When troubleshooting network flow issues, we can enable VPC flow logs
  for each ENI separately.



### Routing, nat and internet access

#### Connecting public subnets to the internet

* For IPv4 we will be connecting an IGW to public-subnet, which will allow
  us to assing public and Elastic IPs through 1:1 NAT to our instances.
* This means - any traffic coming into the public or Elastic IP will be
  directed by the IGW to the internal IP address of the instance.
* When using IPv6, the addresses are assigned directly to the instances in
  the public subnet, and by connecting an IGW, we allow the traffic to
  flow in and out of those instances.

* To allow the traffic from the instances to flow to and from the internet,
  we will also need to create a default route in the routing table of each
  public subnet that has an IGW attached to it.
* For IPv4 will need a route for 0.0.0.0/0, whereas for IPv6 will have a
  destination of ::/0. Both routes will define target as the id of the IGW
  that is connected to the subnet.

**Enabling Internet Access:**
* Attach and IGW to your VPC
* Add a route to the routing table that directs internet-bound traffic to
  the IGW.(A subnet that has this route is a public subnet)
* Ensure - instances in the subnet have a globally unique IP addr.
* Ensure NACL and security group rules allow relevant traffic to flow to and from
  your instance.

* To provide your instances internet access without assigning public IP address, you
  can use a NAT device instead.

#### Connecting private subnets to the internet

* For IPV4 subnet - use a NAT gateway. The NAT gateway will allow all outgoing
  traffic to pass to the internet.


* A NAT gateway has the following features:
  - Supports 5 GBps of bandwidth - scales up to 45 GBps
  - Supports up to 55,000 simultaneous TCP, UDP and ICPM connections to each unique
    destination.
  - Can associate exactly one EIP address with a NAT gateway - once created it
    cannot be dissociated.
  - Cannot associate a SG with a NAT gateway, but access can be controlled at EC2
    using SGs.
  - NAT gateway has an automatically assigned private IP in your subnet that can be
    viewed in AWS console.

* Can create multiple NAT gateways for performance.

* In case of IPv6, an egress-only internet gateway is needed.
* The egress only gateway has all the characteristics of an internet gateway,
  with the difference being that it blocks all incoming traffic to IPv6 address space.
* You can manage your own EC2 instance as a NAT instance - allows any custom
  traffic shaping and security checks, with packket inspection and firewalling
  software.

* If you have resources in multiple AZs and they share one NAT gateway, in the event
  that the NAT gateway's AZ is down, resources in other AZs loose internet access.
* To create AZ independent architecture, create a NAT gateway in each AZ and
  configure your routing to ensure that resources use NAT gateway in the same AZ.

### VPC endpoints and Privatelink
* To allow access to AWS services like S3, SQS, KMS and DynamoDB from a private 
  subnet, which does not have access to internet.
* Enables you to create a private connection between your VPC and another AWS service
  without requiring access over the internet, or a NAT interface, VPN connection or 
  AWS direct connect.
* VPC endpoint currently supports S3 and dynamodb.
* Does not require an IGW, Nat device, VPN connection or AWS direct connect connections.
* Instances in your VPC do not require public IP addresses to communicate with resources in
  the service.
* You can use the describe-prefix-lists to list the CIDRs for your
  endpoints in the vpc. This can be useful when opening specific CIDRs for
  outbound access from your EC2 instances.

```
$ aws ec2 describe-prefix-lists --profile devaccount
PREFIXLISTS pl-6333400a com.amazonaws.us-east-1.s3
CIDRS 53.251.0.0/17
CIDRS 51.116.0.0/15
PREFIXLISTS pl-04442c6b com.amazonaws.us-east-1.dynamodb
CIDRS 51.44.0.0/22
CIDRS 54.159.224.0/21
```

* A VPC endpoint can connect to the VPC and allow for communication to the service 
  within a private IP space.

* VPC endpoint connections come in two different types:
  - Gateway endpoints
  - Interface endpoints

#### Gateway endpoint
* S3 and DynamoDB support gateway endpoints.
* Instance running within the VPC can consult the routing table to access the AWS
  service.

#### Interface endpoint
* An interface endpoint - essentially a service-level ENI. The service is attached
  straight to the VPC subnet through the ENI.
* Enables assigning a private IP address from the subnet pool directly to the
  service.
* Can communicate with the service on private network.

### Network ACLs:
* Your VPC automatically comes with a default Network ACL, and by default it allows
  all outbound and inbound traffic.
* Operates at subnet level (second level of defense)
* Supports allow and deny rules.
* Stateless: Return traffic must be explicitly allowed by rules.
* Processes rules in numbered order when deciding whether to allow traffic, starting
  with the lowest numbered rule.
* Automatically applied to all instances in the associated subnets.
* When you create a custom network ACL, it's initial configuration will deny all
  inbound and outbound traffic, until you create rules to allow otherwise.
* Each subnet in your VPC must be associated with a network ACL. If you do not
  explicitly associate a subnet with a network ACL, the subnet is automatically 
  associated with the default network ACL.
* You can associate a network ACL with multiple, subnets, however a subnet can be
  associated to only one network ACL at a time.


### VPC peering
* A VPC peering connection is a networking connection between two VPCs that allow
  you to route traffic between tem privately and have the ability to connect
  instances in private subnets.
* Standard inter-region charges apply for VPC peering between regions. No charges
  to traffic within a region.

#### Limitations of VPC peering
* [VPC Invalid peering configs](https://docs.aws.amazon.com/vpc/latest/peering/invalid-peering-configurations.html#transitive-peering)

* No overlapping IPV4 or IPV6 CIDR blocks.
* Transitive peering is not supported.
* Unicast reverse path forwarding in VPC peering connections is not supported.

* Additionally inter-region VPC peering has following Limitations:
  - peer VPC's security groups cannot be referenced in security groups created
    in the other VPC.
  - DNS resolution of hostnames that have both public and private IPS, will only
    resolve public IPs when queried from peer VPC.
  - Communication over IPV6 is not supported
  - Communication over ClassicLink for EC2-classic instances is not supported
  - Jumbo frames are not supported across inter region VPC peering connection.


### VPC Flowlogs:
* VPC FLow logs enables you to capture information about the IP traffic going to
  and from network interfaces in your VPC.
* VPC flow logs can be created at the VPC, subnet and network interface levels.
* Flow log data is stored in Amazon cloudwatch logs.
* You cannot enable flow logs for VPCs that are peered with your VPC unless the peer
  VPC is in your account.
* You can tag flow logs.
* After you have created a flow log you cannot change it's configuration.

### Global Accelerator:
* It is a service in which you create accelerators to improve availability and
  performance of your applications for local and global users.
* You are assigned two static IP addresses (or you can bring your own)
* You can control traffic using traffic dials. This is done within the endpoint group.
* A network zone services the static IP addresses for your accelerator from a unique 
  IP subnet. Similar to availability zone, a network zone is an isolated unit with its
  own set of physical infrastructure.
* When you configure an accelerator, by default it allocates two IPv4 addresses for it.
* Includes the following components:
  ---------------------------------
  * Static IP addresses      * Listener
  * Accelerator              * Endpoint Group
  * DNS Name                 * Endpoint
  * Network Zone

* Listner:
  * A listner processes inbound connections from clients to the Global Accelarator,
    based on the port (or port range) and protocol you configure. It supports both
    UDP and TCP protocols.
  * Each listner has 1 or more endpoint groups associated, and traffic is forwarded
    to endpoints in one of the groups.
  * You associate endpoint with listner groups by specifying the regions that you
    want to distribute traffic to.

* Endpoint group:
  * Each endpoint group is associatated with a specific AWS Region.
  * Endpoint groups include one ore more endpoints in the Region.
  * You can increase or reduce the percentage of traffic that would be otherwise
    directed to an endpoint group by adjusting a setting called a traffic dial.
  * The traffic dial lets you easily do performance testing or blue/green deployment
    testing for new releases across different AWS regions.

* Endpoints
  * Endpoints can be Network LB, Application LBs, EC2 instances, or Elastic IP addr.
  * An ALB endpoint can be internet-facing or internal. Traffic is routed to
    endpoints based on configuration options that you choose, such as endpoint
    weight.
  * For each endpoint, you can configure weights, which are numbers that you can
    use to specify the proportion of traffic to route to each one. This can be
    useful, for example, to do performance testing within a Region.



### AWS Transit Gateway:
* Allows you to have transitive peering between thousands of VPCs and on-premises
  data centers.
* Works on a hub-and-spoke model.
* Works on a regional basis, but you can have it across multiple regions.
* You can use it across multiple AWS accounts using Resource Access Manager.
* You can use route tables to limit how VPCs talk to one another.
* Works with Direct Connect as well as VPN connections.
* Supports IP Multicast (not supported by any other AWS service)


### AWS VPN CloudHub:
* If you have multiple sites, each with it's own VPN connection, you can use AWS
  VPN Cloudhub to connect to those sites together.
* Hub and spoke model
* Low cost; easy to manage
* It operates over the public internet, but all traffic between the customer gateway
  and the AWS VPN cloudhub is encrypted.

## AWS Networking costs
* Use private IP addresses over public ip addresses to save cost. This utilizes the AWS
  backbone.
* Traffic between instances within the same AZ is free, but flowing across AZs is 0.01$/Gb.
* Traffic across regions will be charged at 0.02$/Gb (depending on regions)
* Traffic going out to the internet will have a cost.


## VPC Network security
Network security is a small part of an overall strategy in securing our applications.

### Network security vulnerabilities

#### Network layer attacks
some n/w layer attacks:
* Automated port scanning: Attempt to discover open ports to compromise
* Spoofing: Attacker sets up his own server with an IP address of the server being
  attacked and intercept traffic intended of the legitimate IP.
* DoS: Attack and application entry point with traffic designed to overwhelm the
  system, either with volume or packets that will cause errors to accumulate.

* AWS inherently prevents IP spoofing and port scanning within EC2 networks. An
  attempt to do so will result in violation of AWS terms and immediately blocked.

* AWS services WAF and Shield help with preventing these attacks.


#### Service layer attacks
* Attacks are designed to attack a service that an application relies on to
  function correctly.
* Most commonly used attacks is DNS and domain hijacking. Intercept DNS traffic -
  inject incorrect DNS information - requests from the application will be sent
  to attackers DNS instead of the legitimate one.

#### Exploiting vulnerabilities

#### application layer attacks


### Security in the OSI model

#### Layer 2
* AWS Config allows us to detect any changes (creation of instances and network
  interfaces) that could be connected to the VPC.

#### Layer 3
* Stateless firewalls - NACLs are good at stopping layer 3 attacks. Stopping attack
  at the perimeter of the network.

#### Layer 4
* firewalling at the transport layer.
* Stateful firewall.
* Security groups, operating system firewalling, AWS Shield and WAF all play a role
  in stopping layer 4 attacks.

#### Layer 7
* Application firewalls is perhaps the most difficult and wide-ranging subject.
* There are many ways to approach it.
* AWS offers WAF which can help in securing web applications.


### WAN to LAN access patterns
* Any time an application is internet facing, it will need to be protected with as many mechanisms as possible.

* Focus on minimizing the footprint of the attack - should disable any
  unnecessary access and limit the incoming traffic only to the legitimate sources
* For eg: when using an ELB, create a SG that only allows access to the ELB IP instead of both the ELB and the instances it load balances traffic to. The instances should only be accessible from the ELB itself.




### Securing EC2

### operating systmes


### Threats to modern applications

AWS outlines several aspects of how to be prepared and mitigate DDoS attacks:
* **Scaling:** An expensive way to mitigate an attack and maintain SLA.
* **Minimizing attack surface:** Remove any unnecessary or unused entry points to
  the application. Also identify all possible mitigation strategies for any
  entry points that are crucial for the operation of the application.
* **Identify traffic patterns:** Understand typical traffic patterns of the
  application. Also monitor to identify pattern and anomalies - can be automated using CloudWatch alarms.
* **Resiliency:** Building applications that are resilient to attacks.

mitigation:
* AWS WAF
* AWS Shield



## AWS WAF (Web Application Firewall)
Lets you monitor and filter traffic that is intended for:
* HTTP/HTTPS web servers behind ALB in EC2
* AWS API gateway
* AWS Cloudfront distributions.


### How WAF Works:
[How WAF Works](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html)

**Web ACLs**:
* You use Web ACLs to protect a set of AWS resources.
* Create a Web ACL and define it's protection strategy by adding rules.
* Rules define criteria for inspecting web requests and how to handle requests
  that match the criteria.
* Set a default action for the web ACL that indicates whether to allow or
  block those requests that pass the rules inspection.

**Rules:**
* Each rule contains a statement that defines the inspection criteria, and
  and action if the request meets criteria.
* When a web requests meets the criteria, that's a match.
* You can block, allow or simply count matching requests.

**Rules groups:**
* You can use rules individually or in a reusable rules group.
* You can define your own rule groups, get them from AWS managed rules or
  marketplace as well.




## Connecting On-premise and AWS

AWS provides layer2 and layer3 connectivity options for connecting your private
AWS subnet to on-prem.

* **Direct connect:** low latency layer 2 connection on dedicated private links
* **VPN with virtual gateway:** layer3 IPSec-encrypted connection over public internet.

### Steps to creating a direct connect connection
* Create a virtual interface in the direct connect console. This is a Public virtual interface.
* Go to the VPC console - to VPN connections. Create a customer gateway
* Create a virtual private gateway
* Attach a virtual private gateway to the desired VPC.
* Select the VPN connections and create a new VPN connection.
* Select the virtual private gateway and the customer gateway
* Once the VPN is available, setup the VPN on the customer gateway or firewall.




















