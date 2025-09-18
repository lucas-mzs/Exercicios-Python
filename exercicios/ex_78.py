# Faça uma calculadora com as 4 operações básicas.

def calculadora():
    while True:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        operador = input('Digite um operador (+ - * /): ')

        numeros_validos = None

        try:
            n1
            n2
            numeros_validos = True
        except:
            numeros_validos = None

        if numeros_validos is None:
            print('Um ou ambos os números são inválidos.')
            continue

        operadores_permitidos = ' + - * / '

        if operador not in operadores_permitidos:
            print('Operador inválido.')
            continue
            
        if len(operador) > 1:
            print('Digite apenas um operador.')
            continue

        print('Realizando sua conta. Confira abaixo:')

        if operador == '+':
            print(f'{n1} + {n2}: {n1 + n2}')
        elif operador == '-':
            print(f'{n1} - {n2}: {n1 - n2}')
        elif operador == '*':
            print(f'{n1} * {n2}: {n1 * n2}')
        else:
            print(f'{n1} / {n2}: {n1 / n2}')
        
        sair = input('Quer sair? [s]im: ').lower().startswith('s')

        if sair is True:
            break

calculadora()