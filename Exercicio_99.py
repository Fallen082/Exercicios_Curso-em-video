from time import sleep



def Maior(*num):
    if len(num) == 0:
        print('Analizando os valores passados...')
        print(f'Foram passados ao todo 0 valores')
        print(f'Sendo 0 o maior')
    else:
        print('Analizando os valores passados...')
        for item in num:
            print(item, end=' ')
            sleep(.3)
        print(f'Foram passados ao todo {len(num)} valores')
        print(f'Sendo {max(num)} o maior')


def Linhas():
    print('==' * 24)


Linhas()
Maior(4, 7, 2, 5, 6, 8, 9, 6, 4, 10)
Linhas()
Maior(4, 7, 0)
Linhas()
Maior(111)
Linhas()
Maior(2, 5)
Linhas()
Maior()
