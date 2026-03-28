# Faz a leitura de um arquivo de texto definindo explicitamente o encoding UTF-8.
try:
    arquivo = open('arquivo.txt', 'r', encoding='UTF-8')
    conteudo = arquivo.read()
    print('Conteudo completo: ')
    print(conteudo)
    arquivo.close()

except FileNotFoundError:
    print("diretório não encontrado")
except PermissionError:
    print("Permissão negada!")