# Confirma um ambiente controlado bloqueado caso as informações Login Admin não coincidam perfeitamente.
nome = input(f"""
Login
Nome: """)
senha = input("Senha: ")
if nome == "Admin" and senha == "1234":
    print("Login bem sucedido!")
else:
    print("Login ou senha incorreta")