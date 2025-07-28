# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual 
# será a base de conversão: 1 pra binário; 2 para octal; 3 para hexadecimal.

def converter_base(numero: int, base: int) -> str:
    if base == 1:
        return bin(numero)[2:]
    elif base == 2:
        return oct(numero)[2:]
    elif base == 3:
        return hex(numero)[2:].upper()
    else:
        return 'Opção inválida.'
    
def main():
    print('Conversor de Bases Numéricas\n')

    try:
        numero  = int(input('Digite um número inteiro: '))
    except ValueError:
        print('❌ Entrada inválida. Por favor, digite um número inteiro.')
        return
    
    print('\nEscolha a base da conversão:')
    print('[1] Binário')
    print('[2] Octal')
    print('[3] Hexadecimal')

    try:
        opcao = int(input('Sua opção: '))
    except ValueError:
        print('❌ Entrada inválida. Use apenas números 1, 2 ou 3.')
        return
    
    resultado = converter_base(numero, opcao)

    if resultado == 'Opção inválida.':
        print('❌ Opção inválida. Encerrando.')
    else:
        bases = {1: 'Binário', 2: 'Octal', 3: 'Hexadecimal'}
        print(f'\n✅ {bases[opcao]} de {numero} é: {resultado}')
    
main()