# Atividade Reajuste Salarial
try:
    salario = int(input("Digite seu salário para o reajuste: "))
    if salario <= 280:
        reajuste = salario * 1.20
        aumento = reajuste - salario
        print(f"Seu salario é de {salario}R$, e com o novo reajuste de 20%, é de {reajuste}R$ com o aumento de {aumento}R$")
        
    elif salario > 280 and salario <= 700:
            reajuste = salario * 1.15
            aumento = reajuste - salario
            print(f"Seu salario é de {salario}R$, seu salário com o novo reajuste de 15%, é de {reajuste}R$ com o aumento de {aumento}R$")
except ValueError:
    print("Valor inválido, tente novamente!")