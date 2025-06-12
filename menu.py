import os
import ejercicios_condicionales_sin_arreglos.ejercicio1 as condicionales_ejercicio_1
import ejercicios_condicionales_sin_arreglos.ejercicio2 as condicionales_ejercicio_2
import ejercicios_condicionales_sin_arreglos.ejercicio3 as condicionales_ejercicio_3
import ejercicios_condicionales_sin_arreglos.ejercicio4 as condicionales_ejercicio_4
import ejercicios_condicionales_sin_arreglos.ejercicio5 as condicionales_ejercicio_5
import ejercicios_arreglos.ejercicio_1 as vectores_ejercicio_1
import ejercicios_arreglos.ejercicio_2 as vectores_ejercicio_2
import ejercicios_arreglos.ejercicio_3 as vectores_ejercicio_3
import ejercicios_arreglos.ejercicio_4 as vectores_ejercicio_4
import ejercicios_arreglos.ejercicio_5 as vectores_ejercicio_5
import ejercicios_arreglos.ejercicio_6 as vectores_ejercicio_6
import ejercicios_arreglos.ejercicio_7 as vectores_ejercicio_7
import ejercicios_arreglos.ejercicio_8 as vectores_ejercicio_8
import ejercicios_con_matrices.ejercicio1 as matrices_ejercicio_1
import ejercicios_con_matrices.ejercicio2 as matrices_ejercicio_2
import ejercicios_con_matrices.ejercicio3 as matrices_ejercicio_3
import ejercicios_con_matrices.ejercicio4 as matrices_ejercicio_4
import ejercicios_diccionarios.ejercicio_1 as diccionario_ejercicio_1
import ejercicios_diccionarios.ejercicio_2 as diccionario_ejercicio_2
import ejercicios_diccionarios.ejercicio_3 as diccionario_ejercicio_3
import ejercicios_diccionarios.ejercicio_4 as diccionario_ejercicio_4
import ejercicios_diccionarios.ejercicio_5 as diccionario_ejercicio_5








#////////opciones////



def opciones_menu_principal(opcion_escogida):
    match opcion_escogida:
        case "1": 
            while  opciones_vectores(menu_vectores()) != "9": 
                pass
        case "2": 
            while  opciones_ejercicios_con_matrices(menu_ejercicios_matrices()) != "5": 
                pass
        case "3": 
            while  opciones_ejercicios_con_diccionarios(menu_ejercicios_diccionarios()) != "6":
                pass
        case "4":
            while  opciones_ejercicios_parciales(menu_parciales()) != "5":
                pass        
        case "5":
            while  ejercicios_condicionales_sin_arreglos(menu_ejercicios_condicionales_sin_arreglos()) != "6":
                pass
        case "6": 
            print("fin programa")
            os.system("pause")
            return "6"
        case other:
            os.system("cls")
            print("Error")
            os.system("pause")

def opciones_vectores(opcion_escogida):
    match opcion_escogida:
        case "1":  
            vectores_ejercicio_1.inicializar_ejercicio_1()
            return "1"
        case "2":
            vectores_ejercicio_2.inicializar_ejercicio_2()
            return "2"
        case "3":
            vectores_ejercicio_3.inicializar_ejercicio_3()
            return "3"
        case "4":
            vectores_ejercicio_4.inicializar_ejercicio_4()
            return "3"
        case "5":
            vectores_ejercicio_5.inicializar_ejercicio_5()
            return "3"
        case "6":
            vectores_ejercicio_6.inicializar_ejercicio_6()
            return "3"
        case "7":
            vectores_ejercicio_7.inicializar_ejercicio_7()
            return "3"
        case "8":
            vectores_ejercicio_8.inicializar_ejercicio_8()
            return "3"
        case "9":
            print("atras")
            return "9"
        case other:
            os.system('cls')
            print("opcion no valida vuelva a intentarlo")
            os.system("pause")
            return "4"


    match opcion_escogida:
        case "1":
            print("opcion 1")
            os.system("pause")
            return "1"
        case "2":
            print("opcion 2")
            os.system("pause")
            return "2"
        case "3":
            print("opcion 3")
            os.system("pause")
            return "3"
        case "4":
            print("opcion 4")
            os.system("pause")
            return "4"
        case "5":
            print("opcion 5")
            os.system("pause")
            return "5"
        case "6":
            return "6"
        case other:
            print("error puto")
            os.system("pause")
            return "7"

