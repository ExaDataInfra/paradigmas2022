#Herencia simple
from datetime import datetime 

#Clase Padre

class Fecha():
    
    def getFecha(self):
        fecha = datetime.now()
        print(fecha)
        
        

#Clase hija

class Hora(Fecha):
    
    def getTime(self):
        print("20:52")


hr = Hora()
hr.getTime()
hr.getFecha()
