#6.	Se tiene un vector con datos numéricos donde hay varios Fibonacci, 
# encontrar el segundo y tercer Fibonacci y sus posiciones, reemplazar las posiciones comprendidas
# en estos dos valores con el factorial del Fibonacci menor de los dos.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tiene un vector con datos numéricos donde hay varios Fibonacci")
    print("encontrar el segundo y tercer Fibonacci y sus posiciones")
    print("reemplazar las posiciones comprendidas en estos dos valores con el factorial del Fibonacci menor de los dos.")
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

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = i * resultado
    return resultado

def encontrar_fib_menor(a,b):
    if a < b:
        return a
    else:
        return b
    
def mostrar_respuesta(vector_1,segundo_fibbonaci,tercer_fibbonacci,factorial_fib_menor):
    print(f"el segundo fib es: {segundo_fibbonaci}")
    print(f"el tercer fib es: {tercer_fibbonacci}")
    print(f"el factorial del fib menor es: {factorial_fib_menor}")
    print(f"remplazando la posicion entre estos 2 fibbonaci el vector es: {vector_1}")

def pedir_datos():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista     

def inicializar_ejercicio_6():
    mostrar_el_ejercicio()
    vector_1 = pedir_datos() #[4, 6, 8, 7, 5, 10, 4, 4, 21, 34, 5, 89] cd=12
    os.system("cls")
    contador_fibbonaci = 0
    contador_indice = 0
    tercer_fibbonacci = None
    for numero in vector_1:
        if comprobar_ser_fibbonaci(numero):
            contador_fibbonaci += 1
            if contador_fibbonaci == 2:
                segundo_fibbonaci = numero
                indice_segundo_fibbonaci = contador_indice
            if contador_fibbonaci == 3:
                tercer_fibbonacci = numero
                indice_tercer_fibbonaci = contador_indice
                break
            
        contador_indice +=1
    
    if tercer_fibbonacci == None:
        print("el ejercicio no se puede realizar faltan numeros fibonacci")
    else:
        fib_menor = encontrar_fib_menor(segundo_fibbonaci,tercer_fibbonacci)
        factorial_fib_menor = factorial(fib_menor)
        print(f"el vector original es:{vector_1}")
        for numero in range(indice_segundo_fibbonaci+1,indice_tercer_fibbonaci):
            vector_1[numero] = factorial_fib_menor
        mostrar_respuesta(vector_1,segundo_fibbonaci,tercer_fibbonacci,factorial_fib_menor)
    os.system("pause")
    os.system("cls")   
    
     
    
    

