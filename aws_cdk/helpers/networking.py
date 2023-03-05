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


class Vpc(object):
    def __init__(self, scope, id, **options):
        pass

    def create(self):
        pass

    def setTags(self, tags):
        pass



class SecurityGroup(object):
    def __init__(self, scope, id, groupDescription, **options):
        self.securityGroup = None
        self.securityGroupIngress = []
        self.securityGroupEgress = []
        self.cfnTags = []
        # Parse options.
        self.scope = scope
        self.id = id
        self.groupDescription = groupDescription
        self.sgOptions = options

        delayCreate = options.get("delay_create", False)
       
        if not delayCreate:
            self.create()

    def addIngressRule(self, ingressRule):
        validProtocols = ["tcp", "udp", "icmp", "icmpv6"]
        
        ipProtocol = ingressRule["ip_protocol"]
        fromPort = ingressRule["from_port"]
        toPort = ingressRule["to_port"]
        cidrIp = ingressRule["cidr_ip"]
        description = ingressRule.get("description", "")

        if ipProtocol not in validProtocols: 
            raise TypeError("ip_protocol must be one of %s" % validProtocols)

        self.securityGroupIngress.append(
                ec2.CfnSecurityGroup.IngressProperty(
                    ip_protocol=ipProtocol,
                    from_port=fromPort,
                    to_port=toPort,
                    cidr_ip=cidrIp,
                    description=description))

    def addEgressRule(self, egressRule):
        validProtocols = ["tcp", "udp", "icmp", "icmpv6"]

        ipProtocol = egressRule["ip_protocol"]
        fromPort = egressRule["from_port"]
        toPort = egressRule["to_port"]
        cidrIp = egressRule["cidr_ip"]
        description = egressRule.get("description", "")

        if ipProtocol not in validProtocols:
            raise TypeError("ip_protocol must be one of %s" % validProtocols)

        self.securityGroupEgress.append(
                ec2.CfnSecurityGroup.EgressProperty(
                    ip_protocol=ipProtocol,
                    from_port=fromPort,
                    to_port=toPort,
                    cidr_ip=cidrIp,
                    description=description))

    def setTags(self, tags):
        for tag in tags:
            self.cfnTags.append(addTag(tag["Key"], tag["Value"]))

    def create(self):
        groupName = self.sgOptions.get("group_name", None)
        vpcId = self.sgOptions.get("vpc_id", None)
        tags = self.sgOptions.get("tags", [])

        ingressRules = self.sgOptions.get("ingress_rules", [])
        egressRules = self.sgOptions.get("egress_rules", [])

        self.securityGroupIngress = []
        for ingressRule in ingressRules:
            self.addIngressRule(ingressRule)

        self.securityGroupEgress = []
        for egressRule in egressRules:
            self.addEgressRule(egressRule)

        self.cfnTags = []
        self.setTags(tags)

        self.securityGroup = ec2.CfnSecurityGroup(
            self.scope, self.id, group_description=self.groupDescription,
            vpc_id=vpcId, 
            security_group_ingress=self.securityGroupIngress,
            security_group_egress=self.securityGroupEgress,
            tags=self.cfnTags)



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

