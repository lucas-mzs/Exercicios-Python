# Solicite um número e informe se ele é positivo, negativo ou zero.

print('\n=== Leitor de número: Positivo, Negativo ou Zero ===')

nmr = int(input('\nDigite um número: '))

if nmr == 0:
    print('Seu número é zero (0).')
elif nmr < 0:
    print('Seu número é negativo.')
elif nmr > 0:
    print('Seu número é positivo.')