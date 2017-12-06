import requirements
import boto3
import lib.dynamo as dynamo
import requests as req
import os


def probe(url):
    """
    urlからステータスコードを取得して返す
    例外が発生した場合例外クラスのクラス名を返す
    """
    try:
        response = req.get(url, headers={'User-Agent': os.environ["SERVERLESS_PROJECT"]})
    except req.exceptions.RequestException as e:
        return e.__class__.__name__

    return response.status_code


def check_sites(event, context):
    sites = dynamo.get_sites()
    for site in sites:
        status = probe(site["url"])

        if status != site["code"]:
            dynamo.update_site(site["id"], status)
            sns(site["id"])
            print(site)


def sns(event):
    client = boto3.client('sns')

    client.publish(
        TopicArn=os.environ["SNS_TOPIC_ARN"],
        Message='it is test',
        Subject='Test!',
    )
