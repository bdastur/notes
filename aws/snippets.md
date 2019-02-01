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
