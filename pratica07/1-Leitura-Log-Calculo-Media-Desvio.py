# Exercício 1: Leitura de Log e Cálculo de Média/Desvio Padrão
import numpy as np

def calcular_media_desvio(arquivo_log):
    tempos = []
    with open(arquivo_log, 'r') as f:
        for linha in f:
            if "Tempo de execução:" in linha:
                tempo = float(linha.split(":")[1].strip().split()[0])
                tempos.append(tempo)
    if tempos:
        media = np.mean(tempos)
        desvio = np.std(tempos)
        print(f"Média: {media:.2f}")
        print(f"Desvio padrão: {desvio:.2f}")
    else:
        print("Nenhum tempo encontrado.")

# Assumindo arquivo 'log.txt' com linhas como "Tempo de execução: 10.5 segundos"
calcular_media_desvio('log.txt')