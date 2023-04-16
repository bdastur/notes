/********************************************************************************
 * Rest API.
 ********************************************************************************/


/*
 * Rest API Definition
 */

resource "aws_api_gateway_rest_api" "restApi" {
  name = "lambdaOne"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}


/*
 * Rest API Resources
 */
resource "aws_api_gateway_resource" "restApiResourceRoot" {
    rest_api_id = aws_api_gateway_rest_api.restApi.id 
    parent_id   = aws_api_gateway_rest_api.restApi.root_resource_id
    path_part   = "foo"
}

resource "aws_api_gateway_resource" "restApiResourceOne" {
  rest_api_id = aws_api_gateway_rest_api.restApi.id
  parent_id   = aws_api_gateway_resource.restApiResourceRoot.id
  path_part   = "tasks"
}

resource "aws_api_gateway_method" "restApiResourceOneAny" {
  rest_api_id   = aws_api_gateway_rest_api.restApi.id
  resource_id   = aws_api_gateway_resource.restApiResourceOne.id
  http_method   = "ANY"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "restApiResourceOneIntegration" {
  rest_api_id = aws_api_gateway_rest_api.restApi.id  
  resource_id = aws_api_gateway_resource.restApiResourceOne.id  
  #http_method = aws_api_gateway_method.restApiResourceOneAny.http_method 
  http_method = "ANY"
  integration_http_method = "ANY"
  type        = "AWS"
  uri         = aws_lambda_function.lambdaOne.invoke_arn

  timeout_milliseconds = 15000

  passthrough_behavior    = "WHEN_NO_MATCH"
  content_handling        = "CONVERT_TO_TEXT"
}

/*
 * Rest API Deployment
 */
resource "aws_api_gateway_deployment" "restApiDeployment" {
  rest_api_id = aws_api_gateway_rest_api.restApi.id

  lifecycle {
    create_before_destroy = true
  }
}

/*
 * Rest API stage.
 */
resource "aws_api_gateway_stage" "restApiStageDev" {
  deployment_id = aws_api_gateway_deployment.restApiDeployment.id
  rest_api_id   = aws_api_gateway_rest_api.restApi.id
  stage_name    = "dev"
  description   = "Development Stage"
}

