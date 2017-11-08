from lib.dynamo import get_sites, create_site
from urllib.parse import parse_qs
import requirements
from jinja2 import Environment, FileSystemLoader


def dashboard(event, context):
    """
    /のhtmlを生成する
    """
    env = Environment(loader=FileSystemLoader("./html", encoding="utf-8"))
    tpl = env.get_template("index.html")

    html = tpl.render({"sites": get_sites()})

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
    /registerにpostされたnameとurlをcreate_site()に渡し
    /にリダイレクトする
    """

    body = parse_qs(event["body"])

    site = {"name": body["name"][0], "url": body["url"][0]}

    create_site(site)

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
    pass
