print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos
print(" ")#espacio
age_list = [] #lista vacia

count = 0 #contador iniciando en 0
while count < 20: #mientras contador menor q 20
    age = int(input('Ingresa tu edad: '))#solicita ingresar edad
    age_list.append(age)#agrega el valor de 'age' al final de la lista
    count += 1 #contador mas o igual q 1

i=0 #variable i igual a 0
for e in age_list: #iterar elementos de la lista
    if e > 20: #si e mayor q 20
        i+=1 #variable i mas o igual q 1

print(i)#imprime variable i
print(" ")#espacio