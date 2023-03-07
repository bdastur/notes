from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2
    # aws_sqs as sqs,
)

from constructs import Construct

import helpers.networking as networking 

class LampStack2(Stack):

    def __init__(self, scope: Construct, construct_id: str,options,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cidrBlock = options["cidrBlock"]

        vpcOptions = {
            "enable_dns_hostnames": False,
            "enable_dns_support": False,
            "instance_tenancy": "default"
        }
        vpcOptions["tags"] = [{"Key": "Name", "Value": "vpcOne"},
                {"Key": "Description", "Value": "Test description"}]

        self.vpcTwo = networking.createVpc(self, "vpcTwo", cidrBlock, **vpcOptions)


