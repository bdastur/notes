#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iam_example.iam_example_stack import IamExampleStack
from iam_example.iamone import IAMOneStack


app = cdk.App()

region = os.environ["CDK_DEFAULT_REGION"]
account = os.environ["CDK_DEFAULT_ACCOUNT"]
cdkEnv = cdk.Environment(account=account, region=region)

IamExampleStack(app, "IamExampleStack",env=cdkEnv)
IAMOneStack(app, "IAMOneStack", env=cdkEnv)

app.synth()
