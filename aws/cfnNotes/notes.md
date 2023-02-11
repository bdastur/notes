# Cloudformation Notes.

## Links:

* [AWS Cloudformation guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
* [AWS Cloudformation getting started](https://aws.amazon.com/cloudformation/getting-started/)


* Naming an IAM resource can cause an unrecoverable error if you reuse the same
  template in multiple Regions. To prevent AWS recommends using Fn::Join and AWS::Region
  to create Region-specific name. eg: {"Fn::Join": ["", [{"Ref": "AWS::Region"},
                                                         {"Ref": "MyResourceName"}]]}.


## Creating a new Stack.

### Define parameters:

```
> cat wdinstance_params.json
[
    {
        "ParameterKey": "KeyName",
        "ParameterValue": "testkey"
    },
    {
        "ParameterKey": "DBPassword",
        "ParameterValue": "testpass"
    },
    {
        "ParameterKey": "DBUser",
        "ParameterValue": "admin"
    },
    {
        "ParameterKey": "DBRootPassword",
        "ParameterValue": "MyPass123"
    }
]

```

### Creating the stack.
```
aws cloudformation create-stack --stack-name teststack1 \
    --template-body file://wdinstance.yaml \
    --parameters file://wdinstance_params.json \
    --profile dev --region us-east-1
```

* Creating a stack that creates iam roles, you will need to pass capabilities
  as CAPABILITY_IAM:
```
aws cloudformation create-stack --stack-name cfnbootstrap \
    --template-body file://cfrolestack.yaml \
    --parameters file://cfrolestack_params.json \
    --profile dev --region us-east-1 \
    --capabilities CAPABILITY_IAM

```

## Creating a change set.

```
aws cloudformation create-change-set --stack-name cfnrolestack \
    --change-set-name testchangeset2 --template-body file://cfrolestack.yaml \
    --parameters file://cfrolestack_params.json \
    --profile dev --region us-east-1 \
    --capabilities CAPABILITY_NAMED_IAM

```

## Describe change set.

Describe changeset, shows the resources that are changing. However it does not really
show what change is happening. Terraform does show the specific fields that are
changing.

```
aws cloudformation describe-change-set --stack-name cfnrolestack \
    --change-set-name testchangeset1 \
    --profile dev --region us-east-1

```

## HowTo

## Using a Ref
Ref can be used to reference other variables in the template.

Example 1: Referencing a parameter in a resource property.

```
Parameters:
  RoleNamePrefix:
    Type: String
    Description: "Role name prefix"
    MaxLength: "16"
    MinLength: "1"
Resources:
  CFNRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Ref RoleNamePrefix
      Description: "CFN Service Role"
```


### Using Join

Example 1:
Joining a Ref and another string to form a role name

```
Parameters:
  RoleNamePrefix:
    Type: String
    Description: "Role name prefix"
    MaxLength: "16"
    MinLength: "1"

Resources:
  CFNRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Join ["_", [!Ref RoleNamePrefix, "XYZ" ]]
      Description: "CFN Service Role"
```

### Using Mappings

Example getting ami id from the Mapping of regions and amis
```
Mappings:
  RegionMap:
    us-east-1:
      AMI: "ami-12345"
    us-east-2:
      AMI: "ami-34567"

Outputs:
  ImageIdused:
    Description: "Output the image id for the specific region"
    Value: !FindInMap [RegionMap, !Ref "AWS::Region", AMI]
```

### Using conditions.
Conditions allow you to conditionally create resources. Using functions such as
Fn::If, Fn::Equals and Fn::Not. These conditions are evaulated based on input parameters
that you declare when creating or updating the stack.


Example 1: Conditionally select instance type based on env type. use t3.medium if
prod env, else use t2.small.

```
Parameters:
  EnvType:
    Type: String
    Description: "Specify environment type (prod/dev)"
    AllowedValues: [prod, dev]

Conditions:
  CreateProdCondition: !Equals [!Ref EnvType, prod]
  CreateDevCondition: !Equals [!Ref EnvType, dev]

Resources:
  ProdInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: !If [CreateProdCondition, t3.medium, t2.small]
      KeyName: testkey

```

Example 2: Name a role differently based on prod vs dev.

```
Resources:
  CFNProdOnlyRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Join ["_", [!Ref RoleNamePrefix, !If [CreateProdCondition, "PRODONLY", "NOTPRODOTHER"]]]

```

Example 3: Create a resource only if the condition is met. This is where you want to
           create a resource only in certain conditions.
```
Conditions:
  CreateProdCondition: !Equals [!Ref EnvType, prod]
  CreateDevCondition: !Equals [!Ref EnvType, dev]

Resources:
  CFNDevOnlyRole:
    Condition: CreateDevCondition
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Join ["_", [!Ref RoleNamePrefix, "DEVONLY"]]
      Description: "CFN Prod Only Role"

```

### Importing values from another stack.
To use values created in one stack and reuse them in another stack, you can export
the specific value from one stack and then import that in another stack.

Example: Use the vpc id created in vpcone stack in the subnetone stack. An example created
         to show this

vpcone stack:
```
Resources:
  vpcOne:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: 'true'
:

Outputs:
  vpcOneId:
    Description: "VPC ID for the VPC"
    Value: !GetAtt [vpcOne, VpcId]
    Export:
      Name: !Sub "${AWS::StackName}-VPCID"

```

subnetone stack:
```
Resources:
  subnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        "Fn::ImportValue": "vpcone-VPCID"
      AvailabilityZone: 'us-east-1a'

```
Another way to do this:
```
Parameters:
  vpcStackName:
    Description: "Name of the cf stack that creates vpc"
    Type: String
    Default: vpcone

Resources:
  subnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        "Fn::ImportValue": !Join ["-", [ !Ref vpcStackName, "VPCID"]]

```


## Pseudo parameters.
Pseudo parameters are predefined by AWS cloudformation. you don't declare them in
your template. Use them the same way as you would a parameter usign !Ref function.

AWS::AccountId

AWS::NotificationARNs

























