from urllib.parse import parse_qs
from uuid import uuid1
import requirements
import lib.dynamo as dynamo
import lib.backend as backend
from jinja2 import Environment, FileSystemLoader


def dashboard(event, context):
    """
    /のhtmlを生成する
    """
    env = Environment(loader=FileSystemLoader("./html", encoding="utf-8"))
    tpl = env.get_template("index.html")

    html = tpl.render({"sites": dynamo.get_sites_data()})

    response = {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'text/html',
            "Access-Control-Allow-Origin": "*"
        },
        "body": html
    }

    return response


def register(event, context):
    """
    /registerにpostされたnameとurlをDBに登録し
    /にリダイレクトする
    """

    body = parse_qs(event["body"])

    site = {
        "id": str(uuid1()),
        "name": body["name"][0],
        "url": body["url"][0],
        "code": backend.probe(body["url"][0])
    }

    dynamo.put_site(site)

    response = {
        "statusCode": 302,
        "headers": {
            'Location': './',
        }
    }

    return response


def remove(event, context):
    """
    /removeにpostされたidをremove_site()に渡し
    /にリダイレクトする
    """
    body = parse_qs(event["body"])

    dynamo.remove_site(body["id"][0])

    response = {
        "statusCode": 302,
        "headers": {
            'Location': './',
        }
    }

    return response
