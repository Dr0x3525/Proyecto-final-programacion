#se tiene 2 vectores con datos numericos, sumar los valores correspondientes al segundo primo
# y penultimo fibonacci del primer vector y remplazar esta suma en aquellas posiciones donde haya un numero impar del segundo vector

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene 2 vectores con datos numericos, sumar los valores correspondientes al segundo primo")
    print("y penultimo fibonacci del primer vector y remplazar esta suma en aquellas posiciones donde haya un numero impar del segundo vector")
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

def encontrar_primo_2(vector):
    contador_primos = 0
    for numero in vector:
        if Comprobar_ser_primo(numero):
            contador_primos += 1
            if contador_primos == 2:
                return numero
    return None

def encontrar_penultimo_fib(vector):
    contador_fib = 0
    for numero in reversed(vector):
        if comprobar_ser_fibbonaci(numero):
            contador_fib += 1
            if contador_fib == 2:
                return numero
    return None

def remplazar_valores_vector_2(vector,suma):
    for i in range(len(vector)):
        if vector[i] % 2 != 0:
            vector[i] = suma
    return vector

def inicializar_ejercicio_3():
    mostrar_el_ejercicio()
    print("vector 1")
    vector_1 = pedir_datos()#[4, 5, 7, 8, 13, 12, 10] cd= 7
    os.system("cls")
    print("vector 2")
    vector_2 = pedir_datos()#[3, 6, 8, 9, 10, 11] cd= 6
    os.system("cls")
    segundo_primo = encontrar_primo_2(vector_1)#encontrar segundo primo
    penultimo_fib = encontrar_penultimo_fib(vector_1)#encontrar penultimo fibonaci
    if segundo_primo == None or penultimo_fib == None:
      print("insuficientes datos")
    else:
        suma = segundo_primo + penultimo_fib#sumar los datos
        print(f"vector 1: {vector_1}")
        print(f"segundo primo del vector 1: {segundo_primo}")
        print(f"penultimo fib del vector 1: {penultimo_fib}")
        print(f"suma anteriores digitos: {suma}")
        os.system("pause")
        os.system("cls")
        
        print(f"vector 2 original: {vector_2}")
        vector_2 = remplazar_valores_vector_2(vector_2,suma)#remplazar  los numeros impares del vector 2 con la suma
        os.system("pause")
        os.system("cls")
        print(f"vector 2 nuevo: {vector_2}")
    os.system("pause")
    os.system("cls")

