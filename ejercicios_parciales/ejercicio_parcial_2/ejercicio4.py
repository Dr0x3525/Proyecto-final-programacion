# se tiene un vector con datos numericos, determinar cuantas veces aparecen el segundo impar del vector y el fibonacci menor

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene un vector con datos numericos, determinar cuantas veces aparecen el segundo impar del vector y el fibonacci menor")
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

def encontrar_segundo_impar(vector):
    contado_impares = 0
    for indice in range(len(vector)):
        if vector[indice] % 2 != 0:
            contado_impares += 1
            if contado_impares == 2:
                return vector[indice]
    return None

def encontrar_fib_menor(vector):
    fib_menor = None
    for indice in range(len(vector)):
        if comprobar_ser_fibbonaci(vector[indice]):
            if fib_menor == None:
                fib_menor = vector[indice]
            else:
                if fib_menor > vector[indice]:
                    fib_menor = vector[indice]
    return fib_menor

def pedir_datos():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista   


def inicializar_ejercicio_3():
    mostrar_el_ejercicio()
    vector = pedir_datos() #[4, 7, 2, 8, 3, 5, 7, 1, 8, 13, 7, 3] cd =12

    os.system("cls")
    
    segundo_impar = encontrar_segundo_impar(vector)
    fibonnaci_menor = encontrar_fib_menor(vector)
    
    if segundo_impar == None or fibonnaci_menor == None:
        print("no hay suficientes datos para realizar el ejercicio")
    else:
        contador_segundo_impar = 0
        contador_fib_menor = 0
        
        for numero in vector:
            if numero == segundo_impar:
                contador_segundo_impar += 1
            if numero == fibonnaci_menor:
                contador_fib_menor += 1
                
        print(f"el segundo impar el cual es {segundo_impar} se repite {contador_segundo_impar} veces")
        print(f"el fibonacci menor el cual es {fibonnaci_menor} se repite {contador_fib_menor} veces")
    os.system("pause")
    os.system("cls")
            
