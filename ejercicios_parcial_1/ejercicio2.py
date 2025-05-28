# se tiene una cantidad dada de ternas(3 valores numericos por terna) correspondiente
#a los lados de un triangulo, determinar cuantos triangulos equilateros, escalenos e isoceles se
#encuentran en estos y el triangulo equilatero con mayor perimetro.
import os

def pedir_ternas(lado,triangulo):
    while True: # Bucle infinito hasta que se ingrese opción válida
        os.system("cls")
        numero =  input(f"digita el {lado} del triangulo {triangulo+1} por favor: ")            
        if  numero.isdigit():
            numero = int(numero)
            if numero > 0:
                return numero
            else:
                print("Error: El código debe ser mayor  a 0")   
                os.system("pause")
        else:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
            os.system("pause")

def triangulo_isosceles(lado_a,lado_b,lado_c):
    if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return True # con que 2 lados sean iguales lo convierte en un escaleno
    return False

def triangulo_equilatero(lado_a,lado_b,lado_c):

    if lado_a == lado_b == lado_c:
        return True#si todoos los lados son iguales entonces es un triangulo escaleno
    return False

def mostrar_factura(contador_triangulos_equilateros,contador_triangulos_escalenos,contador_triangulos_isosceles,mayor_perimetro):
    print(f"hay {contador_triangulos_equilateros} triángulos equilateros")
    print(f"hay {contador_triangulos_escalenos} triángulos escalenos")
    print(f"hay {contador_triangulos_isosceles} triángulos isósceles")
    
    if mayor_perimetro > 0:
        print (f"el mayor perímetro del triangulo equilátero es de {mayor_perimetro}")


def repeticiones_del_programa():
    while True: # Bucle infinito hasta que se ingrese opción válida
        os.system("cls")
        repeticiones =  input("cuantas ternas vas a digitar: ")            
        if  repeticiones.isdigit():
            repeticiones = int(repeticiones)
            if repeticiones > 0:
                return repeticiones
            else:
                print("Error: las ternas deben ser mayores a 0")   
                os.system("pause")
        else:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
            os.system("pause")
                
def inicializar_ejercicio_2():
    cd = repeticiones_del_programa()
    os.system("cls")
    contador_triangulos_equilateros = 0
    contador_triangulos_escalenos = 0
    contador_triangulos_isosceles= 0
    mayor_perimetro = 0

    for i in range(cd):
        lado_a = pedir_ternas("lado a",i)
        lado_b = pedir_ternas("lado b",i)
        lado_c = pedir_ternas("lado c",i)

        
        if  triangulo_equilatero(lado_a,lado_b,lado_c):#Equilátero: 3 lados iguales.
            contador_triangulos_equilateros +=  1
            
            perimetro = lado_a * 3
            if perimetro > mayor_perimetro:
                mayor_perimetro = perimetro
                
        elif triangulo_isosceles(lado_a,lado_b,lado_c):#Isósceles: 2 lados iguales.
            contador_triangulos_isosceles += 1
        else:
            contador_triangulos_escalenos += 1#Escaleno: todos los lados diferentes.
        


    mostrar_factura(contador_triangulos_equilateros,contador_triangulos_escalenos,contador_triangulos_isosceles,mayor_perimetro)
    


        
        
#inicializar_variables()
            
    

