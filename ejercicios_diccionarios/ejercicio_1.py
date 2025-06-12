#1.	Se tienen dos matrices, 
# formar un diccionario con los primos de las dos matrices y las veces que se repiten.

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
    print("Se tienen dos matrices")
    print("formar un diccionario con los primos de las dos matrices y las veces que se repiten.")
    os.system("pause")
    os.system("cls")
    
def mostrar_resultado(matriz_1,matriz_2,diccionario):
    print("matriz 1")
    for fila in matriz_1:
        print(fila)
    print("matriz 2")
    for fila in matriz_2:
        print(fila)
    print("diccionario con los primos de las matrices y las veces que se repiten:")
    print(diccionario)
    
def determinar_ser_primo(numero):
    if numero <= 1:
        return False
    else:
        if numero == 2:
            return True
        else:
            for i in range(2,numero-1):
                if numero % i == 0:
                    return False
            return True

def inicializar_ejercicio_1():
    mostrar_el_ejercicio()
    print("matriz 1")
    matriz_1 = pedir_datos()#[[ 2, 4, 6 ],[ 3, 5, 7 ],[ 10, 11, 12 ] ]
    os.system("cls")
    print("matriz 2")
    matriz_2 =  pedir_datos() #[[ 1, 2, 3 ],[ 5, 7, 9 ],[ 13, 2, 17 ] ]
    os.system("cls")
    diccionario = {}
    
    fil_matriz_1 = len(matriz_1)
    col_matriz_1 = len(matriz_1[0])
    fil_matriz_2 = len(matriz_2) 
    col_matriz_2 = len(matriz_2[0])
    
    for fila in range(fil_matriz_1):
        for col in range(col_matriz_1):
            numero_matriz_1 = matriz_1[fila][col]
            if determinar_ser_primo(numero_matriz_1):
                if numero_matriz_1 in diccionario:
                    diccionario[numero_matriz_1] = diccionario[numero_matriz_1]+1 
                else:
                    diccionario[numero_matriz_1] = 1

    for fila in range(fil_matriz_2):
        for col in range(col_matriz_2):
            numero_matriz_2 = matriz_2[fila][col]
            if determinar_ser_primo(numero_matriz_2):
                if numero_matriz_2 in diccionario:
                    diccionario[numero_matriz_2] = diccionario[numero_matriz_2]+1 
                else:
                    diccionario[numero_matriz_2] = 1
    
    mostrar_resultado(matriz_1,matriz_2,diccionario)
    os.system("pause")
    os.system("cls") 
    