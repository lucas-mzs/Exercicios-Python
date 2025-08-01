# Mostre os números ímpares entre 200 e 0 (ordem decrescente).

def mostrar_impares():
    print('=== Números ímpares entre 200 e 1 (decrescente) ===\n')

    for i in range(199, 0, -2):
        print(i, end=' ')
    print('\n\n✅ Fim da lista.')

mostrar_impares()