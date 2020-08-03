import requests
from faker import Faker


fake = Faker(locale='zh_CN')

def submit(form_token):

    cookies = {
                "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1596444101",
                "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1596444101",
                "_caid": "IjVlNjg0YTVlNWQ1ZDdkMjM5MTgyYzFjMSI%3D--376e9e1559dd093e63c11a55e8649b3c657ef9ec",
                "_ga": "GA1.2.550778663.1587982706",
                "_gat_gtag_UA_48208031_13": "1",
                "_gd_session": "a0k3N0U5ZFh2NjF0d3NwYlZsc2dCRkxxSlNYUk9ra1ZoMGFrMnJOSXBLb2N2LzAxY2Y4MXpDVVRRYzhxZU1CREI0VUg1OG5SVGQ3OWFFWEpQOC95WUIwbXNWSUNPeHNTb3RSQzVrVUQwNlJpZ3pjSTZTbmVidFZNL2NyWWhNU0VDcVVDSnZFb3NjTDdkTmJSMENwUjlnPT0tLWJhOXdXRkEyYndPZnZxa1ZqZnduUkE9PQ%3D%3D--e1588cd873182aa9685891b554c9a8464a857aa3",
                "_gid": "GA1.2.1063886214.1596444102",
                "_smt_uid": "5ea6b170.516ca751",
                "_smtv": "",
                "csrf_token": "n6Jg5g7vqVoYBWBoqiHpZIesmoI7WClr+K8ygoDUml0iGoHw6kIeBKNBGITJVV/BdoVoCfqwi+FiF3Fe1xE3nA==",
                "filled_form_scene": "form",
                "jsj_locale": "zh-CN",
                "jsj_uid": "dfc295f7-a911-4529-8330-e5d0b4dd60b1",
                "start_filling_time_P2NeOl": "1596444099",
            }
    headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "zh-CN,zh;q=0.9",
                "content-length": "454",
                "content-type": "application/json;charset=UTF-8",
                "origin": "https://uat.jinshuju.net",
                "referer": "https://uat.jinshuju.net/f/%s"%form_token,
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                "x-csrf-token": "n6Jg5g7vqVoYBWBoqiHpZIesmoI7WClr+K8ygoDUml0iGoHw6kIeBKNBGITJVV/BdoVoCfqwi+FiF3Fe1xE3nA==",
            }
    json = {
            "extensions": {
                "persistedQuery": {
                    "sha256Hash": "4cd6a9aef2820b2c3215f6ddfa87093869461f76f3f2016738f4307268a7df98",
                    "version": 1,
                }
            },
            "operationName": "CreatePublishedFormEntry",
            "variables": {
                "input": {
                    "backgroundImage": False,
                    "captchaData": None,
                    "embedded": False,
                    "entryAttributes": {
                        "field_1": fake.name(),
                        "field_2": fake.phone_number(),
                    },
                    "formId": form_token,
                    "formMargin": False,
                    "weixinAccessToken": None,
                    "weixinInfo": None,
                    "xFieldWeixinOpenid": None,
                }
            }
        }
    res = requests.post(url="https://uat.jinshuju.net/graphql/f/%s"%form_token, json=json,
                               headers=headers)
    cookie = requests.utils.dict_from_cookiejar(res.cookies)
    entry_token = (cookie["entry_token"])
    return entry_token
def run_submit(form_token):
    l_token = []
    for i in range(6):
        e = submit(form_token)
        l_token.append(e)
    return l_token