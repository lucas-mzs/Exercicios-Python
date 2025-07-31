# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a 
# média atingida: média abaixo de 5,0 é REPROVADO; média entre 5,0 e 6,9 fica de RECUPERAÇÃO; média 7,0 ou superior é APROVADO.

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

media = (nota_1 + nota_2) / 2
print(f'\nSua média foi: {media:.2f}')

if media < 5:
    print('❌ Infelizmente, você foi REPROVADO.')
elif 5 <= media and media <= 6.9:
    print('⚠️ Você ficou em RECUPERAÇÃO.')
else:
    print('✅ Parabéns, você foi APROVADO.')