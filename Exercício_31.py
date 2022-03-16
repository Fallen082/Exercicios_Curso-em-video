"""Custos da viagem"""


def viagem(distancia=0):
    """
    :param distancia: O Total de Quilometros da Viagem
    :return: O Valor Total da Viagem em Real
    """
    if distancia <= 200:
        return 0.5 * distancia
    else:
        return 0.45 * distancia


while True:
    try:
        km = int(input('Qual a Distancia da viagem em \033[92mKM/h\033[m: ').strip())
    except (ValueError, IndexError):
        print('\033[91mValor Invalido\033[m')
    else:
        print(f'O Valor Total da Viagem de {km} Quilometros é \033[92m{viagem(km):.2f} R$'.replace('.', ','))
        break
        
