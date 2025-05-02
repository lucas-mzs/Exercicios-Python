# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = input('Digite um número inteiro: ')
numero = int(numero)

sucessor = numero + 1
antecessor = numero - 1

resultado = f'O antecessor do seu número é {antecessor} e o sucessor é {sucessor}'

print(resultado)