from random import randint
from time import sleep
from operator import itemgetter
pessoas = {}
cont = 1
classificacao = dict()
for jogador in range(0, 4):
    pessoas[f'Jogador{cont}'] = randint(1, 6)
    cont += 1
cont = 1
classificacao = sorted(pessoas.items(), key=itemgetter(1), reverse=True)
for k, i in pessoas.items():
    print(f'O {k} tirou o número {i}')
    sleep(.5)
print('\n')
for k, i in classificacao:
    print(f'Em \033[94m{cont}º\033[m ficou o {k} que tirou {i}')
    cont += 1
