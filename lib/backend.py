import requirements
import boto3
import lib.dynamo as dynamo
import requests as req
import os
from datetime import datetime


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
        new_status = probe(site["url"])

        if new_status != site["code"]:
            dynamo.update_site(site["id"], new_status)
            if new_status != 200:
                sns(None, site, new_status)
            print(site)


def sns(event, site, new_status):
    url = site["url"]
    old_status = site["code"]
    time = datetime.now()

    message = f"""\
    Warning! {url} status changed from {old_status} to {new_status} at {time}.
    """

    client = boto3.client('sns')

    client.publish(
        TopicArn=os.environ["SNS_TOPIC_ARN"],
        Message=message,
        Subject='Status Changed',
    )
