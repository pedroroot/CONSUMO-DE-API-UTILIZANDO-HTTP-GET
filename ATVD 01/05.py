import requests

r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})

if r.status_code == 200:
    print('Retorno salvo no arquivo!')
    f = open("resultado.txt", "w", encoding="utf-8")
    f.write(r.text)   
    f.close()         
else:
    print('Nao houve sucesso na requisicao.')

