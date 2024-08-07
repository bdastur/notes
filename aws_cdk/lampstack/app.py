#!/usr/bin/env python3
import os

import aws_cdk as cdk

from lampstack.lampstack_stack import LampstackStack
from lampstack.stack2 import LampStack2


app = cdk.App()

region = os.environ["CDK_DEFAULT_REGION"]
account = os.environ["CDK_DEFAULT_ACCOUNT"]
print("Region: ", region, " Account: ", account)

cdkEnv = cdk.Environment(account=account, region=region)

options = {
    "cidrBlock": "10.0.0.0/16"
}

secondStack = LampStack2(app, "LampStack2", options, env=cdkEnv)

options["vpcRef"] = secondStack.vpcTwo.ref
    

lampStack = LampstackStack(app, "LampstackStack", options, env=cdkEnv,
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
