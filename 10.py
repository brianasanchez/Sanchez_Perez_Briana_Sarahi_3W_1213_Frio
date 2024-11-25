print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos
print(" ")#espacio
def es_bisiesto(anio):#define funcion es_bisiesto
#verifica dos condiciones relacionadas con un año
    if anio % 4 == 0 and anio % 10 != 0:
        return 'Es bisiesto'#devuelve mensaje
    else:#verifica si es falso
        return 'No es bisiesto' #devuelve mensaje

anio = int(input('Ingresa un año '))#solicita un año
eb = es_bisiesto(anio)#funcion y almacena resultado

print(eb)#imprime resultado de la funcion
print(" ")#espacio