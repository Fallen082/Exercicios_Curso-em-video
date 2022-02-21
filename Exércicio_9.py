'''Tábuada de um número'''

try:
  n = int(input('Digite um número para ver sua tábuada: '))
  print(f'''
         1 x {n} = {1 * n}
         2 x {n} = {2 * n}
         3 x {n} = {3 * n}
         4 x {n} = {4 * n}
         5 x {n} = {5 * n}
         6 x {n} = {6 * n}
         7 x {n} = {7 * n}
         8 x {n} = {8 * n}
         9 x {n} = {9 * n}
        10 x {n} = {10 * n}''')
except: 
  print('erro')
