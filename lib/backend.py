import requirements
import requests as req


def probe(url):
    """
    urlからステータスコードを取得する
    """
    response = req.get(url)

    return response.status_code


def sns(event):
    """
    snsに通知する
    """
    pass
