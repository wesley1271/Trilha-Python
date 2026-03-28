# Demonstra a criação, escrita e leitura de um arquivo de texto local (base.txt).
#CRIAR REGISTROS
arquivo = open('base.txt','w',encoding='utf-8')
arquivo.write('Olá, Mundo!!\n')
arquivo.write('Sejam bem vindos!!')
arquivo.close()


#LER REGISTROS
arquivo = open('base.txt','r',encoding='utf-8')
conteudo = arquivo.readline()
arquivo.close()
#print(conteudo)

#LER DINAMICAMENTE
arquivo = open('base.txt','r',encoding='utf-8')
print("Leitura linha por linha")
for linha in arquivo:
    print(linha.strip())
arquivo.close()
