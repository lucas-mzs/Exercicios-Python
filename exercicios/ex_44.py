# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento: à vista 
# dinheiro/cheque: 10% DE DESCONTO; à vista no cartão: 5% DE DESCONTO; em até 2x no cartão: PREÇO NORMAL; 
# 3x ou mais no cartão: 20% DE JUROS.

def calcular_valor_final(preco: float, forma_pagamento: int, parcelas: int = 1) -> tuple[float, float]:
    if forma_pagamento == 1:
        valor_final = preco * 0.90
    elif forma_pagamento == 2:
        valor_final = preco * 0.95
    elif forma_pagamento == 3:
        valor_final = preco
    elif forma_pagamento == 4 and parcelas >= 3:
        valor_final = preco * 1.20
    else:
        return (-1, -1)

    valor_parcela = valor_final / parcelas if parcelas > 1 else valor_final
    return (valor_final, valor_parcela)

def main():
    print('\n=== Calculadora de Pagamento de Produto ===\n')

    try:
        preco = float(input('Digite o preço do produto (R$): '))
    except ValueError:
        print('❌ Valor inválido. Digite um número válido.')
        return

    print('\nEscolha a forma de pagamento:')
    print('[1] À vista (dinheiro ou cheque) → 10% de desconto')
    print('[2] À vista no cartão            → 5% de desconto')
    print('[3] 2x no cartão                 → preço normal')
    print('[4] 3x ou mais no cartão         → 20% de juros')

    try:
        opcao = int(input('\nOpção: '))
        parcelas = 1

        if opcao == 3:
            parcelas = 2
        elif opcao == 4:
            parcelas = int(input('Quantas parcelas (mínimo 3): '))
            if parcelas < 3:
                print('❌ Número de parcelas inválido para esta opção.')
                return

        total, valor_parcela = calcular_valor_final(preco, opcao, parcelas)

        if total == -1:
            print('❌ Opção de pagamento inválida.')
        else:
            print(f'\n💳 Total a pagar: R$ {total:.2f}')
            if parcelas > 1:
                print(f'📦 Parcelado em {parcelas}x de R$ {valor_parcela:.2f}')
            else:
                print('Pagamento à vista.')

    except ValueError:
        print('❌ Entrada inválida.')

main()