"""Comparar Dois Números"""


def Analizer(valor1, valor2):
    if valor1 > valor2:
        return f'O valor {valor1} é \033[96mMaior\033[m que {valor2}'
    elif valor1 < valor2:
        return f'O valor {valor2} é \033[96mMaior\033[m que {valor1}'
    else:
        return 'Os dois valores informados são \033[96mIguais\033[m'


while True:
    try:
        num1 = int(input('Qual o Primeiro Valor: ').strip())
        num2 = int(input('Qual o Segundo Valor: ').strip())
    except:
        print('\033[91mDigite Valores Válidos\033[m')
    else:
        print()
        print(Analizer(num1, num2))
        break
