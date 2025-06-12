#2.	Se tiene una lista con datos numéricos, 
# formar un diccionario donde la clave sea el número Fibonacci 
# y el valor una tupla con los elementos que están al lado de él.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene una lista con datos numéricos, ")
    print("formar un diccionario donde la clave sea el número Fibonacci y el valor una tupla con los elementos que están al lado de él.")
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

def mostrar_respuesta(lista, diccionario):
    print(f"lista: {lista}")
    print(f"diccionario: {diccionario}")
    
def inicializar_ejercicio_2():
    mostrar_el_ejercicio()
    lista = pedir_datos()#[3, 8, 15, 16, 23, 13] cd = 6
    diccionario = {}
    os.system("cls")

    for indice in range(len(lista)):
            numero = lista[indice]
            if comprobar_ser_fibbonaci(numero):
                if indice-1 >= 0:
                  anterior = lista[indice-1]
                else:
                    anterior = "no hay numeros anteriores a este"
                
                if indice+1 < len(lista):
                  siguiente = lista[indice+1]
                else:
                    siguiente = "no hay numeros despues a este"
                           
                diccionario[numero] = (anterior, siguiente)
    
        
    mostrar_respuesta(lista, diccionario)
    
    os.system("pause")
    os.system("cls")
