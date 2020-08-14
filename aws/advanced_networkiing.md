# AWS Advanced Networking:


## Networking with VPC:

* In AWS VPC is the core networking component.
* It serves as private layer 2 isolated network layer
* VPC is the main environment that provides logical network isolation and
  grouping of resources such as EC2, ECS and other AWS services.

* VPC CIDR range (/28 - /16)
* Addressing in VPC defaults to IPV4, but IPV6 and dual stacks can run in
  the VPC if required.

* Provisioning in VPC is irreversible - once provisioned it cannot be changed.
* Also consider that there will be some services running in the VPC reserved
  by AWS - eg: IP address will be consumedd by internet gateway, DHCP service,
  NAT gateway, and reserved addresses AWS keeps unused for future services.

### Private and public subnets:

* Two types of subnets within a VPC - public and private.
* The only difference that makes a subnet public rather than private is that
  instances running in a public network will be able to access the internet
  by default also be made public by attaching a public or Elastic IPs to them.
* The public subnet would also be identified easily as it will have an IGW
  attached to it and route for all addresses pointing to the IGW.
* public subnet is sort of a DMZ in classical n/w terms. The subnet is hidden,
  from public view via a router (IGW) with 1:1 DNAT rules attached that map
  public or Elastic IPs of instances running in the subnet.

* Private networks are completely cut off from any access to the internet by
  default, but can communicate with any instances running in all subnets
  within the VPC.
* We can also control traffic between all subnets through the VPC's NACLs and
  define rules that will prevent certain subnets from communicating from
  each other.
* private subnets are also able to connect to other networks via a NAT gw that
  will allow outbound traffic as well as through a VPN gateway or direct
  connect connection that will allow private subnets to communicate without
  on-premise systems.

* IPV6 addresses are global unicast addresses. This meanss that the only way
  to allow an IPV6 subnet to communicate with the internet is to attach an
  IGW to the subnet.
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



## VPC networking components

### ENI
* The ENI is a virtual network adapter that allows us to connect operating
  systems, containers and other components to a VPC.

* When an EC2 instance is created a special kind of ENI is created and 
  permanently attached to it. This ENI is also called the primary network
  interface.
* A primary network interface has all the characteristics of an ENI, except
  it cannot be detached from the instance.

* An ENI can be created independently of an EC2 instance and arbitarily 
  assign it's characteristics.
* When created separately, the ENI is created with a persistent MAC address.
* Oncee attached to an instance, this adapter will show up as a secondary
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
* This means that any traffic coming into the public or Elastic IP will be
  directed by the IGW to the internal IP address of the instance.
* When using IPv6, the addresses are assigned directly to the instances in
  the public subnet, and by connecting an IGGW, we allow the traffic to
  flow in and out of those instances.

* To allow the traffic from the instances to flow to and from the internet,
  we will also need to create a default route in the routing table of each
  public subnet that has an IGW attached to it.
* For IPv4 will need a route for 0.0.0.0/0, whereas for IPv6 will have a
  destination of ::/0. Both routes will define target as the id of the IGW
  that is connected to the subnet.


#### Connecting private subnets to the internet

* To connect an IPv4 subnet to the internet, we can use NAT gateway. The NAT
  gateway will allow all outgoing traffic to pass to the internet and is used
  when we require instances in private subnet to access the internet.



































