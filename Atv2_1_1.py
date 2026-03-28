# Jogo de detetive onde conta e cataloga a positividade das respostas para julgar suspeito.
valor = float(input("Digite o valor para aplicarmos o desconto: "))

if valor >= 50 and valor <= 100:
    desconto = 0.05
    valorDes = valor * (1 - desconto)
    res = f"Ok, seu desconto é de 5%, entao o valor de {valor:.2f}R$ ficou em {valorDes:.2f}R$!"
    print(res)
elif valor > 100:
    desconto = 0.10
    valorDes = valor * (1 - desconto)
    res = f"Ok, seu desconto é de 10%, entao o valor de {valor:.2f}R$ ficou em {valorDes:.2f}R$!"
    print(res)
else:
    print("Não há desconto para este valor!")