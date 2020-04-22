import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
resp = requests.get(url='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html', headers=headers)
# print(resp)
# print(resp.text)
# print(resp.content)
print(resp.request.headers)
print('=====================')
print(resp.headers)