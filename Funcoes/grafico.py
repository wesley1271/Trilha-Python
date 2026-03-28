# funcao que gera grafico de linha 
import numpy as np
import matplotlib.pyplot as plt

def gerar_grafico():
    # Tempo em segundos (valores fixos)
    tempo_segundos = [0, 30]

    # Porcentagem de bateria (valores fixos representando o consumo da bateria)
    bateria = [100, 80]  

    # Configuração do fundo da figura
    plt.figure(facecolor='lightgrey')

    # Plotar o gráfico de linha
    plt.plot(tempo_segundos, bateria, marker='o', linestyle='-.', color='blue', linewidth=3, markersize=10, label='Porcentagem de Bateria')

    # Adicionar título e rótulos aos eixos
    plt.title('PORCENTAGEM DE BATERIA AO LONGO DO TEMPO', fontsize=16, fontweight="bold", fontfamily="arial")
    plt.xlabel('TEMPO (SEGUNDOS)', fontsize=16, fontweight="bold")
    plt.ylabel('PORCENTAGEM DE BATERIA', fontsize=16, fontweight="bold")

    # Adicionar grade ao gráfico
    plt.grid(True, linestyle='--', alpha=1)

    # Adicionar legenda
    plt.legend(loc='lower left')

    # Ajustar layout para evitar sobreposição de elementos
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()

if __name__ == "__main__":
    gerar_grafico()
