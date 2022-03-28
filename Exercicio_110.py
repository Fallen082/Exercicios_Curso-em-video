from Funcs import *

while True:
    try:
        valor = input('Digite o preço do produto:').strip().replace(',','.')
        print(resumo(float(valor), 80, 35))
        break

    except:
        print('Valor invalido')
