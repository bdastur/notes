#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.apigwstack import ApiGatewayStack
from stacks.lambdastack import LambdaStack


app = cdk.App()

options = {}

region = os.environ["CDK_DEFAULT_REGION"]
account = os.environ["CDK_DEFAULT_ACCOUNT"]
cdkEnv = cdk.Environment(account=account, region=region)

LambdaStack(app, "LambdaStack", options, env=cdkEnv)
ApiGatewayStack(app, "ApiGatewayStack", env=cdkEnv)

app.synth()
