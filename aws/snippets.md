# Snippets of code or cli for simple tasks.

## Describing EC2 Security groups, filter by tags:


```
aws ec2 describe-security-groups \
    --profile dev1 \
    --region us-west-2 \
    --filter  "Name=tag:ClusterStartedBy,Values=john.doe" "Name=tag:aws:cloudformation:logical-id,Values=SecurityGroupEtcd"
```

**Find sg tag have tag Name=httpsg and tag Stack=dev**
```
aws ec2 describe-security-groups \
    --region ca-central-1 \
    --filter "Name=tag:Name,Values=httpsg" "Name=tag:Stack,Values=dev" | jq -r '.SecurityGroups[].GroupId'
```

**use jq to parse json outtput**
```
aws ec2 describe-security-groups \
    --profile dev1 \
    --region us-west-2 \
    --output json \
    --filter  "Name=tag:ClusterStartedBy,Values=john.doe" "Name=tag:aws:cloudformation:logical-id,Values=SecurityGroupEtcd" | jq -r '.SecurityGroups[]| [.GroupId,.VpcId,.Tags] '

```


```
aws ec2 describe-instances \
    --region us-west-2 \
    --filters="Name=tag:Name,Values=general" \
    --output json| jq -r '.Reservations[].Instances[]| .InstanceId'

```

**describe tags. Filter by resource-id**
```
aws ec2 describe-tags --filters="Name=resource-id, Values=vpc-016xxxxxec1" --profile dev1
```

**describe tags. Filter by tag:Name**
```
$ aws ec2 describe-tags --filters="Name=tag:Name, Values=ctest" --profile dev1
```

**Create a new tag.**
```
aws ec2 create-tags  --resources vpc-01xxxxxxxxxxc1 --tags="Key=Protected,Value=true" --profile dev1
```


## Detach IAM managed policies from roles and delete them.
```
#!/bin/bash

roles=$(aws iam list-roles --output text | grep ROLES| grep prod-env| awk -F" " '{print $6'})

for role in $roles
do
    echo $role
    policies=$(aws iam list-attached-role-policies --role-name $role  --output text | grep ATTACHEDPOLICIES | grep myenv- | awk -F" " '{print $2}')
    for policy in $policies
    do
        echo "Role: $role, policY: $policy"
        aws iam detach-role-policy --role-name $role --policy-arn $policy
        sleep 1
        aws iam delete-policy --policy-arn $policy
    done
done

```

## Ec2 get spot price history

*by instance type, az, filter product description, start/end time*
```
aws ec2 --output json \
  describe-spot-price-history --instance-types r4.8xlarge \
  --availability-zone us-west-2a \
  --filters Name=product-description,Values=Linux/UNIX \
  --start-time 2019-10-01 --end-time 2019-10-12
```

