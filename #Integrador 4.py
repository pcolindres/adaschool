#Integrador 4
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

import os
from read import readkey

def convertir laberinto(laberinto):
    #for fila in laberinto.split("\n"):
        #print(list(fila))
    return [list(fila) for fila in laberinto.split("\n")]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_mapa(mapa):
        for fila in mapa:
            print(''.join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        limpiar_pantalla()
        mapa[px][py] = 'P'
        mostrar_mapa(mapa)
        mapa[px][py] = '.'

        tecla = readkey()
        if tecla == key.UP and px > 0 and mapa[px - 1][py] != '#':
            px -= 1  # Flecha arriba
        elif tecla == key.DOWN and px < len(mapa) - 1 and mapa[px + 1][py] != '#':
            px += 1  # Flecha abajo
        elif tecla == key.LEFT and py > 0 and mapa[px][py - 1] != '#':
            py -= 1  # Flecha izquierda
        elif tecla == key.RIGHT and py < len(mapa[0]) - 1 and mapa[px][py + 1] != '#':
            py += 1  # Flecha derecha
    print ("Felicidades Ganaste el juego")
