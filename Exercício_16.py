'''Receber um Valor quebrado e transformar em inteiro'''

from math import trunc

try:
    numero = str(input('Digite Aqui Um número: ')).replace(',', '.').strip()
    a = trunc(float(numero)) 
    print(f'O valor inicial é {numero}, e o valor inteiro é {a}')
except:
  print('Deu Erro :(')
  