## EC2 - describe instances created after certain launch time.
This example was given in [https://github.com/aws/aws-cli/issues/1209](https://github.com/aws/aws-cli/issues/1209)
Using [JMESPatch query language](https://jmespath.org/tutorial.html)

```
aws ec2 describe-instances \
  --query 'Reservations[].Instances[?LaunchTime>=`2020-06-04`][].{id: InstanceId, type: InstanceType, launched: LaunchTime}'
```

## DynamoDB create table:

NOTE: During table creation only specify the primary key and one non-key attribute
you might use for secondary index. You do not need to specify any non-key attributes


ddb_table_definition json file:
Note you do not need to specify any attributes 
```
%~> cat ddb_table_definition.json 
{
    "AttributeDefinitions": [
        {
            "AttributeName": "EmployeeId",
            "AttributeType": "S"
        },
        {
            "AttributeName": "Tenure",
            "AttributeType": "N"
        }
    ],
    "TableName": "employee_table",
    "KeySchema": [
        {
            "AttributeName": "EmployeeId",
            "KeyType": "HASH"
        },
        {
            "AttributeName": "Tenure",
            "KeyType": "RANGE"
        }
    ],
    "BillingMode": "PROVISIONED",
    "ProvisionedThroughput": {
        "ReadCapacityUnits": 1,
        "WriteCapacityUnits": 2
    },
    "SSESpecification": {
        "Enabled": false
    },
    "Tags": [
        {
            "Key": "Application",
            "Value": "ddbtesting"
        }
    ],
    "TableClass": "STANDARD"
}

```


```
%~> aws dynamodb create-table \
  --cli-input-json file://ddb_table_definition.json \
  --profile dev --region us-east-1

```

## DynamoDB scan with filter
```
aws dynamodb scan --table-name TestData \
--filter-expression "build_status = :bs or build_status = :bs2" \
--expression-attribute-values '{":bs": {"S": "SUCCESS"}, ":bs2": {"S": "FAILURE"}}' \
--profile dev --output json --max-items 5000
```

Using contains expression.
```
> aws dynamodb scan --table-name TestTable \
--filter-expression "contains(LockID, :li)" \
--expression-attribute-values '{":li": {"S": "myprodenv"} }' \
--profile prod --region ca-central-1
```


## DynamoDB put-item example

```
aws dynamodb put-item --table-name brdtest \
--item '{"cluster_name": {"S": "test1"}, "creation_date": {"S": "2021-12-21"},
         "owner": {"S": "john"}, "status": {"S": "inprogress"}}' \
 --profile dev1
```

**Another example of put-item. Item defined in file**

```
~> cat /tmp/items.json
{"cluster_name": {"S": "test2"},
 "creation_date": {"S": "2021-12-21"},
 "owner": {"S": "john"},
 "status": {"S": "inprogress"}
}
> aws dynamodb put-item --table-name brdtest --item file:///tmp/items.json --profile dev1

```

**Return consumed capacity for the operation**

```
aws dynamodb put-item --table-name brdtest \
--item file:///tmp/items.json \
--return-consumed-capacity TOTAL \
--profile dev1
```

## DynamoDB Query operation.

```
> cat /tmp/attributes.json
{
  ":name": {"S": "test1"},
  ":date": {"S": "2021-12-21"}
}
%~> aws dynamodb query --table-name brdtest \
--key-condition-expression "cluster_name = :name and creation_date = :date" \
--expression-attribute-values file:///tmp/attributes.json \
--profile dev1
{
    "Items": [
        {
            "owner": {
                "S": "john"
            },
            "cluster_name": {
                "S": "test1"
            },
            "creation_date": {
                "S": "2021-12-21"
            },
            "status": {
                "S": "inprogress"
            }
        }
    ],
    "Count": 1,
    "ScannedCount": 1,
    "ConsumedCapacity": null
}

```

## DynamoDB batch-write items:
```
%~> cat /tmp/items.json
{
    "brdtest": [
    {
        "PutRequest": {
            "Item": {
                "cluster_name": {"S": "test3"},
                "creation_date": {"S": "2022-01-21"},
                "owner": {"S": "John Smith"},
                "status": {"S": "inprogress"}
            }
        }
    },
    {
        "PutRequest": {
            "Item": {
                "cluster_name": {"S": "test4"},
                "creation_date": {"S": "2022-01-21"},
                "owner": {"S": "John Smith"},
                "status": {"S": "inprogress"}
            }
        }
    },
    {
        "PutRequest": {
            "Item": {
                "cluster_name": {"S": "test5"},
                "creation_date": {"S": "2022-01-21"},
                "owner": {"S": "John Smith"},
                "status": {"S": "inprogress"}
            }
        }
    }
]
}
%~> aws dynamodb batch-write-item --request-items file:///tmp/items.json --profile dev1
{
    "UnprocessedItems": {}
}

```
**Another Example**

```
{
    "RequestItems": {
        "employee_table": [
            {
                "PutRequest": {
                    "Item": {
                        "EmployeeId": {"S": "00103"},
                        "Tenure": {"N": "4"},
                        "Name": {"S": "John Loui"},
                        "Skills": {"SS": ["Java", "C++", "programming"]},
                        "Details": {"M": {
                            "Title": {"S": "Sofware Engineer III"},
                            "Rating": {"S": "Above Average"}
                        }}
                    }
                }
            },
            {
                "PutRequest": {
                    "Item": {
                        "EmployeeId": {"S": "00104"},
                        "Tenure": {"N": "3"},
                        "Name": {"S": "Jack Smith"},
                        "Skills": {"SS": ["Python", "C++", "programming"]},
                        "Details": {"M": {
                            "Title": {"S": "Sofware Engineer IV"},
                            "Rating": {"S": "Above Average"}
                        }}
                    }
                }
            }
        ]
    },
    "ReturnConsumedCapacity": "INDEXES",
    "ReturnItemCollectionMetrics": "SIZE"
}

%~> aws dynamodb batch-write-item \
    --cli-input-json file://putitems.json \
    --profile dev --region us-east-1

```





## DynamoDB update items:
```
aws dynamodb update-item --table-name TestTable --key '{"resourceId": {"S": "abc-1112221"}}' \
  --update-expression "SET #LS = :ls" \
  --expression-attribute-names '{"#LS": "lastSorted"}' \
  --expression-attribute-values '{":ls": {"N": "1482727701837"}}' \
  --profile dev --region us-west-2
```


## EBS Volumes. Find available volumes.
```
aws ec2 describe-volumes \
    --filters "Name=status,Values=available" \
    --profile dev1 --output json
```

# EBS Volumes. Find available gp2 volumes.
```
aws ec2 describe-volumes \
    --filters "Name=status,Values=available" "Name=volume-type,Values=gp2" \
    --profile dev1 --output json

```


## Calculate AWS S3 bucket size using cli:

```
   aws s3 ls s3://xyz.acmecorp.com/xyz.acmecorp.com --recursive --human-readable --summarize

```

## Get AWS Cloudwatch metrics.

### Get Duration for a specific lambda function.

create a cli input json file as below:
```
   {
    "MetricDataQueries": [
        {
            "Id": "myRequest",
            "MetricStat": {
                "Metric": {
                    "Namespace": "AWS/Lambda",
                    "MetricName": "Duration",
                    "Dimensions": [
                        {
                            "Name": "FunctionName",
                            "Value": "HelloWorld"
                        }
                    ]
                },
                "Period": 3600,
                "Stat": "Average",
                "Unit": "Milliseconds"
            },
            "Label": "myRequestLabel",
            "ReturnData": true
        }
    ],
    "StartTime": "2021-06-10T10:40:0000",
    "EndTime": "2021-06-23T14:12:0000"
}

```

Execute cli:
```
   aws cloudwatch get-metric-data --cli-input-json file://cw_metric.json --profile test

```



## Cognito userpools

**List user pools**
```
~> aws cognito-idp list-user-pools --profile dev1 --max-results 5 --output text
USERPOOLS	1641738585.975	us-west-2_0VwrsEoVZ	1641738585.975	testuserpool
```

```

**List users in a cognito user pool**

```
> aws cognito-idp list-users --user-pool-id us-west-2_0VwrsEoVZ --profile dev1 --output text
USERS	True	1641738784.888	1641738784.888	FORCE_CHANGE_PASSWORD	b2dcee5b-aae4-4e3b-93d7-34ac7c1bbe17
ATTRIBUTES	sub	b2dcee5b-aae4-4e3b-93d7-34ac7c1bbe17
ATTRIBUTES	email_verified	true
ATTRIBUTES	email	xxxxxx@xxxx.xxx

```

**Create a user pool client**

```
aws cognito-idp create-user-pool-client --user-pool-id us-west-2_BLcbQ9DHK --client-name testclient1 --profile dev1
{
    "UserPoolClient": {
        "UserPoolId": "us-west-2_BLcbQ9DHK",
        "ClientName": "testclient1",
        "ClientId": "8ik2s2uk8d9ekh7k3s1hstlgt",
        "LastModifiedDate": 1641740003.101,
        "CreationDate": 1641740003.101,
        "RefreshTokenValidity": 30,
        "TokenValidityUnits": {},
        "AllowedOAuthFlowsUserPoolClient": false,
        "EnableTokenRevocation": true
    }
}
```

**User sign-up**
This command will send an email to the email provided, with a confirmation code,
which will be used in the subsequent confirm signup step.

```
aws cognito-idp sign-up --client-id 8ik2s2uk8d9ekh7k3s1hstlgt \
--username xyz@acme.com --password xxxxx  \
--user-attributes Name="email",Value="xxxx@acme.com" --profile dev1
{
    "UserConfirmed": false,
    "CodeDeliveryDetails": {
        "Destination": "x***@x***.xxx",
        "DeliveryMedium": "EMAIL",
        "AttributeName": "email"
    },
    "UserSub": "9301f852-88c2-4613-b70a-7b67ccb1fe92"
}
```

**User confirm signup**
```
~> aws cognito-idp confirm-sign-up --client-id 8ik2s2uk8d9ekh7k3s1hstlgt \
--username xxxxxx@acme.xxx \
--confirmation-code 821489 --profile dev1
%~> 

```

**Login initiate Authentication**
```
~> aws cognito-idp initiate-auth \
--client-id 8ik2s2uk8d9ekh7k3s1hstlgt \
--auth-flow USER_PASSWORD_AUTH \
--auth-parameters USERNAME=behzad.dastur@workday.com,PASSWORD=Password@1 --profile dev1
{
    "ChallengeParameters": {},
    "AuthenticationResult": {
        "AccessToken": "whYhsUITzQQ3eBXAwI6VX7Gi7Dmv2eP3T1w",
        "ExpiresIn": 3600,
        "TokenType": "Bearer",
        "RefreshToken": "RwrB-FIu6ZaQkv3AP_htR9QhD.hHZoXervix8HcvMnyi8oVw",
        "IdToken": "Ngf2ZbCZZ-FJwY-7ptPGpKMdA7NjjYVX8hM7DA"
    }
}

```



## Cognito Identity pools.

**Create a new Identity pool**
```
 %~> aws cognito-identity create-identity-pool \
--identity-pool-name testidentitypool \
--no-allow-unauthenticated-identities \
--cognito-identity-providers \
ProviderName="cognito-idp.us-west-2.amazonaws.com/us-west-2_BLcbQ9DHK",ClientId="8ik2s2uk8d9ekh7k3s1hstlgt"
{
    "IdentityPoolId": "us-west-2:7ee6b627-f894-4b3b-bc7c-1107c054e6de",
    "IdentityPoolName": "testidentitypool",
    "AllowUnauthenticatedIdentities": false,
    "CognitoIdentityProviders": [
        {
            "ProviderName": "cognito-idp.us-west-2.amazonaws.com/us-west-2_BLcbQ9DHK",
            "ClientId": "8ik2s2uk8d9ekh7k3s1hstlgt",
            "ServerSideTokenCheck": false
        }
    ],
    "IdentityPoolTags": {}
}

```

**Delete identity pool**
```
aws cognito-identity delete-identity-pool \
--identity-pool-id us-west-2:c5d8e930-89ff-49df-b097-d6672ab39b05 \
--profile dev1
```
**Set identity pool roles**
```
> aws cognito-identity set-identity-pool-roles \
--identity-pool-id us-west-2:7ee6b627-f894-4b3b-bc7c-1107c054e6de \
--roles authenticated=arn:aws:iam::461168169469:role/Cognito_testidentitypoolAuth_Role

```

**Get Cognito identity pool Identity Id**
The login information is available from the `aws cognito-idp initate-auth` CLI
IdToken value.

```
 %~> aws cognito-identity get-id \
--identity-pool-id us-west-2:7ee6b627-f894-4b3b-bc7c-1107c054e6de \
--login  cognito-idp.us-west-2.amazonaws.com/us-west-2_BLcbQ9DHK=eyJraWQiOiJlMF.....Z20mCsfhv4RHy0GSdJxLvZkZ-w10Gloz8cApb71QrvxY2vPvqq0klDvWzeA
{
    "IdentityId": "us-west-2:bbc7f768-1a17-4c02-8f48-56d2e84c3947"
}

```

**Get cognito identity credentials**
Use the IdentityId from the get-id command
```
~> aws cognito-identity get-credentials-for-identity \
--identity-id us-west-2:bbc7f768-1a17-4c02-8f48-56d2e84c3947 \
--login  cognito-idp.us-west-2.amazonaws.com/us-west-2_BLcbQ9DHK=eyJraWQ......sj5bOd3hu824g --profile dev1
{
    "IdentityId": "us-west-2:bbc7f768-1a17-4c02-8f48-56d2e84c3947",
    "Credentials": {
        "AccessKeyId": "AS....O57QPE",
        "SecretKey": "f....CJsfDV5Y2jW",
        "SessionToken": "IQWvwc.......BDXm+5khWB5m/NWYUbf7leZ/Sk2f2y4Le",
        "Expiration": 1641857034.0
    }
}
```












