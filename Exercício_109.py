from Funcs import *

while True:
    try:
        numb = input(' Qual o Valor do produto:').strip().replace(',', '.')
        number = float(numb)
        lines(40)
        print(f'''   Seu Dobro é : \033[94m{real(multiplicador(number, 2), True)}\033[m
      Seu Triplo é : \033[94m{real(multiplicador(number, 3), True)}\033[m
        Com Aumento de 28% : \033[94m{real(aumentar(number, 28), True)}\033[m
          Com Desconto de 37% : \033[94m{real(diminuir(number, 37), True)}\033[m''')
        lines(40)

    except:
        print('Alguma Informação foi colocada incorretamente')
