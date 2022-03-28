def Notas(*valor, estado=False):
    """
    :param estado:Se será mostrado como esta a situação das notas Boa, Razoavel ou Ruim
    :param valor: Aqui será colocado todas as notas que deseja analisar
    :return: um dicionario com com informações sobre as notas
    """
    sala = dict()
    sala['Quantidade'] = len(valor)
    sala['Maior'] = max(valor)
    sala['Menor'] = min(valor)
    sala['Média'] = f'{sum(valor) / len(valor):.2f}'
    if estado:
        if float(sala['Média']) >= 7:
            sala['Estado'] = 'BOM'

        elif float(sala['Média']) >= 5:
            sala['Estado'] = 'RAZOAVEL'

        else:
            sala['Estado'] = 'RUIM'

    return sala


for k, v in Notas(5, 4, 6, 7, 10, estado=True).items():
    print(f'{k} é : {v}')


