import requests

url = 'https://viacep.com.br/ws/'
cep_inicial = 30140071
formato = '/json/'

for i in range(5):
    cep = str(cep_inicial + i)
    r = requests.get(url + cep + formato)

    if r.status_code == 200:
        print()
        print(f'CEP: {cep}')
        print(r.json())
        print()
    else:
        print(f'Falha ao consultar CEP {cep}. Status:', r.status_code)
