# Exercício 2: Perfil de Usuário Aleatório
import requests

response = requests.get("https://randomuser.me/api/")
if response.status_code == 200:
    data = response.json()["results"][0]
    nome = f"{data['name']['first']} {data['name']['last']}"
    email = data["email"]
    pais = data["location"]["country"]
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")
else:
    print("Erro ao acessar a API.")