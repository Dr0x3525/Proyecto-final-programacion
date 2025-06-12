#hallar el promedio de los numeros pares que se encuentra en el penultimo primo y el segundo fibonacci de un vector con datos numericos

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("hallar el promedio de los numeros pares que se encuentra en el penultimo primo y el segundo fibonacci de un vector con datos numericos")
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

def encontrar_penultimo_primo(vector):
    penultimo_primo = None
    contador_primos = 0
    for indice in range (len(vector)-1,0,-1):
        if determinar_ser_primo(vector[indice]):
            contador_primos += 1
            if contador_primos == 2:
                penultimo_primo = vector[indice]
                return indice,penultimo_primo 
    return None,None

def encontrar_segundo_fib(vector):
    contador_fib = 0
    for indice in range(0,len(vector)):
        if comprobar_ser_fibbonaci(vector[indice]):
            contador_fib += 1
            if contador_fib == 2:
                segundo_fib = vector[indice]
                return indice, segundo_fib
        indice +=1
    return None,None

def ordenar_valores(a,b):
    if a < b:
        return a,b
    else:
        return b,a

def mostrar_resultado(vector,segundo_fib,penultimo_primo,resultado):
    print(f"del vector:{vector}")
    print(f"el segundo fib es: {segundo_fib}")
    print(f"el penultimo primo es: {penultimo_primo}")
    print(f"el promedio de los numeros pares comprendidos entre estos dos es: {resultado}")
    
    
def inicializar_ejercicio_2():
    mostrar_el_ejercicio()
    vector =  pedir_datos()#[3, 4, 5, 7, 8, 11, 12, 13, 15, 16, 17, 18, 19, 20] cd=14
    os.system("cls")
    indice_penultimo_primo, penultimo_primo = encontrar_penultimo_primo(vector)
    indice_segundo_fib, segundo_fib = encontrar_segundo_fib(vector)
    
    if penultimo_primo == None or segundo_fib == None:
        print("no se encontraron suficientes datos para continuar el ejercicio")
    else:
        indice_menor, indice_mayor = ordenar_valores(indice_segundo_fib,indice_penultimo_primo)
        promedio = 0
        contador = 0
        for indice in range(indice_menor+1,indice_mayor):
            if vector[indice] % 2 == 0:
                promedio = promedio + vector[indice]
                contador +=1
        
        if contador == 0:
            print("no se encontraron numeros pares")
        else:
            resultado = promedio / contador
            mostrar_resultado(vector,segundo_fib,penultimo_primo,resultado)
    os.system("pause")
    os.system("cls")   
        
