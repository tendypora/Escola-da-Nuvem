# Programa para converter valores em reais para dólares e euros
# Calcula e exibe os valores convertidos com base nas taxas fornecidas

def converter_moeda(valor_reais: float, taxa: float) -> float:
    """
    Converte um valor em reais para outra moeda com base na taxa fornecida.
    
    Args:
        valor_reais (float): Valor em reais a ser convertido.
        taxa (float): Taxa de conversão (ex.: R$ por dólar).
    
    Returns:
        float: Valor convertido, arredondado para duas casas decimais.
    """
    return round(valor_reais / taxa, 2)

def exibir_conversao(valor_reais: float, valor_dolar: float, valor_euro: float, taxa_dolar: float, taxa_euro: float) -> None:
    """
    Exibe os detalhes da conversão de moeda no terminal.
    
    Args:
        valor_reais (float): Valor original em reais.
        valor_dolar (float): Valor convertido para dólares.
        valor_euro (float): Valor convertido para euros.
        taxa_dolar (float): Taxa de conversão para dólar.
        taxa_euro (float): Taxa de conversão para euro.
    """
    print(f"\n=== Conversor de Moeda ===")
    print(f"Valor em reais: R$ {valor_reais:.2f}")
    print(f"Taxa do dólar: R$ {taxa_dolar:.2f}")
    print(f"Valor em dólares: US$ {valor_dolar:.2f}")
    print(f"Taxa do euro: R$ {taxa_euro:.2f}")
    print(f"Valor em euros: € {valor_euro:.2f}")

def main():
    """
    Função principal que define os dados de entrada e orquestra a conversão.
    """
    # Dados de entrada
    valor_reais = 100.00
    taxa_dolar = 5.60
    taxa_euro = 6.60
    
    # Calcula conversões
    valor_dolar = converter_moeda(valor_reais, taxa_dolar)
    valor_euro = converter_moeda(valor_reais, taxa_euro)
    
    # Exibe resultados
    exibir_conversao(valor_reais, valor_dolar, valor_euro, taxa_dolar, taxa_euro)

if __name__ == "__main__":
    main()