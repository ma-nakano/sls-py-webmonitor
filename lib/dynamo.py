import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ["SITE_TABLE_NAME"])


def put_site(site):
    """
    :param dict site:{"name": "foo.com", "url": "https://foo.com"}
    Put Site Data in DynamoDB
    """
    table.put_item(Item=site)


def get_sites():
    """
    Get ALL Site Data in DynamoDB
    """
    response = table.scan()
    return response["Items"]


def remove_site(uuid):
    """
    Remove Site Data in DynamoDB
    """
    table.delete_item(Key={"id": uuid})


def update_site(uuid, new_code):
    """
    Update Site Data
    """
    table.update_item(
        Key={
            'id': uuid,
        },
        UpdateExpression='SET code = :val1',
        ExpressionAttributeValues={
            ':val1': new_code
        }
    )
