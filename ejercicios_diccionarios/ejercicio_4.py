#4.	Se tiene una matriz con datos numéricos, formar un diccionario de la siguiente forma:

#Clave el índice de la fila, 
#Valor lista con los números pares de cada fila


def inicializar_ejercicio_4_ejercicio_diccionario():
    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    lista = []
    diccionario = {}
    
    fil = len(matriz)
    col = len(matriz[0])
    
    contador = 1
    
    for fila in matriz:
        lista = []
        for col in fila:
            numero = col
            if numero % 2 == 0:
                lista.append(numero)
        diccionario[contador] = lista
        contador += 1
    
    print(diccionario)
    return diccionario
