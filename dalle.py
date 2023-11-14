from openai import OpenAI


def generate_image(prompt, api_key):

    client = OpenAI(
        api_key=api_key,
    )

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    return image_url
