'''Calcular o desconto de algum valor'''
-
try:
  valor = str(input('Digite Aqui p valor do produto em R$: ')).replace(',', '.')
  porcentagem = str(input('Quantos pórcento de desconto: ')).replace(',', '.')
  desconto = float(valor) * (float(porcentagem) / 100.00)

  print(f'''
        O Valor Inicial do Produto: {float(valor)}
         A Porcentagem do Desconto: {float(porcentagem)}
            Valor Final do Produto: {float(valor) - desconto}''')
except:
  print('Erro')
