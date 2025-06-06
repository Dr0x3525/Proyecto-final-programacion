#se tiene una cantidad de numeros dada donde hay varios primos 
#determinar si el primo 2 y el primo 3 
#de acuerdo al orden de entrada son consecutivos

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

def pedir_cantidad_de_datos():
    cd = input("cuantos datos vas a escribir: ")
    cd = int(cd)
    return cd

def pedir_numero():
    numero =input("dime un numero: ")
    numero = int(numero)
    return numero

def organizar_numeros(a,b):
    if a > b:
        temp = a 
        a = b 
        b = temp
        
    return a, b

def determinar_si_son_consecutivos(a,b):
        for i in range(a+1,b-1):
            if determinar_ser_primo(i):
                return False
        return True

def mostrar_respuesta(respuesta,a,b):
    if respuesta:
        print(f"los numeros {a} y {b} son consecutivos")
    else:
        print(f"los numeros {a} y {b} no son consecutivos")

def inicializar_ejercicio_2_ejercicio_con_ciclos_sin_arreglos():
    hay_primos = False
    cantidad_de_datos = pedir_cantidad_de_datos()
    for i in range(cantidad_de_datos):
        numero = pedir_numero()
        if determinar_ser_primo(numero):
            if hay_primos == 0:
                hay_primos = 2#este se convierte en 2 porque si hay otro primo seria el segundo
            else:
                if hay_primos == 2:
                    primo_2 = numero
                if hay_primos == 3:
                    primo_3 = numero
                hay_primos += 1
                
    numero_menor, numero_mayor =organizar_numeros(primo_2,primo_3)

    son_consecutivos = determinar_si_son_consecutivos(numero_menor,numero_mayor)
    mostrar_respuesta(son_consecutivos,numero_menor,numero_mayor)
    
inicializar_ejercicio_2_ejercicio_con_ciclos_sin_arreglos()