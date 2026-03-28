# Programa iterativo onde o indivíduo pode modificar, expor e deletar tipos sortidos de seus gostos frugívoros.
# Dicionário de frutas
try:
    listaFrutas = []
    i = 0
    print("Digite um total de 5 frutas para serem listadas e escolhidas")
    for frutas in range(0, 5):
        fruta = input(f"fruta {i + 1}: ")
        listaFrutas.append(fruta)
        i += 1
    pergunta = input(f"""Sua lista atual: {listaFrutas}
    Gostaria de adicionar mais frutas?
    S = Sim
    N = Não
    D = Deletar frutas""").upper()

    if pergunta == "S":
        while pergunta == "S":
                add = input(f"fruta: {len(listaFrutas) + 1}")
                listaFrutas.append(add)
                i += 1
                print(f"Sua lista atual: {listaFrutas}")
                pergunta = input(f"""Gostaria de adicionar mais frutas?
    S = Sim
    N = Nâo 
    D = Deletar frutas:  """).upper()
    elif pergunta == "D":
        while pergunta == "D":
        
            for i, fruta in enumerate(listaFrutas): 
                print(f"{i+1}: {fruta}")
            delet = int(input("Digite o número que gostaria de remover: "))    
            if delet >= 1 and delet <= len(listaFrutas):
                fruta_removida = listaFrutas.pop(delet - 1)
                print(f"Você removeu {fruta_removida}")
                print(f"Sua lista atual: {listaFrutas}")
                break
            else:
                print("Número inválido! Tente novamente.")
except ValueError:
    print("Valor incorreto. Tente novamente!")
            