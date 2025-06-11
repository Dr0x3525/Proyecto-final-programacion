#2.	Se tiene una lista con datos numéricos, 
# formar un diccionario donde la clave sea el número Fibonacci 
# y el valor una tupla con los elementos que están al lado de él.

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


def inicializar_ejercicio_2_ejercicio_diccionario():

    lista = [3, 8, 15, 16, 23, 13]
    diccionario = {}
    
    for indice in range(len(lista)):
            numero = lista[indice]
            if comprobar_ser_fibbonaci(numero):
                if indice-1 >= 0:
                  anterior = lista[indice-1]
                else:
                    anterior = "no hay numeros anteriores a este"
                
                if indice+1 < len(lista):
                  siguiente = lista[indice+1]
                else:
                    siguiente = "no hay numeros despues a este"
                           
                diccionario[numero] = (anterior, siguiente)
            
    print(diccionario)
    

inicializar_ejercicio_2_ejercicio_diccionario()