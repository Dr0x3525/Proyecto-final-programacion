#se tienen dos vectores con datos numericos, 
#sumar los primos del primer vector e insertar esta suma 
#a la derecha del segundo fibonnaci del segundo vector
import os

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

def insertar_suma_en_vector_2(vector,dato_a_insertar,indice_2_primo):
    vector.insert(indice_2_primo,dato_a_insertar)
    print(vector)
    return vector
    
            
def incializar_ejercicio_1_parcial_2():
    vector1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Primos: 2, 3, 5, 7, 11 (suma = 28)
    vector2 = [1, 1, 2, 3, 4, 5, 8, 13, 21]     # Fibonacci: todos excepto el 4
    suma_primos_primer_vector = sumar_primos_primer_vector(vector1)
    print(suma_primos_primer_vector)
    segundo_fib = encontrar_el_segundo_fib(vector2)
    print(segundo_fib)
    insertar_suma_en_vector_2(vector2,suma_primos_primer_vector,segundo_fib)
    os.system("pause")
    
incializar_ejercicio_1_parcial_2()