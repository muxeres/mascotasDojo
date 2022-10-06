# from mascota import Mascota

# class Ninja(Mascota):
#     def __init__(self, nombre, apellido, mascota, tipo, comida_mascota ):
#         super().__init__( mascota, tipo, comida_mascota )
#         self.nombre=nombre
#         self.apellido=apellido
                	
#     def pasear(self): 
#         #walk the ninja's pet by invoking the play() pet method
#         self.jugar() 
#     def alimentar(self): 
#         #feed the ninja's pet by invoking the eat() pet method 
#         self.comer()
#     def bañar(self): 
#         #clean the ninja's pet by invoking the pet method sound()
#         self.sonido()
class Ninja:
    def __init__(self, nombre, apellido, golosinas,comida_mascota,mascota ):
        self.nombre=nombre
        self.apellido=apellido
        self.golosinas=golosinas
        self.comida_mascota=comida_mascota
        self.mascota=mascota
                	
    def pasear(self): 
        #walk the ninja's pet by invoking the play() pet method
        self.mascota.jugar() 
        return self
    def alimentar(self): 
        #feed the ninja's pet by invoking the eat() pet method 
        if len(self.comida_mascota) > 0:
            food = self.comida_mascota.pop()
            print(f"Feeding {self.mascota.name} {food}!")
            self.mascota.comer()
        else:
            print("Oh no!!! you need more pet food!")
        return self
        
    def bañar(self): 
        #clean the ninja's pet by invoking the pet method sound()
        self.mascota.sonido()