#Hallar el factorial de un número con sumas  

def pedir_numero():
    numero =input("dime un numero: ")
    numero = int(numero)
    return numero

def incializar_ejercicio_5_ejercicios_con_ciclos_sin_arreglos():
    numero = pedir_numero()
    contador = numero 
    factorial = numero
    for item in range(numero,1,-1):
        sumatoria = 0
        for item in range(contador,1,-1):
            sumatoria = sumatoria + factorial
        factorial = sumatoria
        contador -= 1 
     
    print(factorial)
    
incializar_ejercicio_5_ejercicios_con_ciclos_sin_arreglos()