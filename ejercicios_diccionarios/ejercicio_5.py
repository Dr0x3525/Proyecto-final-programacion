#5.	En el diccionario anterior determinar cual es el par mayor y la clave donde se encuentra.

from ejercicios_diccionarios.ejercicio_4 import inicializar_ejercicio_4

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("En el diccionario anterior determinar cual es el par mayor y la clave donde se encuentra (ejercicio 4)")
    os.system("pause")
    os.system("cls")

def inicializar_ejercicio_5():
    mostrar_el_ejercicio()
    diccionario = inicializar_ejercicio_4()
    mayor_par = None
    clave_mayor_par = None
    
    for clave, lista_pares in diccionario.items():
        for numero in lista_pares:
            if mayor_par is None or numero > mayor_par:
                mayor_par = numero
                clave_mayor_par = clave
    
    if mayor_par is not None:
        print(f"El mayor número par es {mayor_par} y se encuentra en la fila {clave_mayor_par}.")
    else:
        print("No hay números pares en el diccionario.")
    os.system("pause")
    os.system("cls")


