'''Mostrar o dobro, triplo, Raiz quadrada do número informado'''
import math

num = input('Digite algum número')
try:

  num = int(num)
  print(f'''
          Analisando o Valor {num} vi que:
          O dobro deste número é {num * 2}
          O triplo deste número é {num * 3}
          e sua raiz quadrada é : {math.sqrt(num)}
          ''')
except:
       print('Alguma informação foi digitada errada :(')

