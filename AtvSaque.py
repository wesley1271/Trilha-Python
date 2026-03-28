# Estruturadas nas distribuições dos blocos, simulam os saques dos valores no terminal automatizando as notáveis cédulas da economia num ATM automático.
convidados = []

for i in range(3):
    convite = input(f"Digite o nome do {i+1}° convidado que gostaria de chamar para seu jantar? ")
    message = (f"{convite.title()}, Bem-vindo a meu jantar! ")
    print(message)
    convidados.append(convite)
    
print("\nSua lista de convidados:\n")

for i, convidado in enumerate(convidados):
    print(f"{i+1} - {convidado}")

excluir = int(input(("\nDigite o número do convidado que desistiu de ir: ")))
if excluir >= 1 and excluir <= 3:
    excluido = convidados.pop(excluir-1)
    print(f"Convidado {excluido} excluido!")
else:
    print("Número incorreto!")

print(convidados)
