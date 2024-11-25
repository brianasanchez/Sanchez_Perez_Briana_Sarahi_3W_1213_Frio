print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos del realizador
print(" ")#espacio
lista = ['nadie', 'cero', 'numero', 'sola']#lista de palabras
n = 4 #numero de palabras

def filtrar_palabras(lista, n):#define funcion filtrar_palabras
    palabras = [] #lista vacia 'palabras'
    # Itera sobre cada palabra 'l' en la lista 'lista'
    for l in lista:
        #longitud de la palabra
        if len(l) > n:
            palabras.append(l)
    #devuelve lista de palabras
    return palabras
#Llamada a la función 'filtrar_palabras' pasando la lista 'lista' y el número 'n'
fp = filtrar_palabras(lista,n)
#imprime resultado de funcion filtrar_palabras
print(fp)
print(" ")#espacio