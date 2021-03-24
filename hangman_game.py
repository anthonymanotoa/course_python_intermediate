# ¡Adivina la palabra!
# _ _ _ _ _ _
# Ingresa una letra:
# La consola se debe reiniciar cada que ingrese una palabra
# Incorpora list o dic comprehensions, manejo de errores, manejo de archivos, 
# Investiga la función enumerate (documentacion)
# El método get de los diccionarios te puede servir
# Con os.system("cls") puedes limpiar la pantalla
# Anade un sistema de puntos
# Dibuja el ahorcado con el codigo ascii y dibujar en pantalla
# Mejora la interfaz, emojis

import os
import random

def read_words():
    word = []
    with open('./words.txt', 'r', encoding='utf-8') as f: 
        for words in f:
            word.append(words)
    return word[random.randint(0, len(word))]


def ahorcado():
    for _ in read_words():
        print('_', end=' ')


def run():
    os.system('cls')
    print('¡Adivina la palabra!')
    print(ahorcado())


if __name__ == '__main__':
    run()