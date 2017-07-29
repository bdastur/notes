# AWS Notes:


## Dynamo DB:

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
*
