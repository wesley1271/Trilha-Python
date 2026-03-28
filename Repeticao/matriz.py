# Preenche nas formatações bi dimensionais diagonais dos vetores "0", comutando "1" quando o x e o eixo baterem os espelhamentos em simulações puramente imagéticas lógicas de index range size len i e j arrays loops inter secando no grid terminal interativo console matrix etc...
linha = 1
tamanho = 3
for i in range(tamanho):
    for j in range(tamanho):
        if i == j or  i + j == tamanho - 1 :
            linha = 1 
        else:
            linha = 0
        print(linha, end=" ")
        linha += 1
    print()