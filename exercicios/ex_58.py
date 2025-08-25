# Conte quantos múltiplos de 3 entre 1 e 500 também são pares.

def qtd_multiplos():
    contador = 0

    for m in range(1, 501):
        if m % 3 == 0 and m % 2 == 0:
            contador += 1
    
    print(f'Quantidade de múltiplos de 3 que também são pares entre 1 e 500: {contador}')

qtd_multiplos()