# Desenvolva um programa que pergunte a distância de uma viagem em km. 
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia_viagem = float(input('Qual é a distancio da sua viagem: '))

if distancia_viagem <= 200:
    preco_pessagem_viagem_curta = distancia_viagem * 0.5
    print(f'O valor do preço da passagem foi de R${preco_pessagem_viagem_curta:.2f}'.replace('.', ','))
elif distancia_viagem > 200:
    preco_pessagem_viagem_longa = distancia_viagem * 0.45
    print(f'O valor do preço da passagem foi de R${preco_pessagem_viagem_longa:.2f}'.replace('.', ','))