#requestsの挙動確認用のファイル
import requests

url = 'https://google.com/'

test = requests.get(url)

print(test)
print(test.url)
# print(test.text)