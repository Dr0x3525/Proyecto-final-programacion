#Hallar la potencia de dos números con sumas

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Hallar la potencia de dos números con sumas")
    os.system("pause")
    os.system("cls")

def pedir_numero():
    numero =input("")
    numero = int(numero)
    return numero

def calcular_potencia_con_sumas(base, exponente):
    if exponente < 0:
        return "No se validan exponentes negativos con sumas."
    resultado = 1
    for i in range(exponente):  # Multiplicar 'base' 'exponente' veces
        suma_parcial = 0
        for _ in range(base):
            suma_parcial += resultado
        resultado = suma_parcial
        
    return resultado


def inicializar_ejercicio_4():
    mostrar_el_ejercicio()
    print("Ingresa la base:")
    base = pedir_numero()
    print("Ingresa el exponente:")
    exponente  = pedir_numero()
    
    resultado = calcular_potencia_con_sumas(base,exponente)
        
    print(f"la potencia del numero {base} elevado a la {exponente} es {resultado}")
    os.system("pause")
    os.system("cls")