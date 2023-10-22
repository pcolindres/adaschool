# Proyecto Integrador 3 de Paola Colindres
#1) Importar os.
#2) Importar la librería read char
#3) Crear función de limpiar pantalla
#4)  Crear función que aumentará N de 0 a 50,# dónde se hará un bucle que va hacer en cada
# interacción un ciclo limpiando la pantalla y aumentando el valor de N.
import os
import readchar as rchar


def clear_pantalla():
    return os.system('cls' if os.name=='nt' else 'clear')

def ingresar_n():

    n = 0
    print("Usuario por favor presione la tecla N para aumentar el valor")

    while n < 50: 
        letra = rchar.readkey()
        clear_pantalla()
        if n < 50 and letra == "n":
            n = n + 1
            print("n = ",n) #para poner el valor nuevo de n
        else: 
            print("favor recordar que dedebe presionar la tecla n")
    
    return "Programa Finalizado, Gracias por jugar"

print(ingresar_n())