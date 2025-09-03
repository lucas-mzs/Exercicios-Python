# Peça a idade e diga em qual faixa etária ela se encaixa (infantil, adolescente, adulto...).

idade = int(input('Digite sua idade: '))

if idade <= 13:
    print('Você ainda é infantil.')
elif idade <= 17:
    print('Você é adolescente.')
elif idade >= 18:
    print('Você já é adulto.')