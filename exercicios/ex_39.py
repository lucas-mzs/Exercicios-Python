# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se 
# alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

def verificar_alistamento(ano_nascimento: int) -> None:
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    print(f'\n Você tem {idade} anos em {ano_atual}.')

    if idade < 18:
        anos_faltando = 18 - idade
        ano_alistamento = ano_atual + anos_faltando
        print(f'🟡 Ainda faltam {anos_faltando} ano(s) para o alistamento.')
        print(f'Seu alistamento será em {ano_alistamento}.')

    elif idade == 18:
        print('🟢 Está na hora de se alistar ao serviço militar **neste ano**!')
    else:
        anos_atrasado = idade - 18
        ano_alistamento = ano_atual - anos_atrasado
        print(f'🔴 Você já deveria ter se alistado há {anos_atrasado} ano(s).')
        print(f'Seu alistamento foi em {ano_alistamento}.')

def main():
    print('=== Verificador de Alistamento Militar ===\n')

    try:
        nascimento = int(input('Digite seu ano de nascimento: '))
        verificar_alistamento(nascimento)
    except ValueError:
        print('❌ Entrada inválida. Digite um ano válido.')

main()