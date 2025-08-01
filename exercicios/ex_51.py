# Escreva um programa que exiba os múltiplos de 4 entre 1 e 100.

def mostrar_multiplos():
    for i in range(1, 101):
        if i % 4 == 0:
            print(i, end=' ')

mostrar_multiplos()