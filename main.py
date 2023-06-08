import json

def lambda_handler(event, context):
    print("In lambda handler")
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from ArtAlchemy!')
    }
