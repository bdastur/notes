from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from .hitcounter import HitCounter



class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function
        myLambda = _lambda.Function(self, 'HelloHandler', 
                                    runtime=_lambda.Runtime.PYTHON_3_9, 
                                    code=_lambda.Code.from_asset('lambda'), 
                                    handler='hello.handler')

        # Use our hit counter.
        helloWithCounter = HitCounter(self, "HelloHitCounter", downstream=myLambda)


        myApi = apigw.LambdaRestApi(
                self, 'Endpoint',
                handler=helloWithCounter._handler)
