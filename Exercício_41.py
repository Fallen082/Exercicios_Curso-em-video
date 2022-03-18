"""Classificar Categoria do nadador de acordo com a idade"""


def classific(ano_nasc):
    from datetime import date
    atual = date.today().year
    if atual - ano_nasc <= 9:
        print(f'Este Atleta tem \033[93m{atual - ano_nasc}\033[m Anos')
        print('Classificação do Atleta: \033[93mMirim\033[m')
    elif atual - ano_nasc <= 14:
        print(f'Este Atleta tem \033[93m{atual - ano_nasc}\033[m Anos')
        print('Classificação do Atleta: \033[93mInfantil\033[m')
    elif atual - ano_nasc <= 19:
        print(f'Este Atleta tem \033[93m{atual - ano_nasc}\033[m Anos')
        print('Classificação do Atleta: \033[93mJuníor\033[m')
    elif atual - ano_nasc <= 25:
        print(f'Este Atleta tem \033[93m{atual - ano_nasc}\033[m Anos')
        print('Classificação do Atleta: \033[93mSênior\033[m')
    else:
        print(f'Este Atleta tem \033[93m{atual - ano_nasc}\033[m Anos')
        print('Classificação do Atleta: \033[93mMaster\033[m')


while True:
    try:
        ano = int(input('Qual seu ano de nascimento: ').strip())
    except:
        print('Insira dados Válidos')
    else:
        if len(str(ano)) == 4:
            classific(ano)
            break
        else:
            print('Insira dados Válidos')
            continue
