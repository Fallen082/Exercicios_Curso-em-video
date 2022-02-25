from math import sqrt

"""Calcular Cateto e a Hipotenuza"""

def Hipo(CO, CA):
  hipotenusa = sqrt((CO * CO) + (CA * CA))
  return hipotenusa

try:
  Ca = input('Qual o comprimento do cateto adjacente: ').strip().replace(',',',')
  Co = input('Qual o comprimento do cateto oposto: ').strip().replace(',','.')
  print(f'O Valor da hipotenusa é {Hipo(float(Co), float(Ca)):.2f}')

except:
  print('Alguma informção errada foi inserida')
