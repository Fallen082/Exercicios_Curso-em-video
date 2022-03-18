"""Confirmar se dá para fazer Triângulo com 3 Segmentos e qual tipo de triângulo"""


def title(texto):
    print('=' * (len(texto) + 9))
    print(texto.center(len(texto) + 9))
    print('=' * (len(texto) + 9))


def triangulo(seg1, seg2, seg3):
    if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
        # Aqui Foi Feito o Foco Principal do Exercício
        if seg1 == seg2 and seg1 == seg3 and seg2 == seg3:
            return 'É Possivel \033[92mSIM\033[m fazer um triãngulo e ele é \033[97mEQUILÁTERO\033[m'
        elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
            return 'É Possivel \033[92mSIM\033[m fazer um triãngulo e ele é \033[97mESCALENO\033[m'
        else:
            return 'É Possivel \033[92mSIM\033[m fazer um triãngulo e ele é \033[97mISÓCELES\033[m'
        # Fim!
    else:
        return'\033[91mNÃO\033[m é possivel fazer um triângulo com essas retas'


seg = list()
title('Analisador de Triângulos')
for i in range(1, 4):
    while True:
        try:
            obj = float(input(f'{i}º Segmento: ').replace(',', '.'))
            seg.append(obj)
        except:
            print('\033[91mValor Inválido\033[m')
        else:
            break

print('=================================')
print(triangulo(seg[0], seg[1], seg[2]))