def opciones_ejercicios_con_matrices(opcion_escogida):
    match opcion_escogida:
        case "1":
            print("opcion 1")
            matrices_ejercicio_1.inicializa_ejercicio_1()
            return "1"
        case "2":
            print("opcion 2")
            matrices_ejercicio_2.inicializa_ejercicio_2()
            return "2"
        case "3":
            print("opcion 3")
            matrices_ejercicio_3.inicializa_ejercicio_3()
            return "3"
        case "4":
            print("opcion 4")
            matrices_ejercicio_4.inicializa_ejercicio_4()
            return "4"
        case "5":
            return "5"
        case other:
            os.system('cls')
            print("opcion no valida vuelva a intentarlo")
            os.system("pause")
            return "12"

def opciones_ejercicios_con_diccionarios(opcion_escogida):
    match opcion_escogida:
        case "1":
            print("opcion 1")
            diccionario_ejercicio_1.inicializar_ejercicio_1()
            return "1"
        case "2":
            print("opcion 2")
            diccionario_ejercicio_2.inicializar_ejercicio_2()
            return "2"
        case "3":
            print("opcion 3")
            diccionario_ejercicio_3.inicializar_ejercicio_3()
            return "3"
        case "4":
            print("opcion 4")
            diccionario_ejercicio_4.inicializar_ejercicio_4()
            return "4"
        case "5":
            print("opcion 5")
            diccionario_ejercicio_5.inicializar_ejercicio_5()
            return "5"
        case "6":
            print("ejercicio 6")
            os.system("pause")
            return "6"
        case other:
            os.system('cls')
            print("opcion no valida vuelva a intentarlo")
            os.system("pause")
            return "12"

def opciones_ejercicios_parciales(opcion_escogida):
    match opcion_escogida:
        case "1":
            print("opcion 1")
            while opciones_ejercicios_parcial_1(menu_parcial_1()) != "5":
              pass  
            return "1"
        case "2":
            print("opcion 2")
            parcial_1_ejercicio_2.inicializar_ejercicio_2()
            return "2"
        case "3":
            print("opcion 3")
            os.system("pause")
            return "3"
        case "4":
            print("opcion 4")
            os.system("pause")
            return "4"
        case "5":
            return "5"
        case other:
            print("error ")
            os.system("pause")
            return "6"

def opciones_ejercicios_parcial_1(opcion_escogida):
    match opcion_escogida:
        case "1":
            print("opcion 1")
            parcial_1_ejercicio_1.inicializar_ejercicio_1()
            return "1"
        case "2":
            print("opcion 2")
            parcial_1_ejercicio_2.inicializar_ejercicio_2()
            return "2"
        case "3":
            print("opcion 3")
            parcial_1_ejercicio_3.inicializar_ejercicio_3_parcial_1()
            return "3"
        case "4":
            print("opcion 4")
            parcial_1_ejercicio_4.inicializar_ejercicio_4_parcial_1()
            return "4"
        case "5":
            return "5"
        case other:
            print("error ")
            os.system("pause")
            return "6"

def ejercicios_condicionales_sin_arreglos(opcion_escogida):
    match opcion_escogida:
        case "1":
            print("opcion 1")
            
            condicionales_ejercicio_1.inicializar_ejercicio_1()
            return "1"
        case "2":
            print("opcion 2")
            condicionales_ejercicio_2.inicializar_ejercicio_2()
            return "2"
        case "3":
            print("opcion 3")
            condicionales_ejercicio_3.inicializar_ejercicio_3()
            return "3"
        case "4":
            print("opcion 4")
            condicionales_ejercicio_4.inicializar_ejercicio_4()
            return "4"
        case "5":
            print("opcion 5")
            condicionales_ejercicio_5.inicializar_ejercicio_5()
            return "5"
        case "6":
            return "6"
        case other:
            os.system("cls")
            print("error digite un numero correcto")
            os.system("pause")
            return "12"

