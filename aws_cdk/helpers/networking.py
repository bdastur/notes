#!/usr/bin/env python
# -*- coding: utf-8 -*-


import aws_cdk
from aws_cdk import aws_ec2 as ec2


def addTag(key, value):
    return aws_cdk.CfnTag(key=key, value=value)


def createVpc(scope, id, cidrBlock, **options):

    # Parse options.
    enableDnsHostnames = options.get("enable_dns_hostnames", False)
    enableDnsSupport = options.get("enable_dns_support", False)
    instanceTenancy = options.get("instance_tenancy", "default")
    tags = options.get("tags", None)
    cfnTags = []

    if tags is not None:
        for tag in tags:
            cfnTags.append(addTag(tag['Key'], tag['Value']))

    vpc = ec2.CfnVPC(scope, id, cidr_block=cidrBlock, 
                     enable_dns_support=enableDnsSupport, 
                     enable_dns_hostnames=enableDnsHostnames, 
                     instance_tenancy=instanceTenancy, 
                     tags=cfnTags) 
    return vpc


class SecurityGroup(object):
    def __init__(self, scope, id, groupDescription, **options):
        self.securityGroup = None
        # Parse options.
        self.scope = scope
        self.id = id
        self.groupDescription = groupDescription
        self.sgOptions = options

        self.create()

    def create(self):
        groupName = self.sgOptions.get("group_name", None)
        vpcId = self.sgOptions.get("vpc_id", None)
        tags = self.sgOptions.get("tags", [])

        ingressRules = self.sgOptions.get("ingress_rules", [])
        egressRules = self.sgOptions.get("egress_rules", [])

        securityGroupIngress = []
        for ingressRule in ingressRules:
            securityGroupIngress.append(
                    ec2.CfnSecurityGroup.IngressProperty(
                        ip_protocol=ingressRule['ip_protocol'],
                        from_port=ingressRule["from_port"],
                        to_port=ingressRule["to_port"],
                        cidr_ip=ingressRule["cidr_ip"]
                    ))

        securityGroupEgress = []
        for egressRule in egressRules:
            securityGroupEgress.append(
                    ec2.CfnSecurityGroup.EgressProperty(
                        ip_protocol=egressRule["ip_protocol"],
                        from_port=egressRule["from_port"],
                        to_port=egressRule["to_port"],
                        cidr_ip=egressRule["cidr_ip"],
                    ))

        cfnTags = []
        for tag in tags:
            print("set tags: ", tag["Key"], tag["Value"])
            cfnTags.append(addTag(tag["Key"], tag["Value"]))

        self.securityGroup = ec2.CfnSecurityGroup(
            self.scope, self.id, group_description=self.groupDescription,
            vpc_id=vpcId, 
            security_group_ingress=securityGroupIngress,
            security_group_egress=securityGroupEgress,
            tags=cfnTags)




def createSecurityGroup(scope, id, groupDescription, **options):
    # Parse options
    groupName = options.get("group_name", None)
    vpcId = options.get("vpc_id", None)
   
    ingressRules = [
        ec2.CfnSecurityGroup.IngressProperty(
            ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="10.0.0.0/24")
    ]

    securityGroup = ec2.CfnSecurityGroup(
            scope, id, group_description=groupDescription, 
            vpc_id=vpcId, security_group_ingress=ingressRules)

