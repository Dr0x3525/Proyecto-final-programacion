#se tiene una cantidad de numeros dada donde hay varios primos 
#determinar si el primo 2 y el primo 3 
#de acuerdo al orden de entrada son consecutivos

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene una cantidad de numeros dada donde hay varios primos")
    print("determinar si el primo 2 y el primo 3")
    print("de acuerdo al orden de entrada son consecutivos")
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
    cd = input("cuantos datos vas a escribir: ")
    cd = int(cd)
    return cd

def pedir_numero():
    numero =input("dime un numero: ")
    numero = int(numero)
    return numero

def organizar_numeros(a,b):
    if a > b:
        temp = a 
        a = b 
        b = temp
        
    return a, b

def determinar_si_son_consecutivos(a,b):
        for i in range(a+1,b):
            if determinar_ser_primo(i):
                return False
        return True

def mostrar_respuesta(respuesta,a,b):
    if respuesta:
        print(f"los numeros {a} y {b} son consecutivos")
    else:
        print(f"los numeros {a} y {b} no son consecutivos")

def inicializar_ejercicio_2():
    mostrar_el_ejercicio()
    hay_primos = None
    primo_2 = None
    primo_3 = None
    cantidad_de_datos = pedir_cantidad_de_datos()
    for i in range(cantidad_de_datos):
        numero = pedir_numero()
        if determinar_ser_primo(numero):
            if hay_primos == None:
                hay_primos = 1
            else:
                hay_primos += 1
                if hay_primos == 2:
                    primo_2 = numero
                if hay_primos == 3:
                    primo_3 = numero
                    break
                
    if primo_2 == None or primo_3 == None:
        print("no hay suficientes numeros primos")
    else:                
        numero_menor, numero_mayor =organizar_numeros(primo_2,primo_3)
        son_consecutivos = determinar_si_son_consecutivos(numero_menor,numero_mayor)
        mostrar_respuesta(son_consecutivos,numero_menor,numero_mayor)
        
    os.system("pause")
    os.system("cls")
    
