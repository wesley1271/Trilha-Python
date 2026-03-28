# Identifica se a pessoa é maior de idade e se mora dentro ou fora do país.
idade = int(input("Digite sua idade: "))
nac = input("Você está vivendo fora do país? S/N ")

if idade >= 18 and nac == "N":
    print("Maior de idade vivendo no Brasil")
elif idade < 18 and nac == "N":
    print("Menor de idade vivendo no Brasil")
elif idade >= 18 and nac == "S":
    print("Maior de idade vivendo fora do Brasil")
else:
    print("Menor de idade vivendo fora do Brasil, me informe onde estão seus pais e seus documentos de autenticação")
