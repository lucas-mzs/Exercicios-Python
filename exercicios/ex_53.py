# Leia 10 números e conte quantos são negativos.

def ler_negativos():
    negativos = 0
    print('=== Contando quantidade de negativos ===')

    for i in range(1, 11):
        try:
            numero = float(input(f'Digite o {i}º número: '))
            if numero < 0:
                negativos += 1
        except ValueError:
            print('❌ Entrada inválida. Digite um número válido.')

    print(f'\n🔢 Você digitou {negativos} número(s) negativo(s).')

ler_negativos()