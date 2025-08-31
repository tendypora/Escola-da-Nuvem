# Exercício 7: Calculadora da Média
def calcular_media():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())
    
    pesos = [2, 3, 4, 1]
    media = (n1 * pesos[0] + n2 * pesos[1] + n3 * pesos[2] + n4 * pesos[3]) / sum(pesos)
    print(f"Media: {media:.1f}")
    
    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        nota_exame = float(input())
        print(f"Nota do exame: {nota_exame:.1f}")
        media_final = (media + nota_exame) / 2
        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {media_final:.1f}")

