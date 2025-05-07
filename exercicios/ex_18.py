# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo_graus = float(input('Digite um ângulo qualquer: '))
angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')