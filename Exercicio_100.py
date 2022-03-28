from random import randint
from time import sleep
numeros = list()


def Sorteio(lista):
    for item in range(0, 8):
        num = randint(0, 15)
        lista.append(num)


def SomaPar(lista):
    cont = 0
    for item in lista:
        if item % 2 == 0:
            cont += item
    return cont


Sorteio(numeros)
print(f'Sorteando 8 valores : ', end='')
for item in numeros:
    print(item, end=' ')
    sleep(.3)
print()
print(f'A soma total dos números pares da lista é: {SomaPar(numeros)}')
