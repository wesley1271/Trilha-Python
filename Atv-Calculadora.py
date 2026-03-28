# Calculadora inteligente no console baseada na operação pedida pelo input.
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
operacao = input("Escolha qual operação será utilizada (+, -, *, /): ")
if operacao == "+":
    print(n1 + n2)
elif operacao == "-":
    print (n1 - n2)
elif operacao == "*":
    print (n1 * n2)
elif operacao == "/":
    print (n1 / n2)
else:
    print ("Operação inválida!")