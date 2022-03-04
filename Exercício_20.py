""" Fazer o sorteio de uma ordem de pessoas """

from random import shuffle
pessoas = list()
for candidato in range(1,5):
  while True:
    try:
      nome = str(input(f'{candidato}º Pessoa:')).strip().title()
      if nome.isalpha():
        break
      else:
        print('Digite um nome válido')
    except:
      print('algo deu errado :(')
  pessoas.append(nome)

for pos, pessoa in enumerate(pessoas):
  print(f'O {pos + 1}º a se apresentaar será {pessoa}\n')
