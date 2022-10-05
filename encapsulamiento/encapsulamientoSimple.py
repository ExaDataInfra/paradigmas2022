#Otro ejemplo de encapsulamiento

class Enteros():
    
    def setEntero(self, valor1):
        self.valor1 = int(valor1)
        
    
    def incrementar(self, unidad):
        self.unidad = unidad
        
        self.valor1 = self.valor1 + int(self.unidad)
        
    def getEntero(self):
        print(self.valor1)
        

objeto = Enteros()

objeto.setEntero(30)

objeto.incrementar(20)

#objeto.getEntero()

estaMal = Enteros()

estaMal.valor1 = '90'

#estaMal.setEntero('90')

estaMal.incrementar(20)

#estaMal.unidad = 20

estaMal.getEntero()
