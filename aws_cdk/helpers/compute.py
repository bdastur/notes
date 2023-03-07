#!/usr/bin/env python
# -*- coding: utf-8 -*-


import aws_cdk
from aws_cdk import aws_ec2 as ec2
import aws_cdk.aws_lambda as awslambda


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
            self.cfnTags.append(aws_cdk.CfnTag(key=tag["Key"], value=tag["Value"]))

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




class AWSLambda(object):
    def __init__(self, scope, id, **options):
        self.scope = scope
        self.id = id
        self.options = options


        delayCreate = options.get("delay_create", False)

        if not delayCreate:
            self.create()


    def create(self):
        print("options: ", self.options)

        try:
            runTime = self.options["runtime"]
            handler = self.options["handler"]
            role = self.options["role"]
        except KeyError as err:
            print("Required arguments missing [%s]" % err)
            return

        functionName = self.options.get("function_name", None)
        description = self.options.get("description", None)

        # Get code type. Note there can be only one type.
        # "code_property": { "zip_file": "path to file" }
        codeType = list(self.options["code_property"].keys())[0]
        print("Code type: ", codeType)

        if codeType == "zip_file":
            with open("lambdas/hello.py", encoding="utf8") as inFile:
                lambdaCode = inFile.read()

            self.codeProperty = awslambda.CfnFunction.CodeProperty(
                    zip_file=lambdaCode)    

        lambdaFunction = awslambda.CfnFunction(
                self.scope, self.id, code=self.codeProperty,
                handler=handler, runtime=runTime,
                role=role,
                function_name=functionName, description=description)









