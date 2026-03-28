# Função para criar um dicionário de álbuns musicais
def album(nome_album, nome_artista, num_faixas=None):
    """Dicionario contendo informações de artistas e albuns"""
    album_dic = {'nome': nome_album, 'artista': nome_artista}
    if num_faixas:
        album_dic = {'nome': nome_album, 'artista': nome_artista, 'faixas':num_faixas}

    return album_dic
while True:
    print("Digite as informações para adicionar o album")
    print("Se quiser sair do programa digite 'sair'")
    nome_album = input("Digite o nome do álbum: ")
    if nome_album == 'sair':
        break
    nome_artista = input("Digite o nome do artista: ")
    if nome_artista == 'sair':
        break
    num_faixas = (input("Digite o número de faixas (ou deixe vazio): "))
    if num_faixas == 'sair' or '':
        break
    
    album_info = album(nome_album, nome_artista, num_faixas)
    print(album_info)
   
