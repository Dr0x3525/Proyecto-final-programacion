#se tiene un vector con datos numericos,
#ordenar en forma descendente el rango de un vector
#comprendido entre el primo menor y el fibbonacci mayor
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene un vector con datos numericos,")
    print("ordenar en forma descendente el rango de un vector comprendido entre el primo menor y el fibbonacci mayor")
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

def encontrar_primo_menor(vector):
    primo_menor = None
    indice_menor = None
    for indice in range(len(vector)):
        if Comprobar_ser_primo(vector[indice]):
            if primo_menor == None:
                primo_menor = vector[indice]
                indice_menor = indice
            else:
              if primo_menor > vector[indice]:
                  primo_menor = vector[indice]
                  indice_menor = indice
    return primo_menor, indice_menor

def encontrar_fibbonacci_mayor(vector):
    fib_mayor = None
    indice_mayor = None
    for indice in range(len(vector)):
        if comprobar_ser_fibbonaci(vector[indice]):
            if fib_mayor == None:
                fib_mayor = vector[indice]
                indice_mayor = indice
            else:
                if fib_mayor < vector[indice]:
                    fib_mayor = vector[indice]
                    indice_mayor = indice
    return fib_mayor, indice_mayor

def ordenar_primo_menor_y_fib_mayor(a,b):
    if a < b:
        return a, b
    else:
        return b,a
        

def ordenar_vector_descendentemente(vector,menor,mayor):
    subvector = []
    for indice in range(menor+1,mayor):
        subvector.append(vector[indice])
    subvector = sorted(subvector, reverse=True)
        
    subindice = 0
    
    for indice in range(menor+1,mayor):
        vector[indice] = subvector[subindice]
        subindice +=1
        
    return vector
    

def inicializar_ejercicio_2():
    mostrar_el_ejercicio()
    vector = pedir_datos()#[4, 8, 15, 7, 13, 2, 21, 5, 34, 1, 89, 3] cd = 12
    os.system("cls")
    primo_menor, indice_primo_menor = encontrar_primo_menor(vector)#encontrar primo menor
    fib_mayor, indice_fib_mayor = encontrar_fibbonacci_mayor(vector)#encontrar fibbonaci mayor
    
    if primo_menor == None or fib_mayor == None:
        print("no hay suficientes valores para realizar el ejercicio")
    else:
        menor, mayor = ordenar_primo_menor_y_fib_mayor(indice_primo_menor,indice_fib_mayor)#ordenar_primo_menor_y_fib_mayor
        print(f"vector original: {vector}")
        print(f"primo menor: {primo_menor}")
        print(f"fibonacci mayor: {fib_mayor}")
        vector = ordenar_vector_descendentemente(vector,menor,mayor)
        print(f"vector nuevo: {vector}")
    os.system("pause")
    os.system("cls")

    
