#4.	Intercambiar las filas de una matriz 
#de acuerdo al orden ascendente de los promedios de cada fila



def ordenar_filas_por_promedio_ascendente(matriz):
    # Ordenamos las filas directamente usando el promedio como clave
    matriz_ordenada = sorted(matriz, key=lambda fila: sum(fila) / len(fila))
    return matriz_ordenada

def inicializar_ejercicio_4_matrices():
    matriz = [
        [3, 5, 1],
        [2, 2, 2],
        [4, 1, 0]
    ]
    
    matriz_ordenada = ordenar_filas_por_promedio_ascendente(matriz)
    
    for fila in matriz_ordenada:
        print(fila)

inicializar_ejercicio_4_matrices()