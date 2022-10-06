class Mascota:
    def __init__(self, name , tipo , golosinas, sonido1):
        self.name=name
        self.tipo=tipo
        self.golosinas=golosinas
        self.sonido1=sonido1
        self.energia=0
        self.salud=0
    def dormir(self):
        #increases pet energia by 25
        self.energia += 25 
        print(f'Energia: {self.energia}')
    def comer(self): 
        #increases pet energia by 5 and salud by 10
        self.energia += 5
        self.salud += 10 
        print(f'Energia: {self.energia} Salud: {self.salud}')
    def jugar(self):
        #increases the pet's salud by 5
        self.salud += 5 
        self.energia -= 5
        print(f'Salud: {self.salud}')
    def sonido(self):
        print(self.sonido1) 
        # if self.tipo == "dog":
        #     print("guau guau guau")
        # if self.tipo == "cat":
        #     print("miau miau miau")
        # if self.tipo == "chicken":
        #     print("guau guau guau")

class TipoMascota(Mascota):
    def __init__(self, mascota, tipo,comida_mascota,sonido1, raza,color,peso):
        super().__init__( mascota,tipo, comida_mascota, sonido1 )
        self.raza=raza
        self.color=color
        self.peso=peso