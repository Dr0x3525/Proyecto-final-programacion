#5.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci, 
# formar un tercer vector con los números primos
# que están entre el Fibonacci mayor y el Fibonacci menor.

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

def inicializar_ejercicio_5_ejercicio_arreglos():

    Vector_1 =  [4, 7, 13, 10, 5, 21, 8, 3, 34, 12]
    Vector_2 = []
    
    fib_menor = False
    fib_mayor = False
    for numero in Vector_1:
        if comprobar_ser_fibbonaci(numero):
            if fib_menor == False:
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
            
    print(Vector_2)
     
    
    
inicializar_ejercicio_5_ejercicio_arreglos()