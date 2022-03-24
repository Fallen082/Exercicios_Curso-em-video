"""Analisar Números Primos"""


def prim(number):
    cont = 0
    for numeros in range(1,number + 1):
        if number % numeros == 0:
            print(f'\033[92m{numeros}\033[m',end='-')
            cont +=1
        else:
            print(f'\033[91m{numeros}\033[m',end='-')
    if cont <=2:
        print(f"""\nO número \033[94m{number}\033[m é divisivel por {cont} números
        Por Isso \033[92mele É Primo\033[m""")
    else:
        print(f"""\nO número \033[94m{number}\033[m é divisivel por {cont} números
        Por Isso \033[91mele NÃO é Primo\033[m""")


while True:
    try:
        ler_num = int(input('Digite Aqui Um Número:').strip())
    except:
        print('\033[91mDigite um número válido\033[m')
    else:
        prim(ler_num)
        break