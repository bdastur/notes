provider "aws" {
  region                  = var.region
  shared_credentials_files = var.credentials_files
  profile                 = var.profile
}

terraform {
  backend "s3" {
    bucket = "cwbench-terraform-state-us-east-1"
    key    = "tfstates/sample/sample.tfstate"
    kms_key_id = "arn:aws:kms:us-east-1:462972568455:alias/tfkey"
    region = "us-east-1"
    profile = "dev" 
  }
}

/****************************************
 * Lambda function Role.
 ****************************************/
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
 
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "lambda_role" {
  name = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json

}

/*****************************************
 *
 *****************************************/
data "archive_file" "lambda" {
  type = "zip"
  source_file = "source/main.py"
  output_path = "main/lambda_payload.zip"
}

resource "aws_lambda_function" "test_lambda" {
  function_name = "lambda_function_one"
  description   = "My tf created test function"
  role          = aws_iam_role.lambda_role.arn
  filename      = data.archive_file.lambda.output_path
  handler       = "main.handler"

  runtime       = "python3.9"
  architectures = ["x86_64"]
  
}
