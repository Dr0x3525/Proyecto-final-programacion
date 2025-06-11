#3.	Se tienen dos listas con datos numéricos 
# formar un diccionario donde la clave sea el número Fibonacci, 
# y el valor sea el factorial de este.

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

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado = i * resultado
    return resultado

def inicializar_ejercicio_3_ejercicio_diccionario():

    lista_1 = [0, 1, 4, 2, 3, 5] 
    diccionario = {}
    
    for numero in lista_1:
        if comprobar_ser_fibbonaci(numero):
            diccionario[numero] = factorial(numero)
            
    print(diccionario)
            
inicializar_ejercicio_3_ejercicio_diccionario()