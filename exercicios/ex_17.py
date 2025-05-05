# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.

import math

ctt_oposto = float(input('Qual comprimento do cateto oposto: '))
ctt_adjacente = float(input('Qual comprimento do cateto adjacente: '))

hipotenusa = math.sqrt((ctt_oposto**2) + (ctt_adjacente**2))

print(f'O comprimento da hipotenusa é {hipotenusa:.2f}')