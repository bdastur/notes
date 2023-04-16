#!/bin/bash

# Import rest API.

# Import REST API.
# terraform import aws_api_gateway_rest_api.restApi <api id>
terraform import aws_api_gateway_rest_api.restApi 9rukk9funf

# Import Resource.
# terraform import aws_api_gateway_resource.restApiResourceOne <api id>/<resource id>
terraform import aws_api_gateway_resource.restApiResourceOne 9rukk9funf/s80lp0

# Import Method.
# terraform import aws_api_gateway_method.restApiResourceOneAny <api id>/<resource id>/<METHOD>
terraform import aws_api_gateway_method.restApiResourceOneAny 9rukk9funf/s80lp0/ANY

# Import Integration.
# terraform import aws_api_gateway_integration.restApiResourceOneIntegration <api id>/<Resource id>/HTTP Method
terraform import aws_api_gateway_integration.restApiResourceOneIntegration 9rukk9funf/s80lp0/ANY

# Import deployment.
# terraform import aws_api_gateway_deployment.restApiDeployment <api id>/<deployment id>
terraform import aws_api_gateway_deployment.restApiDeployment 9rukk9funf/vlx59n


# Import stage.
# terraform import aws_api_gateway_stage.restApiStageDev <api id>/<stage name>
terraform import aws_api_gateway_stage.restApiStageDev 9rukk9funf/dev

