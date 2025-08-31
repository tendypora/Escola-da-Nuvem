# Exercício 2: Classificador de Idade
def classificar_idade():
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <= 12:
        print("Criança")
    elif 13 <= idade <= 17:
        print("Adolescente")
    elif 18 <= idade <= 59:
        print("Adulto")
    else:
        print("Idoso")

