def aluguel(dia=1,num=0):
  valor =(dia * 60) + (num * 0.15)
  return f'R$ {valor:.2f}'


while True:
  try:
    dias = int(input('Quantos dias foram rodados:').strip())
    valor = input('Quantos Quilométros Foram Percorridos: ').strip().replace(',','.')
    valor = float(valor)
    print(f'\nO valor total a ser pago é : {aluguel(dias, valor):}')
    break
    
  except:
    print('Alguma Informação foi passada errada, Tente novamente')
