#4.	Se tiene dos vectores con datos numéricos}
# formar un tercer vector con los Fibonacci 
# de los dos vectores sin tener en cuenta los Fibonacci que son comunes.


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


def inicializar_ejercicio_4_ejercicio_arreglos():
    Vector_1 = [4, 7, 8, 12]
    Vector_2 = [2, 3, 5, 7, 13]
    Vector_3 = []
    
    for numero in Vector_1:
        if comprobar_ser_fibbonaci(numero):
            if numero not in Vector_2 and numero not in Vector_3:
                Vector_3.append(numero)
                
    for numero in Vector_2:
        if comprobar_ser_fibbonaci(numero):
            if numero not in Vector_1 and numero not in Vector_3:
                Vector_3.append(numero)
    
    print(Vector_3)
     
        
     

inicializar_ejercicio_4_ejercicio_arreglos()