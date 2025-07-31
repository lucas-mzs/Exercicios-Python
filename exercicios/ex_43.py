# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, onde: abaixo de 18,5 
# é ABAIXO DO PESO; entre 18.5 e 25 é PESO IDEAL; 25 até 30 é SOBREPESO; 30 até 40 é OBESIDADE; acima de 40 é OBESIDADE MÓRBIDA.

def calcular_imc(peso: float, altura:float) -> float:
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return 'ABAIXO DO PESO.'
    if imc < 25:
        return 'PESO IDEAL.'
    if imc < 30:
        return 'SOBREPESO.'
    if imc < 40:
        return 'OBESIDADE.'
    else:
        return 'OBESIDADE MÓRBIDA.'
    
def main():
    print('\n=== Calculadora de IMC ===\n')

    try:
        peso = float(input('Digite seu peso (kg): '))
        altura = float(input('Digite sua altura (m): '))
    except ValueError:
        print('❌ Entrada inválida. Use apenas números com ponto, se necessario (ex: 70.5).')
        return
    
    if peso <= 0 or altura <= 0:
        print('❌ Peso e altura devem ser maiores que zero.')

    imc = calcular_imc(peso, altura)
    status = classificar_imc(imc)

    print(f'\nSeu IMC é: {imc:.2f}')
    print(f'Classificação: {status}')

main()