# Promove cálculos matemáticos em formatações de USD para BRL via multiplicadores predefinidos nas variáveis lógicas.
n1 = float(input("Digite um valor em R$ para uma conversão: "))
VC = float(input("Digite o valor da cotação do Dólar: "))
print (f"O valor de {n1}R$ em dólar com a cotação de {VC} é de {n1 * VC} USD")