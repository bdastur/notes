/*
 * HTTP API.
 */

resource "aws_apigatewayv2_api" "simpleApi" {
  name          = "simple-http-api"
  protocol_type = "HTTP"
}


resource "aws_apigatewayv2_integration" "simpleApiIntegration" {
  api_id             = aws_apigatewayv2_api.simpleApi.id
  description        = "Simple API Integration"
  integration_type   = "AWS_PROXY"
  integration_method = "POST"
  integration_uri    = aws_lambda_function.test_lambda.invoke_arn
  connection_type    = "INTERNET"
}


resource "aws_apigatewayv2_route" "simpleApiRoute" {
  api_id = aws_apigatewayv2_api.simpleApi.id
  route_key = "ANY /test/{proxy+}"

  target = "integrations/${aws_apigatewayv2_integration.simpleApiIntegration.id}"
}


resource "aws_apigatewayv2_stage" "dev" {
  api_id = aws_apigatewayv2_api.simpleApi.id
  name = "dev"
  auto_deploy = true

  default_route_settings {
    detailed_metrics_enabled = true
  }

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.simpleApiLogGroup.arn
    format          = jsonencode(
      {
        httpMethod     = "$context.httpMethod"
        ip             = "$context.identity.sourceIp"
        protocol       = "$context.protocol"
        requestId      = "$context.requestId"
        requestTime    = "$context.requestTime"
        responseLength = "$context.responseLength"
        routeKey       = "$context.routeKey"
        status         = "$context.status"
      }
    )
  }

}

resource "aws_apigatewayv2_deployment" "stagingDeployment" {                         
  depends_on = [aws_apigatewayv2_route.simpleApiRoute]

  api_id      = aws_apigatewayv2_api.simpleApi.id                                    
  description = "Staging Deployment"                                                 
}        


output "apiendpoint" {
    value = aws_apigatewayv2_api.simpleApi.api_endpoint
}

/*
resource "local_file" "outputfile" {
    content = aws_apigatewayv2_api.simpleApi.api_endpoint 
    filename = "./apiendpoint"
}
*/

