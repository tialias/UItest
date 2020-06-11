import requests
from bs4 import BeautifulSoup

print("1")
res = requests.get(url="https://staging.jinshuju.net")

cookies = res.cookies
soup = BeautifulSoup(res.text, 'html.parser')
csrf_token = soup.find(attrs={"name": "csrf-token"})['content']
print(cookies)
