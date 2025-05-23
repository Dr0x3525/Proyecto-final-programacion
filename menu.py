import os

import ejercicios_parcial_1.ejercicio1 as parcial_1_ejercicio_1
#////////opciones////

def opciones_menu_principal(opcion_escogida):
    match opcion_escogida:
        case "1": 
            while  opciones_vectores(menu_vectores()) != "3": 
                pass
        case "2": 
            while  opciones_ejercicios_con_matrices(menu_ejercicios_matrices()) != "11": 
                pass
        case "3": 
            while  opciones_ejercicios_con_vectores_y_matrices(menu_ejercicios_vectores_y_matrices()) != "11":
                pass
        case "4":
            while  opciones_ejercicios_parciales(menu_parciales()) != "5":
                pass        
        case "5":
            while  opciones_ejercicios_con_cadenas(menu_ejercicios_con_cadenas()) != "11":
                pass
        case "6": 
            print("fin programa")
            os.system("pause")
            return "6"
        case other:
            print("Error")
            os.system("pause")

def opciones_vectores(opcion_escogida):
    match opcion_escogida:
        case "1":  
            while  opciones_ejercicios_con_un_vector(menu_ejercicio_con_un_vector()) != "6": 
                pass
            return "1"
        case "2":
            while  opciones_ejercicios_varios_vectores(menu_ejercicio_con_varios_vectores()) != "6":
                pass
            return "2"
        case "3":
            print("atras")
            return "3"
        case other:
            os.system('cls')
            print("opcion no valida vuelva a intentarlo")
            os.system("pause")
            return "4"

def opciones_ejercicios_con_un_vector(opcion_escogida):
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

def opciones_ejercicios_varios_vectores(opcion_escogida):
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
            print("ejercicio 6")
            os.system("pause")
            return "6"
        case "7":
            print("ejercicio 7")
            os.system("pause")
            return "7"
        case "8":
            print("ejercicio 8")
            os.system("pause")
            return "8"
        case "9":
            print("ejercicio 9")
            os.system("pause")
            return "9"
        case "10":
            print("ejericio 10")
            os.system("pause")
            return "10"
        case "11":
            return "11"
        case other:
            print("error puto")
            os.system("pause")
            return "12"

def opciones_ejercicios_con_vectores_y_matrices(opcion_escogida):
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
            print("ejercicio 6")
            os.system("pause")
            return "6"
        case "7":
            print("ejercicio 7")
            os.system("pause")
            return "7"
        case "8":
            print("ejercicio 8")
            os.system("pause")
            return "8"
        case "9":
            print("ejercicio 9")
            os.system("pause")
            return "9"
        case "10":
            print("ejericio 10")
            os.system("pause")
            return "10"
        case "11":
            return "11"
        case other:
            print("error puto")
            os.system("pause")
            return "12"

def opciones_ejercicios_parciales(opcion_escogida):
    match opcion_escogida:
        case "1":
            print("opcion 1")
            parcial_1_ejercicio_1.inicializar_ejercicio_1()
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
            return "5"
        case other:
            print("error puto")
            os.system("pause")
            return "6"



def opciones_ejercicios_con_cadenas(opcion_escogida):
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
            print("ejercicio 6")
            os.system("pause")
            return "6"
        case "7":
            print("ejercicio 7")
            os.system("pause")
            return "7"
        case "8":
            print("ejercicio 8")
            os.system("pause")
            return "8"
        case "9":
            print("ejercicio 9")
            os.system("pause")
            return "9"
        case "10":
            print("ejericio 10")
            os.system("pause")
            return "10"
        case "11":
            return "11"
        case other:
            print("error puto")
            os.system("pause")
            return "12"

#////////fin opciones////

#////////menus////
def menu_principal():
    os.system('cls') 
    print('---------------------------------')
    print('   1. Ejercicios vectores')
    print('   2. Ejercicios matrices')
    print('   3. Ejercicios vectores y matrices ')
    print('   4. Ejercicios parciales ')
    print('   5. Ejercicios cadenas ')
    print('   ')
    print('   6. Terminar programa')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :") #ya que la variable para la variable opcion no se van a realizar operaciones lo mejor es dejala con un string     
    return opcion


def menu_vectores():
    os.system('cls')
    print('---------------------------------')
    print('   1. Ejercicios con un vectores')
    print('   2. Ejercicios con varios vectores')
    print('   ')
    print('   3. Regresar')
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
    print('---------------------------------')
    print('   1. Ejercicios mat')
    print('   2. Ejercicios mat')
    print('   3. Ejercicios con mat')
    print('   4. Ejercicios con mat')
    print('   5. Ejercicios con mat')
    print('   6. Ejercicios con mat')
    print('   7. Ejercicios con mat')
    print('   8. Ejercicios con mat')
    print('   9. Ejercicios con mat')
    print('   10. Ejercicios con mat')
    print('   ')
    print('   11. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion

def menu_ejercicios_vectores_y_matrices():
    os.system('cls')
    print('---------------------------------')
    print('   1. Ejercicios mat y v')
    print('   2. Ejercicios mat y v')
    print('   3. Ejercicios con mat y v')
    print('   4. Ejercicios con mat y v')
    print('   5. Ejercicios con mat y v')
    print('   6. Ejercicios con mat y v')
    print('   7. Ejercicios con mat y v')
    print('   8. Ejercicios con mat y v')
    print('   9. Ejercicios con mat y v')
    print('   10. Ejercicios con mat y v')
    print('   ')
    print('   11. Regresar')
    print('')
    print('--------------------------------')
    
    opcion = input("elija una opcion :")   
    return opcion



def menu_ejercicios_con_cadenas():
    os.system('cls')
    print('---------------------------------')
    print('   1. Ejercicios ca')
    print('   2. Ejercicios ca')
    print('   3. Ejercicios ca')
    print('   4. Ejercicios ca')
    print('   5. Ejercicios ca')
    print('   6. Ejercicios ca')
    print('   7. Ejercicios ca')
    print('   8. Ejercicios ca')
    print('   9. Ejercicios ca')
    print('   10. Ejercicios ca')
    print('   ')
    print('   11. Regresar')
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
        
