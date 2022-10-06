class Mascota:
    def __init__(self, name , tipo , golosinas):
        self.name=name
        self.tipo=tipo
        self.golosinas=golosinas
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
        if self.tipo == "dog":
            print("guau guau guau")
        if self.tipo == "cat":
            print("miau miau miau")
        if self.tipo == "chicken":
            print("guau guau guau")

class Ninja(Mascota):
    def __init__(self, nombre, apellido, mascota, tipo, comida_mascota ):
        super().__init__( mascota, tipo, comida_mascota )
        self.nombre=nombre
        self.apellido=apellido
                	
    def pasear(self): 
        #walk the ninja's pet by invoking the play() pet method
        self.jugar() 
    def alimentar(self): 
        #feed the ninja's pet by invoking the eat() pet method 
        self.comer()
    def bañar(self): 
        #clean the ninja's pet by invoking the pet method sound()
        self.sonido()
