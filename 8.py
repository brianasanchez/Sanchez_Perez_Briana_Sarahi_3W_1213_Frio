print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos
print(" ")#espacio
#lista de nombres
lista_nombres = ['Rocio', 'Jose','Jerry','Tommy','Cesar','Julia','Lia', 'Devora']
def buscar_letra(letra): #define funcion buscar_letra
    count = 0 #contador inicia en 0
    for nombre in lista_nombres: #bucle for
#Verifica si la primera letra del nombre (nombre[0]) es igual a la letra dada 'letra'
        if nombre[0].upper() == letra.upper():
            count += 1 #contador mas o igual q 1
    return count #devuelve valor de count

letra = str(input('Ingresa una letra: '))#solicita ingresar letra
num_let = buscar_letra(letra)#llama la funcion y almacena resultado
print(num_let)#imprime resultado de la funcion
print(" ")#espacio