#se tiene un vector con datos numericos ordenar en forma ascendente el rango comprendido entre el penultimo fibonacci y el segundo primo. incluir las posiciones de estos valores

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene un vector con datos numericos determinar si las veces que se repite el penultimo primo es un numero fibonacci")
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

def encontrar_penultimo_fib(vector):
    contador_fib = 0
    for indice in range(len(vector)-1,0,-1):
        numero = vector[indice]
        if comprobar_ser_fibbonaci(numero):
            contador_fib += 1
            if contador_fib == 2:
                return indice
    return None

def encontrar_primo_2(vector):
    contador_primos = 0
    for indice in range(len(vector)):
        numero = vector[indice]
        if Comprobar_ser_primo(numero):
            contador_primos += 1
            if contador_primos == 2:
                return indice
    return None

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

def ordenar_valores(a,b):
    if a < b:
        return a , b
    else:
        return b , a 

def ordenar_vector_rangos(vector,menor,mayor):
    sub_vector = []
    for indice in range(menor,mayor+1):
        sub_vector.append(vector[indice])
    sub_vector = sorted(sub_vector)
    
    indice_sub_vector = 0
    
    for indice in range(menor,mayor+1):
        vector[indice] = sub_vector[indice_sub_vector]
        indice_sub_vector += 1
    return vector    
    
    
    
    
def inicializar_ejercicio_4():
    mostrar_el_ejercicio()
    vector = pedir_datos()#[4, 8, 15, 16, 23, 42, 5, 7, 11, 13, 2, 3] cd = 12
    os.system("cls")
    indice_penultimo_fib = encontrar_penultimo_fib(vector)#encontrar indice penultimo fibonacci
    indice_primo_2 = encontrar_primo_2(vector)#encontrar indice segundo primo 
    
    if indice_penultimo_fib == None or indice_primo_2 == None:
      print("datos insuficientes")
    else:
        menor, mayor = ordenar_valores(indice_penultimo_fib,indice_primo_2)#ordenar valores
        
        print(f"vector original: {vector}")
        print(f"penultimo fibonacci: {vector[indice_penultimo_fib] }")
        print(f"segundo primo: {vector[indice_primo_2] }")
        
        os.system("pause")
        os.system("cls")
        vector = ordenar_vector_rangos(vector,menor,mayor)#ordenar en forma ascendente el vector entre rangos
        print(f"vector ordenado: {vector}")
    os.system("pause")
    os.system("cls")

