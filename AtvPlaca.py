# Sistema de cadastro que gera placas de veículos aleatórias (letras e números).
import random
import string

filename = "usuarios.txt"

def gerar_placa():
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    digito1 = str(random.randint(0, 9))
    letra4 = random.choice(string.ascii_uppercase)
    digitos_finais = ''.join(str(random.randint(0, 9)) for _ in range(2))
    return f"{letras}{digito1}{letra4}{digitos_finais}"

while True:
    print("\n== Sistema de Cadastro ==")
    print("1. Criar Usuário e adicionar carro")
    print("2. Listar Usuários e ver carro")
    print("3. Editar Usuário")
    print("4. Deletar Usuário")
    print("5. Sair")

    opcao = input("Digite a opção desejada (1-5): ")

    if opcao == '1':
        print("\n== CREATE: Adicionando um novo usuário ==")

        cpf = input("Digite o CPF do usuário (11 dígitos, apenas números): ")
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        carro = input("Digite o carro desejado: ")
        modelo = input("Digite o modelo do carro: ")
        cor = input("Digite a cor do carro: ")
        ano = input("Digite o ano do carro (ex: 2020): ")
        preco = input("Digite o preço do carro (ex: 85000): ")
        completo = input("O carro vem completo? (Sim/Não): ")
        placa_gerada = gerar_placa()

        with open(filename, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"CPF: {cpf}\n")
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"E-mail: {email}\n")
            arquivo.write(f"Carro: {carro}\n")
            arquivo.write(f"Modelo: {modelo}\n")
            arquivo.write(f"Cor: {cor}\n")
            arquivo.write(f"Ano: {ano}\n")
            arquivo.write(f"Preco: {preco}\n")
            arquivo.write(f"Completo: {completo}\n")
            arquivo.write(f"Placa: {placa_gerada}\n")
            arquivo.write("===\n")

        print(f"\nUsuário com CPF {cpf} adicionado com sucesso!")
        print(f"Carro: {carro} | Modelo: {modelo} | Cor: {cor} | Ano: {ano} | Preço: R$ {preco} | Completo: {completo} | Placa: {placa_gerada}")

    elif opcao == '2':
        print("\n== READ: Lista de usuários ==")
        try:
            with open(filename, 'r', encoding='utf-8') as arquivo:
                usuario = []
                for linha in arquivo:
                    linha = linha.strip()
                    if linha == "===":
                        print("\n".join(usuario))
                        print("-" * 40)
                        usuario = []
                    else:
                        usuario.append(linha)
                if usuario:
                    print("\n".join(usuario))
        except FileNotFoundError:
            print("Arquivo de usuários ainda não existe.")

    elif opcao == '3':
        print("\n== UPDATE: Atualizando um usuário ==")
        cpf_busca = input("Digite o CPF do usuário a ser atualizado: ")

        try:
            with open(filename, 'r', encoding='utf-8') as arquivo:
                blocos = arquivo.read().split("===\n")

            novos_blocos = []
            encontrado = False

            for bloco in blocos:
                if bloco.strip() == "":
                    continue
                linhas = bloco.strip().split("\n")
                if linhas[0] == f"CPF: {cpf_busca}":
                    novo_nome = input("Novo nome: ")
                    novo_email = input("Novo e-mail: ")
                    linhas[1] = f"Nome: {novo_nome}"
                    linhas[2] = f"E-mail: {novo_email}"
                    encontrado = True
                novos_blocos.append("\n".join(linhas))

            if encontrado:
                with open(filename, 'w', encoding='utf-8') as arquivo:
                    for bloco in novos_blocos:
                        arquivo.write(bloco + "\n===\n")
                print("Usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado.")

        except FileNotFoundError:
            print("Arquivo de usuários ainda não existe.")

    elif opcao == '4':
        print("\n== DELETE: Removendo um usuário ==")
        cpf_remover = input("Digite o CPF do usuário a ser removido: ")

        try:
            with open(filename, 'r', encoding='utf-8') as arquivo:
                blocos = arquivo.read().split("===\n")

            novos_blocos = []
            encontrado = False

            for bloco in blocos:
                if bloco.strip() == "":
                    continue
                if bloco.startswith(f"CPF: {cpf_remover}"):
                    encontrado = True
                    continue
                novos_blocos.append(bloco.strip())

            if encontrado:
                with open(filename, 'w', encoding='utf-8') as arquivo:
                    for bloco in novos_blocos:
                        arquivo.write(bloco + "\n===\n")
                print("Usuário removido com sucesso!")
            else:
                print("Usuário não encontrado.")
        except FileNotFoundError:
            print("Arquivo de usuários ainda não existe.")

    elif opcao == '5':
        print("\nSaindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida! Por favor, digite um número entre 1 e 5.")

