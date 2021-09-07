import json

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
   
    return {
        "isBase64Encoded": "true",
        "statusCode": 200,
        "headers": { "Content-Type": "application/json"},
        "body": "Lambda Response"
    }
    
    #raise Exception('Something went wrong')

