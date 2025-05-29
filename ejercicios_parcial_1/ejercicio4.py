#busca un dato en una cantidad de datos dada
#y hallar la multiplicacion con sumas del primer primo
#y el primer fibbonacci que se encuentra despues de este dato hallado
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

def recortar_lista(lista,buscar_dato):
    b1 = 0 
    lista_nueva = []
    for i in lista:
        if b1 == 1:
            lista_nueva.append(i)
        if i == buscar_dato:
            b1 = 1

    
    return lista_nueva        

def buscar_primer_fib(lista_recortada):
    for i in lista_recortada:
        if comprobar_ser_fibbonaci(i):
            return i
        
def buscar_primer_primo(lista_recortada):
    for i in lista_recortada:
        if Comprobar_ser_primo(i):
            return i

    
def multiplicacion_con_sumas(a, b):
    resultado = 0
    for i in range(b):
        resultado += a
    return resultado

def pedir_lista():
    lista = []
    cantidad_datos = input("cuantos datos va a ingresar: ")
    cantidad_datos = int(cantidad_datos)
    for i in range(cantidad_datos):
        numero = input("digite un numero: ")
        numero = int(numero)
        lista.append(numero)
        
    return lista
        
def pedir_numero_buscado():
    numero_buscado = input("digite el numero que va a buscar: ")
    numero_buscado = int(numero_buscado)
    return numero_buscado

def inicializar_ejercicio_4_parcial_1():
    os.system("cls")
    lista = pedir_lista()
    buscar_dato = pedir_numero_buscado()
    lista_recortada= recortar_lista(lista,buscar_dato)
    primer_fib = buscar_primer_fib(lista_recortada)
    primer_primo = buscar_primer_primo(lista_recortada)
    resultado = multiplicacion_con_sumas(primer_primo,primer_fib)
    os.system("cls")
    print(f"Datos: {lista}")
    print(f"numero buscado: {buscar_dato}")
    print(f"el resultado de la multiplicacion del primer fibbonaci despues del dato buscado {primer_fib} y el primer primo despues del dato buscado {primer_primo} es {resultado}")
    os.system("pause")

