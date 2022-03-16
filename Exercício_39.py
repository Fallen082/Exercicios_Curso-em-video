"""AListamento Militar"""


def alist(nascmento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascmento
    print(f'Quem nasceu no ano de {nascmento} hoje tem {atual - nascmento}')
    if idade < 18:
        print(f'Ainda faltam {18 - idade} anos para você se alistar')
        print(f'Seu alistamento será em {atual + (18 - idade)}')
    elif idade == 18:
        print('Você Terá que se alistar neste ano')
    else:
        print(f'Ja passaram {idade - 18} anos do seu alistamento')
        print(f'Seu alistamento foi no ano de {atual - (idade - 18)}')


while True:
    try:
        nasc = int(input('Em qual ano você nasceu : '))
    except:
        print('\033[91mDigite um valor válido\033[m')
    else:
        alist(nasc)
        break
