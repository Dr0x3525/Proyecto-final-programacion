#1.una empres de servicios publicos 
# desea calcular el valor de las facturas de una cantidad dada de usuarios 
# del servicio de agua.
# por cada usuario se tiene:
#-codigo del usuario
#-consumo mensual de metros cubicos
#-estrato
#de acuerdo al estarto del usuario se realizara lo siguiente.
#estrato1---descuento del 40% del valor total
#estrato2---descuento del 30% del valor total
#estrato3---descuento del 15% del valor total
#estrato4---sin descuento
#estrato 5 y 6---incremento del valor en un 20%

#mostrar por cada usuario:
#codigo, valor total, descuento o incremento, valor Neto 

#ademas de esto mostrar el promedio de los balores pagados por estrato 1
#pago total mayor de los del estrato 2 mostrar el codigo y el valor

import os 

def pedir_codigo():
    codigo_usuario =  input("digita tu codigo por favor: ")
    codigo_usuario = int(codigo_usuario)    
    return codigo_usuario 

def pedir_consumo_mensual():
    consumo_mensual = input("cual es tu consumo mensual en m2: ")
    return consumo_mensual



def menu_estrato():
    print("escoge tu estrato social")
    os.system('cls') 
    print('---------------------------------')
    print('   1. estrato 1')
    print('   2. estrato 2')
    print('   3. estrato 3 ')
    print('   4. estrato 4')
    print('   5. estrato 5')
    print('   6. estrato 6')
    print('   0. Regresar')
    print('')
    print('--------------------------------')
    opcion = input("elija una opcion :")   
    return opcion


def opciones_menu_estrato(opcion_escogida,codigo_usuario,consumo_mensual):
    match opcion_escogida:
        case "1":
            descuento_estrato_1(codigo_usuario,consumo_mensual)
        case "2":
            print(opcion_escogida)
        case "3":
            print(opcion_escogida)
        case "4":
            print(opcion_escogida)
        case "5":
            print(opcion_escogida)
        case "6":
            print(opcion_escogida)
        case "0":
            print(opcion_escogida)
        case other:
            print("opcion no valida")

def descuento_estrato_1(codigo_usuario,consumo_mensual):
    print(f"descuento del 40% del valor total")
    print(codigo_usuario)
    print(consumo_mensual)
    os.system("pause")

continuar = True
valor_m2 = 10000

while continuar == True:
    codigo_usuario = pedir_codigo()
    consumo_mensual = pedir_consumo_mensual()
    
    while  opciones_menu_estrato(menu_estrato(),codigo_usuario,consumo_mensual) != 0:
        pass