# Examina e guarda na var de referência (Maior_N) no meio de rodadas de envios para reter as variáveis máximas limitantes fornecidas.
maior_n = 0
print("Digite 5 valores para descobrir o maior")
for i in range(5):
    n = int(input(f"Digite o {i+1}° número:"))
    if n > maior_n:
        maior_n = n
print(f"O maior número é {maior_n}")