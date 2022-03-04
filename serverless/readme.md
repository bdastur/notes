# Serverless.

There is a section on serverless (Lambda) in aws/readme.md. However I think now
serverless deserves a new folder.

## Useful links

* [AWS Lambda Introduction](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
* [AWS Lambda - best practices](http://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
* [AWS Lamda quotas](http://docs.aws.amazon.com/lambda/latest/dg/limits.html)
* [AWS Lambda Powertools Python](https://awslabs.github.io/aws-lambda-powertools-python/latest/)
* [Lambda event resources](https://michaelbrewer.github.io/aws-lambda-events/#objectives)

* Run code/service without provisioning or managing servers.
* Pay only for the compute time that you consume.
* Supports synchronous and asynchronous invocation of lambda function.
* When the lambda function is invoked from another aws service, the invocation type
  is pre-determined.
* Languages supported: C#, Java, Node.js, Python.
* Lambda billing is based on both, the MB of RAM reserved and the execution duration
  in 100ms units.


### Creating a Lamda layer with python.

Lambda layers need to follow a specific [directory structure](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
The PATH variable includes specific folders in the /opt directory. If you define the
same folder structure in your layer .zip file, your function code can access the layer
content without the need to specify the path.

For python : python

#### Creating a zip file for the layer
```
mkdir tempdir
cd tempdir
python3 -m venv python
source ./python/bin/activate
pip3 install requests
deactivate
zip -r py38_layer.zip python
```

#### Creating or updating a lambda layer.

The same CLI works for creating a new layer or updating an existing layer. If the 
layer already exist, it's version will be bumped up by 1.

```
aws lambda publish-layer-version \
    --layer-name py38_layer \
    --description "Boto3, requests"  \
    --compatible-runtimes python3.8 \
    --zip-file fileb://py38_layer.zip \
    --profile dev1 --region us-west-2

```

