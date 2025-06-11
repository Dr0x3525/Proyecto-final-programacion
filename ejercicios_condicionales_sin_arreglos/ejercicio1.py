#se tiene una cantidad de numeros dada donde hay varios numeros primos, obtener los primos 2,3,4 
#(de acuerdo al orden de entrada)y mostrarlos en forma ascendente, sin utilizar condiciones compuestas 
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene una cantidad de numeros dada donde hay varios numeros primos, obtener los primos 2,3,4")
    print("(de acuerdo al orden de entrada)y mostrarlos en forma ascendente, sin utilizar condiciones compuestas")
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

def pedir_cantidad_de_datos():
    cantidad_de_datos = input("cuantos datos vas a escribir: ")
    cantidad_de_datos = int(cantidad_de_datos)
    return cantidad_de_datos

def pedir_numero():
    numero =input("dime un numero: ")
    numero = int(numero)
    return numero

def organizar_numeros(a, b, c):
    if a > b:
        temp = a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    if a > b:
        temp = a
        a = b
        b = temp
        
    mostar_numeros(a,b,c)

def mostar_numeros(a,b,c):
    os.system("cls")
    print("numeros ordenados en orden ascendente:")
    print(a)
    print(b)
    print(c)
    
def inicializar_ejercicio_1():
    mostrar_el_ejercicio()
    hay_primos = 0
    cantidad_de_datos = pedir_cantidad_de_datos()
    primo_2 = None
    primo_3 = None
    primo_4 = None
    
    #se inicia el ciclo para pedir numeros
    for i in range(cantidad_de_datos):
        numero = pedir_numero()
        if determinar_ser_primo(numero):
            hay_primos += 1
            if hay_primos == 2:
                primo_2 = numero
            elif hay_primos == 3:
                primo_3 = numero
            elif hay_primos == 4:
                primo_4 = numero
                break
    
    if primo_2 == None or primo_3 == None or primo_4 == None:
        print("no hay suficientes numeros primos para el ejercicio")
    else:
        organizar_numeros(primo_2,primo_3,primo_4)
    os.system("pause")




