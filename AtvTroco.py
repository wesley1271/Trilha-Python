# Estruturadas nas distribuições dos blocos, simulam os saques dos valores no terminal automatizando as notáveis cédulas da economia num ATM automático.
try:
    saque = int(input("Digite o valor desejado (valor de no mínimo entre 10 e 600): "))
    
    if saque < 10 or saque > 600:
        raise ValueError("Valor inválido")
    
    if saque >= 100:
        notas = saque // 100
        print(f"{notas} nota(s) de 100 reais!")
        saque %= 100 
    
    if saque >= 50:
        notas = saque // 50
        print(f"{notas} nota(s) de 50 reais!")
        saque %= 50

    if saque >= 10:
        notas = saque // 10
        print(f"{notas} nota(s) de 10 reais!")
        saque %= 10

    if saque >= 5:
        notas = saque // 5
        print(f"{notas} nota(s) de 5 reais!")
        saque %= 5 

    if saque >= 1:
        notas = saque // 1
        print(f"{notas} notas de 1 real!")
        
except ValueError:
   print("Digite um número!")
finally:
    print("Fim do programa")
