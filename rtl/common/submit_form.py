import requests
from bs4 import BeautifulSoup


class AddEntries:
    def __init__(self, forms_url):
        res = requests.get(forms_url)

        self.cookies = res.cookies
        soup = BeautifulSoup(res.text, 'html.parser')
        self.csrf_token = soup.find(attrs={"name": "csrf-token"})['content']
    def add_entries(self, graphql_url):
        data = {
            "field_1": "张三",
            "field_2": "18383157715"
        }
        headers = {
            "Host": "uat.jinshuju.net",
            "Connection": "keep-alive",
            "Content-Length": "459",
            "accept": "*/*",
            "X-CSRF-TOKEN": self.csrf_token,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "content-type": "application/json;charset=UTF-8",
            "Origin": "https://staging.jinshuju.net",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://staging.jinshuju.net/f/DIoQKq",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cookie": self.cookies
        }
        res = requests.post(url=graphql_url, data=data, cookies=self.cookies)
        print(res.status_code)


if __name__ == "__main__":
    ad = AddEntries("https://staging.jinshuju.net/f/DIoQKq")
    ad.add_entries("https://staging.jinshuju.net/graphql/f/DIoQKq")

