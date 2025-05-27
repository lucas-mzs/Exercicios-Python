# Crie um programa que leia o nome completo de uma pessoa e mostre:
# (a) O nome com todas as letras maiúsculas e minúsculas.
# (b) Quantas letras ao todo (sem considerar espaços).
# (c) Quantas letras tem o primeiro nome.

nome = input('Informe seu nome: ')

print(f'Nome: {nome}')

primeiro_nome = nome.split()[0]
nome = nome.upper().replace(' ', '')
nmr = len(nome)
nmrp = len(primeiro_nome)

print(f'Letras nome completo: {nmr}')
print(f'Letras primeiro nome: {nmrp}')