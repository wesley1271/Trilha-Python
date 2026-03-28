# Mantêm o cursor solicitando input usando While, estagnando quando totaliza as 5 quantias onde por fim a soma cumulativa global somou todas e as enviou imprimindo somas no terminal.
soma = 0
contador = 0
while contador < 5 :
    num = int(input("Digite um número: "))
    contador += 1
    soma += num
print("A soma dos 5 números são de: ", soma)