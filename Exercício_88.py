from random import randint
from time import sleep

jogos_total = list()
jogos = list()

print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 13)
quantidade = str(input('Quantos Jogos Você Quer Fazer: ').strip())
while not quantidade.isnumeric():
    print('\033[91mOpção Invalida')
    quantidade = str(input('Quantos Jogos Você Quer Fazer: ').strip())
quantidade = int(quantidade)
for coisa in range(0, quantidade):
    while len(jogos) < 6:
        number = randint(1, 60)
        if jogos.count(number) == 0:
            jogos.append(number)
    jogos_total.append(jogos[:])
    jogos.clear()
print('\033[93m=\033[92m-\033[94m=\033[95m-\033[m' * 13)
print('Os Jogos foram :')
pos = 0
for joguin in jogos_total:
    pos += 1
    print(f'{pos}º Jogo: {sorted(joguin)}')
    sleep(.3)
