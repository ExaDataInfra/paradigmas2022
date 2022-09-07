def funcionQueSuma(numeroUnoP, numeroDosP):
    return ( numeroUnoP + numeroDosP ) / 2
    


print("El promedio es " + str(funcionQueSuma(95, 5)))


def funcionQuePromedia(*args):
    suma = sum(args)
    return suma / len(args)


print(funcionQuePromedia(1, 1, 1, 1, 1))
