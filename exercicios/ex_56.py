# Imprima a tabuada de um número digitado pelo usuário.

numero = int(input('Digite um número inteiro: '))

for n in range(10):
    tab = numero * (n + 1)
    print(f'{numero} x {n + 1} = {tab}')