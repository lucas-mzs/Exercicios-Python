# Faça um programa que leia uma frase pelo teclado e mostre:
# (a) Quantas vezes aparece a letra "A".
# (b) Em que posição ela aparece pela primeira vez.
# (c) Em que posição ela aparece pela última vez.

frase = input('Digite uma breve frase: ').strip()

letras_maiuscula = frase.upper()

qtd_a = letras_maiuscula.count('A')
print(f'A letra "a" apareceu {qtd_a} vezes.')

primeira_pos = letras_maiuscula.find('A') + 1
print(f'A primeira letra "a" apareceu na posição {primeira_pos}.')

ultima_pos = letras_maiuscula.rfind('A')
print(f'A ultima letra "A" apareceu na posição {ultima_pos}.')