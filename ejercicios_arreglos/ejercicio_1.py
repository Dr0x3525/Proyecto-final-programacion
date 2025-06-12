#1.	Se tienen dos vectores ordenados el primero ascendentemente y el segundo descendentemente.
#Formar un tercer vector ordenado con la mezcla de los dos llenando 
# únicamente los números que son primos y sin repetidos.
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("Se tienen dos vectores ordenados el primero ascendentemente y el segundo descendentemente.")
    print("Formar un tercer vector ordenado con la mezcla de los dos llenando")
    print("únicamente los números que son primos y sin repetidos.")
    os.system("pause")
    os.system("cls")
    
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

def mostrar_respuesta(vector_1, vector_2,vector_3):
    print(f"vector 1: {vector_1}")
    print(f"vector 2: {vector_2}")
    print("el vector 3 esta compuesto por los numeros primos del vector 1 y de 2 sin repetirse")
    print(f"vector 3: {vector_3}")
 
def inicializar_ejercicio_1():
    mostrar_el_ejercicio()
    print("vector 1")
    Vector_1 = sorted(pedir_datos())    #[2, 4, 5, 8, 11, 12, 13] cd = 7
    os.system("cls")
    print("vector 2")
    Vector_2 = sorted(pedir_datos(),reverse=True)    #[17, 13, 11, 10, 7, 6, 5, 3] cd = 8 
    os.system("cls")
    vector_3 = []
    
    for i in Vector_1:
        if determinar_ser_primo(i):
            if i not in vector_3:
                vector_3.append(i)
            
    for i in Vector_2:
        if determinar_ser_primo(i):
            if i not in vector_3:
                vector_3.append(i)
     
    vector_3 = sorted(vector_3)
    mostrar_respuesta(Vector_1,Vector_2,vector_3)
    os.system("pause")
    os.system("cls")
            


