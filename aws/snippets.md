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


## DynamoDB scan with filter

```
aws dynamodb scan --table-name TestData \
--filter-expression "build_status = :bs or build_status = :bs2" \
--expression-attribute-values '{":bs": {"S": "SUCCESS"}, ":bs2": {"S": "FAILURE"}}' \
--profile dev --output json --max-items 5000
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





