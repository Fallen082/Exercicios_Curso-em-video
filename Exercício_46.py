"""Contagem Regressiva"""

cores = ['\033[90m', '\033[91m',
         '\033[92m', '\033[93m',
         '\033[94m', '\033[95m',
         '\033[96m', '\033[97m' ]


def temporizador(Sec):
  from random import choice
  from time import sleep
  while Sec != 0:
    print(f'{choice(cores)}{Sec}\033[m')
    sleep(1)
    Sec -= 1


temporizador(10)
print('\033[92mFeliz Ano Novo!!')
