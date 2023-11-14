import boto3
from botocore.exceptions import ClientError
import json


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
    secret_dict = json.loads(get_secret_value_response['SecretString'])
    return secret_dict['openAIKey']
