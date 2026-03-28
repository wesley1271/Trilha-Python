# Lida e monta um gerador visual via range multiplicando contador a cada step gerando e desenhando o limite decimal padronizado tabuadista iterativamente multiplicável no console.
contador = 1
for numero in range(1 , 11):
    print(f" {numero} x {contador} = {contador * numero}")
    contador += 1
    