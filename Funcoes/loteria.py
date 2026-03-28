# Função para sortear números e letras de uma lista
from random import choice

sorteio = [12, 45, 7, 88, 23, 56, 91, 34, 67, 10, 'A', 'M', 'T', 'X', 'L']

def sortear():
    return [choice(sorteio) for i in range(4)]
    
sorteado = sortear()
print(sorteado)