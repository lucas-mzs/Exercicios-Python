# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

def e_bissexto(ano):
    return ano % 4 == 0 or ano % 100 != 0

print(e_bissexto(2007))
print(e_bissexto(2025))
print(e_bissexto(2032))