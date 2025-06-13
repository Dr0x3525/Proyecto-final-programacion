#el dato a buscar es el segundo primo de un vector 2 que se encuentra despues de la posicion de dato correspondiente a la suma del primo 2 y fibonacci menor del vector 1
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("el dato a buscar es el segundo primo de un vector 2 que se encuentra despues de la posicion de dato correspondiente a la suma del primo 2 y fibonacci menor del vector 1")
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
        
def encontrar_primo_2(vector):
    contador_primo = 0
    for numero in vector:
        if Comprobar_ser_primo(numero):
            contador_primo += 1
            if contador_primo == 2:
                return numero
    return None

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

def encontrar_fib_menor(vector):
    fib_menor = None
    for numero in vector:
        if comprobar_ser_fibbonaci(numero):
            if fib_menor == None:
              fib_menor = numero
            else:
                if fib_menor > numero:
                    fib_menor = numero
    return fib_menor

def buscar_dato_vector_2(vector,suma):
    encontrar_primo_2 = False
    contador_primo = 0
    
    for numero in vector:
        if numero == suma:
            encontrar_primo_2 = True
        if encontrar_primo_2:
            if Comprobar_ser_primo(numero):
                contador_primo += 1
                if contador_primo == 2:
                    return numero
    return None


def inicializar_ejercicio_1():
    mostrar_el_ejercicio()
    print("vector 1")
    vector_1 = pedir_datos()# [4, 6, 7, 9, 10, 11,1] cd = 7
    os.system("cls")
    print("vector 2")
    vector_2 = pedir_datos()# [12,3, 5, 8, 10, 11, 13, 14, 17, 19, 20] cd = 11
    os.system("cls")

    primo_2 = encontrar_primo_2(vector_1)#encontrar primo 2
    fib_menor = encontrar_fib_menor(vector_1)#encontrar fibonaci menor
    

    
    if primo_2 == None or fib_menor == None:
        print("no hay suficientes datos para comprobar")
    else:
            print(f"vector 1: {vector_1}")
            print(f"segundo primo del vector 1: {primo_2}")
            print(f"fibonacci menor del vector 1: {fib_menor}")
            os.system("pause")
            os.system("cls")
            suma = primo_2 + fib_menor#realizar suma
            dato_encontrado = buscar_dato_vector_2(vector_2,suma)#encontrar dato a buscar
            if dato_encontrado == None:
                print("no se encontro la suma del numero")
            else:   
                print(f"vector 2: {vector_2}")
                print(f"suma de los datos pedidos del primer vector para encontrar el segundo vector: {suma}")
                print(f"dato buscado en el vector: {dato_encontrado}")
    os.system("pause")
    os.system("cls")

