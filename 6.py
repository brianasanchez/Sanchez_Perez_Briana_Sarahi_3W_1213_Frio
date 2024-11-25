print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos
print(" ")#espacio
import datetime 
anio_actual = int(input('Año actual: '))#solicita ingresar año

count = 0 #contador inciando en 0
while count < 3: #mientras contador menor q 3
    name = input('Ingresa tu nombre: ')#solicita ingresar nombre
    nacimiento = int(input('Año de nacimiento: '))#solicita año de nacimiento
    count += 1 #contador mas o igual q 1
#imprime mensaje con los datos
    print('Hola', name, 'cumples', anio_actual-nacimiento,'años')
    print('*'*10)#imprime 
print(" ")#espacio