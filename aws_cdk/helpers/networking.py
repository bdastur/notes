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


