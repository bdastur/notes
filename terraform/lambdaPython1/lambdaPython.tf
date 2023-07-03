/*************************************************************
 * Lambda 'mainLambda' function role.
 *************************************************************/

data "aws_iam_policy_document" "rolePolicyDoc" {
    statement {
        effect = "Allow"
        principals {
            type = "Service"
            identifiers = ["lambda.amazonaws.com"]
        }
        actions = ["sts:AssumeRole"]
    }
}

resource "aws_iam_role" "mainLambdaRole" {
    name = "main_lambda_role"
    assume_role_policy = data.aws_iam_policy_document.rolePolicyDoc.json
}

resource "aws_iam_role_policy" "mainLambdaRolePermissions" {
    name = "main_lambda_rolePermissions"
    role = aws_iam_role.mainLambdaRole.id

    # Policy definition.
    policy = jsonencode ({
        Version = "2012-10-17"
        Statement = [
            {
                Action = [
                    "s3:*",
                    "sns: *"
                ],
                Effect = "Allow"
                Resource = "*"
            }
        ]

    })
}

/*************************************************************
 * Lambda 'mainLambda' definition.
 *************************************************************/

data "archive_file" "mainLambdaSource" {
    type = "zip"
    source_dir = "source/"
    output_path = "bin/main_lambda_package.zip"
}

resource "aws_lambda_function" "mainLambda" {
    function_name = "main_lambda"
    description = "Test function - list buckets"
    role = aws_iam_role.mainLambdaRole.arn
    filename = data.archive_file.mainLambdaSource.output_path
    handler = "main.handler"
    # To rebuild on code change.
    source_code_hash = filebase64sha256(data.archive_file.mainLambdaSource.output_path)

    runtime = "python3.9"
    architectures = ["x86_64"]

}


// Enable Lambda logging to cloudwatch.

resource "aws_cloudwatch_log_group" "mainLambdaLogGroup" {
    name = join("/", ["/aws/lambda", aws_lambda_function.mainLambda.function_name])
    retention_in_days = 7
}


resource "aws_iam_role_policy" "cwLogsPermissions" {
    name = "main_lambda_cwLogsPermissions"
    role = aws_iam_role.mainLambdaRole.id

    # Policy definition.
    policy = jsonencode ({
        Version = "2012-10-17"
        Statement = [
            {
                Action = [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                Effect = "Allow",
                Resource = join("", [aws_cloudwatch_log_group.mainLambdaLogGroup.arn, "*"])

            }
        ]

    })
}

/*************************************************************
 * Cloudwatch eventbridge timer rule to trigger lambda at regular
 * interval.
 *************************************************************/
resource "aws_cloudwatch_event_rule" "timerRule" {
    name = "timer-rule"
    schedule_expression = "rate(20 minutes)"
}


resource "aws_cloudwatch_event_target" "targetLambda" {
    rule = aws_cloudwatch_event_rule.timerRule.name
    arn = aws_lambda_function.mainLambda.arn
}

resource "aws_lambda_permission" "allow_cw_to_call_lambda" {
    action = "lambda:InvokeFunction"
    function_name = aws_lambda_function.mainLambda.function_name
    principal = "events.amazonaws.com"
    source_arn = aws_cloudwatch_event_rule.timerRule.arn
}











