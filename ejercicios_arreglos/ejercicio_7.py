#7.	Se tiene dos vectores con datos numéricos, encontrar la suma de los impares del vector e insertar esta suma en el segundo vector así:

#Si el dato del segundo vector es primo, insertarlo a la derecha.
#Si el dato del primer vector es Fibonacci, insertarlo a la izquierda. 

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene dos vectores con datos numéricos, encontrar la suma de los impares del vector e insertar esta suma en el segundo vector así: ")
    print("Si el dato del segundo vector es primo, insertarlo a la derecha.")
    print("Si el dato del primer vector es Fibonacci, insertarlo a la izquierda. ")
    os.system("pause")
    os.system("cls")
    
def suma_primer_vector(vector_1):
    resultado = 0
    for numero in vector_1:
        if numero % 2 != 0:
            resultado = numero + resultado
    return resultado

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


def pedir_datos():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista     

def mostrar_respuesta(vector_1, vector_2):
    print("vectores actualizados: ")
    print(f"vector 1: {vector_1}")
    print(f"vector 2: {vector_2}")
    
    
def inicializar_ejercicio_7():
    mostrar_el_ejercicio()
    print("vector 1")
    vector_1 = pedir_datos()#[4, 7, 10, 6, 5] cd = 5
    os.system("cls")
    print("vector 2")
    vector_2 = pedir_datos()#[8, 3, 12, 9] cd = 4
    os.system("cls")

    suma_impares = suma_primer_vector(vector_1)    
    print("vectores originales:")
    print(f"vector 1: {vector_1}")
    print(f"vector 2: {vector_2}")
    
    i = 0
    while i < len(vector_2):
        num = vector_2[i]
        if comprobar_ser_fibbonaci(num):
            vector_2.insert(i, suma_impares)  # Insertar a la izquierda
            i += 1  
        if determinar_ser_primo(num):
            vector_2.insert(i + 1, suma_impares)  
            i += 1  
        i += 1  
        
    mostrar_respuesta(vector_1, vector_2,)
    os.system("pause")
    os.system("cls")   