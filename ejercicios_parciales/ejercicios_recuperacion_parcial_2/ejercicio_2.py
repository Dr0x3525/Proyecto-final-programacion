#se tiene un vector con datos numericos determinar si las veces que se repite el penultimo primo es un numero fibonacci
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene un vector con datos numericos determinar si las veces que se repite el penultimo primo es un numero fibonacci")
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

def encontrar_penultimo_primo(vector):
    contador_primos = 0
    for indice in range(len(vector)-1,0,-1):
        numero = vector[indice]
        if Comprobar_ser_primo(numero):
            contador_primos += 1 
            if contador_primos == 2:
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

def repeticiones_penultimo_primo(vector,penultimo_primo):
    contador_repeticiones_primo = 0
    for numero in vector:
        if numero == penultimo_primo:
            contador_repeticiones_primo += 1
    return contador_repeticiones_primo

def inicializar_ejercicio_2():
    mostrar_el_ejercicio()
    vector = pedir_datos()#[6, 2, 4, 5, 2, 7, 5, 9, 2] cd=9
    os.system("cls")
    print(f"vector: {vector}")
    
    penultimo_primo = encontrar_penultimo_primo(vector)#encontrar el penultimo primo
    
    if penultimo_primo == None:
      print("no se encontraron datos suficientes para el ejercicio")
    else:
        print(f"penultimo primo: {penultimo_primo}")
        
        repeticiones = repeticiones_penultimo_primo(vector,penultimo_primo)#ver cuantas veces se repite
        
        print(f"repeticiones del penultimo primo: {repeticiones}")

            
        if comprobar_ser_fibbonaci(repeticiones): #comprobar si es fibonacci
            print(f"el numero de repeticiones que es {repeticiones} es un numero fibbonaci")
        else:
            print(f"el numero de repeticiones que es {repeticiones} no es un numero fibbonaci")
    os.system("pause")
    os.system("cls")
