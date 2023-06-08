import json

def lambda_handler(event, context):
    if 'queryStringParameters' in event:
        query_string_params = event['queryStringParameters']

        if 'access_token' in query_string_params and 'username' in query_string_params:

            access_token = query_string_params['access_token']
            username = query_string_params['username']
            print(access_token)
            print(username)
            return {
            'statusCode': 200,
            'body': json.dumps('Hello from ArtAlchemy!')
            }
        else:
            response = {
            'statusCode': 400,
            'body': json.dumps('Missing access_token or username')
            }
            print(response)
            return response
        
    response = {
    'statusCode': 400,
    'body': json.dumps('Missing query string parameters')
    }
    print(response)
    return response


event = {'queryStringParameters': {'access_token': '1234', 'username': 'wasabiibunni'}}
lambda_handler(event, None)