#4.	Se tiene una matriz con datos numéricos, formar un diccionario de la siguiente forma:

#Clave el índice de la fila, 
#Valor lista con los números pares de cada fila

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene una matriz con datos numéricos, formar un diccionario de la siguiente forma: ")
    print("Clave el índice de la fila,")
    print("Valor lista con los números pares de cada fila")
    os.system("pause")
    os.system("cls")
    
def pedir_datos():
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

def mostrar_respuesta(matriz, diccionario):
    print(f"matriz:")
    for fila in matriz:
        print(fila)
    print(f"diccionario: {diccionario}")
    
def inicializar_ejercicio_4():
    mostrar_el_ejercicio()
    
    matriz = pedir_datos()#[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
    os.system("cls")
    lista = []
    diccionario = {}
    contador = 1
    
    for fila in matriz:
        lista = []
        for col in fila:
            numero = col
            if numero % 2 == 0:
                lista.append(numero)
        diccionario[contador] = lista
        contador += 1
    
    mostrar_respuesta(matriz, diccionario)
    os.system("pause")
    os.system("cls")
    
    return diccionario
