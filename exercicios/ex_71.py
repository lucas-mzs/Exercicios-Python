# Leia um número e mostre o seu fatorial.

def fatorial_numero():
    n = int(input('Digite um número inteiro para calcular o fatorial: '))
    fatorial = 1

    for i in range(1, n + 1):
        fatorial *= i
    
    print(f'O fatorial de {n} é: {fatorial}')

fatorial_numero()