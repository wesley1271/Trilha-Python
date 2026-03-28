# Checa a idade do usuário para avisar se o voto nas eleições é obrigatório ou não.
idade = int(input("Informe sua idade para sabermos sua situação eleitoral: "))
if idade >=18 and idade < 65:
    print ("Voto obrigatório!")
elif idade >= 16 or idade >= 65:
    print ("Voto não obrigatório!")
else:
    print ("Não pode votar!")