#////////fin opciones////

#////////menus////
def menu_principal():
    os.system('cls') 
    print("menu principal")
    print('---------------------------------')
    print('   1. Ejercicios vectores')
    print('   2. Ejercicios matrices')
    print('   3. Ejercicios diccionarios ')
    print('   4. Ejercicios parciales ')
    print('   5. Ejercicios con condicionales sin arreglos ')
    print('   ')
    print('   6. Terminar programa')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :") #ya que la variable para la variable opcion no se van a realizar operaciones lo mejor es dejala con un string     
    return opcion


def menu_vectores():
    os.system('cls')
    print("menu vectores")
    print('---------------------------------')
    print('   1. Ejercicios 1')
    print('   2. Ejercicios 2')
    print('   3. Ejercicios 3')
    print('   4. Ejercicios 4')
    print('   5. Ejercicios 5')
    print('   6. Ejercicios 6')
    print('   7. Ejercicios 7')
    print('   8. Ejercicios 8')
    print('   ')
    print('   9. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion



def menu_parciales():
    os.system('cls') 
    print('---------------------------------')
    print('   1. parcial 1')
    print('   2. recuperacion parcial 1')
    print('   3. parcial 2 ')
    print('   4. recuperacion parcial 2')
    print('   ')
    print('   5. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :") #ya que la variable para la variable opcion no se van a realizar operaciones lo mejor es dejala con un string     
    return opcion

def menu_parcial_1():
    os.system('cls') 
    print('---------------------------------')
    print('   1. ejercicio 1')
    print('   2. ejercicio 2')
    print('   3. ejercicio 3')
    print('   4. ejercicio 4')
    print('   ')
    print('   5. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :") #ya que la variable para la variable opcion no se van a realizar operaciones lo mejor es dejala con un string     
    return opcion

#////////menus ejercicios////

def menu_ejercicio_con_un_vector():
    os.system('cls')
    print('---------------------------------')
    print('   1. Ejercicios 1')
    print('   2. Ejercicios 2')
    print('   3. Ejercicios 3')
    print('   4. Ejercicios 4')
    print('   5. Ejercicios 5')
    print('   ')
    print('   6. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion

def menu_ejercicio_con_varios_vectores():
    os.system('cls')
    print('---------------------------------')
    print('   1. Ejercicios 1')
    print('   2. Ejercicios 2')
    print('   3. Ejercicios 3')
    print('   4. Ejercicios 4')
    print('   5. Ejercicios 5')
    print('   ')
    print('   6. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion


def menu_ejercicios_matrices():
    os.system('cls')
    print("menu matrices")
    print('---------------------------------')
    print('   1. Ejercicios 1')
    print('   2. Ejercicios 2')
    print('   3. Ejercicios 3')
    print('   4. Ejercicios 4')
    print('   ')
    print('   5. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion

def menu_ejercicios_diccionarios():
    os.system('cls')
    print("menu diccionarios")
    print('---------------------------------')
    print('   1. Ejercicio 1')
    print('   2. Ejercicio 2')
    print('   3. Ejercicio 3')
    print('   4. Ejercicio 4')
    print('   5. Ejercicio 5')
    print('   ')
    print('   6. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion



def menu_ejercicios_condicionales_sin_arreglos():
    os.system('cls')
    print("menu ejercicios con condicionales sin arreglos")
    print('---------------------------------')
    print('   1. Ejercicios 1')
    print('   2. Ejercicios 2')
    print('   3. Ejercicios 3')
    print('   4. Ejercicios 4')
    print('   5. Ejercicios 5')
    print('   6. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion
#////////menus ejercicios////


#////////fin menus////

    
#////////EJERCICIOS ////

#////////EJERCICIOS PARCIALES////

#////////fin menus////


#////////FIN EJERCICIOS////





while  opciones_menu_principal(menu_principal()) != "6":
    pass
        
