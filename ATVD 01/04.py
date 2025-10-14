import requests

url = 'https://viacep.com.br/abc/'

r = requests.get(url)

print('Status Code:', r.status_code)
print('Resposta:')
print(r.text)
