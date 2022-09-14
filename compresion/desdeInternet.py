from urllib import request

f = request.urlopen('https://www.ifts18.edu.ar/acad%C3%A9mico/calendario-presencialidad')

info = f.read()

print(info.decode('utf-8'))
