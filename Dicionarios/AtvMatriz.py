# Solicita as notas passadas das disciplinas de alunos de uma escola para montar uma matriz bidimensional (listas nas listas).
matriz = []
matriz_aprovados = []
print("Digite a nota de 3 alunos e descubra sua média")
for i in range(3):
    soma = 0
    notas = []
    print(f"Aluno {i+1}")
    for l in range (4):
        
        nota = int(input(f"Digite a nota {l+1}: "))
        notas.append(nota)
        soma += nota
    matriz.append(notas)
       
    print("\nnotas:")
    for notas in matriz:
        print(notas)
    media = soma / len(notas)
    print (f"Media do aluno {i+1}: {media}")
    if media >= 6:
        lista_aprovados = []
        lista_aprovados.append(f"Aluno {i+1} aprovado, notas: {notas}")
        matriz_aprovados.append(f"{lista_aprovados}")
        print("\nAlunos aprovados:")
    for linha in matriz_aprovados:
        print(linha)
    
