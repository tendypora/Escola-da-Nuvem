# Pratica5.py

from datetime import datetime

# Função 1: Calculadora de Gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta com base no valor da conta e na porcentagem desejada.
    Parâmetros:
        valor_conta (float): O valor total da conta
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
    Retorna:
        float: O valor da gorjeta calculada
    """
    return valor_conta * (porcentagem_gorjeta / 100)

# Função 2: Verificador de Palíndromo
def verificar_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços, pontuação e considera letras minúsculas.
    Retorna: "Sim" se for palíndromo, "Não" caso contrário.
    """
    # Remove espaços, pontuação e converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    # Verifica se o texto é igual ao seu reverso
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

# Função 3: Calculadora de Desconto
def calcular_preco_com_desconto():
    """
    Calcula o preço final de um produto após aplicar um desconto.
    Solicita o preço original e o percentual de desconto do usuário.
    Exibe o preço final com duas casas decimais.
    """
    try:
        preco_original = float(input("Digite o preço original do produto: "))
        percentual_desconto = float(input("Digite o percentual de desconto: "))
        
        if preco_original < 0 or percentual_desconto < 0:
            print("Erro: Preço e percentual não podem ser negativos!")
            return
        
        valor_desconto = preco_original * (percentual_desconto / 100)
        preco_final = preco_original - valor_desconto
        print(f"Preço final: R$ {preco_final:.2f}")
        
    except ValueError:
        print("Erro: Entrada inválida! Digite valores numéricos.")

# Função 4: Calculadora de Idade em Dias
def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias com base no ano de nascimento.
    Considera o ano atual (2025) e assume uma média de 365.25 dias por ano.
    Retorna: int: A idade aproximada em dias
    """
    ano_atual = datetime.now().year
    if ano_nascimento > ano_atual:
        return "Erro: Ano de nascimento não pode ser no futuro!"
    idade_anos = ano_atual - ano_nascimento
    idade_dias = int(idade_anos * 365.25)  # Inclui ajuste para anos bissextos
    return idade_dias

# Menu principal para executar as funcionalidades
def main():
    print("=== Calculadora Multifuncional ===")
    print("1 - Calcular Gorjeta")
    print("2 - Verificar Palíndromo")
    print("3 - Calcular Preço com Desconto")
    print("4 - Calcular Idade em Dias")
    
    escolha = input("Digite o número da opção desejada (1-4): ")
    
    if escolha == '1':
        try:
            valor_conta = float(input("Digite o valor da conta: "))
            porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: "))
            if valor_conta < 0 or porcentagem_gorjeta < 0:
                print("Erro: Valor da conta e porcentagem não podem ser negativos!")
            else:
                gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
                print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
        except ValueError:
            print("Erro: Entrada inválida! Digite valores numéricos.")
            
    elif escolha == '2':
        texto = input("Digite a palavra ou frase: ")
        resultado = verificar_palindromo(texto)
        print(f"É palíndromo? {resultado}")
        
    elif escolha == '3':
        calcular_preco_com_desconto()
        
    elif escolha == '4':
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            resultado = calcular_idade_em_dias(ano_nascimento)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print(f"Idade em dias: {resultado} dias")
        except ValueError:
            print("Erro: Digite um ano válido!")
            
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()