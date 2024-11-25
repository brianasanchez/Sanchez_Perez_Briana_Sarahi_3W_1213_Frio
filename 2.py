print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos del realizador
print(" ")#espacio
#lista de palabras
lista = ['Parangaricutirimicuaro','hey yamila','enferma','celular']

def mas_larga(lista): #define funcion mas_larga
    numero = 0  #numero igual q 0
    pala = ''  #pala igual q 'palabra de lista'
    for palabra in lista: #para palabra en lista
        if len(palabra) > numero: #si len(palabra) mayor q numero
            numero = len(palabra)#numero igual q len(palabra)
            pala = palabra #pala igual q palabra
    return pala #return a pala

larga = mas_larga(lista)#larga igual q palabra mas larga

print(larga)#imprime palabra larga de la lista
print(" ")#espacio