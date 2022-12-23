# AWS CDK

* [AWS CDK Guide](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
* [AWS CDK Python Modules](https://docs.aws.amazon.com/cdk/api/v1/python/modules.html)

---

## Installation

1. NPM:
Install NPM.

2. Install CDK

```
sudo npm install -g aws-cdk
```

## Bootstrap:

```
cdk bootstrap aws://xxxxxxxxxxxxx/us-east-1
```

## Creating a new CDK based App.

```
mkdir newapp
cd newapp
cdk init app --language python

source ./venv/bin/activate
pip install -r requirements.txt
```


