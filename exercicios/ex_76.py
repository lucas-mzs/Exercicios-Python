# Crie um jogo de adivinhação entre 1 e 100 (com dicas de maior ou menor).

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print('\n🎲 Bem-vindo ao jogo de adivinhação!')
    print('Tente adivinhar o número entre 1 e 100.')

    while True:
        palpite = int(input('Digite seu palpite: '))
        tentativas += 1

        if palpite < numero_secreto:
            print('🔼 O número secreto é maior.\n')
        elif palpite > numero_secreto:
            print('🔽 O número secreto é menor.\n')
        else:
            print(f'🎉 Parabéns! Você acertou em {tentativas} tentativas. O número é {numero_secreto}')
            break

jogo_adivinhacao()