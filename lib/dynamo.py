from uuid import uuid1

sites = [{
    "id": 'f60ee318-b957-11e7-b276-b8f6b117dc5b',
    "name": "google",
    "url": "https://google.com",
    "code": "200"
}, {
    "id": 'fe2048da-b957-11e7-8e67-b8f6b117dc5b',
    "name": "yahoo",
    "url": "https://yahoo.co.jp",
    "code": "200"
}]


def create_site(site):
    """
    :param dict site:{"name": "foo.com", "url": "https://foo.com"}
    """
    site["id"] = uuid1()

    sites.append(site)


def get_sites():
    return sites


def remove_site():
    pass


def update_site_state():
    pass
