# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome_pessoa = input('Digite seu nome completo: ')

if 'SILVA' in nome_pessoa.upper():
    print('Seu nome contém o sobrenome "Silva".')
else:
    print('Seu nome não contém o sobrenome "Silva".')