# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem: 
# o primeiro valor é maior; o segundo valor é maior; não existe valor maior, os dois são iguais.

def comparar_numeros(a: int, b: int) -> str:
    if a > b:
        return '✅ O primeiro valor é maior.'
    elif b > a:
        return '✅ O segundo valor é maior.'
    else:
        return 'ℹ️ Não existe valor maior, os dois são iguais.'
    
def main():
    print('Comparador de Números Inteiros\n')

    try:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    except ValueError:
        print('❌ Entrada inválida. Certifique-se de digitar apenas números inteiros.')
        return
    
    resultado = comparar_numeros(num1, num2)
    print('\n' + resultado)

main()