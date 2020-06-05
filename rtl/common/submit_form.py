import requests

from rtl.common.conf import get_msg


def add_data(url):
    data = {
        "field_1": "张三",
        "field_2": "18383157715"
    }
    cookies = get_msg(url)
    res = requests.post(url=url, data=data, cookie=cookies)
