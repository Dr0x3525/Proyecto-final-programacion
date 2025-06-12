#se tienen dos vectores con datos numericos, 
#sumar los primos del primer vector e insertar esta suma 
#a la derecha del segundo fibonnaci del segundo vector
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tienen dos vectores con datos numericos")
    print("sumar los primos del primer vector e insertar esta suma a la derecha del segundo fibonnaci del segundo vector")
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

def sumar_primos_primer_vector(vector):
    suma = 0
    for i in vector:
        if Comprobar_ser_primo(i):
            suma += i
    return suma

def encontrar_el_segundo_fib(vector):
    indice = 0  
    contador_fibonacci = 0
    for numero in vector:
        if comprobar_ser_fibbonaci(numero):
            if contador_fibonacci == 0:
                contador_fibonacci = 1
            else:
                return indice+1
        indice += 1  
    return None

def insertar_suma_en_vector_2(vector,dato_a_insertar,indice_2_primo):
    vector.insert(indice_2_primo,dato_a_insertar)
    print(f"vector final: {vector}")
    return vector
    
            
def incializar_ejercicio_1():
    mostrar_el_ejercicio()
    print("vector 1")
    vector_1 = pedir_datos()# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  cd = 10
    os.system("cls")
    print("vector 2")
    vector_2 = pedir_datos()# [1, 1, 2, 3, 4, 5, 8, 13, 21]     cd = 9
    os.system("cls")
    print(f"vector 1: {vector_1}")
    print(f"vector 2: {vector_2}")
    suma_primos_primer_vector = sumar_primos_primer_vector(vector_1)
    print(f"suma de los primos del primer vector {suma_primos_primer_vector}")
    segundo_fib = encontrar_el_segundo_fib(vector_2)
    
    if segundo_fib == None:
      print("no hay suficientes numeros fibonacci")
    else:
        print(f"segundo fibonacci del vector 2: {segundo_fib}")
        insertar_suma_en_vector_2(vector_2,suma_primos_primer_vector,segundo_fib)
    os.system("pause")
    os.system("cls")

