# Peça um número e diga se é perfeito (soma dos divisores = número).

def numero_perfeito():
    n = int(input('Digite um número: '))
    soma_divisores = 0

    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    
    if soma_divisores == n:
        print(f'{n} é um número perfeito.')
    else:
        print(f'{n} não é um número perfeito.')

numero_perfeito()