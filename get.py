import requests

url = "https://lingmo.org"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

res = requests.get(url,headers=headers)

print(res.text)
