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
 * A simple lambda function.
 * Python 3.9.
 * Local file system source.
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

/*****************************************
 * Permissions to allow api gateway to 
 * call the lambda function.
 *****************************************/
resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.test_lambda.function_name}"
  principal     = "apigateway.amazonaws.com"

  # The /*/* portion grants access from any method on any resource
  # within the API Gateway "REST API".
  source_arn = "${aws_apigatewayv2_api.simpleApi.execution_arn}/*/*"
}
