# Peça 7 números ao usuário e calcule quantos são pares e quantos são ímpares.

def contar_par_impar():
    pares = 0
    impares = 0

    for i in range(1, 8):
        numero = int(input(f'Digite o {i}º número inteiro: '))

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f'\n📊 Quantidade de números pares: {pares}')
    print(f'\n📊 Quantidade de números ímpares: {impares}')

contar_par_impar()