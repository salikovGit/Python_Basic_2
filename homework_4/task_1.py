import requests


url = 'http://geekbrains.ru'
response = requests.get(url)
content = response.content
print(content)
