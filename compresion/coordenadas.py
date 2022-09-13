# Escribe tu código aquí :-)
cordenadas = []

for x in range(0, 5 + 1):
    for y in range(0,5 + 1):
        cordenadas.append((x, y))

#print(cordenadas)


coordenadas = [(x, y) for x in range(0, 5 + 1) for y in range (0, 10 +1)]

print(coordenadas)
