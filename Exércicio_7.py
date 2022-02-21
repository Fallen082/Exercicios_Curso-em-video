'''Mostrar a média de um aluno'''

try:
  nota1 = float(input('Qual a primeira nota do aluno:'))
  nota2 = float(input('Qual a segunda nota do aluno:'))
  media = (nota1 + nota2) / 2
  print(f'A média das notas {nota1} e {nota2} é : {media:.2f}')
except:
  print('erro :(')
