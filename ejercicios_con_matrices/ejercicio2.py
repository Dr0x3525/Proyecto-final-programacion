#2.	Se tiene una matriz con datos numéricos, donde hay varios primos, 
# determinar si el segundo primo encontrado al recorrer la matriz por columnas 
# es consecutivo con el cuarto primo encontrado.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene una matriz con datos numéricos, donde hay varios primos,")
    print("determinar si el segundo primo encontrado al recorrer la matriz por columnas es consecutivo con el cuarto primo encontrado.")
    os.system("pause")
    os.system("cls")

def Comprobar_ser_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2,numero-1):
            if numero % i  == 0:
                return False
        return True

def comprobar_ser_consecutivos(a,b):
    
    if a ==2 and b == 3:
        return True
    else:
        for i in range(a+1,b-1):
            if Comprobar_ser_primo(i):
                return False
        return True
         
def ordenar_primos(a,b):
    if a > b:
        temp = a
        a = b
        b = temp

    return a,b        

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

def mostrar_resultado(matriz,a,b):
    print("matriz:")
    for fila in matriz:
        print(fila)
    
    if comprobar_ser_consecutivos(a,b):
        print(f"los numeros {a} y {b} son consecutivos")
    else:
        print(f"los numeros {a} y {b} no son consecutivos")

            
def inicializa_ejercicio_2():
    mostrar_el_ejercicio()
    matriz =  pedir_datos()#[[1, 2, 4],[3, 5, 6],[7, 9, 8]]
    
    os.system("cls")


    contador_primos = 0
    num_columnas = len(matriz[0])  
    num_filas = len(matriz)        

    for col in range(num_columnas):
        for fila in range(num_filas):
            if Comprobar_ser_primo(matriz[fila][col]):
                contador_primos += 1
                if contador_primos == 2:
                    primo_2 = matriz[fila][col]
                elif contador_primos == 4:
                    primo_4 = matriz[fila][col]
                    break
            
    a,b = ordenar_primos(primo_2,primo_4)
                
    mostrar_resultado(matriz,a,b)   
    os.system("pause")
    os.system("cls")   

    
    