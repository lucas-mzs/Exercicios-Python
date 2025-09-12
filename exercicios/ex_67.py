# Solicite 3 notas e diga se o aluno foi aprovado, reprovado ou está em recuperação.

def notas_aluno():
    nota_aluno_1 = float(input('Digite a sua 1º nota: '))
    nota_aluno_2 = float(input('Digite a sua 2º nota: '))
    nota_aluno_3 = float(input('Digite a sua 3º nota: '))

    media = (nota_aluno_1 + nota_aluno_2 + nota_aluno_3) / 2

    print(f'\nSua média foi: {media:.2f}')

    if media >= 7:
        print('🎉 Parabéns! Você foi APROVADO!')
    elif media >= 5:
        print('⚠️ Você está em RECUPERAÇÃO.')
    else:
        print('❌ Infelizmente, você foi REPROVADO.')

notas_aluno()