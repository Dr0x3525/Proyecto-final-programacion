#se tiene un vector con datos numericos,
#ordenar en forma descendente el rango de un vector
#comprendido entre el primo menor y el fibbonacci mayor
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

def encontrar_primo_menor(vector):
    se_encontro_primos = False
    indice_primo_menor = 0
    for i in vector:
        if Comprobar_ser_primo(i):
            if se_encontro_primos == False:
                primo_menor = i
                se_encontro_primos = True
            else:
                if primo_menor > i:
                    primo_menor = i
        indice_primo_menor += 1 
    return primo_menor, indice_primo_menor

def encontrar_fibbonacci_mayor(vector):
    se_encontro_fib = False
    indice_fib_mayor = 0
    for i in vector:
        if comprobar_ser_fibbonaci(i):
            if se_encontro_fib == False:
                fib_mayor = i
                se_encontro_fib = True
            else:
                if fib_mayor < i:
                    fib_mayor = i
        indice_fib_mayor += 1
    return fib_mayor, indice_fib_mayor

def ordenar_primo_menor_y_fib_mayor(a,b):
    if a > b:
        mayor = a
        menor = b
    else:
        menor = a
        mayor = b
        
    return menor,mayor

def ordenar_vector_descendentemente(vector,menor,mayor):
    for i in range(len(vector)):
        if i == menor:
          print(vector[i])

def inicializar_ejercicio_2_parcial_2():
    vector = [4, 8, 15, 7, 13, 2, 21, 5, 34, 1, 89, 3]
    
    primo_menor, indice_primo_menor = encontrar_primo_menor(vector)#encontrar primo menor
    print(primo_menor,indice_primo_menor)
    fib_mayor, indice_fib_mayor = encontrar_fibbonacci_mayor(vector)#encontrar fibbonaci mayor
    print(fib_mayor,indice_fib_mayor)
    menor, mayor = ordenar_primo_menor_y_fib_mayor(indice_primo_menor,indice_fib_mayor)#ordenar_primo_menor_y_fib_mayor
    ordenar_vector_descendentemente(vector,menor,mayor)
    os.system("pause")
    
    
inicializar_ejercicio_2_parcial_2()