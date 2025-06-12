#3.	Se tienen dos matrices ordenadas ascendentemente, 
#obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. 
# (ordenamiento por mezcla).

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tienen dos matrices ordenadas ascendentemente")
    print("obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. (ordenamiento por mezcla).")
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

    return sorted(matriz)

def mostrar_resultado(matriz_a,matriz_b,vector):
    print(f"matriz a:")
    for fila in matriz_a:
        print(fila)
    print(f"matriz b:")
    for fila in matriz_b:
        print(fila)
    print(f"vector resultante {vector}")


        
def inicializa_ejercicio_3():
    mostrar_el_ejercicio()
    print("matriz 1")
    matriz_A =  pedir_datos()#[[ 1,  4,  7],[10, 13, 16],[19, 22, 25]]
    os.system("cls")
    print("matriz 2")

    matriz_B =  pedir_datos()#[[ 2,  5,  8],[11, 14, 17],[20, 23, 26]]
    os.system("cls")

    vector = []
        
    num_filas_matriz_a = len(matriz_A)
    num_columnas_matriz_a = len(matriz_A[0])
    num_filas_matriz_b = len(matriz_B)
    num_columnas_matriz_b = len(matriz_B[0])
    
    indice_fila_matriz_a = 0
    indice_col_matriz_a = 0
    indice_fila_matriz_b = 0
    indice_col_matriz_b = 0


    while indice_fila_matriz_a < num_filas_matriz_a and indice_fila_matriz_b < num_filas_matriz_b: #el bucle termina cuando el indice sea mayor o igual que el numero de filas de la matriz que sea 
        
        numero_matriz_a = matriz_A[indice_fila_matriz_a][indice_col_matriz_a]
        numero_matriz_b = matriz_B[indice_fila_matriz_b][indice_col_matriz_b]
        
        if numero_matriz_a < numero_matriz_b:
            vector.append(numero_matriz_a) #si el numero de la matriz a es mayor lo agrega
            indice_col_matriz_a += 1 #aqui aumenta en uno la columna pero la fila sigue siendo igual
            
            if indice_col_matriz_a == num_columnas_matriz_a:#aqui ya cambia si el indice de la columan es igual que el num_columnas entonces significa que llego al fin de la fila y toca cambiar 
                indice_fila_matriz_a += 1
                indice_col_matriz_a = 0
        else:
            vector.append(numero_matriz_b) #si el numero de la matriz b es mayor lo agrega
            indice_col_matriz_b += 1 #aqui aumenta en uno la columna pero la fila sigue siendo igual
            if indice_col_matriz_b == num_columnas_matriz_b:#aqui ya cambia si el indice de la columan es igual que el num_columnas entonces significa que llego al fin de la fila y toca cambiar 
                indice_fila_matriz_b += 1
                indice_col_matriz_b = 0
    
    
    while indice_fila_matriz_a < num_filas_matriz_a:
        numero_matriz_a = matriz_A[indice_fila_matriz_a][indice_col_matriz_a]
        vector.append(numero_matriz_a) #si el numero de la matriz a es mayor lo agrega
        indice_col_matriz_a += 1 #aqui aumenta en uno la columna pero la fila sigue siendo igual
            
        if indice_col_matriz_a == num_columnas_matriz_a:#aqui ya cambia si el indice de la columan es igual que el num_columnas entonces significa que llego al fin de la fila y toca cambiar 
            indice_fila_matriz_a += 1
            indice_col_matriz_a = 0
                
    while indice_fila_matriz_b < num_filas_matriz_b:
        numero_matriz_b = matriz_B[indice_fila_matriz_b][indice_col_matriz_b]
        vector.append(numero_matriz_b) #si el numero de la matriz b es mayor lo agrega
        indice_col_matriz_b += 1 #aqui aumenta en uno la columna pero la fila sigue siendo igual
        if indice_col_matriz_b == num_columnas_matriz_b:#aqui ya cambia si el indice de la columan es igual que el num_columnas entonces significa que llego al fin de la fila y toca cambiar 
            indice_fila_matriz_b += 1
            indice_col_matriz_b = 0
  
    mostrar_resultado(matriz_A,matriz_B,vector)
    os.system("pause")
    os.system("cls")   
                     
    