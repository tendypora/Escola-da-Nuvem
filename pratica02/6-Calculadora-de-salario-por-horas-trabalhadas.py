# Programa para calcular o salário de um funcionário com base nas horas trabalhadas
# Lê o número do funcionário, horas trabalhadas e valor por hora, e exibe o salário formatado

def calcular_salario(horas_trabalhadas: int, valor_por_hora: float) -> float:
    """
    Calcula o salário com base nas horas trabalhadas e no valor por hora.
    
    Args:
        horas_trabalhadas (int): Quantidade de horas trabalhadas.
        valor_por_hora (float): Valor recebido por hora.
    
    Returns:
        float: Salário calculado, arredondado para duas casas decimais.
    """
    return round(horas_trabalhadas * valor_por_hora, 2)

def exibir_salario(numero_funcionario: int, salario: float) -> None:
    """
    Exibe o número do funcionário e o salário no formato especificado.
    
    Args:
        numero_funcionario (int): Número do funcionário.
        salario (float): Salário calculado.
    """
    print(f"NUMBER = {numero_funcionario}")
    print(f"SALARY = R$ {salario:.2f}")

def main():
    """
    Função principal que lê os dados de entrada, calcula o salário e exibe o resultado.
    """
    # Lê os dados de entrada
    numero_funcionario = int(input())
    horas_trabalhadas = int(input())
    valor_por_hora = float(input())
    
    # Calcula o salário
    salario = calcular_salario(horas_trabalhadas, valor_por_hora)
    
    # Exibe o resultado
    exibir_salario(numero_funcionario, salario)

if __name__ == "__main__":
    main()