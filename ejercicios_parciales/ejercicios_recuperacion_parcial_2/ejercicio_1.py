#se tienen dos vectores con datos numericos, formar un tercer vector sin repetidos con los valores de los dos vectores que no sean primos ni fibbonaci
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tienen dos vectores con datos numericos, formar un tercer vector sin repetidos con los valores de los dos vectores que no sean primos ni fibbonaci")
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

def inicializar_ejercicio_1():
    mostrar_el_ejercicio()
    print("vector 1")
    vector_1 = pedir_datos()#[4, 6, 7, 8, 12, 13, 14] cd = 7
    os.system("cls")
    print("vector 2")
    vector_2 = pedir_datos()#[6, 8, 9, 10, 11, 14, 15] cd = 7
    vector_3 = []
    os.system("cls")

    
    for numero in vector_1:
        if numero not in vector_3 and not comprobar_ser_fibbonaci(numero) and not Comprobar_ser_primo(numero):
            vector_3.append(numero)
    
    for numero in vector_2:
        if numero not in vector_3 and not comprobar_ser_fibbonaci(numero) and not Comprobar_ser_primo(numero):
            vector_3.append(numero)
    print(f"vector 1: {vector_1}")
    print(f"vector 2: {vector_2}")
    print("el vector 3 es la combinacion del vector 1 y 2 sin datos repetidos y sin los numeros fibonacci y primo de ambos")
    print(f"vector 3: {vector_3}")
    os.system("pause")
    os.system("cls")
    
    
