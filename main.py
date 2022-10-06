# from dojo_pets import Ninja
from ninja import Ninja
from mascota import Mascota
# ninja1=Ninja("henry","torres","firulais","dog","galletas")
# print(ninja1.__dict__)
# ninja1.alimentar()
# ninja1.pasear()
# ninja1.bañar()
# print(ninja1.__dict__)

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['Pizza','Burger']

nibbles = Mascota("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")

adrien = Ninja("Adrien","Dion",my_treats,my_pet_food, nibbles)
adrien.alimentar()
adrien.alimentar()
adrien.alimentar()