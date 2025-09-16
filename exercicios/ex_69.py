# Solicite um número de 4 dígitos e mostre invertido (ex: 1234 → 4321).

def numeros_invertidos():
    numeros = input('Digite quatro números: ')

    if len(numeros) == 4 and numeros.isdigit():
        invertido = numeros[::-1]
        print(f'O número invertido é: {invertido}')
    else:
        print("Entrada inválida! Digite exatamente 4 dígitos.")

numeros_invertidos()