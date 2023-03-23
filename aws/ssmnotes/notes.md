# AWS System Manager

## Useful Links:
* [SSM Documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)





## Running SSM command on an instance:

```
aws ssm send-command \
  --document-name "AWS-ConfigureDocker" \
  --document-version "1" \
  --targets '[{"Key":"InstanceIds","Values":["i-09341c5ce9586dd4b"]}]' \
  --parameters '{"action":["Install"]}' \
  --timeout-seconds 600 --max-concurrency "50" --max-errors "0" \
  --region us-east-1
```

## Running SSM command on instances matching specific tag.

```
aws ssm send-command \
  --document-name "AWS-ConfigureDocker" \
  --document-version "1" \
  --targets '[{"Key":"tag:SSMEnabled","Values":["True"]}]' \
  --parameters '{"action":["Install"]}' \
  --timeout-seconds 600 --max-concurrency "50" --max-errors "0" \
  --region us-east-1
```

## Running a ShellScript
```
aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --document-version "1" \
  --targets '[{"Key":"tag:SSMEnabled","Values":["True"]}]' \
  --parameters '{"workingDirectory":[""],"executionTimeout":["3600"],"commands":["ps -ef","df -h","pwd",""]}' \
  --timeout-seconds 600 --max-concurrency "50" --max-errors "0" \
  --region us-east-1
```
