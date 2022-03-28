from Funcs import *

lines(40)
while True:
    try:
        number = int(input('Digte o número para ver os dados: ').strip())
        lines(40)
        print(f'''    Seu Dobro é : \033[94m{multiplicador(number, 2)}\033[m
      Seu Triplo é : \033[94m{multiplicador(number, 3)}\033[m
        Com Aumento de 28% : \033[94m{aumentar(number, 28)}\033[m
          Com Desconto de 37% : \033[94m{diminuir(number, 37)}\033[m''')
        lines(40)
    except:
        print('\nAlgo Deu erro... \033[91mFim do Programa\033[m')
        break
