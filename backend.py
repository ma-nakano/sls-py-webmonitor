from lib.dynamo import get_sites, update_site_state
from lib.aws_lambda import check_site
from requests import get, RequestException


def trigger():
    for site in get_sites():
        check_site(site)

    return {"message": "Trigger Succeeded"}


def probe(event):
    response = get(event.url)

    array = {
        "site": event,
        "date": response.headers["Date"],
        "state": "OK",
        "code": response.status_code,
        "message": response.reason
    }



def sns(event):
    pass
