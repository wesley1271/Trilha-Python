# Jogo de detetive onde conta e cataloga a positividade das respostas para julgar suspeito.
try:
    print(f"""Vamos fazer algumas perguntas sobre a vítima.
Você só poderá responder com 's' ou 'n'.""")

    res = 0
    
    pergunta1 = input("Telefonou para a vítima? (s/n): ")
    
    if pergunta1 == "s":
        res += 1    
    elif pergunta1 != "n":
        print("Valor inválido!")
        exit()
        
    pergunta2 = input("Esteve no local do crime? (s/n): ")
    
    if pergunta2 == "s":
        res += 1   
    elif pergunta2 != "n":
        print("Valor inválido!")
        exit()
        
    pergunta3 = input("Mora perto da vítima? (s/n): ")
    
    if pergunta3 == "s":
        res += 1    
    elif pergunta3 != "n":
        print("Valor inválido!")
        exit()
        
    pergunta4 = input("Devia para a vítima? (s/n): ")
    
    if pergunta4 == "s":
        res += 1   
    elif pergunta4 != "n":
        print("Valor inválido!")
        exit()
        
    pergunta5 = input("Já trabalhou com a vítima? (s/n): ")
    
    if pergunta5 == "s":
        res += 1    
    elif pergunta5 != "n":
        print("Valor inválido!")
        exit()

    if res == 0 or res == 1:
        print("Inocente!")
    elif res == 2:
        print("Suspeito!")
    elif res == 3 or res == 4:
        print("Cúmplice!")
    elif res == 5:
        print("Assassino!")

except ValueError:
    print("Valor inválido. Tente novamente!")

finally:
    print("Fim do programa")
