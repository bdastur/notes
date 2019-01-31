# Snippets of code or cli for simple tasks.

## Describing EC2 Security groups, filter by tags:

```
aws ec2 describe-security-groups \
    --profile dev \
    --region us-west-2 \
    --filter Name=tag:ClusterOwner,Values=dummy --filter Name=tag:ClusterStartedBy,Values=john_doe
```
