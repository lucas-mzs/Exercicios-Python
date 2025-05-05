# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade 
# de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

km_rodado = float(input('Quantos km foi percorrido com o carro: '))
dias_alugados = int(input('Por quantos ele foi alugado: '))

calculo_dias = dias_alugados * 60
calculo_km = km_rodado * 0.15

valor_pagar = calculo_dias + calculo_km

print(
    f'O valor total com {km_rodado} Km rodados e {dias_alugados} dias alugados, deu R${valor_pagar:.2f}'
)