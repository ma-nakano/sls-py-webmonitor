from uuid import uuid1
import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["SITE_TABLE_NAME"])


def create_site(site):
    """
    :param dict event:{"name": "foo.com", "url": "https://foo.com"}
    Put Site Data in DynamoDB
    """
    site["id"] = str(uuid1())
    table.put_item(Item=site)


def get_sites():
    """
    Get ALL Site Data in DynamoDB
    """
    response = table.scan()
    return response["Items"]


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
