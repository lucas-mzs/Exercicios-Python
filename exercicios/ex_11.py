# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura_parede = float(input('Digite a largura da sua parede: '))
altura_parede = float(input('Digite a altura da sua parede: '))

area = largura_parede * altura_parede

tinta_necessaria = area / 2

print(f'A área da parede é {area:.2f} m².')
print(f'Você precisará de {tinta_necessaria:.2f} litro(s) de tinta.')