# Monta o objeto lógico (POO) pra restaurantes que guardam as funções metodificadoras pro usuário ativar aberturas e descrever serviços locais.
class Restaurant:
    def __init__(self, nome, culinaria):
        self.nome = nome
        self.culinaria = culinaria
        self.num_servidos = 0 
        
    def describe_restaurant(self):
        print(f"\nNome do restaurante: {self.nome}")
        print(f"Culinária: {self.culinaria}")
        
    def open_restaurant(self):
        print(f"\nO restaurante {self.nome} está aberto ao público!")
        
    def clientes_servidos(self):   
        print(f"Clientes servidos: {self.num_servidos}")
        
    def mudar_num_servidos(self, num):
        self.num_servidos = num
        
    def incrementar_num_servidos(self, num_increment):
        self.num_servidos += num_increment
        
restaurant1 = Restaurant(nome='farofeiros', culinaria='baiana')

restaurant2 = Restaurant(nome='cantinho do café', culinaria='Sulista')

restaurant3 = Restaurant(nome='Mamamias bolas', culinaria='italiana')
"""
print(restaurant1.describe_restaurant())
restaurant1.open_restaurant()

restaurant1.mudar_num_servidos(34)
restaurant1.incrementar_num_servidos(12)
restaurant1.clientes_servidos()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()
"""

class Clientes:
    def __init__(self, nome, sobrenome, num_mesa):
        self.nome = nome
        self.sobrenome = sobrenome
        
        self.num_mesa = num_mesa
        self.login_tentativas = 0
    
    def cumprimentar_clientes(self):
        print(f"\nOlá, {self.nome} {self.sobrenome}, seja bem vindo ao ")
        print(f"O número da sua mesa é o {self.num_mesa}!")
        
    def mostrar_login_tentativa(self):
        print(f"Tentativa de login: {self.login_tentativas}")
    
    def increment_login_tentativas(self):
       self.login_tentativas += 1
    
        
cliente1 = Clientes(nome='Ricardo', sobrenome='Melanda', num_mesa=1)


"""
cliente1.increment_login_tentativas()
cliente1.mostrar_login_tentativa()
cliente1.cumprimentar_clientes() 

cliente2 = Clientes(nome='Fernanda', sobrenome='Meza', num_mesa=2) 
cliente3 = Clientes(nome='Rafael', sobrenome='Rodriguez', num_mesa=3)
cliente4 = Clientes(nome='Manuela', sobrenome='Silva', num_mesa=4)
        

cliente2.cumprimentar_clientes()     
cliente3.cumprimentar_clientes()     
cliente4.cumprimentar_clientes()        

"""
class Sorveteria(Restaurant):
    def __init__(self, nome, culinaria):
        super().__init__(nome, culinaria)
    
    def sabor_sorvete(self, sabor):
        print(f"Seu sabor de sorvete é: {sabor}")
        
sorveteria1 = Sorveteria('gelatto', 'alemã')
sorveteria1.describe_restaurant()
sorveteria1.sabor_sorvete('morango')




