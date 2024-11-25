print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos
print(" ")#espacio
def contar_vocales(palabra): #define funcion contar_vocales
    vocales = ['a','e','i','o','u']#lista de vocales
    count = 0 #contador igual 0
    for pal in palabra: #para pal en palabra
        for vocal in vocales:#para vocal en lista
            if pal == vocal:#si pal igual vocal
                count += 1 #contador mas o igual 1
    return count #devuelve valor de count

palabra = str(input('Ingraesa una palabra: '))#solicita una palabra

cv = contar_vocales(palabra)#funcion y palabra
print(cv)#imprime resultado de la funcion
print(" ")#espacio