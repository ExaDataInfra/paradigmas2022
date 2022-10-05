#Encapsulamiento
#ROMPER EL ENCAPSULAMIENTO ES MUY MALO Y HACE DAÑO

class myClass():
    
    #setear,establecer el valor.
    def setVal(self, val1):
        self.val1 = val1
    
    def getVal(self):
        print(self.val1)
    
    
objectA = myClass()

objectB = myClass()

objectB.setVal('My tech Institute is cool :O')

objectA.setVal('Hi Alex')


objectA.val1 = '900'  #<------------- ESTO ESTA MAL! ROMPE EL ENCAPSULAMIENTO!!

objectA.getVal()

objectB.getVal()
