from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2
    # aws_sqs as sqs,
)

from constructs import Construct

import helpers.ec2 as libec2 

class LampstackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str,options,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Create network stack
        # If you get this error: "TypeError: type of argument scope
        # must be constructs.Construct; got constructs.Construct instead",
        # the issue here is scope is set to Construct, instead set it to
        # self

        # L2 Construct. Creates, vpc, 2 subnets (priv and pub), iGW, VPCGW.
        # vpcOne = ec2.Vpc(self, "vpcOne",
        #                  ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"))

        cidrBlock = options["cidrBlock"]
        vpcRef = options["vpcRef"]

        vpcOne = ec2.Vpc.from_lookup(self, "NewVpc", tags={"Name": "vpcOne"})

        #vpcOptions = {
        #    "enable_dns_hostnames": False,
        #    "enable_dns_support": False,
        #    "instance_tenancy": "default"
        #}
        #vpcOptions["tags"] = [{"Key": "Name", "Value": "vpcOne"},
        #        {"Key": "Description", "Value": "Test description"}]

        #vpcOne = networking.createVpc(self, "vpcOne", cidrBlock, **vpcOptions)


        # Using vpcOne.ref to refrence the vpc created.
        subnetOne = ec2.CfnSubnet(self, "subnetOne", cidr_block="10.0.0.0/24",
                                  vpc_id=vpcOne.vpc_id, availability_zone="us-east-1a")

        # Creating a security group.
        securityGroupOptions = {
            "vpc_id": vpcRef,
            "ingress_rules": [
                {
                    "ip_protocol": "tcp",
                    "from_port": 22,
                    "to_port": 22,
                    "cidr_ip": "10.0.0.0/28"
                },
                {
                    "ip_protocol": "tcp",
                    "from_port": 443,
                    "to_port": 443,
                    "cidr_ip": "10.0.1.0/28"
                },
                {
                    "ip_protocol": "tcp",
                    "from_port": 43434,
                    "to_port": 43434,
                    "cidr_ip": "10.0.0.2/24",
                    "description": "This is a test rule"
                }
            ],
            "egress_rules": [
                {
                    "ip_protocol": "tcp",
                    "from_port": 45050,
                    "to_port": 45050,
                    "cidr_ip": "0.0.0.0/0"
                },
                {
                    "ip_protocol": "tcp",
                    "from_port": 34533,
                    "to_port": 34533,
                    "cidr_ip": "0.0.0.0/0",
                    "description": "A test rule"
                },
            ],
            "tags": [
                {"Key": "Name", "Value": "SampleSecurityGroup"},
                {"Key": "Description", "Value": "A test security group"}
            ]
        }
        secGroup = libec2.SecurityGroup(
                self, "secGroupOne", "Test Description", **securityGroupOptions)


        """
        secGroupOne = ec2.CfnSecurityGroup(
                self, "secGroupOne", group_name="Mysecuritygroup",
                group_description="This is a cdk test", vpc_id=vpcOne.ref,
                security_group_ingress=[
                        ec2.CfnSecurityGroup.IngressProperty(
                        ip_protocol="tcp", cidr_ip="10.0.1.0/24",
                        from_port=22, to_port=22),
                        ec2.CfnSecurityGroup.IngressProperty(
                            ip_protocol="tcp", cidr_ip="10.0.0.0/16",
                            from_port=443, to_port=443)
                    ])
        """


