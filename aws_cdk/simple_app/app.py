#!/usr/bin/env python3

"""
This cdk app gives an example of
- multiple stacks for an application
- S3 bucket creation
- iam role creation
- granting permissions to s3 bucket to the role.
- creating cfnrole with inline and managed policy attachments.
- cross stack reference (bucket from stack1 is referenced in stack2)
"""

import aws_cdk as cdk

from stacks.SimpleStackOne import SimpleAppStack
from stacks.SimpleStackTwo import SimpleAppStack2
from stacks.SimpleStackWithParams import SimpleStackWithParameter


app = cdk.App()
stackOne = SimpleAppStack(app, "SimpleAppStack")
stackTwo = SimpleAppStack2(app, "Stack2", myBucket=stackOne.myBucket)
stackThree = SimpleStackWithParameter(app, "Stack3")

app.synth()

