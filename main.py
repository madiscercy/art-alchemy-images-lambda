import json
from chatgpt import get_image_description
from dalle import generate_image
from utils import decode_base64_image, get_secret


def lambda_handler(event, context):
    # Extracting image data and style from the event
    base64_image = event['imageData']
    selected_style = event['style']
    api_key = get_secret()

    # Decode the base64 image
    image = decode_base64_image(base64_image)

    # Get image description using ChatGPT
    prompt = get_image_description(base64_image, api_key, selected_style)

    # Generate a new image using DALL-E with the description and style
    new_image = generate_image(prompt, api_key)

    # Return the new image as a response (or a URL to the image if stored in S3)
    return {
        'statusCode': 200,
        'body': json.dumps({'newImage': new_image})
    }
