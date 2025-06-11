#se tiene una cantidad dada de ternas (3 valores numericos por terna) 
#correspondiente a los lados de triangulos,
#determinar el perimetro mayor y menor de los triangulos escalenos
import os

def mostrar_el_ejercicio():
    os.system("cls")
    print("se tiene una cantidad dada de ternas (3 valores numericos por terna)")
    print("correspondiente a los lados de triangulos,")
    print("determinar el perimetro mayor y menor de los triangulos escalenos")
    os.system("pause")
    os.system("cls")
    
def pedir_cantidad_de_datos():
    cd = input("cuantos datos vas a escribir: ")
    cd = int(cd)
    return cd

def pedir_numeros():
    a =input("dime el valor del lado a: ")
    b =input("dime el valor del lado b: ")
    c =input("dime el valor del lado c: ")    
    a = int(a)
    b = int(b)
    c = int(c)
    return a , b, c 


def determinar_si_es_triangulo_escaleno(a,b,c):
    if a == b or a == c or b == c:
        return False
    return True

def calcular_perimetro(a,b,c):
    perimetro = a+b+c
    return perimetro

def mostrar_perimetros(perimetro_mayor,perimetro_menor):
    os.system("cls")
    if perimetro_mayor != False and  perimetro_menor != False:
        print(f"el perimetro mayor es {perimetro_mayor}")
        print(f"el perimetro menor es de {perimetro_menor}")
    else:
        print("no se encontro ningun triangulo escaleno")
    

def inicializar_ejercicio_3():
    
    mostrar_el_ejercicio()
    
    perimetro_menor = None 
    perimetro_mayor = None
    
    cantidad_de_datos = pedir_cantidad_de_datos()
    
    for item in range(cantidad_de_datos):
        print(f"triangulo {item+1}")
        lado_a, lado_b, lado_c =pedir_numeros()
        es_escaleno = determinar_si_es_triangulo_escaleno(lado_a, lado_b, lado_c)#un triangulo escaleno es un triangulo que no tienen ningun lado en comun
        if es_escaleno:
            perimetro = calcular_perimetro(lado_a, lado_b, lado_c)
            if perimetro_mayor == None:
                perimetro_mayor = perimetro
                perimetro_menor = perimetro
            elif perimetro > perimetro_mayor:
                perimetro_mayor = perimetro
            elif perimetro < perimetro_menor:
                perimetro_menor = perimetro
    mostrar_perimetros(perimetro_mayor,perimetro_menor)   
    os.system("pause")
    os.system("cls")
    
