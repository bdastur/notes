from aws_cdk import (
    Stack,
    aws_apigateway as apigw
)
from constructs import Construct

class ServerlessOneStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Rest API.
        restApi = apigw.CfnRestApi(self, "MyCfnRestAPI",)
