import json
from chatgpt import get_image_description
from dalle import generate_image
from utils import get_secret


def lambda_handler(event, context):
    if 'body' in event:
        body = json.loads(event['body'])

        base64_image = body.get('imageData')
        selected_style = body.get('style')

        api_key = get_secret()

        # Get image description using ChatGPT
        prompt = get_image_description(base64_image, api_key, selected_style)

        # Generate a new image using DALL-E with the description and style
        new_image = generate_image(prompt, api_key)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'  # or your specific origin
            },
            'body': json.dumps({'newImage': new_image})
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('No payload provided')
        }
