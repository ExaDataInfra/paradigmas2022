def imprimeRegistro(nombre, apellido, **registro):
    print("El nombre es: ", nombre)
    print("El apellido es: ",apellido)
    
    for i in registro:
        print("{0}: {1}".format(i, registro[i]))
        

imprimeRegistro('Juan', 'Carlos', edad=27, domicilio='Av. Los alamos 787', empleado='si')
