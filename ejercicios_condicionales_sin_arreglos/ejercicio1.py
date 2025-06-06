#se tiene una cantidad de numeros dada donde hay varios numeros primos, obtener los primos 2,3,4 
#(de acuerdo al orden de entrada)y mostrarlos en forma ascendente, sin utilizar condiciones compuestas 
import os

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
    
def inicializar_ejercicio_1_ejercicio_con_ciclos_sin_arreglos():
    hay_primos = 0
    cantidad_de_datos = pedir_cantidad_de_datos()
    for i in range(cantidad_de_datos):
        numero = pedir_numero()
        if determinar_ser_primo(numero):
            if hay_primos == 0:
                hay_primos = 2#este se convierte en 2 porque si hay otro primo seria el segundo
            else:
                if hay_primos == 2:
                    primo_2 = numero
                if hay_primos == 3:
                    primo_3 = numero
                if hay_primos == 4:
                    primo_4 = numero
                    break 
                hay_primos += 1
                
    organizar_numeros(primo_2,primo_3,primo_4)
    os.system("pause")

inicializar_ejercicio_1_ejercicio_con_ciclos_sin_arreglos()


