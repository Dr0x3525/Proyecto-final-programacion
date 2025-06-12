#4.	Se tiene dos vectores con datos numéricos
# formar un tercer vector con los Fibonacci 
# de los dos vectores sin tener en cuenta los Fibonacci que son comunes.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene dos vectores con datos numéricos")
    print("formar un tercer vector con los Fibonacci de los dos vectores sin tener en cuenta los Fibonacci que son comunes.")
    os.system("pause")
    os.system("cls")
    
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

def pedir_datos():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista     

def mostrar_respuesta(vector_1, vector_2,vector_3):
    print(f"vector 1: {vector_1}")
    print(f"vector 2: {vector_2}")
    print("el vector 3 esta compuesto con con los Fibonacci de los dos vectores sin tener en cuenta los Fibonacci que son comunes emtre el vector 1 y 2")
    print(f"vector 3: {vector_3}")

def inicializar_ejercicio_4():
    mostrar_el_ejercicio()
    print("vector 1")
    Vector_1 = pedir_datos()#[4, 7, 8, 12] cd = 4
    os.system("cls")
    print("vector 2")
    Vector_2 = pedir_datos()#[2, 3, 5, 7, 13] cd = 5
    os.system("cls")

    Vector_3 = []
    
    for numero in Vector_1:
        if comprobar_ser_fibbonaci(numero):
            if numero not in Vector_2 and numero not in Vector_3:
                Vector_3.append(numero)
                
    for numero in Vector_2:
        if comprobar_ser_fibbonaci(numero):
            if numero not in Vector_1 and numero not in Vector_3:
                Vector_3.append(numero)
    
    Vector_3 = sorted(Vector_3)
    
    mostrar_respuesta(Vector_1, Vector_2,Vector_3)
    os.system("pause")
    os.system("cls")     
        
     

