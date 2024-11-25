print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos del realizador
print(" ")#espacio
def binario_a_entero(binario):#denine funcion binario_a_entero
    entero = 0 #entero igual a 0
#Convertimos el número binario a una cadena de texto
    binario = str(binario)
#Se calcula el rango, que es la longitud de la cadena 'binario' menos 1
    rango = len(binario)-1
#Inicializamos una variable 'i' en 0
    i=0
#Ciclo 'for' que recorre cada carácter de la cadena 'binario'
    for bi in binario:
        entero += int(bi)*2**(rango+i)
 #Se decrementa 'i' en 1 en cada iteración para ajustar la potencia de 2
        i=i-1
    return entero
#Llamada a la función 'binario_a_entero' con el número 274
be = binario_a_entero(274)

print(be)#imprime resultado de la conversion
print(" ")#espacio