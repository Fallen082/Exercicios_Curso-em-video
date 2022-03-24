"""Soma Dos Números pares informados"""

def soma_par(lista=[]):
  sum = 0
  for item in lista:
    if item % 2 == 0:
      sum += item
    else: 
      continue
  return sum


lista_num = list()
for numeros in range(1, 7):
  while True:
    try:
      number = int(input(f'Qual o {numeros}º Número Inteiro: '))
    except:
      print('\033[91mDigite um número válido\033[m')
    else:
      lista_num.append(number)
      break

print(f'O Valor da soma de todos os números pares é : {soma_par(lista_num)})
