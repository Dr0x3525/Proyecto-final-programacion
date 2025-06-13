#se tienen un vector y una matriz con datos numericos, reemplazar el rango de la matriz comprendido entre el segundo primo y el tercer fibonacci, 
# con el factorial del valor mayor del segundo y ultimo fibonacci del vector.
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tienen un vector y una matriz con datos numericos, reemplazar el rango de la matriz comprendido entre el segundo primo y el tercer fibonacci,")
    print("con el factorial del valor mayor del segundo y ultimo fibonacci del vector.")
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
    
def comprobar_ser_fibbonaci(numero):
    numero = int(numero)
    f1 = 0 
    f2 = 1
    while f1 <= numero:
        if f1 == numero:
            return True
        temp =  f1
        f1 = f2
        f2 = f1 + temp
    return False

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

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = i * resultado
    return resultado

def encontrar_segundo_fibbonaci(vector):
    contador_fib = 0
    for indice in range(len(vector)):
        if comprobar_ser_fibbonaci(vector[indice]):
            contador_fib += 1
            if contador_fib == 2:
                return indice
    return None

def encontrar_ultimo_fibbonaci(vector):
    for indice in range(len(vector)-1,0,-1):
        if comprobar_ser_fibbonaci(vector[indice]):
                return indice
    return None

def encontrar_valor_mayor_vector(vector,menor,mayor):
    valor_mayor = None  
    for indice in range(menor+1,mayor):
        if valor_mayor == None:
            valor_mayor = vector[indice]
        else:
            if valor_mayor < vector[indice]:
                valor_mayor = vector[indice]
    valor_mayor = factorial(valor_mayor)
    return valor_mayor

def encontrar_segundo_primo_matriz(matriz):
    fil = len(matriz)
    col = len(matriz[0])
    contador_primos = 0
    for filas in range(fil):
        for cols in range(col):
            numero = matriz[filas][cols]
            if Comprobar_ser_primo(numero):
                contador_primos += 1
                if contador_primos == 2:
                    return filas,cols
    return None,None

def encontrar_tercer_fib_matriz(matriz):
    fils = len(matriz)
    cols = len(matriz[0])
    contador_fib = 0 
    for fil in range(fils):
        for col in range(cols):
            numero = matriz[fil][col]
            if comprobar_ser_fibbonaci(numero):
                contador_fib += 1
                if contador_fib == 3:
                    return fil,col
    return None,None

def ordenar_menor_indice_matriz(fila1, col1, fila2, col2):
    if (fila1 < fila2) or (fila1 == fila2 and col1 < col2):
        return fila1, col1, fila2, col2  # Ordena la fila del segundo primo primero
    else:
        return fila2, col2, fila1, col1  # Ordena fila del tercer fib primero
    

def incializar_ejercicio_1():
    mostrar_el_ejercicio()
    print("vector:")
    vector = pedir_datos_lista()#[4,3,3, 7, 3, 10, 3, 8, 2] cd = 9
    os.system("cls")
    print("matriz:")
    matriz =  pedir_datos_matriz()#[[5, 12, 8, 9],[7, 11, 4, 6],[3, 10, 2, 15]] 
    os.system("cls")
    
    indice_segundo_fib = encontrar_segundo_fibbonaci(vector)#encontrar segundo fibbonaci vector
    indice_ultimo_fib = encontrar_ultimo_fibbonaci(vector)#encontrar segundo fibbonaci vector
    
    if indice_segundo_fib == None or indice_ultimo_fib == None:
      print("insuficientes datos en el vector")
    else:
        print(f"vector: {vector}")
        print(f"segundo fibonacci: {vector[indice_segundo_fib]}")
        print(f"ultimo fibonacci: {vector[indice_ultimo_fib]}")
        
        numero_mayor_vector = encontrar_valor_mayor_vector(vector,indice_segundo_fib,indice_ultimo_fib)#aqui hay que encontrar el numero mayor entre el segundo fib y ultimo fib del vector
        
        print(f"el numero mayor entre esto 2 es: {numero_mayor_vector}")
        
        fila_segundo_primo, columna_segundo_primo = encontrar_segundo_primo_matriz(matriz)#encontrar_segundo_primo_matriz
        fila_tercer_fib, columna_tercer_fib = encontrar_tercer_fib_matriz(matriz)#encontrar_tercer_fib_matriz
        
        if fila_segundo_primo == None or fila_tercer_fib == None:
          print("insuficientes datos en la matriz")
        else:        
            os.system("pause")
            os.system("cls")
            
            print("matriz original:")
            for fila in matriz:
                print(fila)
            
            print(f"segundo primo de la matriz: {matriz[fila_segundo_primo][columna_segundo_primo]}")
            print(f"tercer fibbonacci de la matriz: {matriz[fila_tercer_fib][columna_tercer_fib]}")
            
            fila_menor, col_menor, fila_mayor, col_mayor = ordenar_menor_indice_matriz(fila_segundo_primo, columna_segundo_primo,fila_tercer_fib, columna_tercer_fib)
            
            for fila in range (fila_menor+1,fila_mayor):#cambia los numeros de las filas que estan entre la fila menor y la fila mayor
                for col in range(len(matriz[0])):
                    matriz[fila][col] = numero_mayor_vector
                
            for col in range (col_menor+1,len(matriz[0])):#cambia los numeros de la fila menor despues de la columan menor
                matriz[fila_menor][col] = numero_mayor_vector
                
            for col in range (col_mayor,0,-1):#cambia los numeros de la fila menor antes de la columan mayor
                matriz[fila_menor][col] = numero_mayor_vector

            os.system("pause")
            os.system("cls")
            
            print("matriz nueva:")
            for fila in matriz:
                print(fila)
        
    os.system("pause")
    os.system("cls")
        
        
