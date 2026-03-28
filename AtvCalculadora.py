# Calculadora de console capaz de executar as quatro operações básicas (soma, subtracao etc).
try:
    n1 = int(input(f"""Bem vindo(a) a calculadora!
Digite um número a ser calculado: """))
    n2 = int(input("Agora digite outro número: "))
    operacao = (input(f""" Muito bem, agora escolha uma operacao para utilizar: 
                      (+ | - | * | /):   """))
    if operacao == "+":
        res = (f"Você escolheu '+', A soma de {n1} + {n2} é de: {n1 + n2}!")
        print (res)
    elif operacao == "-":
        res = (f"Você escolheu '-', A subtração de {n1} - {n2} é de: {n1 - n2}!")
        print(res)
    elif operacao == "*":
        res = (f"Você escolheu '*', A multiplicação de {n1} * {n2} é de: {n1 * n2}!")
        print(res)
    elif operacao == "/":
        res = (f"Você escolheu '/', A divisão de {n1} / {n2} é de: {n1 / n2}!")
        print(res)
except ZeroDivisionError:
    print("O número não pode ser dividido por 0, Tente novamente!")
except ValueError:
    print("Valor inválido, Tente novamente!")
finally:
    print("Fim do programa!")