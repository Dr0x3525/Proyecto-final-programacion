#se tienen dos vectores con datos numericos, 
#hallar la suma de los datos que se encuentran entre el segundo impar y el penultimo par 
#y llenar esta suma en el rango del segundo vector comprendido entre el segundo y el cuarto primo
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tienen dos vectores con datos numericos,")
    print("hallar la suma de los datos que se encuentran entre el segundo impar y el penultimo par y llenar esta suma en el rango del segundo vector comprendido entre el segundo y el cuarto primo")
    os.system("pause")
    os.system("cls")

def Comprobar_ser_primo(numero):
    numero = int(numero)
    if numero <= 1:
        return False
    else:
        if numero == 2:
            return True
        else:
            for i in range(2,numero-1):
                if numero % i  == 0:
                    return False
            return True
        
        
def encontrar_segundo_impar(vector):
    contador_impares = 0
    for indice in range(len(vector)):
        if vector[indice] % 2 != 0:
            contador_impares += 1
            if contador_impares == 2:
                return vector[indice], indice
    return None, None

def encontrar_penultimo_par(vector):
    contador_pares = 0
    for indice in range(len(vector)-1,0,-1):
        if vector[indice] % 2 == 0:
            contador_pares += 1
            if contador_pares == 2:
                return vector[indice], indice
    return None,None

def ordenar_vector(a,b):
    if a < b:
        return a,b
    else:
        return b,a

def encontrar_segundo_y_cuarto_primo(vector):
    
    contador_primos = 0
    for indice in range(len(vector)):
        if Comprobar_ser_primo(vector[indice]):
            contador_primos += 1
            if contador_primos == 2:
                indice_primo_2 = indice
                primo_2 = vector[indice]
            if contador_primos == 4:
                indice_primo_4 = indice
                primo_4 = vector[indice]
                
    return indice_primo_2,primo_2,indice_primo_4,primo_4 
     

def pedir_datos():
    lista = []
    cantidad_de_datos = int(input("cuantos datos vas a ingresar: "))
    
    for numero in range(cantidad_de_datos):
        dijito = input(f"digita el valor {numero+1}: ")
        dijito = int(dijito)
        lista.append(dijito)
    return lista   


def inicializar_ejercicio_3():
    mostrar_el_ejercicio()
    print("vector 1")
    vector_1 = pedir_datos()#[3, 8, 5, 2, 7, 4, 6, 9, 10] cd= 9
    os.system("cls")
    print("vector 2")
    vector_2 = pedir_datos()#[1, 4, 6, 3, 8, 5, 7, 2] cd = 8
    os.system("cls")
    segundo_impar,indice_segundo_impar = encontrar_segundo_impar(vector_1)
    penultimo_par,indice_penultimo_par = encontrar_penultimo_par(vector_1)
    
    if segundo_impar == None:
      print("no se encontraron datos suficientes para realizar el ejercicio")
    else:    
        print(f"vector 1: {vector_1}")
        print(f"el segundo impar del vector 1 es: {segundo_impar}")
        print(f"el penultimo par del vector 1 es: {penultimo_par}")
        
    
        
        menor , mayor = ordenar_vector(indice_segundo_impar,indice_penultimo_par)
        
        sumatoria = 0
        for indice in range(menor+1,mayor):
            sumatoria = sumatoria + vector_1[indice]
        
        print(f"la sumatoria entre el segundo impar y el penultimo par del vector 1 es: {sumatoria}")    
        os.system("pause")
        os.system("cls")
        
        indice_primo_2,primo_2,indice_primo_4,primo_4  = encontrar_segundo_y_cuarto_primo(vector_2)

        print(f"el vector 2 original es: {vector_2}")
        print(f"el segundo primo del vector es: {primo_2}")
        print(f"el cuarto primo del vector es:{primo_4}")
            
        for indice in range(indice_primo_2+1,indice_primo_4):
            vector_2[indice] = sumatoria
            
            
        print(f"el vector 2 nuevo es: {vector_2}")
    
    os.system("pause")
    os.system("cls")
