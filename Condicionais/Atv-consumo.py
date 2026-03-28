# Calcula valor de conta de luz formatando o preço por faixas lógicas do consumo em KWh.
consumo = int(input("Digite o quanto você consumiu de energia em KWh: "))
if consumo <= 100 and consumo > 0:
    print("Você consumiu", consumo, "KWh, e gastou o total de R$", 0.50 * consumo)
elif consumo >= 101 and consumo <= 200:
    print("Você consumiu", consumo, "KWh, e gastou o total de R$", 0.75 * consumo)
elif consumo > 200 and consumo < 300:
    print("Você consumiu", consumo, "KWh, e gastou o total de R$", consumo)
elif consumo > 300:
    print("Você consumiu", consumo, "KWh, e gastou o total de R$",  round(consumo * 1.1))
else:
    print("Valor inválido, digite um valor positivo")