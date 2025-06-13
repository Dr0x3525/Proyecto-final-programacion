#se tiene un vector y una matriz con datos numericos,
#ordenar la fila de una matriz descendentemente corresponiendente a la posicion de un numero fibonacci que sale
#del vector y esta en la matriz, este valor es el menor de los valores correspondientes al segundo y cuarto primo

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene un vector y una matriz con datos numericos,")
    print("ordenar la fila de una matriz descendentemente corresponiendente a la posicion de un numero fibonacci que sale")
    print("del vector y esta en la matriz, este valor es el menor de los valores correspondientes al segundo y cuarto primo")

    os.system("pause")
    os.system("cls")
    
def pedir_datos_lista():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista   

def pedir_datos_matriz():
    filas = int(input("cuantos filas tiene la matriz: "))
    cols = int(input("cuantos columnas tiene la matriz: "))
    matriz = []
    for fil in range(filas):
        filas = []
        for col in range(cols):
            numero = int(input(f"digita el valor de la fila {fil} y la columna {col}: "))
            filas.append(numero)
        matriz.append(filas)
        os.system("cls")

    return matriz
    
def comprobar_ser_fibbonaci(numero):
    numero = int(numero)
    f1 = 0 
    f2 = 1
    while f1 <= numero:
        if f1 == numero:
            return True
        temp =  f1
        f1 = f2
        f2 = f1 + temp
    return False

def Comprobar_ser_primo(numero):
    numero = int(numero)
    if numero <= 1:
        return False
    else:
        if numero == 2:
            return True
        else:
            for i in range(2,numero-1):
                if numero % i  == 0:
                    return False
            return True


def encontrar_indice_segundo_primo_y_cuarto_primo_del_vector(vector):
    contador_primos = 0
    for indice in range(len(vector)):
        numero = vector[indice]
        if Comprobar_ser_primo(numero):
            contador_primos += 1
            if contador_primos == 2:
                indice_segundo_primo = indice
            if contador_primos == 4:
                indice_cuarto_primo = indice
                return indice_segundo_primo,indice_cuarto_primo
    return None,None

def encontrar_indice_menor_numeros_rango(vector,menor,mayor):
    menor_numero = None
    for indice in range(menor+1,mayor):
        numero = vector[indice]
        if menor_numero == None:
          menor_numero = numero
          indice_menor_numero = indice
        else:
            if menor_numero > numero:
                menor_numero = numero
                indice_menor_numero = indice
                

    return indice_menor_numero


def encontra_fila_numero_menor_matriz(matriz,numero_buscado):
    filas = len(matriz)
    cols = len(matriz[0])
    
    for fil in range(filas):
        for col in range(cols):
             numero = matriz[fil][col]
             if numero == numero_buscado:
                 return fil 
    return None         

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)  

def incializar_ejercicio_3():
    mostrar_el_ejercicio()#mostrar ejercicio
    print("vector")
    vector = pedir_datos_lista()#[1, 2, 3, 5, 8, 13, 21, 34] cd = 8
    os.system("cls")
    print("matriz")    
    matriz = pedir_datos_matriz()#[[10, 20, 30],[2,  1,  3],[8,  5, 12],[21, 34, 55]]
    
    print(f"vector : {vector}")#mostrar vector
    
    indice_segundo_primo_vector, indice_cuarto_primo_vector = encontrar_indice_segundo_primo_y_cuarto_primo_del_vector(vector)#encontrar indice del segundo primo y 4 primo del vector
    
    if indice_cuarto_primo_vector == None:
        print("datos insuficientes en el vector")
    else:
        
        print(f"segundo primo: {vector[indice_segundo_primo_vector]}")#mostrar segundo primo vector 
        print(f"cuarto primo: {vector[indice_cuarto_primo_vector]}") #mostrar cuarto primo vector
        indice_menor_numero = encontrar_indice_menor_numeros_rango(vector,indice_segundo_primo_vector,indice_cuarto_primo_vector)#encontrar el indice del menor de todos los numeros
        
        print(f"numero menor en el rango: {vector[indice_menor_numero]}") #numero  menor en el rango
        os.system("pause")
        os.system("cls")
        
        fila_indice = encontra_fila_numero_menor_matriz(matriz,vector[indice_menor_numero])#encontrar en que fila de la matriz esta el numero del anterior paso
        
        print("matriz original")
        mostrar_matriz(matriz)#mostrar matriz original
        
        os.system("pause")
        os.system("cls")
        
        matriz[fila_indice] = sorted(matriz[fila_indice])  #ordenar esa fila descendentemente
        
        
        print("matriz nueva")
        mostrar_matriz(matriz)#mostrar matriz nueva
        
    os.system("pause")
    os.system("cls")

