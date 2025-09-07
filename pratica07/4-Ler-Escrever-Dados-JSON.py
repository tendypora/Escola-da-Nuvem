# Exercício 4: Ler e Escrever Dados em JSON
import json

# Escrever em JSON
dados = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

with open('pessoa.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

# Ler do JSON
with open('pessoa.json', 'r') as arquivo_json:
    dados_lidos = json.load(arquivo_json)
    print(dados_lidos)