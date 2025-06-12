#3 buscar un dato

#se tienen dos secuencias de datos con cantidadesdadas de numerosque van a entrar una a una
#el numero buscado esta determinado por la suma del fibonnaci menor y el segundo primo de la primera serie de numeros
#esta suma se encuentra en la segunda serie de numeros, el dato buscado esta dos posiciones despues de la posicion del dato encontrado de
#acuerdo al orden de entrada. no realizar validaciones

import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("buscar un dato")
    print("se tienen dos secuencias de datos con cantidadesdadas de numerosque van a entrar una a una el numero buscado esta determinado por la suma del fibonnaci menor y el segundo primo de la primera serie de numeros esta suma se encuentra en la segunda serie de numeros,")
    print("el dato buscado esta dos posiciones despues de la posicion del dato encontrado de acuerdo al orden de entrada. no realizar validaciones")    
    os.system("pause")
    os.system("cls")
    
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

        
def Pedir_1_Secuencia():
    
    return int(input("cuantos datos vas a ingresar en la primer secuencia: "))

def Pedir_2_Secuencia():
        return int(input("cuantos datos vas a ingresar en la segunda secuencia: "))


def llenar_secuencia(cantidad):
    secuencia = []
    for i in range(cantidad):
        dato = input("ingrese un dato en la secuencia: ")
        secuencia.append(dato)
    return secuencia

     


def encontrar_fib_menor(secuencia_1):
    lista_fibbonaci = []
    for i in secuencia_1:
        if comprobar_ser_fibbonaci(i):
            lista_fibbonaci.append(i)
            
    lista_fibbonaci.sort()
    return int(lista_fibbonaci[0])

def encontrar_segundo_primo(secuencia_1):
    lista_primos = []
    for i in secuencia_1:
        if Comprobar_ser_primo(i):
            lista_primos.append(i)
            
    lista_primos.sort()
    return int(lista_primos[1])

def encontrar_el_dato_buscado(numero,secuencia_2):
    return secuencia_2.index(str(numero))
     

def inicializar_ejercicio_3_parcial_1():
    mostrar_el_ejercicio()
    os.system("cls")
    secuencia_1 =[]
    secuencia_2 =[]
    
    cantida_de_datos_1_secuencia = Pedir_1_Secuencia()
    cantida_de_datos_2_secuencia = Pedir_2_Secuencia()
    
    print("secuencia 1")
    secuencia_1 = llenar_secuencia(cantida_de_datos_1_secuencia)
    print("secuencia 2")
    secuencia_2 = llenar_secuencia(cantida_de_datos_2_secuencia)
    
    
    #aqui encontramos fibmenor 

    os.system("cls")
    
    print(f"primera secuencia: {secuencia_1}")
    print(f"primera secuencia: {secuencia_2}")

    fib_menor = encontrar_fib_menor(secuencia_1)
    print(f"fibonnaci menor: {fib_menor}")
    #aqui encontramos el primo menor

    segundo_primo = encontrar_segundo_primo(secuencia_1)
    print(f"segundo_primo: {segundo_primo}")

    resultado = fib_menor + segundo_primo
    
    posicion = encontrar_el_dato_buscado(resultado,secuencia_2)
    #encontrar el dato buscado
    dato_buscado = secuencia_2[posicion+2]
    print(f"el dato buscado es: {dato_buscado}")
    os.system("pause")
