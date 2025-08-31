# Atividade: Calculadora Completa com Múltiplas Funcionalidades

# Função 1: Calculadora de Operações Básicas
def calculadora_basica():
    print("=== Calculadora Básica ===")
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            
            if operacao not in ['+', '-', '*', '/']:
                print("Erro: Operação inválida! Use +, -, * ou /.")
                continue
                
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            else:  # operacao == '/'
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida!")
                    continue
                resultado = num1 / num2
                
            print(f"Resultado: {resultado:.2f}")
            break
            
        except ValueError:
            print("Erro: Entrada inválida! Digite números válidos.")
            continue

# Função 2: Registro de Notas da Turma
def registrar_notas():
    print("\n=== Registro de Notas ===")
    notas = []
    while True:
        entrada = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ")
        if entrada.lower() == 'fim':
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Erro: Nota inválida! Deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Entrada inválida! Digite um número ou 'fim'.")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

# Função 3: Verificador de Senha Forte
def verificar_senha_forte():
    print("\n=== Verificador de Senha Forte ===")
    while True:
        senha = input("Digite uma senha ou 'sair' para encerrar: ")
        if senha.lower() == 'sair':
            break
        
        has_digit = any(char.isdigit() for char in senha)
        if len(senha) >= 8 and has_digit:
            print("Senha forte válida!")
            break
        else:
            print("Erro: A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")

# Função 4: Verificador de Números Pares e Ímpares
def verificar_par_impar():
    print("\n=== Verificador de Números Pares e Ímpares ===")
    pares = 0
    impares = 0
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é par")
                pares += 1
            else:
                print(f"{numero} é ímpar")
                impares += 1
        except ValueError:
            print("Erro: Entrada inválida! Digite um número inteiro ou 'fim'.")
    
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

# Menu principal para executar as funcionalidades
def main():
    print("=== Calculadora Completa ===")
    print("Escolha uma funcionalidade:")
    print("1 - Calculadora Básica")
    print("2 - Registro de Notas")
    print("3 - Verificador de Senha Forte")
    print("4 - Verificador de Números Pares e Ímpares")
    
    escolha = input("Digite o número da opção desejada (1-4): ")
    
    if escolha == '1':
        calculadora_basica()
    elif escolha == '2':
        registrar_notas()
    elif escolha == '3':
        verificar_senha_forte()
    elif escolha == '4':
        verificar_par_impar()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()