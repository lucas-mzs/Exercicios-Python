# Crie um programa que leia quanto dinheiro uma pessoas tem na carteira e mostre quantos dólares ela pode comprar. 
# Considere U$$1,00 = R$3,37.

valor_real = input('Quantos reais você tem? ')
valor_real = float(valor_real)

dolar = valor_real / 3.37

resultado = f'Com R${valor_real} você pode comprar U${dolar:.2f} dolares'

print(resultado)