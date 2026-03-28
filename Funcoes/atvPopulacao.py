# funcao que calcula o tempo para um país ultrapassar o outro em população
def calcular_populacao(taxaA, paisA, taxaB, paisB):
    contadorAnual = 1
    while paisA < paisB:
        paisA += paisA * (taxaA / 100)
        paisB += paisB * (taxaB / 100)
        contadorAnual += 1
    return contadorAnual, paisA, paisB
con, A, B = calcular_populacao(3.5, 98000000, 1.5, 200000000)
print(f"O país A ultrapassará o país B em {con} anos")
print(f"População final: A = {A:.2f}, B = {B:.2f}")
        
        
        