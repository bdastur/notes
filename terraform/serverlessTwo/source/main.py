import json

def handler(event, context):
    print(json.dumps(event))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello CDK Version 1.0!, you have hit url %s\n' % event['path']
    }

