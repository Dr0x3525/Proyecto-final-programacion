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
    while True: # Bucle infinito hasta que se ingrese opción válida
        os.system("cls")
        codigo_usuario =  input("digita tu codigo por favor: ")            
        if  codigo_usuario.isdigit():
            codigo_usuario = int(codigo_usuario)
            if codigo_usuario > 0:
                return codigo_usuario
            else:
                print("Error: El código debe ser mayor  a 0")   
                os.system("pause")
        else:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
            os.system("pause")

def mostrar_el_ejercicio():
    os.system("cls")
    print("""#1.una empres de servicios publicos 
 desea calcular el valor de las facturas de una cantidad dada de usuarios 
 del servicio de agua.
 por cada usuario se tiene:
-codigo del usuario
-consumo mensual de metros cubicos
-estrato
de acuerdo al estarto del usuario se realizara lo siguiente.
estrato1---descuento del 40% del valor total
estrato2---descuento del 30% del valor total
estrato3---descuento del 15% del valor total
estrato4---sin descuento
estrato 5 y 6---incremento del valor en un 20%

mostrar por cada usuario:
codigo, valor total, descuento o incremento, valor Neto 

ademas de esto mostrar el promedio de los balores pagados por estrato 1
pago total mayor de los del estrato 2 mostrar el codigo y el valor
formar un diccionario con los primos de las dos matrices y las veces que se repiten.""")
    os.system("pause")
    os.system("cls")

def pedir_consumo_mensual():
    while True:# Bucle infinito hasta que se ingrese opción válida
        os.system("cls")
        consumo_mensual =  input("digita tu consumo mensual en m3 por favor: ")            
        if  consumo_mensual.isdigit():
            consumo_mensual = int(consumo_mensual)
            if consumo_mensual > 0:
                return consumo_mensual
            else:
                print("Error: El consumo mensual debe ser mayor  a 0")   
                os.system("pause")
        else:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
            os.system("pause")
            

def menu_estrato():
    while True:  # Bucle infinito hasta que se ingrese opción válida
        os.system('cls') 
        print("Escoge tu estrato social")
        print('---------------------------------')
        print('   1. Estrato 1')
        print('   2. Estrato 2')
        print('   3. Estrato 3')
        print('   4. Estrato 4')
        print('   5. Estrato 5')
        print('   6. Estrato 6')
        print('')
        print('---------------------------------')
        
        opcion = input("Elija una opción (1-6): ")
        
        # Verificar si la opción es válida
        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":
            return opcion
        else:
            print("Opción no válida. Intente nuevamente.")
            os.system('pause') 


def opciones_descuento(opcion_escogida):
    match opcion_escogida:
        case "1":
            descuento = 0.4
            return descuento
        case "2":
            descuento = 0.3
            return descuento
        case "3":
            descuento = 0.15
            return descuento
        case "4":
            descuento = 0
            return descuento
        case "5":
            incremento = -0.2
            return incremento
        case "6":
            incremento = -0.2
            return incremento

def calcular_valor_neto(valor_total,descuento):
    valor_neto = valor_total - (valor_total * descuento)
    valor_neto = int(valor_neto)
    return valor_neto
    
def continua_digitando():
    os.system("cls")
    continuar_digitando_usuarios = input("¿Desea continuar? (S): ").upper()

    if continuar_digitando_usuarios == "S":
            return True   
    return False   

def Mostrar_factura(codigo_usuario,descuento_estrato,valor_total,valor_neto):
    os.system("cls")
    print(f"codigo de usuario: {codigo_usuario}")
    print(f"valor total: {valor_total:,} $") #el :, es para separar en miles lo vi en tik tok
    print(f"descuento del {int(descuento_estrato*100)}%: {valor_total-valor_neto}$")
    print(f"valor neto: {valor_neto:,} $")#el :, es para separar en miles lo vi en tik tok
    os.system("pause")

    
def inicializar_ejercicio_1():
    mostrar_el_ejercicio()
    continuar_digitando_usuarios = True
    VALOR_M3 = 10000 #esto es una constante y segun la documentacion que estaba leyendo se escriben en mayusculas xd
    contador_estrato1  = 0
    valor_total_pagado = 0
    codigo_usuario_mayor_valor_total = False
    suma_valores_estrato_1 = 0
    
    while continuar_digitando_usuarios == True:
        os.system("cls")
        codigo_usuario = pedir_codigo()#hay que realizar que no ingrese valores diferentes de un numero
        consumo_mensual = pedir_consumo_mensual()#hay que realizar que no ingrese valores diferentes de un numero
        valor_total = consumo_mensual * VALOR_M3
        Estrato_usuario = menu_estrato()
        descuento = opciones_descuento(Estrato_usuario)
        valor_neto = calcular_valor_neto(valor_total,descuento)
        Mostrar_factura(codigo_usuario,descuento,valor_total,valor_neto)
        if Estrato_usuario == "1":
            suma_valores_estrato_1 = valor_neto + suma_valores_estrato_1
            contador_estrato1  = contador_estrato1  + 1
            promedio = suma_valores_estrato_1 / contador_estrato1 
        elif Estrato_usuario =="2":
            if valor_total > valor_total_pagado:
                valor_total_pagado = valor_total
                codigo_usuario_mayor_valor_total = codigo_usuario
                
        continuar_digitando_usuarios = continua_digitando()  
        if continuar_digitando_usuarios == False:
            os.system("cls")
            if contador_estrato1  != 0:
                print(f"promedio valor pagado estrato 1: {int(promedio)}$")
            if codigo_usuario_mayor_valor_total != False:
                print(f"el usuario estrato 2 con el mayor valor total es el usuario {codigo_usuario_mayor_valor_total}")
                print(f"y su valor total es: {valor_total_pagado:,}$")
                
            os.system("pause")
    

#inicializar_ejercicio_1()