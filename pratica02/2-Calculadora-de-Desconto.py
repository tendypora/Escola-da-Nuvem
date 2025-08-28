# Programa para calcular o desconto de um produto
# Calcula o valor do desconto e o preço final com base no preço original e na porcentagem de desconto

def calcular_valor_desconto(preco_original: float, percentual_desconto: float) -> float:
    """
    Calcula o valor do desconto com base no preço original e na porcentagem de desconto.
    
    Args:
        preco_original (float): Preço original do produto.
        percentual_desconto (float): Porcentagem de desconto (ex.: 20 para 20%).
    
    Returns:
        float: Valor do desconto calculado, arredondado para duas casas decimais.
    """
    return round(preco_original * (percentual_desconto / 100), 2)

def calcular_preco_final(preco_original: float, valor_desconto: float) -> float:
    """
    Calcula o preço final após aplicar o desconto.
    
    Args:
        preco_original (float): Preço original do produto.
        valor_desconto (float): Valor do desconto calculado.
    
    Returns:
        float: Preço final após desconto, arredondado para duas casas decimais.
    """
    return round(preco_original - valor_desconto, 2)

def exibir_detalhes_desconto(nome_produto: str, preco_original: float, percentual_desconto: float, valor_desconto: float, preco_final: float) -> None:
    """
    Exibe os detalhes do cálculo de desconto no terminal.
    
    Args:
        nome_produto (str): Nome do produto.
        preco_original (float): Preço original do produto.
        percentual_desconto (float): Porcentagem de desconto.
        valor_desconto (float): Valor do desconto.
        preco_final (float): Preço final após desconto.
    """
    print(f"\n=== Calculadora de Desconto ===")
    print(f"Produto: {nome_produto}")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Percentual de desconto: {percentual_desconto}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")

def main():
    """
    Função principal que define os dados de entrada e orquestra o cálculo de desconto.
    """
    # Dados de entrada
    nome_produto = "Camiseta"
    preco_original = 50.00
    percentual_desconto = 20
    
    # Calcula desconto e preço final
    valor_desconto = calcular_valor_desconto(preco_original, percentual_desconto)
    preco_final = calcular_preco_final(preco_original, valor_desconto)
    
    # Exibe resultados
    exibir_detalhes_desconto(nome_produto, preco_original, percentual_desconto, valor_desconto, preco_final)

if __name__ == "__main__":
    main()