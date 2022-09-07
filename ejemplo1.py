

def funcionSuperior():
    x = "Local"
    
    def funcionAnidada():
        nonlocal x
        x = "XXXXXXXXXXXXXXXXXX"
        print("Ambito interno: ", x)
         
         
    funcionAnidada()
    print("Ambito EXTERNO: ", x)
    

x = "GLOBAL"
funcionSuperior()
