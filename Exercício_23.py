"""Separar números"""

while True:
    try:
        number = int(input('Digite Aqui Um número:'))
    except(TypeError, ValueError):
        print('\033[91mDigite Um número Valido\033[m\n')
        continue
    else:
        number = str(number)
        if len(number) == 1:
            print(f'\nUnidade = {number[0]}')
            break
        elif len(number) == 2:
            print(f'\n Dezena = {number[0]} \nUnidade = {number[1]}')
            break
        elif len(number) == 3:
            print(f'\nCentena = {number[0]} \n Dezena = {number[1]} \nUnidade = {number[2]}')
            break
        elif len(number) >= 4:
            print(f'\n Milhar = {number[0:-3]} \nCentena = {number[-3]} \n Dezena = {number[-2]} \nUnidade = {number[-1]}')
            break
