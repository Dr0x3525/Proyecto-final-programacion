#2.	Se tienen dos vectores con datos numéricos 
#formar un vector con los primos comunes sin datos repetidos.

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



def inicializar_ejercicio_2_ejercicio_arreglos():

    Vector_1 = [7, 13, 5, 8, 13, 2]
    Vector_2 = [5, 2, 11, 7, 2, 19]
    vector_con_primos_comun_sin_repetir = []

    for numero in Vector_1:
        if determinar_ser_primo(numero):
            if numero in Vector_2 and numero not in vector_con_primos_comun_sin_repetir:
                vector_con_primos_comun_sin_repetir.append(numero)
    
    print(vector_con_primos_comun_sin_repetir)
 

inicializar_ejercicio_2_ejercicio_arreglos()

