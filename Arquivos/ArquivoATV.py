# Lê o conteúdo de um arquivo de texto e lida com erros de permissão.
try:
    arquivo = open('arquivo.txt', 'r')
    conteudo = arquivo.read()
    print('Conteudo completo: ')
    print(conteudo)
    arquivo.close()

except FileNotFoundError:
    print("diretório não encontrado")
except PermissionError:
    print("Permissão negada!")