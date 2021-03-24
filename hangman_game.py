# ¡Adivina la palabra!
# _ _ _ _ _ _
# Ingresa una letra:
# La consola se debe reiniciar cada que ingrese una palabra
# Incorpora list o dic comprehensions, manejo de errores, manejo de archivos
# Investiga la función enumerate (documentacion)
# El método get de los diccionarios te puede servir
# Con os.system("cls") puedes limpiar la pantalla
# Anade un sistema de puntos
# Dibuja el ahorcado con el codigo ascii y dibujar en pantalla
# Mejora la interfaz, emojis

import os
import random


def read_words():

    with open('./words.txt', 'r', encoding='utf-8') as f:
        list_words = [i for i in f]
        word = list_words[random.randint(0, len(list_words))]

    return word


def ahorcado(letter):
    magic_word = read_words()
    if letter in magic_word:
        for i in range(len(magic_word)):
            if letter == magic_word[i]:
                print(letter, end=' ')
            else:
                print('_', end=' ')
    else:
        for _ in magic_word:
            print('_', end=' ')


def run():
    letter = ''
    count = 0
    while count < 10:
        os.system('cls')
        print('¡Adivina la palabra!')
        print(ahorcado(letter))
        letter = input('Escoge una letra: ').lower()
        count += 1


if __name__ == '__main__':
    run()