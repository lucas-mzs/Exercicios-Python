# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer
import time

mixer.init()

mixer.music.load('arquivo.mp3')

mixer.music.play()

print('\nComandos:')
print('[p] - Pausar')
print('[c] - Continuar')
print('[s] - Parar')
print('[q] - Sair do programa')

while True:
    comando = input("\nDigite um comando: ").lower()

    if comando == 'p':
        mixer.music.pause()
        print('Música pausada.')

    elif comando == 'c':
        mixer.music.unpause()
        print('Continuando música.')

    elif comando == 's':
        mixer.music.stop()
        print('Música parada.')

    elif comando == 'q':
        print('Saindo...')
        break

    else:
        print('Comando inválido. Use: p, c, s ou q.')