# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

def numeros_pares():
    print('Números pares entre 1 e 50:')
    for i in range(2, 51, 2):
        print(i, end=', ')
    print('\n\n✅ Fim da contagem.')

numeros_pares()