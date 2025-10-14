import requests

url = 'https://viacep.com.br/ws/MG/Belo Horizonte/Rua dos Aimores/json/'

r = requests.get(url)

if r.status_code == 200:
    print()
    print('Resultados encontrados:')
    for endereco in r.json():
        print(endereco)
    print()
else:
    print('Nao houve sucesso na requisicao. Status:', r.status_code)
