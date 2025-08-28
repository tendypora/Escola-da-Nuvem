# Programa para calcular a média escolar de um aluno
# Calcula a média de notas e exibe os detalhes

def calcular_media(notas: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de notas.
    
    Args:
        notas (list[float]): Lista com as notas do aluno.
    
    Returns:
        float: Média das notas, arredondada para duas casas decimais.
    """
    return round(sum(notas) / len(notas), 2)

def exibir_detalhes_media(notas: list[float], media: float) -> None:
    """
    Exibe as notas e a média final no terminal.
    
    Args:
        notas (list[float]): Lista com as notas do aluno.
        media (float): Média calculada.
    """
    print(f"\n=== Calculadora de Média Escolar ===")
    for i, nota in enumerate(notas, 1):
        print(f"Nota {i}: {nota}")
    print(f"Média final: {media:.2f}")

def main():
    """
    Função principal que define os dados de entrada e orquestra o cálculo da média.
    """
    # Dados de entrada
    notas = [7.5, 8.0, 6.5]
    
    # Calcula a média
    media = calcular_media(notas)
    
    # Exibe resultados
    exibir_detalhes_media(notas, media)

if __name__ == "__main__":
    main()