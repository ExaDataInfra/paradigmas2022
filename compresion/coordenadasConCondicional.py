cordenadas = []

for x in range(0, 5 + 1):
    for y in range(0,5 + 1):
        cordenadas.append((x, y))

#print(cordenadas)


coordenadas = [(x, y) for x in range(0, 5 + 1) for y in range (0, 10 +1) if x%5 and y%5 == 0]

print(coordenadas)# Escribe tu código aquí :-)
