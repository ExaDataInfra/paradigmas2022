multiplos  = [i for i in range(1,101) if i%6 == 0]

print(multiplos)

multiplos = []
noMultiplos = []
for i in range(1,101):
    if i%5 == 0:
        multiplos.append(i)
    else:
        noMultiplos.append(i)

print(noMultiplos)


#[expresion FOR variable in lista/coleccion if condicion]
