import json
import os

import boto3

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['HITS_TABLENAME'])
_lambda = boto3.client('lambda')


def handler(event, context):
    print(json.dumps(event))

    table.update_item(
        Key={'path': event['path']},
        UpdateExpression='Add hits :incr',
        ExpressonAttributeValues={':incr': 1}
    )

    resp = _lambda.invoke(FunctionName=os.environ['DOWNSTREAM_FUNCTION'],
                          Payload=json.dumps(event))

    body = resp['Payload'].read()

    print("Downsteram reponse %s" % body)
    return json.loads(body)

