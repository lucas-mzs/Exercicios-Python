# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

def soma_pares():
    soma = 0
    print('\n=== Soma de números pares ===')

    for i in range(1, 7):
        try:
            numero = int(input(f'Digite o {i}º número inteiro: '))
            if numero % 2 == 0:
                soma += numero
        except ValueError:
            print('❌ Valor inválido. Digite um número inteiro.')
            return

    print(f'\n✅ A soma dos números pares, é: {soma}')

soma_pares()