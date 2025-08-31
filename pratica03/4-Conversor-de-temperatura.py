# Exercício 4: Conversor de Temperatura
def conversor_temperatura():
    temperatura = float(input("Digite a temperatura: "))
    unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
    unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()
    
    result = temperatura
    if unidade_origem == "C":
        if unidade_destino == "F":
            result = (temperatura * 9/5) + 32
        elif unidade_destino == "K":
            result = temperatura + 273.15
    elif unidade_origem == "F":
        if unidade_destino == "C":
            result = (temperatura - 32) * 5/9
        elif unidade_destino == "K":
            result = (temperatura - 32) * 5/9 + 273.15
    elif unidade_origem == "K":
        if unidade_destino == "C":
            result = temperatura - 273.15
        elif unidade_destino == "F":
            result = (temperatura - 273.15) * 9/5 + 32
    
    print(f"Temperatura convertida: {result:.2f} {unidade_destino}")

