# Bloco preventor contendo o Try / Except no tratamento ante o colapso e a queima imprevista aos não-arquivos instáveis nas pastas locais ou pastas desfeitas sem as falhas.
try:
    documento = open ("documento.txt", "r")
    with documento:
        conteudo = documento.read
        print(conteudo)
except FileNotFoundError:
    print("Erro, o arquivo 'documento.txt' não foi encontrado!")
finally:
    documento.close()