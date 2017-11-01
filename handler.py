from lib.dynamo import get_sites, create_site
from urllib.parse import parse_qs
import requirements
from jinja2 import Environment, FileSystemLoader


def dashboard(event, context):
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
    params = event["body"]
    site = {"name": params["name"], "url": params["url"]}

    create_site(site)

    response = {
        "statusCode": 302,
        "headers": {
            'Location': './',
        }
    }

    return response


def remove(event, context):
    pass


def trigger(event, context):
    """
    Invoke probe function.
    :param event:
    :param context:
    :return:
    """
    pass