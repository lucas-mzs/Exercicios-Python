# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores o iguais, o aumento é de 15%.

salario = float(input('Quanto você recebe de salario: '))

if salario > 1250:
    acrescimo_maior = salario * 1
    print(f'O seu salario teve um aumento de 10%, e ficou com esse valor final R${acrescimo_maior}')
elif salario <= 1250:
    acrescimo_menor = salario * 1.15
    print(f'O seu salario teve um aumento de 15%, e ficou com esse valor final R${acrescimo_menor}')