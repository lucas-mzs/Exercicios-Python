# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero_usr = int(input('Digite um número: '))

if numero_usr % 2 == 0:
    print(f'{numero_usr} é par.')
else:
    print(f'{numero_usr} é ímpar.')