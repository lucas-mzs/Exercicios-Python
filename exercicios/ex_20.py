# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = [
    'Lucas Felipe',
    'Mayara Rosa',
    'Clara Matos',
    'Marlon Grabriel',
]

sorteio_alunos = random.sample(alunos, 4)

print('O sortei dos alunos que iram apresentar o trabalho foi: ')

for i, aluno in enumerate(sorteio_alunos):
    print(f'{i})', aluno)