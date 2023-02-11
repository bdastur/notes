# Cloudformation Notes.

## Links:

* [AWS Cloudformation guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)


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

























