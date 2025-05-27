# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
# Exemplo: Ana Maria de Souza, primeiro: Ana, último: Souza.

nome = input('Digite seu nome completo: ')

primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]
print(f'Seu primeiro nome é {primeiro_nome} e o seu ultimo nome é {ultimo_nome}.')