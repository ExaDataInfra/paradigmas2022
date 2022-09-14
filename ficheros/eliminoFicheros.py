import os

f = 'prueba.txt'

if os.path.isfile(f):
    os.rename(f, 'bienvenido.txt')

else:
    print('El fichero', f, 'no existe')



f = 'bienvenido.txt'

if os.path.isfile(f):
    os.remove(f)
else:
    print("No pude borrarlo")
