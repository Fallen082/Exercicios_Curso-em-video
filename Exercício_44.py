"""Simulador Fallen Store"""


def pagamento(valor=0.0,form=1):
    if form == 1:
        print(f'''\n
        Pagando A vista você consegue 10% de desconto
        O valor que você pagará sera: R$ {valor - (valor * 0.10):.2f}'''.strip().rjust(50))
    elif form == 2:
        print(f'''\n
        Pagando A no cartão em 1X você consegue 5% de desconto
        O valor que você pagará sera: R$ {valor - (valor * 0.05):.2f}'''.strip())
    elif form == 3:
        print(f'''\n
        O Valor que você irá pagar é : R$ {valor:.2f}
        será 2 Parcelas de {valor / 2:.2f}'''.strip())
    else:
        while True:
            try:
                parc = int(input('Quantas Parcelas Serão: ').strip())
            except:
                print('\033[91mDigite um valor válido\033[m')
            else:    
                print(f'''\n
            Pagando no cartão em {parc}X tem um acrescimo de 15%
            O valor que você pagará sera: R$ {valor + (valor * 0.20):.2f}
            será {parc} Parcelas de {(valor + (valor * 0.20)) / parc:.2f}'''.strip())
            break
        
print('=============| Fallen Store |=============')
while True:
    try:
        valor = float(input('Qual o valor total das compras R$: ').strip().replace(',', '.'))
        break
    except:
        print('\033[91mDigite um valor válido\033[m')
print('==========| Forma De Pagamento |==========',end='')
print('''
[1] > \033[92mÁ Vista Dinheiro / Débito\033[m
[2] > \033[92mÁ Vista Cartão Crédito\033[m
[3] > \033[92mParcelado no Cartão em \033[94m2X\033[92m Sem Juros\033[m
[4] > \033[92mPArcelado no Cartão em \033[94m3X\033[92m ou Mais\033[m''')

while True:
    try:
        form = int(input('\033[92mOPCÃO:\033[m '))
    except:
        print('\033[91mDigite um valor válido\033[m')
    else:
        if str(form) in '1234':
            pagamento(valor, form)
            break
        else:
            print('\033[91mDigite um valor válido\033[m')
            continue
