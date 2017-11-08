from uuid import uuid1
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('nagashima-serverless')


def create_site(event, context):
    """
    :param dict event:{"name": "foo.com", "url": "https://foo.com"}
    Put Site Data in DynamoDB
    """
    responce = table.scan()
    return responce["Items"];

def get_sites(event, context):
    """
    Get ALL Site Data in DynamoDB
    """
    pass


def remove_site(event, context):
    """
    Remove Site Data in DynamoDB
    """
    pass


def update_site_state(event, context):
    """
    Update Site Data
    """
    pass
