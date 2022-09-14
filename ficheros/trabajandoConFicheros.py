multiplos  = [i for i in range(1,101) if i%6 == 0]

with open('prueba.txt', 'a') as f:
    f.write('Hola, los multiplos son:')

    for i in multiplos:
        f.write('\n' + str(i))

with open('prueba.txt', 'r') as f:
    print(f.read())

