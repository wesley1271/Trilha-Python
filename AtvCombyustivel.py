# Atividade Abastecimento
try:
    quantidade = float(input("Digite a quantidade em litros do combustível: "))
    combustivel = input(f"""Digite o combustível desejado
G = GASOLINA
A = ÁLCOOL: """)

    if quantidade <= 20 and combustivel == "A":
        abastecer = 1.90 * quantidade
        desconto = abastecer - (abastecer * 0.97)
        custo = abastecer - desconto
        res = (f"O valor de {quantidade}L de álcool, é de  {custo:.2f}R$")
        print(res)
        exit()

    elif quantidade > 20 and combustivel == "A":
        abastecer = 1.90 * quantidade
        desconto = abastecer - (abastecer * 0.95)
        custo = abastecer - desconto         
        res = (f"O valor de {quantidade}L de álcool, é de  {custo:.2f}R$")
        print(res)

    if quantidade <= 20 and combustivel == "G":
        abastecer = 2.50 * quantidade
        desconto = abastecer - (abastecer * 0.96)
        custo = abastecer - desconto
        res = (f"O valor de {quantidade}L de gasolina, é de  {custo:.2f}R$")
        print(res)
        exit()

    elif quantidade > 20 and combustivel == "G":
        abastecer = 2.50 * quantidade
        desconto = abastecer - (abastecer * 0.94)
        custo = abastecer - desconto         
        res = (f"O valor de {quantidade}L de gasolina, é de  {custo:.2f}R$")
        print(res)

except ValueError:
    print("O valor digitado tem que ser numérico")
