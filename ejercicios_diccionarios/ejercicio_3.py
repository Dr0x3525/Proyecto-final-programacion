#3.	Se tienen dos listas con datos numéricos 
# formar un diccionario donde la clave sea el número Fibonacci, 
# y el valor sea el factorial de este.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene una lista con datos numéricos, ")
    print("formar un diccionario donde la clave sea el número Fibonacci, y el valor sea el factorial de este.")
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

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = i * resultado
    return resultado

def mostrar_respuesta(lista, diccionario):
    print(f"lista: {lista}")
    print(f"diccionario: {diccionario}")
    
def inicializar_ejercicio_3():
    mostrar_el_ejercicio()
    lista = pedir_datos()#[0, 1, 4, 2, 3, 5] cd= 6
    diccionario = {}
    os.system("cls")
    for numero in lista:
        if comprobar_ser_fibbonaci(numero):
            diccionario[numero] = factorial(numero)
            
    mostrar_respuesta(lista, diccionario)
    os.system("pause")
    os.system("cls")
     
