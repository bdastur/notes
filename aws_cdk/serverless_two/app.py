#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.apigwstack import ApiGatewayStack
from stacks.lambdastack import LambdaStack


app = cdk.App()

options = {}


LambdaStack(app, "LambdaStack", options,)
ApiGatewayStack(app, "ApiGatewayStack",)

app.synth()
