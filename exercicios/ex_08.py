# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Quantos metros você quer converter para centímetros e milímetros: '))

centimetros = metros * 100
milimetros = metros * 1000

print(f'{metros} convertido para centímetros é {centimetros} e convertido para milímetros é {milimetros}'.replace('.', ','))
