# Programa para calcular o consumo médio de combustível de um veículo
# Calcula o consumo (km/l) e exibe os detalhes da viagem

def calcular_consumo_medio(distancia: float, combustivel_gasto: float) -> float:
    """
    Calcula o consumo médio de combustível em km/l.
    
    Args:
        distancia (float): Distância percorrida em quilômetros.
        combustivel_gasto (float): Quantidade de combustível gasto em litros.
    
    Returns:
        float: Consumo médio em km/l, arredondado para duas casas decimais.
    """
    return round(distancia / combustivel_gasto, 2)

def exibir_detalhes_consumo(distancia: float, combustivel_gasto: float, consumo_medio: float) -> None:
    """
    Exibe os detalhes da viagem e o consumo médio no terminal.
    
    Args:
        distancia (float): Distância percorrida em quilômetros.
        combustivel_gasto (float): Quantidade de combustível gasto em litros.
        consumo_medio (float): Consumo médio calculado em km/l.
    """
    print(f"\n=== Calculadora de Consumo de Combustível ===")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Combustível gasto: {combustivel_gasto:.2f} litros")
    print(f"Consumo médio: {consumo_medio:.2f} km/l")

def main():
    """
    Função principal que define os dados de entrada e orquestra o cálculo do consumo.
    """
    # Dados de entrada
    distancia = 300.0
    combustivel_gasto = 25.0
    
    # Calcula o consumo médio
    consumo_medio = calcular_consumo_medio(distancia, combustivel_gasto)
    
    # Exibe resultados
    exibir_detalhes_consumo(distancia, combustivel_gasto, consumo_medio)

if __name__ == "__main__":
    main()