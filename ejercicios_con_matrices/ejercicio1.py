#1.	Se tiene una matriz cuadrada con datos numéricos, 
#Comparar el promedio de los números pares que están 
#sobre la diagonal principal, con el promedio de los impares 
#de los datos que están bajo la diagonal principal.




def mostrar_resultado(a,b):
    if a > b:
     print(f"el promedio la matriz superior {a} es  mayor que el promedio de la matriz inferior {b}")
    elif a == b:
        print(f"el promedio la matriz superior {a} es  igual que el promedio de la matriz inferior {b}")
    else:
         print(f"el promedio la matriz superior {a} es  menor que el promedio de la matriz inferior {b}")

def encontrar_promedios(matriz):
    
    sumatoria_pares_superior = 0
    contador_pares_superior = 0
    sumatoria_impares_inferior = 0 
    contadores_impares_inferior = 0
    
    tamaño_matriz = len(matriz)#como es una matriz cuadrada tiene el mismo de filas y columnas
    
    for fila in range(tamaño_matriz):
        for col in range(tamaño_matriz):
            if fila < col:  # Superior a diagonal
                if matriz[fila][col] % 2 == 0:#comprueba ser par
                    sumatoria_pares_superior += matriz[fila][col]
                    contador_pares_superior += 1
            elif fila > col:  # Inferior a diagonal
                if matriz[fila][col] % 2 != 0:#comprueba si es impar
                    sumatoria_impares_inferior += matriz[fila][col]
                    contadores_impares_inferior += 1
    
    
    if contador_pares_superior != 0:
        prom_superior = sumatoria_pares_superior / contador_pares_superior 
    
    if contadores_impares_inferior:
        prom_inferior = sumatoria_impares_inferior / contadores_impares_inferior 
    
    
    return prom_superior, prom_inferior

def inicializa_ejercicio_1_matrices():
    
    matriz = [[4,6,1],
              [2,3,5],
              [7,8,9],
              ] 
    
    promedio_superior, promedio_inferior = encontrar_promedios(matriz)
    mostrar_resultado(promedio_superior, promedio_inferior)
    
inicializa_ejercicio_1_matrices()