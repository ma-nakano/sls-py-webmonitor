import requirements
import boto3
import lib.dynamo as dynamo
import requests as req
import os


def probe(url):
    """
    urlからステータスコードを取得する
    """
    response = req.get(url, headers={'User-Agent': os.environ["SERVERLESS_PROJECT"]})

    return response.status_code


def check_sites(event, context):
    sites = dynamo.get_sites()

    for site in sites:
        status_code = probe(site["url"])

        if status_code != site["code"]:
            dynamo.update_site(site["id"], status_code)
            sns(site["id"])


def sns(event):
    client = boto3.client('sns')

    response = client.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message='it is test',
        Subject='Test!',
    )
