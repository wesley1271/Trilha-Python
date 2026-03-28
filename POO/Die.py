# Define uma Classe "Dado" programando o número dos lados customizados que fará suas faces se inverterem via randint pseudo-aleatório.
from random import randint

class Die:
    def __init__(self, sides=6):
        
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)
    
d6 = Die()
print("d6", d6.roll_die())

d10 = Die(10)
print("d10:", d10.roll_die())

d20 = Die(20)
print("d20:", d20.roll_die())