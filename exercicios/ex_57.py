# Mostre a soma dos quadrados dos 20 primeiros números naturais.

def soma_quadrados():
    soma = 0

    for n in range(1, 21):
        soma += n ** 2
    
    print(f'A soma dos quadrados dos primeiros 20 números naturais é {soma}')

soma_quadrados()