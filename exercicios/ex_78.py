# Faça uma calculadora com as 4 operações básicas.

def calculadora():
    while True:
        try:
            n1 = float(input('Digite um número: '))
            n2 = float(input('Digite outro número: '))
        except:
            print('Entrada inválida! Digite apenas números.')

        operador = input('Digite um operador (+ - * /): ')

        operadores_permitidos = ' + - * / '

        if operador not in operadores_permitidos:
            print('Operador inválido.')
            continue

        print('Realizando sua conta. Confira abaixo:')

        if operador == '+':
            print(f'{n1} + {n2} = {n1 + n2}')
        elif operador == '-':
            print(f'{n1} - {n2} = {n1 - n2}')
        elif operador == '*':
            print(f'{n1} * {n2} = {n1 * n2}')
        elif operador == '/':
            if n2 == 0:
                print('Erro! Não é possível dividir por zero.')
            else:
                print(f'{n1} / {n2} = {n1 / n2}')
        
        sair = input('Quer sair? [s]im: ').lower().startswith('s')

        if sair:
            break

calculadora()