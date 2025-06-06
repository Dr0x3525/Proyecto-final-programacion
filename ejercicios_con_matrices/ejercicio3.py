#3.	Se tienen dos matrices ordenadas ascendentemente, 
#obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. 
# (ordenamiento por mezcla).



def inicializar_ejercicio_3_matrices():

    matriz_A = [    [ 1,  4,  7],  
                    [10, 13, 16],  
                    [19, 22, 25]  ]
    
    matriz_B = [    [ 2,  5,  8],
                    [11, 14, 17], 
                    [20, 23, 26]   ]
    
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
  
  
    print(vector)
                     
inicializar_ejercicio_3_matrices()
    