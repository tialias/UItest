import grequests,requests
from post_data import run_submit
import time,sys

class Lot():
    
    def __init__(self,form_token):
        self.l = run_submit(form_token)
        self.form_token = form_token
    def access_lot(self):
        for i in range(3):
            cookies = {
                "Hm_lpvt_47cd03e974df6869353431fe4f4d6b2f": "1596445088",
                "Hm_lvt_47cd03e974df6869353431fe4f4d6b2f": "1596444101",
                "_caid": "IjVlNjg0YTVlNWQ1ZDdkMjM5MTgyYzFjMSI%3D--376e9e1559dd093e63c11a55e8649b3c657ef9ec",
                "_ga": "GA1.2.550778663.1587982706",
                "_gd_session": "Q0hmM2htLytlNHRheUdXNG5MNE4xdDNuZ1gxeDlXQXVLdWk0V3pnU3VER2ZWZXZoUGx0a3RMbFZJSzk5WVFPUi9iemJCUVB1ZnBnM3V1TXRkQzRaWkpiZkVJdmVvR0U2ajFubVFpZkRNeDV1eTBiRkh4N2MyaU5YSlNHZHQrMFBBcDNxVks1TGFqSm1pS1Vyai9ReGRBPT0tLWFQZ3ZseWM0OXNkaG1qaWVPaWxLY3c9PQ%3D%3D--49963e2e5744cb2c9bb3e42642b7d332df492f00",
                "_gid": "GA1.2.1063886214.1596444102",
                "_smt_uid": "5ea6b170.516ca751",
                "_smtv": "",
                "csrf_token": "jOfGeGut1RjZLnwFQExf5BZVrWL2tRPKTfajDCenVcwxXydujwBiRmJqBOkjOOlB53xf6TddsUDXTuDQcGL4DQ==",
                "entry_token": self.l[i],
                "filled_form_scene": "form",
                "gd_ssf": "MTU5NjQ0NTA4Nw%3D%3D--80f5dcf551bd35cd80e9f6119e31e256d13ef19f",
                "jsj_locale": "zh-CN",
                "jsj_uid": "dfc295f7-a911-4529-8330-e5d0b4dd60b1",
                "last_fill_entry_token": self.l[i],
                "referer_url": "https://uat.jinshuju.net/f/%s"%self.form_token,
                    }
            headers = { 
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "cache-control": "max-age=0",
                    "if-none-match": 'W/"11735c441dda85e409f7799f4bd6708a"',
                    "referer": "https://uat.jinshuju.net/f/P2NeOl/wheel_fortune",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                        }
            res1 = requests.get(url="https://uat.jinshuju.net/f/%s/wheel_fortune"%self.form_token,headers=headers,cookies=cookies)
        return self.l    

if __name__ =="__main__":

    Lottery =Lot(sys.argv[1])
    l = Lottery.access_lot()
    req_list = [   # 请求列表
        grequests.get("https://uat.jinshuju.net/entries/%s/wheel_fortunes/lottery"%l[0]),
        grequests.get("https://uat.jinshuju.net/entries/%s/wheel_fortunes/lottery"%l[1]),
        grequests.get("https://uat.jinshuju.net/entries/%s/wheel_fortunes/lottery"%l[2]),
        # grequests.get("https://uat.jinshuju.net/entries/%s/wheel_fortunes/lottery"%l[3]),
        # grequests.get("https://uat.jinshuju.net/entries/%s/wheel_fortunes/lottery"%l[4]),
        # grequests.get("https://uat.jinshuju.net/entries/%s/wheel_fortunes/lottery"%l[5]),
    ]
    res_list = grequests.map(req_list)    # 并行发送，等最后一个运行完后返回
    print(res_list[0].text,"\n",res_list[1].text,"\n",res_list[2].text)