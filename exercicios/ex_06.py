# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = input('Digite um número: ')
numero = int(numero)

dobro_nmr = numero * 2
triplo_nmr = numero * 3
raiz_qdd_nmr = numero ** 2

resultado = f'O dobro do seu número é {dobro_nmr}, o triplo é {triplo_nmr} e a raiz quadrada é {raiz_qdd_nmr}'

print(resultado)