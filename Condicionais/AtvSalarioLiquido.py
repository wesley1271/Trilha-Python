# Calcula quantitativamente o salário líquido de um funcionário que recebeu X% de porcentagem extra mensal.
salario = int(input("Digite seu salário atual: "))
porcentagem = int(input("Digite a porcentagem salarial: "))
if salario <=0:
    print("Salario inválido")
    exit()

if porcentagem <=0:
    print ("Digite um percentual válido")
    exit()
SF = salario * porcentagem / 100
print("Seu salario atual é de R$", salario, "e seu aumento é de R$", round(salario * (porcentagem / 100)), "e seu salário atual é de R$", salario + SF)