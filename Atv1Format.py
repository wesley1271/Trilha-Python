# Sistema funcional operando conversões unitárias e fracionais de BRL aos seus valores equivalentes US$.
valor = float(input("Digite um valor em R$ para a conversão: "))
cotacao = float(input("Digite a cotação em USD para ser convertida: "))
valorUSD = valor / cotacao
print(f"O valor em USD é de: {valorUSD:.2f} USD")