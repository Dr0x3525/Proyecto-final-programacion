#1.	Se tienen dos vectores ordenados el primero ascendentemente y el segundo descendentemente.
#Formar un tercer vector ordenado con la mezcla de los dos llenando 
# únicamente los números que son primos y sin repetidos.

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

def inicializar_ejercicio_1_ejercicio_arreglos():
    Vector_1 = [2, 4, 5, 8, 11, 12, 13] 
    Vector_2 = [17, 13, 11, 10, 7, 6, 5, 3] 
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
    print(vector_3)
            
inicializar_ejercicio_1_ejercicio_arreglos()


