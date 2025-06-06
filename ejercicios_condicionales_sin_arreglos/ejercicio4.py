#Hallar la potencia de dos números con sumas

def pedir_numero():
    numero =input("dime un numero: ")
    numero = int(numero)
    return numero

def incializar_ejercicio_4_ejercicios_con_ciclos_sin_arreglos():
    numero = pedir_numero()
    sumatoria = 0
    for item in range(numero):
        sumatoria = numero + sumatoria
        
    print(f"la potencia del numero {numero} es {sumatoria}")

incializar_ejercicio_4_ejercicios_con_ciclos_sin_arreglos()