import requests
import json


def get_image_description(image, api_key, selected_style):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": 'Find what is in this image and then format a prompt to create a similar image in the style of ' + selected_style + '. Return in this format {"description": "description", "prompt": "prompt"}. Be descriptive and creative!'
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(response.json())
    content = response.json().get('choices')[0].get('message').get('content')
    prompt = json.loads(content).get('prompt')
    return prompt
