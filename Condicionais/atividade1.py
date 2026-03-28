# Calcula a média num bimestre e informa via IFs se o aluno foi aprovado ou reprovado.
nota = int(input("Digite a nota: "))
nota2 = int(input("Digite a segunda nota: "))      
media = (nota + nota2) / 2
print ("Sua nota final é", media )
if media >= 6:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")
    