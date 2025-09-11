# Leia um número de 1 a 7 e mostre o dia da semana correspondente.

def dias_semana():
        dias = [
                None,
                'domingo',
                'segunda-feira',
                'terça-feira',
                'quarta-feira',
                'quinta-feira',
                'sexta-feira',
                'sábado'
        ]

        dia = int(input(f'Digite o número de 1 a 7 para saber o dia da semana: '))

        if 1 <= dia <= 7:
            print(f'O número {dia} corresponde ao dia {dias[dia]} da semana.')
        else:
            print('❌ Número inválido! Digite um número de 1 a 7.')
        
dias_semana()