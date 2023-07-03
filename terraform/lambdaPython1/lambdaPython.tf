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
            },
            {
                Action = [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                Effect = "Allow",
                Resource = "arn:aws:logs:us-east-1:462972568455:log-group:*:*"

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





















