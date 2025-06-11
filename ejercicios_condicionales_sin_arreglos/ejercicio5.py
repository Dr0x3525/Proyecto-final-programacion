#Hallar el factorial de un número con sumas  

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Hallar el factorial de un número con sumas")
    os.system("pause")
    os.system("cls")
    
    
def pedir_numero():
    numero =input("dime un numero: ")
    numero = int(numero)
    return numero

def inicializar_ejercicio_5():
    mostrar_el_ejercicio()
    numero = pedir_numero()
    
    if numero == 0:
        print("el factoria de 0 es 1")
        os.system("pause")
        os.system("cls")
        return
    
    if numero < 0:
        print("no se puede calcular el factorial de un negativo")
    else:
        factorial = numero
        contador = numero-1
        
        while contador > 0:
            sumatoria = 0
            for _ in range(contador):
                sumatoria += factorial
            factorial = sumatoria
            contador -= 1
        
        print(f"el factorial de {numero} es {factorial}")
    os.system("pause")
    os.system("cls")
    
