# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Informe um número: '))

for t in range(10):
    tabuada = num * (t + 1)
    print(f'{num} x {t + 1} = {tabuada}')