# Programa para somar dois valores inteiros informados pelo usuário
# Lê os valores, calcula a soma e exibe no formato "X = valor"

def calcular_soma(a: int, b: int) -> int:
    """
    Calcula a soma de dois valores inteiros.
    
    Args:
        a (int): Primeiro valor inteiro.
        b (int): Segundo valor inteiro.
    
    Returns:
        int: Soma dos dois valores.
    """
    return a + b

def exibir_soma(soma: int) -> None:
    """
    Exibe o resultado da soma no formato especificado.
    
    Args:
        soma (int): Resultado da soma.
    """
    print(f"X = {soma}")

def main():
    """
    Função principal que lê os dados de entrada, calcula a soma e exibe o resultado.
    """
    # Lê os dois valores inteiros do usuário
    a = int(input())
    b = int(input())
    
    # Calcula a soma
    soma = calcular_soma(a, b)
    
    # Exibe o resultado
    exibir_soma(soma)

if __name__ == "__main__":
    main()