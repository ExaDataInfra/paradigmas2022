#Otro ejemplo de herencia


class Animal():
    def __init__(self, nombreP, jugeteP):
        self.nombreP = nombreP
        self.jugeteP = jugeteP
        
    def comer(self, comida):
        print(self.nombreP + " esta comiendo " + comida)
        
    
class Perro(Animal):
    def emiteSonido(self, sonido):
        print("Mi perro dinamita hace... " + sonido)
        

class Gato(Animal):
    
    def duerme(self, estado):
        print("Mi gata " + self.nombreP + " esta " + estado) 
    
    def juega(self):
        print("Ahora "+ self.nombreP +" esta jugando con su " + self.jugeteP)
        

dinamita = Perro('Dinamita', 'Pelota')
dinamita.comer('Balanceado Royal Canin')

sakura = Gato('Sakura', 'Caja')
sakura.duerme('durmiendo')
sakura.juega()


print("Mi perro se llama " + dinamita.nombreP)
