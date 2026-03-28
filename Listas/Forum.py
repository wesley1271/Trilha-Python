# Interação contendo cadastramentos de string em loops condicionais if and in pro array para negar se existia ou inserir com Welcome liberado log.
lista_usuarios = []

nickname = True
while nickname == True:
    usuario = input("Digite seu nome de usuario: ")
    if usuario.lower() in lista_usuarios:
        print("Nome já registrado!")
    else:
        print(f"Nome criado! Bem vindo {usuario.title()}!")
        lista_usuarios.append(usuario)
        nickname = False
print(lista_usuarios)
