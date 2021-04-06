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


def game(magic_word, letter, game_word):
    if letter in magic_word:
        for i in range(len(magic_word)):
            if letter == magic_word[i]:
                game_word[i] = letter

    return ' '.join(game_word)


def game_print(magic_word, letter, game_word):
    pass #podrias poner parametros boleanos para saber si estas continuando el jeugo o si ya se acabo


def run():
    lives = 5
    letter = ''
    magic_word = read_words()
    game_word = ['_' for i in range(len(magic_word) - 1)]

    while lives > 0:
        if game(magic_word, letter, game_word).count('_') > 0:
            if letter in game(magic_word, letter, game_word):
                os.system('cls')
                print(f'Vidas restantes: {"❤" * (lives)}')
                print('¡Adivina la palabra!')
                print(game(magic_word, letter, game_word))
                letter = input('Escoge una letra: ').lower()
            else:
                lives -= 1
                if lives > 0:
                    os.system('cls')
                    print(f'Vidas restantes: {"❤" * (lives)}')
                    print('¡Adivina la palabra!')
                    print(game(magic_word, letter, game_word))
                    letter = input('Escoge una letra: ').lower()
                else:
                    os.system('cls')
                    print('¡Te quedaste sin vidas!\nJuego terminado...\n')
                    print('La palabra era: ' + magic_word)
        else:
            os.system('cls')
            print('¡Adivina la palabra!')
            print(game(magic_word, letter, game_word))
            print('¡Ganaste! √')
            break
    

if __name__ == '__main__':
    run()