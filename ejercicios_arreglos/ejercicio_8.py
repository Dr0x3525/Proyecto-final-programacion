#8.	Se tiene un vector con datos numéricos, eliminar todos los números que sean Fibonacci.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene un vector con datos numéricos, eliminar todos los números que sean Fibonacci.")
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
    mostrar_el_ejercicio()
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista     

def mostrar_respuesta(vector):
    print(f"vector actualizados: {vector}")

    
    
def inicializar_ejercicio_8():
    vector = pedir_datos() # [4, 7, 10, 13, 16, 21, 24, 29, 34, 55, 89, 144] cd= 12
    os.system("cls")
    print(f"vector original {vector}")
    indice = 0
    while indice < len(vector):
        if comprobar_ser_fibbonaci(vector[indice]):
            del vector[indice]
        else:
            indice += 1 
            
    mostrar_respuesta(vector)
    os.system("pause")
    os.system("cls")  
     
