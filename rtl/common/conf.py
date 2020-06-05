import requests


def get_msg(url):
    res = requests.get(url)

    return res.cookies

