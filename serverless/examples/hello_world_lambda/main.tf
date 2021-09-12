provider "aws" {
  region                  = var.region
  shared_credentials_file = var.credentials_file
  profile                 = var.profile
}

/*
 * Using S3 backend. backed definition in custom_backend.tf  
 */
terraform {
  backend "s3" {
    bucket = "us-west-2-dev1-ilm-state"
    key    = "lambda/hello_world/lambda.tfstate"
    region = "us-west-2"
    profile = "dev1"
  }
}


resource "aws_iam_role" "iam_lambda_role" {
    name = "example_lambda_iam_role"
    assume_role_policy = <<POLICY
{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": "sts:AssumeRole",
          "Principal": {
            "Service": "lambda.amazonaws.com"
          },
          "Effect": "Allow",
          "Sid": ""
        }
      ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "lamba_role_policy_attachment" {
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    role       = aws_iam_role.iam_lambda_role.name
}

data "aws_lambda_layer_version" "py38_layer" {
    layer_name = "py38_layer"
}


resource "aws_lambda_function" "hello_example" {
    filename = "code/hello_example.zip"
    description = "Example - terraform created lambda function"
    function_name = "hello_example"
    role = aws_iam_role.iam_lambda_role.arn 
    handler = "lambda_function.lambda_handler"

    source_code_hash = filebase64sha256("code/hello_example.zip")
    runtime = "python3.8"

    environment {
        variables = {
            name = "Behzad"
        }
    }
    tags = var.tags
    layers = [data.aws_lambda_layer_version.py38_layer.arn]
}


resource "aws_cloudwatch_event_rule" "cw_schedule_5m" {
    name = "cloudwatch_schedule_timeout"
    description = "Cloudwatch event rule to trigger every 5 mins"
    schedule_expression = "rate(5 minutes)"
    is_enabled = true
}

resource "aws_cloudwatch_event_target" "cw_invoke_lambda" {
    rule = aws_cloudwatch_event_rule.cw_schedule_5m.name
    arn = aws_lambda_function.hello_example.arn
}
