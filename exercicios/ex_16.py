# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. 
# Exemplo: o número 6,127 tem a parte inteira 6.

nmr_real = float(input('Digite um número real (ex: 6.127): '))

nmr_real = int(round(nmr_real))

print(
    f'O seu número inteiro é {nmr_real}'
)