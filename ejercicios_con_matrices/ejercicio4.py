#4.	Intercambiar las filas de una matriz 
#de acuerdo al orden ascendente de los promedios de cada fila

import os

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

def mostrar_el_ejercicio():
    os.system("cls")
    print("Intercambiar las filas de una matriz")
    print("de acuerdo al orden ascendente de los promedios de cada fila")
    os.system("pause")
    os.system("cls")

def ordenar_filas_por_promedio_ascendente(matriz):
    # Ordenamos las filas directamente usando el promedio como clave
    matriz_ordenada = sorted(matriz, key=lambda fila: sum(fila) / len(fila))
    return matriz_ordenada

def mostrar_resultado(matriz,matriz_ordenada):
    print("matriz original")
    for fila in matriz:
        print(fila)
    print("matriz ordenada por promedios")
    for fila in matriz_ordenada:
        print(fila)

def inicializa_ejercicio_4():
    mostrar_el_ejercicio()
    matriz = pedir_datos()#[[3, 5, 1],[2, 2, 2],[4, 1, 0]]
    
    matriz_ordenada = ordenar_filas_por_promedio_ascendente(matriz)
    
    mostrar_resultado(matriz,matriz_ordenada)


    os.system("pause")
    os.system("cls")  
