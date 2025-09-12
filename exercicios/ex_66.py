# Valide a entrada de um número entre 0 e 10. Repita até o usuário acertar.

def validar_numero():
    numero_correto = 7

    while True:
        numero = int(input('Digite um número entre 0 e 10: '))

        if numero == numero_correto:
            print(f'🎉 Parabéns! Você acertou, o número era {numero_correto}.')
            break
        else:
            print('❌ Número inválido! Tente novamente.')

validar_numero()