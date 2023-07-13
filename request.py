import requests

url = 'http://localhost:8080/api/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro na solicitação GET:', response.status_code)
