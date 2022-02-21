'''Mostrar o dobro, triplo, Raiz quadrada do número informado'''
import math

try:
    num = int(input('Digite um número')
          
    print(f'''
          Analisando o Valor {num} vi que:
          O dobro deste número é {num * 2}
          O triplo deste número é {num * 3}
          e sua raiz quadrada é : {sqrt(num)}''')
except:
       print('Alguma informação foi digitada errada :(')
