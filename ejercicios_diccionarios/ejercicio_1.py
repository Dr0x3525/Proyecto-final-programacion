#1.	Se tienen dos matrices, 
# formar un diccionario con los primos de las dos matrices y las veces que se repiten.

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

def inicializar_ejercicio_1_ejercicio_diccionario():
    matriz_1 = [    [ 2, 4, 6 ],
                    [ 3, 5, 7 ],
                    [ 10, 11, 12 ] ]
    
    matriz_2 =  [   [ 1, 2, 3 ],
                    [ 5, 7, 9 ],
                    [ 13, 2, 17 ] ]
    
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
    
    
    print(diccionario)
     
    
inicializar_ejercicio_1_ejercicio_diccionario()