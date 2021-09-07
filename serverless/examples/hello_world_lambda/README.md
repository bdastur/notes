# Lambda Example.

## Description.

The terraform module creates a simple lambda function with runtime python. It also creates
cloudwatch schedule event to trigger it every 5 minutes.

## Resources

```
%~> terraform show | grep resource

resource "aws_cloudwatch_event_rule" "cw_schedule_5m"
resource "aws_cloudwatch_event_target" "cw_invoke_lambda"
resource "aws_iam_role" "iam_lambda_role"
resource "aws_iam_role_policy_attachment" "lamba_role_policy_attachment"
resource "aws_lambda_function" "hello_example"

```
