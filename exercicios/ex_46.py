# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com 
# uma pequena pausa de 1 segundo entre eles.

import time

def estourar_fogos():
    print('=== Começar queima de fogos! ===')

    for i in range(10, 0, -1):
        print(f'\n{i}...')
        time.sleep(1)

    print('\n🎆 BUUM! EXPLODIU! 🎇')

estourar_fogos()