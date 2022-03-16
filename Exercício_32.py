from datetime import date
"""Identificador de ano bissexto"""


def ano_bi(year=2):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f'O Ano {year} \033[92mé sim\033[m Bissexto'
    else:
        return f'O ano {year} \033[91mnão é\033[m Bissexto'


while True:
    print('\033[94m[Digite 0 para o ano atual]\033[m')
    try:
        ano = int(input('Digite o o valor de algum ano para ver se é bissexto:').strip())
    except (ValueError, IndexError):
        print('\033[91mValor Inválido\033[m')
    else:
        if ano == 0:
            print(ano_bi(date.today().year))
            break
        else:
            print(ano_bi(ano))
            break
