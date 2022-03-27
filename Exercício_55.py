"""Descobrir Qual o Maior e Menor Peso do Grupo"""

grupo = list()

for pessoa in range(1, 5):
  while True:
    try:
      pessoa = float(input(f'Digite o Peso da {pessoa}º Pessoa: ').replace(',', '.'))
    except:
      print('\033[91mDigite um valor válido\033[m')
    else:
        grupo.append(pessoa)
        break

print(f"""
O Maior peso do grupo está com: \033[92m{max(grupo)} KG\033[m
O Menor peso do grupo está com: \033[92m{min(grupo)} KG\033[m""")
