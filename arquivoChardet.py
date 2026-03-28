# Detecta o encoding de um arquivo usando chardet e lê o conteúdo em texto.
import chardet


with open('arquivo.txt', 'rb') as f:
    data = f.read(1000)  
    resultado = chardet.detect(data)
    print("Saida de dados de forma crua(em bytes)")
    print(data)

print('Codificação detectada:', resultado['encoding'])


with open('arquivo.txt', 'r', encoding=resultado['encoding']) as f:
    conteudo = f.read()
    print('Conteúdo lido corretamente:')
    print(conteudo)