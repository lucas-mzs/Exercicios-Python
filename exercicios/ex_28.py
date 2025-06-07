# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para 
# o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_cmp = random.randint(0, 5)

numero_usr = int(input('Qual número entre 0 e 5 o computador escolheu: '))

if numero_usr not in (0, 1, 2, 3, 4, 5):
    print('Número inválido.')
elif numero_usr == numero_cmp:
    print('Você acertou!!')
else:
    print(f'Você errou! O número escolhido foi {numero_cmp}.')
