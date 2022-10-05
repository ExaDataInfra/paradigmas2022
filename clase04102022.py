class myClass():
    
    def __init__(self, args1, args2, args3):
        self.args1 = args1
        self.args2 = args2
        self.args3 = args3
        
        
    def method1 (self):
        print("The args2 is: " + str(self.args2))
        
    def method2 (self,someString): 
        print ("Program-Method" + someString)
  
  
class 
#Instanciando una clase / Creando un objeto de mi clase
obj = myClass(5,4,3)

#llamando a un método de una clase
obj.method1()
#llamando a un método de una clase, con pasaje de parámetros
obj.method2('parametr')
