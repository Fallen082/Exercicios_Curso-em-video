"""Progressão Aritimética"""

from sys import exec_prefix


def linha(texto):
    print('=' * (len(texto) + 4))
    print(texto.center((len(texto)+ 4)))
    print('=' * (len(texto) + 4))

def PA(inicio=0, tempo=1):
    for valores in range (inicio,inicio + 10 * tempo,tempo):
        print(f'{valores}',end='-->')
    print('\033[92mFIM!\033[m')


linha('Progressão Aritimética de 10 Termos')
while True:
    try:
        começo = int(input('Qual O Primeiro Termo: ').strip())
        pulos = int(input('Qual A distância dos pulos: ').strip())
    except:
        print('\033[91m\nERRO!\033[m Digite Valores Válidos\n')
    else:
        PA(começo, pulos)
        break
