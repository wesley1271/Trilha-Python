# Guarda a pluralidade temporal de nomes em perfis alocados via iterações pro dicionário "usuarios[]".
usuarios = {
    "nome": "",
    "idade": ""
}
i = 1
for nomes in range(1, 4):
    nome = input(f"Digite o {i}° nome: ")
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    i += 1    
    usuarios.append({"nome": nome, "idade": idade})
for usuario in usuarios:
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")