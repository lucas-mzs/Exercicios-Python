# Peça 3 números e mostre a soma apenas dos pares.

def soma_pares():
    soma = 0
    numeros = []

    for i in range(1, 4):
        n = int(input(f'Digite o {i}º número: '))
        numeros.append(n)
        if n % 2 == 0:
            soma += n
    
    if soma > 0:
        print(f'Você digitou os números: {numeros}')
        print(f'A soma dos pares é {soma}')
    else:
        print(f'Você digitou os números: {numeros}')
        print('Nenhum número par foi digitado.')

soma_pares()