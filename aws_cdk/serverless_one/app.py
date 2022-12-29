#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.serverless_one_stack import ServerlessOneStack


app = cdk.App()
ServerlessOneStack(app, "ServerlessOneStack")

app.synth()
