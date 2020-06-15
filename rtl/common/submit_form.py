import requests
from bs4 import BeautifulSoup


class AddEntries:
    def __init__(self):
        self.cookies = {
            "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1592188302",
            "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1591856820,1591861646,1591862203,1591862283",
            "UM_distinctid": "172312b859c1da-05ce04942ee527-30677d00-1fa400-172312b859da72",
            "_caid": "IjVjN2JlOGU3ZDM3Zjc3NTQyOTI4MDM3YiI%3D--373bb3121c485a7fb2ee7da6c68a45e094a25de4",
            "_ga": "GA1.2.627629228.1589856192",
            "_gd_session": "SVJjMThaZUNONUx2MzhBcEdxZE5wTlJKbW5xRDI2U1dEby9wNWUrdkxZQi8zdVJVTFNjY0VxaTJLV1g0NGluSGNjaFo5SlB4dnlkcnhxZUk1eW1FaVVPemtpYmdzNFFoaVE3b2JzR2YwUnF4cTBUZXppRGcwRE00NDBaMjZRZlBKR2tIMWhGY1laL2RKbWFXU3MvMUd3a3NhQjJCenp3dFBxWnYzYi9QOEpvZjFzS3NESko0RHZrMzlKQ3ZZNkFQYmVGQUI4MTBKR1hoTHFOMFVtTGVuZVp1by9QU1J2SWJpbjIzZkJ6K2Z0UEFoRWwrcnFXK04yL2NQUHRPQzl3YytXUG5OdEp3QVFBbGlpckp0MDNGK3J2bEV1Ymh0Rk1uSkhRbXMzeDN6RWZsZGlScXNyU1FTQmhYelMva1VRNGtPQ2VKUGx0NFRpanM5N0F0UWhlR3ZRPT0tLXJFekRJQkRzLzNLWHZwbTNFdStjUWc9PQ%3D%3D--4e4bf49fe856ca2373692b30fa53558ae3ab47db",
            "_gd_sid": "IjVlZTIwY2U5ZGQwODY1ZDFmYzgyMWI0MyI%3D--092e352f8004928ce6ff1911e685a27db034ed56",
            "_gd_sid_cny": "IjVlZDg2YzQyZmM1MzI5NzI3Zjc1Nzc5YyI%3D--af2fe7f0810a35bb88783db3de9844ad1eaee9c2",
            "_gd_sid_fusion": "IjVlZTJlODkzMGJjMmIzMWZkY2QxZDI4NSI%3D--ee9ee21fc3c7436f96cc9ef2555580f5d55d5cf6",
            "_gd_sid_mo": "IjVlY2I2M2E2NWI2NTE2MzJjNGNmMDMzOSI%3D--0929e44eb7696d06b219a2c2311aa75a652371db",
            "_gd_sid_staging": "IjVlZTFkMzQzNmVjNWQ5NzE0NjdlMmY3OSI%3D--53285fbf3241f7428697dbec5bc06685b72c0f66",
            "_gd_sid_uat": "IjVlZTFlMTZjZDQ5NmNlNjA0M2YwMjViZiI%3D--8931ce882ea4fb85f086b4689f9d61431f81fee9",
            "_gid": "GA1.2.1628975044.1592185200",
            "_jinshuju_ut": "IjVjOGI2YTBkOTYwMjY4N2U0OGI4Zjg4YSI%3D--3d0d333baebbb142e894251a445237f0e74cb611",
            "country_code": "CN",
            "csrf_token": "ewjPgVrFkzNXP449Z/zhtYCpVZ8S2bGfcoFc0bXsHJnkO60XZ8Mr1ivBMPVJRIL0ozqr/g7TZzq+SnXHaX5vyg==",
            "jsj_locale": "zh-CN",
            "jsj_uid": "d93ef053-e8bf-4c3c-ae93-2bb8257727b9",
            "mixpanel_event_history": "form_created",
            "need_show_switch_modal_to_user": "false",
            "start_filling_time_DIoQKq": "1592188301",
        }
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "content-length": "426",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://staging.jinshuju.net",
            "referer": "https://staging.jinshuju.net/f/DIoQKq",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "x-csrf-token": "ewjPgVrFkzNXP449Z/zhtYCpVZ8S2bGfcoFc0bXsHJnkO60XZ8Mr1ivBMPVJRIL0ozqr/g7TZzq+SnXHaX5vyg==",
        }

        self.json = {
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
                        "field_1": "李12锤",
                        "field_2": "18282157715",
                    },
                    "formId": "DIoQKq",
                    "formMargin": False,
                    "weixinAccessToken": None,
                    "weixinInfo": None,
                    "xFieldWeixinOpenid": None,
                }
            }
        }

    def add_entries(self, graphql_url):
        res = requests.post(graphql_url, json=self.json, headers=self.headers)
        print(res.status_code)


if __name__ == "__main__":
    AddEntries().add_entries("https://staging.jinshuju.net/graphql/f/DIoQKq")
