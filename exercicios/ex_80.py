# Leia dois números e calcule o MMC (mínimo múltiplo comum).

import math

def calculando_mmc(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)

def main():
    print('=== Cálculo do MMC ===')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    mmc = calculando_mmc(n1, n2)
    print(f'\nO MMC de {n1} e {n2} é: {mmc}')

main()