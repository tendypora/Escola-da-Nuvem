# Exercício 3: Consulta de Endereço por CEP
import requests

cep = input("Informe o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if "erro" not in data:
        print(f"Logradouro: {data['logradouro']}")
        print(f"Bairro: {data['bairro']}")
        print(f"Cidade: {data['localidade']}")
        print(f"Estado: {data['uf']}")
    else:
        print("CEP inválido.")
else:
    print("Erro ao acessar a API.")