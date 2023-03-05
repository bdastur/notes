# AWS CDK

* [AWS CDK Guide](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
* [AWS CDK Python Modules](https://docs.aws.amazon.com/cdk/api/v1/python/modules.html)
* [Construct Hub](https://constructs.dev/search?q=&cdk=aws-cdk&cdkver=2&sort=downloadsDesc&offset=0)
* [AWS Construct Library](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html)
* [Construct HUB](https://constructs.dev/)
* [Construct HUB - DLM Construct library](https://constructs.dev/packages/@aws-cdk/aws-dlm/v/1.185.0/api/ActionProperty?lang=python)

---

## Installation

1. NPM:
Install NPM.

2. Install CDK

```
sudo npm install -g aws-cdk
```

## Basic Usage.

### Bootstrap:
You will need to do this once per account/region if you have not already.
This will create the required CFN stack and resources required for CDK to 
work.


```
cdk bootstrap --profile dev --region us-east-1
```

```
cdk bootstrap aws://xxxxxxxxxxxxx/us-east-1
```

### Creating a new CDK based App.

```
mkdir newapp
cd newapp
cdk init app --language python

source ./venv/bin/activate
pip install -r requirements.txt
```

### Deploying your app.

```
cdk deploy --profile dev --region us-east-1
```

### Destroying the stack

```
cdk destroy HelloCdkStack --profile dev --region us-east-1
```

## CDK HowTos.

### Referencing resources between Stacks.

Here's an example of how we can reference resources from one stack, into
another stack.

Stack 1, creates a VPC. Stack 2 references vpc.

VPC Stack (LampStack2 creates the vpc):
```
class LampStack2(Stack):
    def __init__(self, scope: Construct, construct_id: str,options,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        :

        self.vpcTwo = ec2.createVpc(self, "vpcTwo", cidrBlock, **vpcOptions)

```

app.py:
We create the secondStack, which creates the vpc, we pass the vpc ref to the second
stack.
```
#!/usr/bin/env python3
import os
:
from lampstack.lampstack_stack import LampstackStack
from lampstack.stack2 import LampStack2

app = cdk.App()

options = {
    "cidrBlock": "10.0.0.0/16"
}

secondStack = LampStack2(app, "LampStack2", options, env=cdkEnv)

options["vpcRef"] = secondStack.vpcTwo.ref
    

lampStack = LampstackStack(app, "LampstackStack", options,)

app.synth()

```

Second stack usage:
The secondstack gets the options as arguments, which has the vpcRef which is the
reference to the vpc created in the first stack.
```
class LampstackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str,options,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpcRef = options["vpcRef"]
        subnetOne = ec2.CfnSubnet(self, "subnetOne", cidr_block="10.0.0.0/24",
                                  vpc_id=vpcRef, availability_zone="us-east-1a")
```


### Referencing a resource from your AWS account that is not managed by CDK.
Sometimes you want to reference a resource and use it in your CDK.
Example, you want to create security groups in an already existing vpc.

Here we search the vpc using tags , search of vpc with tag Name as value 'vpcOne'
And referencing it when creating a subnet.
```
   vpcOne = ec2.Vpc.from_lookup(self, "NewVpc", tags={"Name": "vpcOne"})

    subnetOne = ec2.CfnSubnet(self, "subnetOne", cidr_block="10.0.0.0/24",
                              vpc_id=vpcOne.vpc_id, availability_zone="us-east-1a")

```

Results of Vpc.from_lookup() are cached in the project's cdk.context.json file. 
You can commit this file to version control, so that your app will continue to
refer to the same Amazon VPC. This works even if you later change the attributes 
of your VPCs in a way that would result in a different VPC being selected. 

A note here when referencing other resources. You will need to specify the CDK
environment at the stack level, otherwise the CDK API will have no way of knowing

With an error as below:
```
RuntimeError: Error: Cannot retrieve value from context provider vpc-provider since 
account/region are not specified at the stack level. Configure "env" with an account 
and region when you define your stack.
See https://docs.aws.amazon.com/cdk/latest/guide/environments.html for more details.

```
How to fix this? See the note below:

### How to configure the env with an account and region when you define your stack.

```
#!/usr/bin/env python3
import os
import aws_cdk as cdk
from lampstack.lampstack_stack import LampstackStack
from lampstack.stack2 import LampStack2

app = cdk.App()

region = os.environ["CDK_DEFAULT_REGION"]
account = os.environ["CDK_DEFAULT_ACCOUNT"]

cdkEnv = cdk.Environment(account=account, region=region)
:
:
secondStack = LampStack2(app, "LampStack2", options, env=cdkEnv)
lampStack = LampstackStack(app, "LampstackStack", options, env=cdkEnv)

app.synth()

```

CDK_DEFAULT_REGION and ACCOUNT env variables are populate when you call cdk
command as below:
```
cdk synth/deploy LampstackStack --region us-east-1 --profile dev
```











