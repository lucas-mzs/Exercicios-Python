# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade_carro = float(input('Digite a velocidade do seu carro: '))

multa = velocidade_carro * 7

if velocidade_carro >= 80:
    print(f'Você foi multado no valor de {multa}')
else:
    print('Você está na velocidade correta. Boa viagem!')