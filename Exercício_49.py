"""Atualizar á Tábuada do Exercício 009"""

def tabuada (numero):
    for multiplicador in range(1, 11):
        print(f'{numero} x {multiplicador:2} = {numero * multiplicador} ')


while True:
    try:
        ler_num = int(input('Digite aqui um número, para ver sua tábuada:').strip())
    except:
        print('\033[91mDigite um número válido\033[m')
    else:
        tabuada(ler_num)
        break
