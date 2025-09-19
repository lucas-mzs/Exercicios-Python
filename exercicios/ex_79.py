# Solicite um número e diga se ele é palíndromo (ex: 121).

def eh_palindromo():
    s = input('Digite um número: ').strip()

    if s.startswith('-'):
        print(f'{s} NÃO é palíndromo (números negativos não são considerados).')
        return
    
    if not s.isdigit():
        print('Entrada inválida. Digite apenas dígitos (ex.: 121 ou 1221).')
        return
    
    if s == s[::-1]:
        print(f'{s} É palíndromo.')
    else:
        print(f'{s} NÃO é palíndromo.')

eh_palindromo()