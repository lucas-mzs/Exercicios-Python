# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Em qual cidade você mora: ')

primeira_palavra = cidade.split()[0]

if primeira_palavra == 'Santo':
    print('Sua cidade começa com "Santo".')
else:
    print('Sua cidade não começa com "Santo".')