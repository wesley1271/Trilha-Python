# Calculadora onde saídas são tratadas e formatadas unicamente via F-Strings de sintaxe.
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
operacao = input("Escolha qual operação será utilizada (+, -, *, /): ")
if operacao == "+":
    print (f"A soma de {n1} + {n2} = {n1 + n2}")
elif operacao == "-":
    print (f"A subtração de {n1} - {n2} = {n1 - n2}")
elif operacao == "*":
    print (f"A multiplicação de {n1} * {n2} = {n1 * n2}")
elif operacao == "/":
    print (f"A divisão de {n1} / {n2} = {n1 / n2}")
else:
    print ("Operação inválida!")