import requests
from faker import Faker
from locust import task, HttpUser, SequentialTaskSet
from locust.runners import Runner


class Wftasks(SequentialTaskSet):
    def on_start(self):
        self.fake = Faker(locale='zh_CN')
        self.client.get(url="https://staging.jinshuju.net/f/DIoQKq")

    @task
    def add_entries(self):
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
                        "field_1": self.fake.name(),
                        "field_2": self.fake.phone_number(),
                    },
                    "formId": "DIoQKq",
                    "formMargin": False,
                    "weixinAccessToken": None,
                    "weixinInfo": None,
                    "xFieldWeixinOpenid": None,
                }
            }
        }
        res = self.client.post(url="https://staging.jinshuju.net/graphql/f/DIoQKq", json=self.json,
                               headers=self.headers)
        assert res.status_code == 200
        cookie = requests.utils.dict_from_cookiejar(res.cookies)
        self.entry_token = (cookie["entry_token"])

    @task
    def wheel_fortune(self):
        cookies = {
            "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1592376825",
            "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1592203783,1592208337,1592208724,1592211630",
            "UM_distinctid": "172312b859c1da-05ce04942ee527-30677d00-1fa400-172312b859da72",
            "_caid": "IjVjN2JlOGU3ZDM3Zjc3NTQyOTI4MDM3YiI%3D--373bb3121c485a7fb2ee7da6c68a45e094a25de4",
            "_ga": "GA1.2.627629228.1589856192",
            "_gd_session": "NzM5SXVNM1FRUDNHaHA4V0czVFlRbGhUTit3RWZscDcyZHNWMENHRFRUMEZWbncyd2h5RGFQMG1LaEpHZzBYaDczVzBaOGg0NWFxNUtyZUtrbm4zNStxRVdZZnVkQ0pzaHJSQjE5UnVKNkZSdjNwZGpPMHBkRkljVUpKSDRjL0pXUjNIWVBUWmNzOWNHZyt4MGEyNUVCZ1ozbUpZYnFzbUNoVm93elFOd2dQeFdIOTlKOUxVS21TQ09vVHQ2Z0JyaGZTRDFaK09RNUcxcStlTEM4Mm44THc3TFBqeG0xRzhHbitFMlhTRGVGL09CTG0vQkZyNndZRWMvMFlRMnpFYTNJTnpVQk9oUzgzR2VWQ3l0cTdqU0dxUDc5SUFNWXhpdUtuNFNRT2hidHYvQjR6bFg0cEJtdUNMRGpaWmJianJZbEdZVmY1OGVDb3VIcHlOOFJXOEl3PT0tLS93NmMyT095T1oyRVVLRitTMzE1U3c9PQ%3D%3D--55841e2456d77d7315eb4dd961c813c2bcf3b65c",
            "_gd_sid": "IjVlZTk4MjQ0YzgxNTdlODE3MWZmMTlkZCI%3D--c521aff7a6b35bf265d6610eb99f21ba7a961c28",
            "_gd_sid_cny": "IjVlZDg2YzQyZmM1MzI5NzI3Zjc1Nzc5YyI%3D--af2fe7f0810a35bb88783db3de9844ad1eaee9c2",
            "_gd_sid_fusion": "IjVlZThhMTUyMGJjMmIzMDQxOWI3NTc5MCI%3D--5369217dec1accaa8d1dd24932df1eecc2c5b6f0",
            "_gd_sid_mo": "IjVlY2I2M2E2NWI2NTE2MzJjNGNmMDMzOSI%3D--0929e44eb7696d06b219a2c2311aa75a652371db",
            "_gd_sid_staging": "IjVlZTcxNjZlNmVjNWQ5MWYwOTRlYjlhYyI%3D--bd2db442ea71a251ed79d52259cf0eed2caafcdb",
            "_gd_sid_uat": "IjVlZTlhYjBlZDQ5NmNlNzEyOWM3YTc4OSI%3D--6bfcea6f318d6d8f6ffc57e5c7c9f5349707d3d3",
            "_gid": "GA1.2.1628975044.1592185200",
            "_jinshuju_ut": "IjVjZjRlNThiNGU2ZTBlNDVjYWMwMjg2NiI%3D--c39bc95f1f7e3fbe5b68f5a65880120107856a1c",
            "country_code": "CN",
            "csrf_token": "fbMJZ01+6KLOx6JTq1U2DN2rrtZkLTET2GpgTECmM507NzA2RggFD/PSThkKAENNywjASFOjYQ9Ez+w8hoJhpg==",
            "entry_token": self.entry_token,
            "gd_registered_from": "jsj_success_ad",
            "gd_ssf": "MTU5MjM3NjQ3OQ%3D%3D--3c779368c741582bc9656cb29033686283241ac4",
            "has_visited_dashboard_in_two_days": "true",
            "jsj_locale": "zh-CN",
            "jsj_uid": "d93ef053-e8bf-4c3c-ae93-2bb8257727b9",
            "last_fill_entry_token": "CAfYAJU3",
            "mixpanel_event_history": "open_publish_link",
            "need_show_switch_modal_to_user": "false",
            "restore_entry_tooltip_viewed": "true",
            "show_template_for_double_zero_user": "true",
        }

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "if-none-match": 'W/"7302119ce5c4b4121f1c653dc8113f90"',
            "referer": "https://staging.jinshuju.net/f/DIoQKq/wheel_fortune",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        }
        res = self.client.get(url="https://staging.jinshuju.net/f/DIoQKq/wheel_fortune", cookies=cookies,
                              headers=headers)
        print(res.status_code)

    @task
    def lottery(self):
        res = self.client.get(url="https://staging.jinshuju.net/entries/%s/wheel_fortunes/lottery" % self.entry_token)
        print(res.status_code)

    @task
    def receive(self):
        res = self.client.get(url="https://staging.jinshuju.net/entries/5trVFx03/wheel_fortunes/results/dbbcce3b")
        print(res.status_code)



class WfUser(HttpUser):
    tasks = [Wftasks]
    min_wait = 500
    max_wait = 2000
