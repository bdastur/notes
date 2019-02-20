# Snippets of code or cli for simple tasks.

## Describing EC2 Security groups, filter by tags:


```
aws ec2 describe-security-groups \
    --profile dev1 \
    --region us-west-2 \
    --filter  "Name=tag:ClusterStartedBy,Values=john.doe" "Name=tag:aws:cloudformation:logical-id,Values=SecurityGroupEtcd"
```

*Find sg tag have tag Name=httpsg and tag Stack=dev*
```
aws ec2 describe-security-groups \
    --region ca-central-1 \
    --filter "Name=tag:Name,Values=httpsg" "Name=tag:Stack,Values=dev" | jq -r '.SecurityGroups[].GroupId'
```

*use jq to parse json outtput*
```
aws ec2 describe-security-groups \
    --profile dev1 \
    --region us-west-2 \
    --output json \
    --filter  "Name=tag:ClusterStartedBy,Values=cathal.conroy" "Name=tag:aws:cloudformation:logical-id,Values=SecurityGroupEtcd" | jq -r '.SecurityGroups[]| [.GroupId,.VpcId,.Tags] '

```



```
aws ec2 describe-instances --region us-west-2 --filters="Name=tag:Name,Values=general" --output json| jq -r '.Reservations[].Instances[]| .InstanceId'

```

*describe tags. Filter by resource-id*
```
aws ec2 describe-tags --filters="Name=resource-id, Values=vpc-016xxxxxec1" --profile dev1 
```

*describe tags. Filter by tag:Name*
```
$ aws ec2 describe-tags --filters="Name=tag:Name, Values=ctest" --profile dev1 
```

*Create a new tag.*
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
