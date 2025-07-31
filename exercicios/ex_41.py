# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade: até 9 anos é MIRIM; até 14 anos é INFANTIL, até 19 anos
#  é JUNIOR, até 25 anos é SÊNIOR; acima é MASTER.

from datetime import date

def classificar_categoria(ano_nascimento: int) -> None:
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    print(f'\nIdade do atleta: {idade} anos')

    if idade <= 9:
        categoria = 'MIRIM'
    elif idade <= 14:
        categoria = 'INFANTIL'
    elif idade <= 19:
        categoria = 'JUNIOR'
    elif idade <= 25:
        categoria = 'SÊNIOR'
    else:
        categoria = 'MASTER'

    print(f'Categoria: {categoria}')

def main():
    print('\n=== Classificação de Categoria da Natação ===\n')
    try:
        ano = int(input('Digite o ano de nascimento do atleta: '))
        classificar_categoria(ano)
    except ValueError:
        print('❌ Entrada inválida. Por favor, digite um ano válido.')

main()