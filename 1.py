print(" ")#espacio
print("Sanchez Perez Briana Sarahi 1213, 3W")#datos del realizador
print(" ")#espacio
def max(n1, n2): #define funcion max
    if n1>n2:  #if si n1 mayor q num2
        return 'El mayor es {}'.format(n1)#return si el mayor es n1
    elif n1<n2:  #elif si n1 menor q n2
        return 'El mayor es {}'.format(n2)#return si el mayor es n2
    else: #else si ningun numero es mayor
        return 'Ninguna es mayor' #return si ninguno es mayor

if __name__ == '__main__': #bloque de codigo
    n1=int(input('Ingresa un numero: '))#solicita al usuario un numero
   
    n2=int(input('Ingresa otro numero: '))#solicita al usuario un numero
   
    mayor = max(n1,n2)#calcula el numero mayor

    print(mayor)#imprime numero mayor
print(" ")#espacio