import requests as req
import requirements
import lib.dynamo as dynamo
import os


def probe(url):
    """
    urlからステータスコードを取得する
    """
    response = req.get(url, headers={'User-Agent': os.environ["SERVERLESS_PROJECT"]})

    return response.status_code


def check_sites():
    sites = dynamo.get_sites()

    for site in sites:
        status_code = probe(site["url"])

        if status_code != site["code"]:
            dynamo.update_site(site["id"], status_code)


def sns(event):
    """
    snsに通知する
    """
    pass
