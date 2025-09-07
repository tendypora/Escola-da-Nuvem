# Exercício 3: Ler e Exibir Dados de CSV
import csv

with open('pessoas.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)