"""Confirmar se dá para fazer Triangulo com 3 Segmentos"""

def title(texto):
    print('=' * (len(texto) + 9))
    print(texto.center(len(texto) + 9))
    print('=' * (len(texto) + 9))


def triangulo(seg1, seg2, seg3):
    if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
        return 'É Possivel \033[92mSIM\033[m fazer um triãngulo com essas retas'
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

