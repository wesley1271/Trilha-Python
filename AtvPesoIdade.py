# Verifica 5 requisitos lógicos estruturados (idade, peso) para liberar doação de sangue.
idade = int(input("Qual sua idade?"))
peso = int(input("Precisamos saber o quanto você está pesando: "))
bafometro = input("Você ingeriu álcool dentro de 12h? S/N ")
tatoo = input("Você possui tatuagens? S/N ")
if idade >= 19 and idade <= 69 and peso >= 50 and tatoo == "N" and bafometro == "N":
    print ("Você pode doar sangue")
else:
    print ("Requisitos não atendidos")