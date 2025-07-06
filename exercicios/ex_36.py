# Escreva um programa para aprovar o empréstimo bancário para a compra de um casa. 
# Pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


def aprovar_emprestimo():
    print('Vamos verificar se seu empréstimo para compra da casa será aprovado.')

    valor_casa = float(input('Valor da casa: R$ '))
    salario = float(input('Salário mensal: R$ '))
    anos_pagamento = int(input('Em quantos anos desaja pagar: '))

    meses = anos_pagamento * 12
    prestacao = valor_casa / meses
    limite = salario * 0.3

    print(f'\nValor da prestação: R${prestacao:.2f}')
    print(f'30% do seu salário: R${limite:.2f}')

    if prestacao <= limite:
        print('\n✅ Empréstimo aprovado!')
    else:
        print('\n❌ Empréstimo negado: a prestação excede 30% do seu salário.')

aprovar_emprestimo()