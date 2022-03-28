from datetime import date

def Votacao(Nasc):
    """
    ---> Está Função  Mostra se seu voto é obrigatorio ou opcional ou se não pode votar
    :param Nasc:  Ano de nascimento do usuário
    :return: se Nasc >16 Não vota | nasc <= 16 e >18 voto Opcional | <18 e >65 Voto Obrigatorio | <65 Voto Opcional
    """
    idade = date.today().year - Nasc
    if idade < 16:
        print(f'Com {idade} Anos, NÃO VOTA')
    elif 16 <= idade < 18:
        print(f'Com {idade} Anos, SEU VOTO É OPCIONAL')
    elif 18 <= idade < 65:
        print(f'Com {idade} Anos, SEU VOTO É OBRIGÁTORIO')
    elif idade > 65:
        print(f'Com {idade} Anos, SEU VOTO É OPCIONAL')


while True:
    try:
        print('##' * 13)
        ano = int(input('Qual Ano Voçê Nasceu: '))
        if ano > date.today().year or ano < 1500:
            print('Alguma Informação foi digitada errada :( Tente Novamente\n')
        else:
            break
    except:
        print('Alguma Informação foi digitada errada :( Tente Novamente\n')

print('##' * 16)
Votacao(ano)
