# Sistema automatizado for onde Admin desfruta da área Status Report reservada a administradores, diferentemente dos usuários casuais no laço condicional interativo dos usuários listados.
usuarios = ['Adriano', 'admin', 'lucas', 'Marcos', 'joão']
contador = 0

if usuarios:
    for usuario in usuarios:
        usuario = usuario.title()
        if usuario == 'admin':
            print(f"\nOlá, sr(a) {usuario}! Gostaria de ver um relatório de status?")
        else:
            print(f"\nOlá, {usuario}, bem-vindo de volta!") 
        contador += 1
    print("="*40)
    print(f"{contador} pessoa(s) logadas!")
    
else:
    print
    print("0 usuários existentes!")
    
novo_usuario = input("Digite seu nome de usuário: ")
for novo_usuario, usuario in usuarios:
    if novo_usuario == usuario:
        print("usuario existente")
    else:
        print("True!")

