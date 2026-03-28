# Modificador nativo do py para processamentos limpos das cordas.
message = "Hello world, python!"
print(message)
message = "Hello world, python3 congratulations!"
print(message)
print("The language 'python' is one of the most usable languages in the world! ")
print("python")
print("\tpython")

videogame = "  nintendoswitch2  "
print(videogame)
videogame = videogame.removeprefix("nintendo").strip()
print (videogame)
nome = "wesley  "
nome = nome.title().strip()
print(f"Olá {nome} como está seu dia?")