#2.	Se tienen dos vectores con datos numéricos 
#formar un vector con los primos comunes sin datos repetidos.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tienen dos vectores con datos numéricos")
    print("formar un vector con los primos comunes sin datos repetidos.")
    os.system("pause")
    os.system("cls")

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

def mostrar_respuesta(vector_1, vector_2,vector_3):
    print(f"vector 1: {vector_1}")
    print(f"vector 2: {vector_2}")
    print("el vector 3 esta compuesto por los numeros primos comunes sin datos repetidos")
    print(f"vector 3: {vector_3}")
    
def inicializar_ejercicio_2():
    mostrar_el_ejercicio()
    print("vector 1")
    Vector_1 = pedir_datos() #[7, 13, 5, 8, 13, 2] #cd = 6
    os.system("cls")
    print("vector 2")
    Vector_2 = pedir_datos() #[5, 2, 11, 7, 2, 19] #cd = 6
    os.system("cls")

    vector_3 = []

    for numero in Vector_1:
        if determinar_ser_primo(numero):
            if numero in Vector_2 and numero not in vector_3:
                vector_3.append(numero)
    
    
    mostrar_respuesta(Vector_1, Vector_2,vector_3)
    os.system("pause")
    os.system("cls")


