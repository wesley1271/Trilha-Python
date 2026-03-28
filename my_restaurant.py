# Exporta a base estrutural de Restaurant construindo subclasses funcionais da sua cozinha externa.
from restaurant import Restaurant

my_restaurant = Restaurant('wesley sabor', 'Árabe')
my_restaurant.describe_restaurant()

my_restaurant.mudar_num_servidos(3)
my_restaurant.clientes_servidos()
