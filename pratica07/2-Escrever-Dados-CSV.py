# Exercício 2: Escrever Dados em CSV
import csv

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', 30, 'São Paulo'],
    ['Maria', 25, 'Rio de Janeiro'],
    ['Pedro', 35, 'Belo Horizonte']
]

with open('pessoas.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso.")