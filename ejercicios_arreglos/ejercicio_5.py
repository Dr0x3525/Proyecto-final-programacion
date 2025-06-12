#5.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci, 
# formar un tercer vector con los números primos
# que están entre el Fibonacci mayor y el Fibonacci menor.

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tienen un vector con datos numéricos donde hay varios números Fibonacci")
    print("formar un segundo vector con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.")
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

def pedir_datos():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista     

def mostrar_respuesta(vector_1, vector_2,fib_mayor,fib_menor):
    print(f"vector 1: {vector_1}")
    print("el vector 2 esta compuesto con con los Fibonacci del vector 1 con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.")
    print(f"fibonacci mayor : {fib_mayor}")
    print(f"fibonacci menor : {fib_menor}")
    print(f"vector 2: {vector_2}")
    
    
def inicializar_ejercicio_5():
    mostrar_el_ejercicio()
    print("vector 1")
    Vector_1 = pedir_datos() # [4, 7, 13, 10, 5, 21, 8, 3, 34, 12] cd = 10
    os.system("cls")
    Vector_2 = []
    
    fib_menor = None
    fib_mayor = None
    for numero in Vector_1:
        if comprobar_ser_fibbonaci(numero):
            if fib_menor == None:
                fib_menor = numero
                fib_mayor = numero
            else:
                if fib_menor > numero:
                    fib_menor = numero
                if fib_mayor < numero:
                    fib_mayor = numero
    
    for numero in range(fib_menor+1,fib_mayor-1):
        if determinar_ser_primo(numero):
            Vector_2.append(numero)
            
    mostrar_respuesta(Vector_1,Vector_2,fib_mayor,fib_menor)
    os.system("pause")
    os.system("cls")   
    
    
