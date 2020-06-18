import requests
from faker import Faker
from threading import Thread

from faker import Faker

fake = Faker(locale='zh_CN')


def add_entries(token):
    cookies = {
        "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1592480640",
        "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1592450714,1592450749,1592451916,1592467618",
        "UM_distinctid": "172312b859c1da-05ce04942ee527-30677d00-1fa400-172312b859da72",
        "_caid": "IjVjN2JlOGU3ZDM3Zjc3NTQyOTI4MDM3YiI%3D--373bb3121c485a7fb2ee7da6c68a45e094a25de4",
        "_ga": "GA1.2.627629228.1589856192",
        "_gd_session": "QmI2c2w5ckYrZWV2bDFvMXNVRmdpSTVKdmlBTkc0RzdEMnFJOHNsMEJKMXZkMTJjMXlkVkRMYkRVc3ZnSkROTUsxRVZNZFZuc25DWXB0MDJJb0svU1FBalRCSXJyU2VDa0FVM1ViQ1RUNXUyYlJkZTI4bWo3U25mVzdlWkdtVlgzSjZ2dThsbjN5bWhKUGZqajFRNEVnNnhHY1JaQnlRMXJQdjNCTUpySlltd2piQVNzZHFrbUY3NWR2UzUwT2xERXBQdmxJSmw3Mm1ZTSs2bGtaeXJLLzl4aW1PcTNDVGNWZk5jMjFnZ2xYTzByOVJJUWp3OHZnamhYM1VySlkva1hyTUQvbVhjV1RGdmEwZndDYlQyRERsaFJkL2lUTVNrTGk5eTIyNmdIN204YkQ4ZGFIRDl6WUc0L05JWE1JSnQ5QnprcVdzc1VLLzB0WGNQWTlUT1lRPT0tLTdjQ0xnZlQ5THZPSHlzelBIeHFPRGc9PQ%3D%3D--7b85bb0eed4b636465c4ee21b20c0039626be0a7",
        "_gd_sid": "IjVlZWIyMDg4NmE4ZDA0Mzg3MTgxNGIwNSI%3D--b863c7b39bb62bc1b5a23a289a182fe9127ab982",
        "_gd_sid_cny": "IjVlZDg2YzQyZmM1MzI5NzI3Zjc1Nzc5YyI%3D--af2fe7f0810a35bb88783db3de9844ad1eaee9c2",
        "_gd_sid_fusion": "IjVlZThhMTUyMGJjMmIzMDQxOWI3NTc5MCI%3D--5369217dec1accaa8d1dd24932df1eecc2c5b6f0",
        "_gd_sid_mo": "IjVlY2I2M2E2NWI2NTE2MzJjNGNmMDMzOSI%3D--0929e44eb7696d06b219a2c2311aa75a652371db",
        "_gd_sid_staging": "IjVlZTcxNjZlNmVjNWQ5MWYwOTRlYjlhYyI%3D--bd2db442ea71a251ed79d52259cf0eed2caafcdb",
        "_gd_sid_uat": "IjVlZTljZjVlZDQ5NmNlMmY0YjdiMmQ2YyI%3D--006aab929ccd40d84fad8e22dc1bb7025e88d457",
        "_gid": "GA1.2.1628975044.1592185200",
        "_jinshuju_ut": "IjVjN2JlOGU3ZDM3Zjc3NTQyOTI4MDM3OSI%3D--bc0971bcd0f6eb762794df2dd62e5a5cd3fea93e",
        "country_code": "CN",
        "csrf_token": "hpLY9JxgqP9kjnjwXPZB2rc+6B0wqT/YCI+Wp6TNDafAFuGllxZFUlmblLr9ozSboZ2Ggwcnb8SUKhrXYulfnA==",
        "entries_pagination_limit": "500",
        "gd_registered_from": "jsj_success_ad",
        "has_visited_dashboard_in_two_days": "true",
        "jsj_locale": "zh-CN",
        "jsj_uid": "d93ef053-e8bf-4c3c-ae93-2bb8257727b9",
        "mixpanel_event_history": "form_created",
        "need_show_switch_modal_to_user": "false",
        "restore_entry_tooltip_viewed": "true",
        "show_template_for_double_zero_user": "true",
        "start_filling_time_DIoQKq": "1592473233",
        "start_filling_time_hMFfOC": "1592479752",
    }
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content-length": "426",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://staging.jinshuju.net",
        "referer": "https://staging.jinshuju.net/f/%s" % token,
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        "x-csrf-token": "ewjPgVrFkzNXP449Z/zhtYCpVZ8S2bGfcoFc0bXsHJnkO60XZ8Mr1ivBMPVJRIL0ozqr/g7TZzq+SnXHaX5vyg==",
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
                "entryAttributes": {"field_1": "测试", "field_2": "vIRa"},
                "formId": token,
                "formMargin": False,
                "weixinAccessToken": None,
                "weixinInfo": None,
                "xFieldWeixinOpenid": None,
            }
        },
    }
    res = requests.post(url="https://hMFfOCstaging.jinshuju.net/graphql/f/%s" % token, json=json, cookies=cookies,
                        headers=headers)
    print(res.text)
    print(type(token))


thread_01 = Thread(target=add_entries, args=("3Fpg1U",))
thread_02 = Thread(target=add_entries, args=("3Fpg1U",))

thread_01.start()
thread_02.start()
