# Trata as métricas calculáveis cobrando lucros aos consumidores e impostos fiscais num veículo zero.
try:
    carne = input(f"""Hoje temos promoção, porém só é possível escolher uma carne.
    Me fale qual carne quer comprar: 
    F = Filé duplo
    A = Alcatra
    P = Picanha   """)
    
    peso = float(input("Escolha o peso da carne escolhida: "))
   
    if carne == "F":
        if peso <= 5:
            preco = 5.80 * peso
        else:
            preco = 4.90 * peso
        carne = "Filé duplo"
        print(f"Você escolheu o {carne}, e escolheu a quantidade de {peso:.2f}kg, e ficou no total de {preco:.2f}R$")
    
    elif carne == "A":
        if peso <= 5:
            preco = 7.50 * peso
        else:
            preco = 5.70 * peso
        carne = "Alcatra"
        print(f"Você escolheu a {carne}, e escolheu a quantidade de {peso:.2f}kg, e ficou no total de {preco:.2f}R$")
    
    elif carne == "P":
        if peso <= 5:
            preco = 8.90 * peso
        else:
            preco = 6.90 * peso
        carne = "Picanha"
        print(f"Você escolheu a {carne}, e escolheu a quantidade de {peso:.2f}kg, e ficou no total de {preco:.2f}R$")
    
    pagamento = input(f"Qual a forma do pagamento, cartão ou dinheiro? C = cartão | D = dinheiro: ")
    
    if pagamento == "C":
        desconto = preco - (preco * 0.05)
        print(f"{desconto:.2f}R$ no cartão ")
        
    elif pagamento == "D":
        print(f"{preco:.2f}R$ no dinheiro ")

except ValueError:
    print("Digite um valor numérico!")