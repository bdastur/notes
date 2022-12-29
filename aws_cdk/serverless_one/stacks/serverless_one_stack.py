from aws_cdk import (
    Stack,
    aws_apigatewayv2 as apigw2
)
from constructs import Construct

class ServerlessOneStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Rest API.

