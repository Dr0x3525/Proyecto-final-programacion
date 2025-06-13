#se tiene 2 vectores con datos numericos, sumar los valores correspondientes al segundo primo
# y penultimo fibonacci del primer vector y remplazar esta suma en aquellas posiciones donde haya un numero impar del segundo vector

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene 2 vectores con datos numericos, sumar los valores correspondientes al segundo primo")
    print("y penultimo fibonacci del primer vector y remplazar esta suma en aquellas posiciones donde haya un numero impar del segundo vector")
    os.system("pause")
    os.system("cls")

def pedir_datos():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista   

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

def inicializar_ejercicio_3():
    mostrar_el_ejercicio()
    print("vector 1")
    vector_1 = pedir_datos()#[4, 5, 7, 8, 13, 12, 10] 
    os.system("cls")
    print("vector 2")
    vector_2 = pedir_datos()#[3, 6, 8, 9, 10, 11] 
    vector_3 = []
    os.system("cls")