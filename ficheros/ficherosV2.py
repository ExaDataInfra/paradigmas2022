import os

#------------------PRIMERA IMPLEMENTACION----------------------

archivo1 = open("archivo.txt","w")

lineas = ["Estoy aprendiendo \nA usar \nArchivos con Python en el IFTS 18.\n\n\nEste es el fin de mi archivo"]


archivo1.write("Hola zaraza!\n")

archivo1.writelines(lineas)

archivo1.close()


#------------------SEGUNDA IMPLEMENTACION----------------------

archivo1 = open("archivo.txt","r+")

print("Funcion leer: ")
print(archivo1.read())
print()

#Movemos el cursos con seek a la posicion dada.

archivo1.seek(0)




print( "Output of Readline function is ")
print(archivo1.readline())
print()

archivo1.seek(0)

# Diferencia entre read y readline
print("Salida de Readline(10) es ")
print(archivo1.read(10))
print()

archivo1.seek(0)

print("Salida de Readline(4) es")
print(archivo1.readline(4))

archivo1.seek(0)

print("Readline en crudo: ")
print(archivo1.readlines())
print()
archivo1.close()

archivoAntiguo = 'archivo.txt'

if os.path.isfile(archivoAntiguo):

    os.rename(archivoAntiguo, 'archivos3.txt')
    #os.remove(archivoAntiguo, 'archivos3.txt')
    os.remove('archivos3.txt')

else:

    print('El fichero', archivoAntiguo, 'no existe')
