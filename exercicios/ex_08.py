# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = input(
    'Quantos metros você quer converter para centímetros e milímetros: ')

metros = float(metros)

centimetros = metros * 100
milimetros = metros * 1000

resultado = f'{metros} convertido para centímetros é {centimetros} e convertido para milímetros é {milimetros}'

print(resultado.replace('.', ','))
