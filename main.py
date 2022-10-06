# from dojo_pets import Ninja
from ninja import Ninja
from mascota import Mascota


my_treats = ['Gallina','Porco',"Bolsa Basura"]
my_pet_food = ['Pizza','Burger']

nibbles = Mascota("Bouchi","Horse",['bouchi on things','is invisible'],"Olá Olá")

adrien = Ninja("Antonio","Mora",my_treats,my_pet_food, nibbles)
adrien.alimentar()
adrien.alimentar()
adrien.alimentar()