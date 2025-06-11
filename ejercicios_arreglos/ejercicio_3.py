#3.	Se tienen dos vectores con datos numéricos 
# formar un vector con la unión de los Fibonacci sin repetidos.

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

def inicializar_ejercicio_3_ejercicio_arreglos():
    Vector_1 = [4, 6, 7, 13, 16, 21, 22, 34, 55, 89, 144]
    Vector_2 = [1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89, 100]
    Vector_3 = []
    
    for i in Vector_1:
        if comprobar_ser_fibbonaci(i) and i not in Vector_3:
            Vector_3.append(i)
            
    for i in Vector_2:
        if comprobar_ser_fibbonaci(i) and i not in Vector_3:
            Vector_3.append(i)
    
    Vector_3 = sorted(Vector_3)
    print(Vector_3)


inicializar_ejercicio_3_ejercicio_arreglos()