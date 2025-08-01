# Crie um programa que faça o computador jogar JOKENPÔ com você.

import random
import time

def jogar_jokenpo():
    opcoes = ['pedra', 'papel', 'tesoura']
    computador = random.choice(opcoes)

    print('=== JOKENPÔ ===')
    print('\nEscolha sua opção:')
    print('[1] Pedra')
    print('[2] Papel')
    print('[3] Tesoura')

    escolha = input('\nEscolha o número da sua jogada: ')
    mapa = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}

    if escolha not in mapa:
        print('❌ Escolha inválida. Tente novamente com 1, 2 ou 3.')
        return
    
    jogador = mapa[escolha]

    print('\nJO...')
    time.sleep(0.5)
    print('KEN...')
    time.sleep(0.5)
    print('PÔ...')
    time.sleep(0.5)

    print(f'\n🧠  Computador jogou: {computador}')
    print(f'🧍 Você jogou: {jogador}')

    if jogador == computador:
        resultado = '🔁 Empate!'
    elif (
        (jogador == 'pedra' and computador == 'tesoura') or
        (jogador == 'tesoura' and computador == 'papel') or
        (jogador == 'papel' and computador == 'pedra')
    ):
        resultado = '✅ Você venceu!'
    else:
        resultado = '❌ Você perder!'

    print(f'Resultado: {resultado}')

jogar_jokenpo()