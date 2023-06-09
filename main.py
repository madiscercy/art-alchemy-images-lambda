import json
from deviant_art_service import DeviantArtService


def lambda_handler(event, context):
    query_string_params = event['queryStringParameters']

    if query_string_params is not None and 'access_token' in query_string_params and 'username' in query_string_params:

        access_token = query_string_params['access_token']
        username = query_string_params['username']

        deviant_art_service = DeviantArtService()
        images = deviant_art_service.get_images(access_token, username)
        if images is not None and len(images) > 0:
            response = {
                'statusCode': 200,
                'body': json.dumps(images)
            }
            print(response)
            return response

        return {
            'statusCode': 400,
            'body': json.dumps('No images found.')
        }
    else:
        response = {
            'statusCode': 400,
            'body': json.dumps('Missing access_token or username')
        }
        print(response)
        return response


event = {'queryStringParameters': {
    'access_token': '4f92c6a79c79e100d720f5fd692c6f10d20724a60c022daf7f', 'username': 'wasabiibunni'}}
lambda_handler(event, None)
