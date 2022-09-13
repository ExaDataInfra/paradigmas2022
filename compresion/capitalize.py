lenguajes = ["python", "HoLaCoMoEsTaS *_*", "c++", "java", "FoRtRaN IV", "cOBOL", "aNSI cOBOL", "pHP"]


miVariableEsPepe = "pepe"

nombre2 = miVariableEsPepe.capitalize()

print(nombre2)

#listaTransformada = []

for lenguaje in lenguajes[::]:
    lenguajes.append(lenguaje.capitalize())
    del lenguajes[0]

print(lenguajes)
