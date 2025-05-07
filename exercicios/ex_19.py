# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random

alunos = [
    'Lucas Felipe',
    'Mayara Rosa',
    'Clara Matos',
    'Marlon Grabriel',
]

aluno_sorteado = random.sample(alunos, 1)

print(f'O aluno(a) sorteado foi {aluno_sorteado}'.join(aluno_sorteado))