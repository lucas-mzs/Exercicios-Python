# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

nmr_1 = 3
nmr_2 = 2
nmr_3 = 1

if nmr_1 > nmr_2 and nmr_1 > nmr_3:
    print(f'{nmr_1} é maior que os números {nmr_2} e {nmr_3}.')
elif nmr_2 > nmr_1 and nmr_2 > nmr_3:
    print(f'{nmr_2} é maior que os números {nmr_1} e {nmr_3}.')
elif nmr_3 > nmr_1 and nmr_3 > nmr_2:
    print(f'{nmr_3} é maior que os números {nmr_1} e {nmr_2}.')