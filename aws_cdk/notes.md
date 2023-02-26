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
















