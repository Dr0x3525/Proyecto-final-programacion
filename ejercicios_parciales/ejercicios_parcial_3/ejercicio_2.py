#se tiene un vector y una matriz con datos numericos, formar un diccionario de la siguiente forma:
#clave:un numero primo
#valor:las veces que se repite en el vector y la matriz 

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene un vector y una matriz con datos numericos, formar un diccionario de la siguiente forma:")
    print("clave:un numero primo")
    print("valor:las veces que se repite en el vector y la matriz")

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

def inicializar_ejercicio_2():
    mostrar_el_ejercicio()
    print("vector")
    vector = pedir_datos_lista()#[2, 5, 8, 5, 3, 10] cd = 6
    os.system("cls")
    print("matriz")
    matriz = pedir_datos_matriz()#[[1, 2, 5],[5, 7, 9],[0, 5, 5]]
    diccionario = {}
    
    for numero in vector:
        if Comprobar_ser_primo(numero):
            if numero not in diccionario:
              diccionario[numero] = 1
            else:
              diccionario[numero] += 1
              
    for fila in matriz:
        for col in fila:
            numero = col
            if Comprobar_ser_primo(numero):
                if numero not in diccionario:
                    diccionario[numero] = 1
                else:
                    diccionario[numero] += 1
                    
    print(f"vector: {vector}")
    print("matriz:")
    for fila in matriz:
        print(fila)
    print("veces que se repite cada numero primo en el vector y en la matriz")
    print(diccionario)
    os.system("pause")
    os.system("cls")        
    
