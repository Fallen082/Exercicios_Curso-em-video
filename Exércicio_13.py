'''Aumento Salarial'''
try:
  salario_in = input('Qual seu Sálario atual: R$').replace(',', '.')
  salario_in = float(salario_in)

  print(f"O funcionario que recebia {salario_in} com os 15% de aumento, irá receber agora {salario_in + (salario_in * 0.15)}")

except:
  print('erro')
