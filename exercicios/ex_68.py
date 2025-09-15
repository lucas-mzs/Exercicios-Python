# Peça um ano e diga se ele é bissexto.

def eh_bissexto(ano):
    return ano % 4 == 0 or ano % 100 != 0

print(eh_bissexto(2025))
print(eh_bissexto(2026))
print(eh_bissexto(2032))