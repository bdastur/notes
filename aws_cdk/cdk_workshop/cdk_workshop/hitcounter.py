from constructs import Construct

from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
)


class HitCounter(Construct):
    def __init__(self, scope: Construct, id: str, downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        table = ddb.Table(
            self, "HitsTable",
            partition_key={'name': 'path', 'type': ddb.AttributeType.STRING})

        self._handler = _lambda.Function(
                self, "HitCountHandler", runtime=_lambda.Runtime.PYTHON_3_9, 
                handler="hitcounter.handler", code=_lambda.Code.from_asset("lambda"),
                environment={
                'DOWNSTREAM_FUNCTION': downstream.function_name,
                'HITS_TABLENAME': table.table_name,
            })




