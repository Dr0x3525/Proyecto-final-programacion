#3.	Se tienen dos vectores con datos numéricos 
# formar un vector con la unión de los Fibonacci sin repetidos.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tienen dos vectores con datos numéricos")
    print("formar un vector con la unión de los Fibonacci sin repetidos.")
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
    print("el vector 3 esta compuesto con la unión de los Fibonacci sin repetidos del vector 1 y 2")
    print(f"vector 3: {vector_3}")

def inicializar_ejercicio_3():
    mostrar_el_ejercicio()
    print("vector 1")
    Vector_1 = pedir_datos()#[4, 6, 7, 13, 16, 21, 22, 34, 55, 89, 144] cd = 11
    os.system("cls")
    print("vector 2")
    Vector_2 = pedir_datos()#[1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89, 100] cd = 12
    os.system("cls")
    
    Vector_3 = []
    
    for i in Vector_1:
        if comprobar_ser_fibbonaci(i) and i not in Vector_3:
            Vector_3.append(i)
            
    for i in Vector_2:
        if comprobar_ser_fibbonaci(i) and i not in Vector_3:
            Vector_3.append(i)
    
    Vector_3 = sorted(Vector_3)
    
    mostrar_respuesta(Vector_1, Vector_2,Vector_3)
    os.system("pause")
    os.system("cls")

