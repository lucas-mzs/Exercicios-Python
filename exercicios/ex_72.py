# Mostre os 20 primeiros termos de uma PA (progressão aritmética).

def pa_20_termos():
    primeiro = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))

    print('\nOs 20 primeiros termos da PA são:')
    for i in range(20):
        termo = primeiro + i * razao
        print(termo, end=' ')

pa_20_termos()