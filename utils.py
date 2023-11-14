import boto3
from botocore.exceptions import ClientError


def get_secret():
    secret_name = "openAI_Key"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    print(get_secret_value_response)
    secret = get_secret_value_response['SecretString']
    return secret


# # Decode the image and show it
# decoded_image = decode_base64_image(base64_image_string)
# decoded_image.show()
