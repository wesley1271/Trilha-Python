# Acumula listagens obtendo informações contínuas buscando limites superiores, identificando também menores e listando cada uma anexada na soma total deles inteiros.
listanum = []
maior = 0
menor = 0
soma = 0
print("Digite 5 números inteiros: ")
for i in range (1, 6):
    num  =  int(input(f"Número {i}: "))
    if num > maior:
        maior = num
    elif num < maior and num < menor:
        menor = num
    listanum.append(num)
    soma += num
print(listanum)
print (f"Da lista mostrada, o maior número é: {maior} e o menor é {menor}")
media = soma / len(listanum)
print(f"A média desta lista é de: {media}")
    
    