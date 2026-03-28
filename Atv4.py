# Trata as métricas calculáveis cobrando lucros aos consumidores e impostos fiscais num veículo zero.
CF = int(input("Digite o custo de fábrica do carro ao consumidor: "))

if CF <= 12000 and CF > 0:
    CT = CF * 1.05
    CT = round (CT, 2)
    print ("O custo total de seu carro é de R$", CT)
elif CF > 12000 and CF <= 25000:
    CT = (CF * 1.25)
    CT = round (CT, 2)
    print ("O custo total de seu carro é de R$", CT)
elif CF > 25000:
    CT = (CF * 1.35)
    CT = round (CT, 2)
    print ("O custo total de seu carro é de R$", CT)
else:
    print ("Valor inválido, digite um valor positivo")
